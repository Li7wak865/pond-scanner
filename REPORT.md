# Pond Scanner Report
**Scan time:** 2026-07-22 14:23 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -73.0% | $572,678 |
| 🟢 | PF_SYNUSD | -63.5% | $1,456,505 |
| 🟢 | PF_BIOUSD | +55.8% | $596,006 |
| 🟢 | PF_EIGENUSD | -33.9% | $1,025,271 |
| 🟢 | PF_NEARUSD | -33.7% | $1,272,999 |
| 🟢 | PF_ONDOUSD | -31.6% | $12,747,262 |
| ⚪ | PF_ACEUSD | -24.5% | $3,698,285 |
| ⚪ | PF_ETHFIUSD | +23.6% | $567,069 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → kraken) — coinbase: $65,613.44, kraken: $65,628.60, gemini: $65,615.75
- ⚪ **ETH** gap **0.011%** (coinbase → gemini) — coinbase: $1,928.21, kraken: $1,928.33, gemini: $1,928.43

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RE (RE) | #301 | $78.5M | 8.61x | +32.5% |
| LAB (LAB) | #427 | $50.2M | 1.29x | +21.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.26, realized vol 10d 35% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.40, realized vol 10d 46% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
