# Pond Scanner Report
**Scan time:** 2026-07-20 13:33 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -224.5% | $9,174,333 |
| 🟢 | PF_KAITOUSD | -143.8% | $1,285,562 |
| 🟢 | PF_SYNUSD | -102.9% | $2,275,697 |
| 🟢 | PF_BBUSD | +77.4% | $1,039,885 |
| 🟢 | PF_ZEREBROUSD | -70.2% | $3,673,667 |
| 🟢 | PF_LRCUSD | +54.3% | $3,315,956 |
| ⚪ | PF_TRUMPUSD | +20.1% | $974,545 |
| ⚪ | PF_NEARUSD | -20.0% | $884,010 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (gemini → kraken) — coinbase: $64,530.01, kraken: $64,531.20, gemini: $64,524.66
- ⚪ **ETH** gap **0.201%** (gemini → coinbase) — coinbase: $1,873.19, kraken: $1,871.52, gemini: $1,869.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.37, realized vol 10d 33% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
