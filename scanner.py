"""
Pond Scanner — hunts for structural edge conditions in public market data
==========================================================================
Runs on a schedule (GitHub Actions). Uses ONLY free public endpoints,
no API keys, no accounts. Writes a human-readable REPORT.md and appends
a one-line summary to history.csv.

Modules (each fails gracefully if an API is down/blocked):
  1. FUNDING SKEW   - crowded perp-futures positioning (Kraken Futures)
  2. CROSS-EXCHANGE BASIS - spot price gaps between US venues
  3. SMALL-COIN RADAR - unusual activity in coins too small for funds
  4. VOLATILITY REGIME - is the market trending or chopping right now?

A scanner that always finds treasure is lying. Most runs should say
"nothing rich right now" - that's the tool working correctly.
"""

import csv
import os
from datetime import datetime, timezone

import requests

TIMEOUT = 15
HEADERS = {"User-Agent": "pond-scanner/1.0 (personal research tool)"}
NOW = datetime.now(timezone.utc)

# Thresholds for flagging (deliberately strict - fewer, better flags)
FUNDING_HOT_ANNUAL = 0.30      # |annualized funding| > 30% = crowded
BASIS_HOT_PCT = 0.30           # >0.30% price gap between US exchanges
SMALLCOIN_VOL_MCAP = 0.50      # 24h volume > 50% of market cap
SMALLCOIN_MOVE_PCT = 15.0      # and |24h move| > 15%
ER_TRENDING = 0.35             # efficiency ratio thresholds
ER_CHOPPY = 0.20


def get_json(url: str, params=None):
    r = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


# ------------------- Module 1: Funding skew (Kraken Futures) -------------------
def scan_funding():
    """Crowded positioning: when perps funding is rich, the crowd is paying
    a fee to hold one side. Historically mean-reverting; also a proxy for
    froth. Capacity-limited => institutions can't fully arb it."""
    data = get_json("https://futures.kraken.com/derivatives/api/v3/tickers")
    rows = []
    for t in data.get("tickers", []):
        sym = t.get("symbol", "")
        # perpetuals only (Kraken perps start with PI_ / PF_)
        if not (sym.startswith("PI_") or sym.startswith("PF_")):
            continue
        fr = t.get("fundingRate")
        mark = t.get("markPrice")
        vol = t.get("vol24h", 0) or 0
        if fr is None or mark in (None, 0) or vol == 0:
            continue
        # Kraken funding conventions differ by contract family:
        #   PI_ (inverse perps): fundingRate is ABSOLUTE (quote ccy) -> divide by price
        #   PF_ (linear perps):  fundingRate is already RELATIVE per hour
        if sym.startswith("PI_"):
            rel_hourly = float(fr) / float(mark)
        else:
            rel_hourly = float(fr)
        annual = rel_hourly * 24 * 365
        # sanity cap: discard obviously-broken values (>1000%/yr either way)
        if abs(annual) > 10:
            continue
        rows.append({"symbol": sym, "annual": annual, "vol24h": float(vol)})
    # rank by absolute annualized funding, keep liquid ones only
    rows = [r for r in rows if r["vol24h"] > 500_000]
    rows.sort(key=lambda r: abs(r["annual"]), reverse=True)
    hot = [r for r in rows if abs(r["annual"]) >= FUNDING_HOT_ANNUAL]
    return {"top": rows[:8], "hot": hot}


# ------------------- Module 2: Cross-exchange basis -------------------
def scan_basis():
    """Price gaps for the same asset across US-accessible venues.
    Usually near zero; a persistent gap >0.3% is unusual and worth a look
    (often explained by withdrawal issues - which is itself information)."""
    out = []
    for asset, feeds in {
        "BTC": {
            "coinbase": ("https://api.exchange.coinbase.com/products/BTC-USD/ticker", lambda j: float(j["price"])),
            "kraken": ("https://api.kraken.com/0/public/Ticker?pair=XBTUSD", lambda j: float(list(j["result"].values())[0]["c"][0])),
            "gemini": ("https://api.gemini.com/v1/pubticker/btcusd", lambda j: float(j["last"])),
        },
        "ETH": {
            "coinbase": ("https://api.exchange.coinbase.com/products/ETH-USD/ticker", lambda j: float(j["price"])),
            "kraken": ("https://api.kraken.com/0/public/Ticker?pair=ETHUSD", lambda j: float(list(j["result"].values())[0]["c"][0])),
            "gemini": ("https://api.gemini.com/v1/pubticker/ethusd", lambda j: float(j["last"])),
        },
    }.items():
        prices = {}
        for venue, (url, extract) in feeds.items():
            try:
                prices[venue] = extract(get_json(url))
            except Exception:
                continue
        if len(prices) < 2:
            continue
        hi_v = max(prices, key=prices.get)
        lo_v = min(prices, key=prices.get)
        gap_pct = (prices[hi_v] - prices[lo_v]) / prices[lo_v] * 100
        out.append({"asset": asset, "prices": prices, "hi": hi_v, "lo": lo_v,
                    "gap_pct": gap_pct, "hot": gap_pct >= BASIS_HOT_PCT})
    return out


