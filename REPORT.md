# Pond Scanner Report
**Scan time:** 2026-08-12 02:45 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HFTUSD | -157.3% | $2,045,896 |
| 🟢 | PF_MOODENGUSD | +112.9% | $1,569,137 |
| 🟢 | PF_UNIUSD | -103.9% | $1,330,788 |
| 🟢 | PF_RUNEUSD | +64.1% | $642,191 |
| 🟢 | PF_JUPUSD | -47.8% | $1,743,431 |
| ⚪ | PF_TRUMPUSD | +28.1% | $567,067 |
| ⚪ | PF_CRVUSD | -27.8% | $11,130,375 |
| ⚪ | PF_SYNUSD | -23.1% | $1,989,956 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → gemini) — coinbase: $63,710.83, kraken: $63,711.10, gemini: $63,716.83
- ⚪ **ETH** gap **0.011%** (gemini → coinbase) — coinbase: $1,883.54, kraken: $1,883.47, gemini: $1,883.34

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #275 | $89.9M | 1.15x | +30.8% |
| Tutorial (TUT) | #382 | $59.3M | 1.03x | -33.7% |
| Prom (PROM) | #415 | $53.4M | 0.66x | -16.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 14% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 20% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 28% (0.8x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 39% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -103.9% | 116.0% |
| PF_RUNEUSD | 2 | +64.1% | 90.2% |
| PF_JUPUSD | 2 | -47.8% | 51.9% |
| PF_HFTUSD | 1 | -157.3% | 157.3% |
| PF_MOODENGUSD | 1 | +112.9% | 112.9% |

**Resolved since last scan:** PF_KAITOUSD (crowded 2d, worst 704%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
