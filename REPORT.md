# Pond Scanner Report
**Scan time:** 2026-07-24 14:13 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -207.9% | $578,904 |
| 🟢 | PF_TRUMPUSD | -135.0% | $521,424 |
| 🟢 | PF_UNIUSD | -62.8% | $969,047 |
| 🟢 | PF_STXUSD | -35.8% | $1,098,986 |
| 🟢 | PF_DOTUSD | -31.5% | $1,291,207 |
| 🟢 | PF_GRASSUSD | -30.0% | $540,280 |
| ⚪ | PF_ACEUSD | -17.5% | $1,034,347 |
| ⚪ | PF_EIGENUSD | -16.5% | $745,189 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.075%** (kraken → gemini) — coinbase: $63,962.83, kraken: $63,957.90, gemini: $64,005.99
- ⚪ **ETH** gap **0.026%** (kraken → gemini) — coinbase: $1,856.07, kraken: $1,856.05, gemini: $1,856.54

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #374 | $58.6M | 2.65x | +29.6% |
| RE (RE) | #260 | $101.2M | 1.49x | +33.2% |
| Rootstock Infrastructure Framework (RIF) | #247 | $106.8M | 0.60x | +33.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 23% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 31% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