# ------------------- Module 3: Small-coin radar -------------------
def scan_small_coins():
    """Coins ranked ~250-500 by market cap: too small for funds.
    Flag unusual activity: volume swamping market cap + big price move.
    This is a WATCHLIST generator, not a buy signal."""
    coins = get_json(
        "https://api.coingecko.com/api/v3/coins/markets",
        params={"vs_currency": "usd", "order": "market_cap_desc",
                "per_page": 250, "page": 2, "price_change_percentage": "24h"},
    )
    flagged = []
    for c in coins:
        mcap = c.get("market_cap") or 0
        vol = c.get("total_volume") or 0
        chg = c.get("price_change_percentage_24h") or 0.0
        if mcap < 1_000_000:
            continue
        ratio = vol / mcap if mcap else 0
        if ratio >= SMALLCOIN_VOL_MCAP and abs(chg) >= SMALLCOIN_MOVE_PCT:
            flagged.append({"name": c.get("name"), "sym": (c.get("symbol") or "").upper(),
                            "mcap_m": mcap / 1e6, "vol_mcap": ratio, "chg24h": chg,
                            "rank": c.get("market_cap_rank")})
    flagged.sort(key=lambda x: x["vol_mcap"], reverse=True)
    return flagged[:10]


# ------------------- Module 4: Volatility regime -------------------
def _closes_kraken_daily(pair: str):
    j = get_json("https://api.kraken.com/0/public/OHLC",
                 params={"pair": pair, "interval": 1440})
    key = [k for k in j["result"] if k != "last"][0]
    return [float(row[4]) for row in j["result"][key]]  # close prices


def scan_regime():
    """Efficiency ratio (Kaufman): |net 20d move| / sum of daily |moves|.
    High = clean trend (momentum strategies feed well).
    Low  = chop (momentum starves; mean-reversion conditions).
    Directly relevant to your live momentum bot."""
    out = []
    for label, pair in [("BTC", "XBTUSD"), ("ETH", "ETHUSD")]:
        closes = _closes_kraken_daily(pair)
        if len(closes) < 61:
            continue
        c = closes
        net = abs(c[-1] - c[-21])
        path = sum(abs(c[i] - c[i - 1]) for i in range(len(c) - 20, len(c)))
        er = net / path if path else 0.0

        def rvol(days):
            rets = [(c[i] - c[i - 1]) / c[i - 1] for i in range(len(c) - days, len(c))]
            mean = sum(rets) / len(rets)
            var = sum((r - mean) ** 2 for r in rets) / len(rets)
            return (var ** 0.5) * (365 ** 0.5) * 100  # annualized %

        regime = ("TRENDING" if er >= ER_TRENDING
                  else "CHOPPY" if er <= ER_CHOPPY else "MIXED")
        out.append({"asset": label, "er": er, "vol10": rvol(10),
                    "vol60": rvol(60), "regime": regime})
    return out


# ------------------- Report writer -------------------
def light(hot: bool, warm: bool = False) -> str:
    return "🟢" if hot else ("🟡" if warm else "⚪")


