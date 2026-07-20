# Pond Scanner Report
**Scan time:** 2026-07-20 19:57 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -305.6% | $12,003,315 |
| 🟢 | PF_KAITOUSD | -176.6% | $530,842 |
| 🟢 | PF_ALCHUSD | +125.8% | $629,120 |
| 🟢 | PF_SUSD | +106.7% | $1,150,838 |
| 🟢 | PF_NEARUSD | -101.5% | $884,104 |
| 🟢 | PF_TRUMPUSD | -78.3% | $1,250,817 |
| ⚪ | PF_JTOUSD | +26.3% | $1,457,314 |
| ⚪ | PF_SYNUSD | -20.8% | $2,322,536 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → gemini) — coinbase: $65,115.47, kraken: $65,122.70, gemini: $65,130.40
- ⚪ **ETH** gap **0.007%** (kraken → coinbase) — coinbase: $1,899.60, kraken: $1,899.47, gemini: $1,899.49

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.40, realized vol 10d 33% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.49, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
