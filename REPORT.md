# Pond Scanner Report
**Scan time:** 2026-07-23 19:46 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -467.1% | $551,083 |
| 🟢 | PF_KAITOUSD | +86.0% | $540,120 |
| 🟢 | PF_UNIUSD | -75.5% | $642,678 |
| 🟢 | PF_NEARUSD | +37.4% | $910,822 |
| ⚪ | PF_MIRAUSD | -26.5% | $1,727,440 |
| ⚪ | PF_TRUMPUSD | -26.4% | $542,609 |
| ⚪ | PF_JTOUSD | -22.0% | $635,695 |
| ⚪ | PF_ARCUSD | -19.8% | $641,421 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $64,691.29, kraken: $64,698.80, gemini: $64,703.50
- ⚪ **ETH** gap **0.013%** (coinbase → gemini) — coinbase: $1,873.28, kraken: $1,873.45, gemini: $1,873.52

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #427 | $50.8M | 1.77x | +33.3% |
| Lorenzo Protocol (BANK) | #252 | $106.6M | 1.30x | +24.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 34% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 49% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
