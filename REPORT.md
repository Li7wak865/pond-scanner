# Pond Scanner Report
**Scan time:** 2026-07-21 14:23 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +879.1% | $542,765 |
| 🟢 | PF_SOLUSD | +273.9% | $670,928 |
| 🟢 | PF_NEARUSD | -60.8% | $1,342,514 |
| 🟢 | PF_RAREUSD | +55.8% | $709,344 |
| 🟢 | PF_SYNUSD | +36.3% | $2,153,896 |
| 🟢 | PF_DOTUSD | +34.9% | $4,352,892 |
| 🟢 | PF_SPXUSD | +31.9% | $688,834 |
| ⚪ | PF_ZEREBROUSD | +25.7% | $1,844,199 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (gemini → kraken) — coinbase: $66,664.00, kraken: $66,678.00, gemini: $66,663.44
- ⚪ **ETH** gap **0.018%** (gemini → kraken) — coinbase: $1,931.39, kraken: $1,931.47, gemini: $1,931.12

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #350 | $67.4M | 2.59x | -44.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.40, realized vol 10d 34% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
