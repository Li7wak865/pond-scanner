# Pond Scanner Report
**Scan time:** 2026-08-14 02:46 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +80.6% | $541,608 |
| 🟢 | PF_ETHFIUSD | -64.4% | $934,957 |
| 🟢 | PF_HFTUSD | +48.5% | $5,380,866 |
| 🟢 | PF_GRASSUSD | -35.6% | $567,230 |
| 🟢 | PF_VIRTUALUSD | +35.0% | $1,069,715 |
| 🟢 | PF_JUPUSD | +34.4% | $535,681 |
| 🟢 | PF_NEARUSD | +34.4% | $1,371,083 |
| ⚪ | PF_GOATUSD | +23.6% | $680,440 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (coinbase → kraken) — coinbase: $63,465.00, kraken: $63,466.80, gemini: $63,466.21
- ⚪ **ETH** gap **0.030%** (gemini → kraken) — coinbase: $1,887.04, kraken: $1,887.21, gemini: $1,886.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 13% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 18% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 27% (0.8x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 36% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ETHFIUSD | 2 | -64.4% | 85.9% |
| PF_UNIUSD | 1 | +80.6% | 80.6% |
| PF_HFTUSD | 1 | +48.5% | 48.5% |
| PF_GRASSUSD | 1 | -35.6% | 35.6% |
| PF_VIRTUALUSD | 1 | +35.0% | 35.0% |
| PF_JUPUSD | 1 | +34.4% | 34.4% |
| PF_NEARUSD | 1 | +34.4% | 34.4% |

**Resolved since last scan:** PF_KAITOUSD (crowded 3d, worst 947%), PF_GPSUSD (crowded 2d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
