# Pond Scanner Report
**Scan time:** 2026-08-03 19:59 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -96.9% | $1,432,878 |
| 🟢 | PF_KAITOUSD | +81.5% | $1,589,081 |
| 🟢 | PF_XRPUSD | +37.1% | $15,844,720 |
| 🟢 | PF_ACEUSD | -31.8% | $5,366,344 |
| 🟢 | PF_NEARUSD | +30.6% | $2,397,481 |
| ⚪ | PF_SYNUSD | +24.7% | $2,474,236 |
| ⚪ | PF_JTOUSD | -23.3% | $880,051 |
| ⚪ | PF_ZKUSD | +21.4% | $3,419,959 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → kraken) — coinbase: $63,850.01, kraken: $63,855.70, gemini: $63,855.42
- ⚪ **ETH** gap **0.023%** (kraken → gemini) — coinbase: $1,869.85, kraken: $1,869.43, gemini: $1,869.86

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 28% vs 60d 34%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 41% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 1 | -96.9% | 96.9% |
| PF_KAITOUSD | 1 | +81.5% | 81.5% |
| PF_XRPUSD | 1 | +37.1% | 37.1% |
| PF_ACEUSD | 1 | -31.8% | 31.8% |
| PF_NEARUSD | 1 | +30.6% | 101.2% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
