# Pond Scanner Report
**Scan time:** 2026-08-12 07:53 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -114.5% | $2,038,038 |
| 🟢 | PF_TRUMPUSD | -88.9% | $538,293 |
| 🟢 | PF_RUNEUSD | +75.3% | $666,119 |
| 🟢 | PF_ATOMUSD | -58.0% | $560,706 |
| 🟢 | PF_JUPUSD | -43.9% | $1,994,924 |
| ⚪ | PF_XRPUSD | +23.3% | $29,135,334 |
| ⚪ | PF_SYNUSD | -21.2% | $1,951,252 |
| ⚪ | PF_FILUSD | -19.3% | $682,973 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $63,659.19, kraken: $63,661.40, gemini: $63,667.43
- ⚪ **ETH** gap **0.039%** (kraken → coinbase) — coinbase: $1,887.54, kraken: $1,886.80, gemini: $1,886.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #333 | $70.0M | 1.44x | -30.2% |
| Tutorial (TUT) | #386 | $56.9M | 1.44x | -24.0% |
| Cap (CAP) | #279 | $86.4M | 1.18x | +17.5% |
| Prom (PROM) | #438 | $47.1M | 0.98x | +15.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 14% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 20% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 28% (0.8x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 39% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -114.5% | 116.0% |
| PF_RUNEUSD | 2 | +75.3% | 90.2% |
| PF_JUPUSD | 2 | -43.9% | 51.9% |
| PF_TRUMPUSD | 1 | -88.9% | 88.9% |
| PF_ATOMUSD | 1 | -58.0% | 58.0% |

**Resolved since last scan:** PF_HFTUSD (crowded 1d, worst 157%), PF_MOODENGUSD (crowded 1d, worst 113%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
