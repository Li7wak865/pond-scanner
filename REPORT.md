# Pond Scanner Report
**Scan time:** 2026-07-22 08:45 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | -79.8% | $2,402,461 |
| 🟢 | PF_GRASSUSD | +48.6% | $530,121 |
| 🟢 | PF_JTOUSD | -37.3% | $742,954 |
| 🟢 | PF_KOMAUSD | +34.9% | $596,734 |
| 🟢 | PF_NEARUSD | -30.6% | $1,529,209 |
| ⚪ | PF_ONDOUSD | -26.8% | $10,744,642 |
| ⚪ | PF_VIRTUALUSD | -25.1% | $1,383,425 |
| ⚪ | PF_ACEUSD | -23.6% | $3,627,943 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (gemini → coinbase) — coinbase: $65,921.28, kraken: $65,908.20, gemini: $65,903.73
- ⚪ **ETH** gap **0.015%** (gemini → coinbase) — coinbase: $1,919.11, kraken: $1,919.06, gemini: $1,918.82

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RE (RE) | #321 | $73.4M | 5.67x | +26.3% |
| LAB (LAB) | #439 | $49.3M | 1.19x | +20.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.29, realized vol 10d 35% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 46% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
