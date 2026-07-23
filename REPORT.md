# Pond Scanner Report
**Scan time:** 2026-07-23 03:45 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -97.3% | $715,922 |
| 🟢 | PF_VIRTUALUSD | -89.3% | $729,391 |
| 🟢 | PF_MIRAUSD | -88.3% | $2,723,772 |
| 🟢 | PF_JTOUSD | +69.5% | $637,147 |
| 🟢 | PF_NEARUSD | -57.6% | $994,237 |
| 🟢 | PF_SYNUSD | -47.6% | $1,255,796 |
| 🟢 | PF_ETHFIUSD | -30.7% | $644,197 |
| 🟢 | PF_SNXUSD | +30.7% | $549,844 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (kraken → gemini) — coinbase: $65,659.96, kraken: $65,654.60, gemini: $65,664.28
- ⚪ **ETH** gap **0.015%** (kraken → gemini) — coinbase: $1,921.80, kraken: $1,921.63, gemini: $1,921.91

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #263 | $103.7M | 2.61x | +39.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 31% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.31, realized vol 10d 44% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
