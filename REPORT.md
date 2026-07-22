# Pond Scanner Report
**Scan time:** 2026-07-22 03:47 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | +89.9% | $2,640,789 |
| 🟢 | PF_NEARUSD | +40.2% | $1,435,565 |
| 🟢 | PF_SPXUSD | +39.2% | $520,663 |
| 🟢 | PF_KOMAUSD | +35.1% | $727,964 |
| ⚪ | PF_FLRUSD | +29.6% | $552,073 |
| ⚪ | PF_ZIGUSD | +24.3% | $787,453 |
| ⚪ | PF_BRETTUSD | +21.9% | $5,165,304 |
| ⚪ | PF_VELOUSD | +16.4% | $981,370 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (kraken → gemini) — coinbase: $66,290.64, kraken: $66,275.80, gemini: $66,295.50
- ⚪ **ETH** gap **0.042%** (kraken → coinbase) — coinbase: $1,933.34, kraken: $1,932.53, gemini: $1,933.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #291 | $82.9M | 3.02x | -26.4% |
| LAB (LAB) | #422 | $52.8M | 0.62x | +24.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 34% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.40, realized vol 10d 46% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
