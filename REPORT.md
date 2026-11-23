# Pond Scanner Report
**Scan time:** 2026-11-23 07:41 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | +786.5% | $23,444,688 |
| 🟢 | PF_UNIUSD | -54.1% | $530,977 |
| 🟢 | PF_JTOUSD | -34.1% | $660,845 |
| ⚪ | PF_ETHFIUSD | -29.9% | $1,068,164 |
| ⚪ | PF_NEARUSD | +27.7% | $1,886,833 |
| ⚪ | PF_BBUSD | +22.1% | $2,683,988 |
| ⚪ | PF_FETUSD | -20.5% | $4,831,275 |
| ⚪ | PF_TRUMPUSD | -17.5% | $645,516 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.042%** (coinbase → gemini) — coinbase: $61,402.47, kraken: $61,402.80, gemini: $61,428.01
- ⚪ **ETH** gap **0.113%** (coinbase → gemini) — coinbase: $1,720.47, kraken: $1,720.54, gemini: $1,722.41

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 52% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 77% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9949 (-0.51% vs peg)
- ⚪ **USDT** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 60% vs 30d norm 52% (1.2x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 65% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 7 | -54.1% | 222.0% |
| PF_ACEUSD | 2 | +786.5% | 786.5% |
| PF_JTOUSD | 1 | -34.1% | 34.1% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 2d, worst 52%), PF_NEARUSD (crowded 2d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
