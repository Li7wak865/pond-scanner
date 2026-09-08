# Pond Scanner Report
**Scan time:** 2026-09-08 21:10 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -246.3% | $1,732,574 |
| 🟢 | PF_INJUSD | -236.2% | $518,394 |
| 🟢 | PF_UNIUSD | -140.2% | $743,747 |
| 🟢 | PF_TRUMPUSD | -77.4% | $764,022 |
| 🟢 | PF_ACEUSD | -47.0% | $2,083,531 |
| 🟢 | PF_FILUSD | -45.9% | $1,177,979 |
| 🟢 | PF_BATUSD | -44.1% | $553,757 |
| 🟢 | PF_CATIUSD | -38.8% | $862,960 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (coinbase → kraken) — coinbase: $78,540.33, kraken: $78,546.20, gemini: $78,543.75
- ⚪ **ETH** gap **0.025%** (gemini → coinbase) — coinbase: $2,485.23, kraken: $2,485.08, gemini: $2,484.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.33, realized vol 10d 37% vs 60d 39%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 40% (0.8x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 54% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -77.4% | 476.2% |
| PF_INJUSD | 2 | -236.2% | 604.5% |
| PF_ACEUSD | 2 | -47.0% | 289.3% |
| PF_NEARUSD | 1 | -246.3% | 246.3% |
| PF_UNIUSD | 1 | -140.2% | 215.3% |
| PF_FILUSD | 1 | -45.9% | 45.9% |
| PF_BATUSD | 1 | -44.1% | 44.1% |
| PF_CATIUSD | 1 | -38.8% | 38.8% |
| PF_XRPUSD | 1 | -34.1% | 47.1% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 1d, worst 91%), PF_JTOUSD (crowded 1d, worst 50%), PF_SUIUSD (crowded 1d, worst 45%), PF_DOTUSD (crowded 1d, worst 55%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
