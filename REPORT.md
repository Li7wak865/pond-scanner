# Pond Scanner Report
**Scan time:** 2026-09-11 11:23 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | -260.9% | $1,189,511 |
| 🟢 | PF_LSKUSD | -171.4% | $577,406 |
| 🟢 | PF_UNIUSD | +166.6% | $1,408,933 |
| 🟢 | PF_APTUSD | +43.7% | $919,576 |
| 🟢 | PF_DOTUSD | +40.5% | $3,035,395 |
| 🟢 | PF_ATOMUSD | +34.6% | $502,384 |
| ⚪ | PF_ASTERUSD | +29.9% | $670,694 |
| ⚪ | PF_RUNEUSD | -22.8% | $719,991 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (kraken → coinbase) — coinbase: $76,772.96, kraken: $76,770.90, gemini: $76,771.03
- ⚪ **ETH** gap **0.043%** (gemini → coinbase) — coinbase: $2,453.36, kraken: $2,453.19, gemini: $2,452.31

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 38% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 36% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 41% (0.8x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 55% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +166.6% | 361.6% |
| PF_APTUSD | 2 | +43.7% | 43.7% |
| PF_ATOMUSD | 2 | +34.6% | 122.6% |
| PF_RAYUSD | 1 | -260.9% | 260.9% |
| PF_LSKUSD | 1 | -171.4% | 171.4% |
| PF_DOTUSD | 1 | +40.5% | 40.5% |

**Resolved since last scan:** PF_RUNEUSD (crowded 2d, worst 44%), PF_VIRTUALUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
