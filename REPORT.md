# Pond Scanner Report
**Scan time:** 2026-07-21 03:46 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +457.0% | $725,386 |
| 🟢 | PF_ALCHUSD | +97.0% | $704,733 |
| 🟢 | PF_ZEREBROUSD | -66.9% | $3,501,692 |
| 🟢 | PF_ACEUSD | -46.9% | $10,641,205 |
| 🟢 | PF_SYNUSD | -41.9% | $2,086,732 |
| 🟢 | PF_TRUMPUSD | -34.7% | $881,655 |
| 🟢 | PF_ETHFIUSD | -34.4% | $529,742 |
| 🟢 | PF_JUPUSD | +31.3% | $584,003 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (kraken → gemini) — coinbase: $65,453.29, kraken: $65,449.80, gemini: $65,464.46
- ⚪ **ETH** gap **0.013%** (kraken → coinbase) — coinbase: $1,924.23, kraken: $1,923.98, gemini: $1,924.17

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.36, realized vol 10d 32% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
