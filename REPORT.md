# Pond Scanner Report
**Scan time:** 2026-09-09 04:44 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -91.4% | $1,541,207 |
| 🟢 | PF_TRUMPUSD | -55.4% | $646,170 |
| 🟢 | PF_FILUSD | -35.2% | $638,271 |
| 🟢 | PF_ATOMUSD | +31.1% | $719,145 |
| 🟢 | PF_SUIUSD | -30.7% | $7,650,529 |
| ⚪ | PF_WLDUSD | +29.7% | $3,498,492 |
| ⚪ | PF_MINAUSD | -29.6% | $1,122,740 |
| ⚪ | PF_DOTUSD | +25.5% | $4,918,458 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → gemini) — coinbase: $79,102.69, kraken: $79,103.50, gemini: $79,124.10
- ⚪ **ETH** gap **0.016%** (kraken → coinbase) — coinbase: $2,505.52, kraken: $2,505.11, gemini: $2,505.22

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 37% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 38% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 40% (0.7x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 54% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 6 | -55.4% | 476.2% |
| PF_NEARUSD | 2 | -91.4% | 246.3% |
| PF_FILUSD | 2 | -35.2% | 45.9% |
| PF_ATOMUSD | 1 | +31.1% | 31.1% |
| PF_SUIUSD | 1 | -30.7% | 30.7% |

**Resolved since last scan:** PF_INJUSD (crowded 3d, worst 604%), PF_UNIUSD (crowded 2d, worst 215%), PF_ACEUSD (crowded 3d, worst 289%), PF_BATUSD (crowded 2d, worst 44%), PF_CATIUSD (crowded 2d, worst 39%), PF_XRPUSD (crowded 2d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
