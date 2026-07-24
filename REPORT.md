# Pond Scanner Report
**Scan time:** 2026-07-24 03:44 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -62.7% | $558,063 |
| 🟢 | PF_TRUMPUSD | -54.6% | $635,565 |
| 🟢 | PF_EIGENUSD | -36.4% | $810,258 |
| 🟢 | PF_NEARUSD | +33.5% | $907,023 |
| ⚪ | PF_ACEUSD | -23.7% | $1,686,113 |
| ⚪ | PF_VIRTUALUSD | -20.5% | $506,677 |
| ⚪ | PF_SUSHIUSD | -18.8% | $777,952 |
| ⚪ | PF_XRPUSD | -15.2% | $16,829,177 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (kraken → gemini) — coinbase: $65,354.01, kraken: $65,345.30, gemini: $65,358.89
- ⚪ **ETH** gap **0.047%** (kraken → gemini) — coinbase: $1,879.34, kraken: $1,878.70, gemini: $1,879.59

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #418 | $50.8M | 3.33x | +18.8% |
| Lorenzo Protocol (BANK) | #245 | $108.5M | 1.26x | +22.2% |
| RE (RE) | #258 | $103.0M | 1.05x | +29.9% |
| Rootstock Infrastructure Framework (RIF) | #247 | $110.9M | 0.56x | +55.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 21% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 31% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
