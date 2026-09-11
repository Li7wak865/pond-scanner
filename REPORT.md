# Pond Scanner Report
**Scan time:** 2026-09-11 04:42 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +271.3% | $1,402,437 |
| 🟢 | PF_ATOMUSD | +102.1% | $665,465 |
| 🟢 | PF_RUNEUSD | -44.3% | $615,287 |
| 🟢 | PF_APTUSD | +35.6% | $794,043 |
| 🟢 | PF_VIRTUALUSD | -35.2% | $543,222 |
| ⚪ | PF_NEARUSD | +28.2% | $1,840,877 |
| ⚪ | PF_ETHFIUSD | -18.3% | $992,677 |
| ⚪ | PF_XRPUSD | -17.6% | $33,080,882 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (gemini → coinbase) — coinbase: $77,101.29, kraken: $77,099.30, gemini: $77,095.81
- ⚪ **ETH** gap **0.009%** (gemini → kraken) — coinbase: $2,459.36, kraken: $2,459.45, gemini: $2,459.22

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Bifrost (BFC) | #423 | $53.4M | 2.41x | +19.7% |
| VeThor (VTHO) | #430 | $53.1M | 2.41x | -28.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.00, realized vol 10d 38% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 36% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 41% (0.8x)
- ⚪ **ETH** 24h vol 50% vs 30d norm 55% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +271.3% | 361.6% |
| PF_ATOMUSD | 2 | +102.1% | 122.6% |
| PF_RUNEUSD | 2 | -44.3% | 44.3% |
| PF_APTUSD | 2 | +35.6% | 42.7% |
| PF_VIRTUALUSD | 1 | -35.2% | 35.2% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 565%), PF_RAYUSD (crowded 2d, worst 373%), PF_OPNUSD (crowded 2d, worst 122%), PF_TRUMPUSD (crowded 3d, worst 508%), PF_NEARUSD (crowded 4d, worst 246%), PF_DOTUSD (crowded 2d, worst 58%), PF_CATIUSD (crowded 2d, worst 37%), PF_SWARMSUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
