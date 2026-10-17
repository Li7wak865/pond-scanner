# Pond Scanner Report
**Scan time:** 2026-10-17 20:37 UTC

**Flags this scan:** 1 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +108.1% | $3,100,150 |
| ⚪ | PF_TRXUSD | -19.3% | $8,683,298 |
| ⚪ | PF_EIGENUSD | -18.3% | $2,883,359 |
| ⚪ | PF_TIAUSD | +14.9% | $5,743,406 |
| ⚪ | PF_WLDUSD | -13.4% | $3,703,626 |
| ⚪ | PF_DOTUSD | -12.2% | $1,032,339 |
| ⚪ | PF_XRPUSD | +10.3% | $5,503,863 |
| ⚪ | PF_BATUSD | -9.8% | $1,568,512 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → kraken) — coinbase: $81,507.61, kraken: $81,515.60, gemini: $81,511.19
- ⚪ **ETH** gap **0.027%** (gemini → kraken) — coinbase: $2,415.81, kraken: $2,416.21, gemini: $2,415.55

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 26% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 39% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 21% vs 30d norm 42% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +108.1% | 135.7% |

**Resolved since last scan:** PF_SANDUSD (crowded 1d, worst 46%), PF_FILUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
