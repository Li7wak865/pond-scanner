# Pond Scanner Report
**Scan time:** 2026-07-22 19:44 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -170.3% | $625,014 |
| 🟢 | PF_MIRAUSD | -99.8% | $1,109,078 |
| 🟢 | PF_MOODENGUSD | +57.8% | $805,116 |
| 🟢 | PF_NEARUSD | -41.7% | $969,108 |
| 🟢 | PF_JUPUSD | -36.0% | $519,316 |
| 🟢 | PF_ETHFIUSD | -31.9% | $659,757 |
| ⚪ | PF_XRPUSD | -29.1% | $19,895,606 |
| ⚪ | PF_EIGENUSD | -28.9% | $999,686 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → coinbase) — coinbase: $65,842.15, kraken: $65,837.80, gemini: $65,839.77
- ⚪ **ETH** gap **0.066%** (coinbase → gemini) — coinbase: $1,924.26, kraken: $1,925.26, gemini: $1,925.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RE (RE) | #303 | $78.2M | 7.96x | +28.8% |
| Lorenzo Protocol (BANK) | #270 | $96.6M | 2.65x | +32.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.28, realized vol 10d 35% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 46% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