def write_report(funding, basis, small, regime, errors):
    L = []
    L.append(f"# Pond Scanner Report")
    L.append(f"**Scan time:** {NOW.strftime('%Y-%m-%d %H:%M UTC')}")
    L.append("")
    n_hot = (len(funding["hot"]) if funding else 0) \
        + sum(1 for b in (basis or []) if b["hot"]) + len(small or [])
    L.append(f"**Flags this scan:** {n_hot} "
             f"{'— quiet market, nothing rich. That is normal.' if n_hot == 0 else ''}")
    L.append("")

    L.append("## 1. Funding skew (crowded positioning)")
    if funding is None:
        L.append("_Data source unavailable this run._")
    else:
        L.append("| | Perp | Annualized funding | 24h vol |")
        L.append("|---|---|---|---|")
        for r in funding["top"]:
            hot = abs(r["annual"]) >= FUNDING_HOT_ANNUAL
            L.append(f"| {light(hot)} | {r['symbol']} | {r['annual']*100:+.1f}% | ${r['vol24h']:,.0f} |")
        L.append("")
        L.append("_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; "
                 "also a froth gauge. Rate math is approximate._")
    L.append("")

    L.append("## 2. Cross-exchange basis (US venues)")
    if basis is None:
        L.append("_Data source unavailable this run._")
    else:
        for b in basis:
            plist = ", ".join(f"{v}: ${p:,.2f}" for v, p in b["prices"].items())
            L.append(f"- {light(b['hot'])} **{b['asset']}** gap **{b['gap_pct']:.3f}%** "
                     f"({b['lo']} → {b['hi']}) — {plist}")
        L.append("")
        L.append("_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually "
                 "mean withdrawal friction somewhere — information either way._")
    L.append("")

    L.append("## 3. Small-coin radar (ranks ~250-500, whale-free zone)")
    if small is None:
        L.append("_Data source unavailable this run._")
    elif not small:
        L.append("Nothing unusual. ⚪")
    else:
        L.append("| Coin | Rank | Mcap | 24h vol/mcap | 24h move |")
        L.append("|---|---|---|---|---|")
        for s in small:
            L.append(f"| {s['name']} ({s['sym']}) | #{s['rank']} | ${s['mcap_m']:.1f}M "
                     f"| {s['vol_mcap']:.2f}x | {s['chg24h']:+.1f}% |")
        L.append("")
        L.append("_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, "
                 "listings, or news. Research before touching; never a buy signal by itself._")
    L.append("")

    L.append("## 4. Volatility regime (feeds your momentum bot)")
    if regime is None:
        L.append("_Data source unavailable this run._")
    else:
        for r in regime:
            icon = "🟢" if r["regime"] == "TRENDING" else ("🔴" if r["regime"] == "CHOPPY" else "🟡")
            L.append(f"- {icon} **{r['asset']}: {r['regime']}** — efficiency ratio "
                     f"{r['er']:.2f}, realized vol 10d {r['vol10']:.0f}% vs 60d {r['vol60']:.0f}%")
        L.append("")
        L.append("_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum "
                 "bot to sit in cash a lot (correct behavior)._")
    L.append("")

    if errors:
        L.append("## Data issues this run")
        for e in errors:
            L.append(f"- {e}")
        L.append("")

    L.append("---")
    L.append("_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). "
             "Nothing here is financial advice; flags are conditions to research, not trades to take._")

    with open("REPORT.md", "w") as f:
        f.write("\n".join(L) + "\n")


def append_history(funding, basis, small, regime):
    exists = os.path.exists("history.csv")
    with open("history.csv", "a", newline="") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(["utc_time", "funding_hot", "basis_hot", "smallcoin_flags",
                        "btc_regime", "eth_regime"])
        reg = {r["asset"]: r["regime"] for r in (regime or [])}
        w.writerow([
            NOW.strftime("%Y-%m-%d %H:%M"),
            len(funding["hot"]) if funding else "err",
            sum(1 for b in (basis or []) if b["hot"]) if basis is not None else "err",
            len(small) if small is not None else "err",
            reg.get("BTC", "err"), reg.get("ETH", "err"),
        ])


def main():
    errors = []
    results = {}
    for name, fn in [("funding", scan_funding), ("basis", scan_basis),
                     ("small", scan_small_coins), ("regime", scan_regime)]:
        try:
            results[name] = fn()
            print(f"[ok] {name}")
        except Exception as e:
            results[name] = None
            errors.append(f"{name}: {type(e).__name__}: {e}")
            print(f"[FAIL] {name}: {e}")

    write_report(results["funding"], results["basis"], results["small"],
                 results["regime"], errors)
    append_history(results["funding"], results["basis"], results["small"],
                   results["regime"])
    print("Report written to REPORT.md")


if __name__ == "__main__":
    main()
