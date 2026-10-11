# Pond Scanner Report
**Scan time:** 2026-10-11 05:48 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_FILUSD | -65.1% | $1,593,678 |
| 🟢 | PF_SUIUSD | +37.6% | $5,266,168 |
| 🟢 | PF_DOTUSD | +35.0% | $1,236,674 |
| 🟢 | PF_NEARUSD | +31.8% | $2,529,240 |
| ⚪ | PF_TIAUSD | +27.7% | $2,609,183 |
| ⚪ | PF_WLDUSD | +21.4% | $2,198,837 |
| ⚪ | PF_KAIAUSD | -19.4% | $6,481,345 |
| ⚪ | PF_JTOUSD | +12.8% | $1,349,639 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → gemini) — coinbase: $82,975.16, kraken: $82,979.40, gemini: $82,983.01
- ⚪ **ETH** gap **0.027%** (coinbase → gemini) — coinbase: $2,502.56, kraken: $2,502.73, gemini: $2,503.24

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.26, realized vol 10d 25% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.51, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 17% vs 30d norm 45% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_FILUSD | 2 | -65.1% | 65.1% |
| PF_DOTUSD | 2 | +35.0% | 53.0% |
| PF_NEARUSD | 2 | +31.8% | 44.5% |
| PF_SUIUSD | 1 | +37.6% | 37.6% |

**Resolved since last scan:** PF_ATOMUSD (crowded 2d, worst 212%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
