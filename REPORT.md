# Pond Scanner Report
**Scan time:** 2026-09-16 04:50 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -441.3% | $2,512,631 |
| 🟢 | PF_UNIUSD | +212.9% | $1,429,554 |
| 🟢 | PF_STEEMUSD | -205.3% | $555,546 |
| 🟢 | PF_NEARUSD | -68.6% | $2,218,298 |
| 🟢 | PF_ACEUSD | -63.3% | $3,156,216 |
| 🟢 | PF_VIRTUALUSD | -42.0% | $623,955 |
| ⚪ | PF_ASTERUSD | -25.8% | $547,708 |
| ⚪ | PF_SWARMSUSD | -23.8% | $759,045 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $75,820.76, kraken: $75,829.20, gemini: $75,831.04
- ⚪ **ETH** gap **0.029%** (coinbase → gemini) — coinbase: $2,403.48, kraken: $2,403.64, gemini: $2,404.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 27% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9980 (-0.20% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 43% vs 30d norm 42% (1.0x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 60% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 3 | -441.3% | 896.9% |
| PF_ACEUSD | 2 | -63.3% | 175.3% |
| PF_UNIUSD | 1 | +212.9% | 212.9% |
| PF_STEEMUSD | 1 | -205.3% | 205.3% |
| PF_NEARUSD | 1 | -68.6% | 68.6% |
| PF_VIRTUALUSD | 1 | -42.0% | 42.0% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 674%), PF_ICPUSD (crowded 2d, worst 152%), PF_HFTUSD (crowded 2d, worst 55%), PF_TRUMPUSD (crowded 2d, worst 125%), PF_XRPUSD (crowded 2d, worst 41%), PF_FILUSD (crowded 2d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
