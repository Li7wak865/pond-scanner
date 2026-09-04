# Pond Scanner Report
**Scan time:** 2026-09-04 20:46 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +126.1% | $1,972,926 |
| 🟢 | PF_TRUMPUSD | +95.1% | $1,444,315 |
| 🟢 | PF_ACEUSD | -87.2% | $641,407 |
| 🟢 | PF_SPXUSD | -84.0% | $793,500 |
| 🟢 | PF_HFTUSD | -35.1% | $5,045,127 |
| 🟢 | PF_CRVUSD | +34.9% | $4,763,924 |
| ⚪ | PF_ICXUSD | -26.5% | $982,308 |
| ⚪ | PF_DOTUSD | +25.4% | $1,882,515 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (gemini → coinbase) — coinbase: $79,726.28, kraken: $79,726.20, gemini: $79,723.92
- ⚪ **ETH** gap **0.008%** (kraken → gemini) — coinbase: $2,453.84, kraken: $2,453.81, gemini: $2,454.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 41% vs 60d 40%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 45% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 50% vs 30d norm 40% (1.3x)
- ⚪ **ETH** 24h vol 62% vs 30d norm 54% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -87.2% | 304.8% |
| PF_NEARUSD | 1 | +126.1% | 126.1% |
| PF_TRUMPUSD | 1 | +95.1% | 196.2% |
| PF_SPXUSD | 1 | -84.0% | 209.6% |
| PF_HFTUSD | 1 | -35.1% | 54.5% |
| PF_CRVUSD | 1 | +34.9% | 34.9% |

**Resolved since last scan:** PF_SAGAUSD (crowded 1d, worst 64%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
