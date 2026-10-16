# Pond Scanner Report
**Scan time:** 2026-10-16 04:33 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -402.0% | $576,312 |
| 🟢 | PF_NEARUSD | -145.4% | $4,877,505 |
| 🟢 | PF_LINKUSD | +78.4% | $625,108 |
| 🟢 | PF_TIAUSD | -71.3% | $2,115,158 |
| 🟢 | PF_BATUSD | -45.5% | $4,035,585 |
| 🟢 | PF_FILUSD | +36.6% | $2,821,279 |
| 🟢 | PF_STXUSD | -34.9% | $1,162,320 |
| 🟢 | PF_WLDUSD | +30.8% | $4,334,587 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → coinbase) — coinbase: $82,008.40, kraken: $82,002.90, gemini: $82,006.23
- ⚪ **ETH** gap **0.043%** (coinbase → gemini) — coinbase: $2,438.82, kraken: $2,438.92, gemini: $2,439.86

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 29% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 45% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 55% vs 30d norm 34% (1.6x)
- ⚪ **ETH** 24h vol 71% vs 30d norm 42% (1.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +78.4% | 403.5% |
| PF_NEARUSD | 2 | -145.4% | 178.9% |
| PF_BATUSD | 2 | -45.5% | 45.5% |
| PF_INJUSD | 1 | -402.0% | 402.0% |
| PF_TIAUSD | 1 | -71.3% | 71.3% |
| PF_FILUSD | 1 | +36.6% | 36.6% |
| PF_STXUSD | 1 | -34.9% | 34.9% |
| PF_WLDUSD | 1 | +30.8% | 30.8% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 582%), PF_ATOMUSD (crowded 2d, worst 116%), PF_TRUMPUSD (crowded 2d, worst 69%), PF_GRASSUSD (crowded 2d, worst 41%), PF_XRPUSD (crowded 2d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
