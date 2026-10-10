# Pond Scanner Report
**Scan time:** 2026-10-10 21:45 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ATOMUSD | -211.8% | $540,851 |
| 🟢 | PF_NEARUSD | +44.5% | $3,252,899 |
| 🟢 | PF_DOTUSD | +38.3% | $1,753,767 |
| 🟢 | PF_FILUSD | -31.2% | $1,802,295 |
| ⚪ | PF_WLDUSD | +28.4% | $2,332,949 |
| ⚪ | PF_TIAUSD | -28.0% | $2,127,554 |
| ⚪ | PF_JTOUSD | +26.3% | $1,425,928 |
| ⚪ | PF_SUIUSD | -24.8% | $5,433,561 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (kraken → coinbase) — coinbase: $83,015.63, kraken: $83,014.00, gemini: $83,015.56
- ⚪ **ETH** gap **0.010%** (kraken → coinbase) — coinbase: $2,507.98, kraken: $2,507.74, gemini: $2,507.86

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 27% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 38% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 8% vs 30d norm 34% (0.2x)
- ⚪ **ETH** 24h vol 13% vs 30d norm 45% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ATOMUSD | 1 | -211.8% | 211.8% |
| PF_NEARUSD | 1 | +44.5% | 44.5% |
| PF_DOTUSD | 1 | +38.3% | 53.0% |
| PF_FILUSD | 1 | -31.2% | 31.2% |

**Resolved since last scan:** PF_KAIAUSD (crowded 2d, worst 251%), PF_WLDUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
