# Pond Scanner Report
**Scan time:** 2026-07-24 08:43 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | -110.2% | $4,812,491 |
| 🟢 | PF_UNIUSD | -64.2% | $808,686 |
| 🟢 | PF_KAITOUSD | +41.1% | $614,693 |
| 🟢 | PF_STXUSD | -31.7% | $645,000 |
| ⚪ | PF_ACEUSD | -24.9% | $1,576,238 |
| ⚪ | PF_NEARUSD | +21.3% | $960,512 |
| ⚪ | PF_VELOUSD | -17.2% | $2,065,790 |
| ⚪ | PF_SUSHIUSD | +13.6% | $914,484 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $65,379.48, kraken: $65,384.30, gemini: $65,388.67
- ⚪ **ETH** gap **0.008%** (kraken → gemini) — coinbase: $1,890.83, kraken: $1,890.69, gemini: $1,890.85

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #404 | $54.0M | 4.49x | +23.8% |
| DeXe (DEXE) | #249 | $108.2M | 2.02x | -33.5% |
| RE (RE) | #256 | $105.3M | 1.30x | +43.3% |
| o1.exchange (O) | #292 | $84.4M | 0.63x | -18.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 21% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.20, realized vol 10d 31% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
