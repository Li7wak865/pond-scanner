# Pond Scanner Report
**Scan time:** 2026-09-09 11:25 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +361.6% | $781,218 |
| 🟢 | PF_LINKUSD | -153.3% | $538,692 |
| 🟢 | PF_PROMPTUSD | -101.0% | $573,093 |
| 🟢 | PF_NEARUSD | -92.2% | $2,117,716 |
| 🟢 | PF_CATIUSD | -85.2% | $855,733 |
| 🟢 | PF_ATOMUSD | -77.0% | $942,378 |
| 🟢 | PF_ACEUSD | -64.2% | $1,381,130 |
| 🟢 | PF_DOTUSD | +53.9% | $5,065,759 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → gemini) — coinbase: $78,910.52, kraken: $78,916.90, gemini: $78,931.50
- ⚪ **ETH** gap **0.142%** (gemini → kraken) — coinbase: $2,489.82, kraken: $2,490.35, gemini: $2,486.82

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 4Stock (4STOCK) | #425 | $55.9M | 2.46x | +48.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 37% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.17, realized vol 10d 38% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 40% (0.9x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 54% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -92.2% | 246.3% |
| PF_UNIUSD | 1 | +361.6% | 361.6% |
| PF_LINKUSD | 1 | -153.3% | 153.3% |
| PF_PROMPTUSD | 1 | -101.0% | 101.0% |
| PF_CATIUSD | 1 | -85.2% | 85.2% |
| PF_ATOMUSD | 1 | -77.0% | 77.0% |
| PF_ACEUSD | 1 | -64.2% | 64.2% |
| PF_DOTUSD | 1 | +53.9% | 53.9% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 6d, worst 476%), PF_FILUSD (crowded 2d, worst 46%), PF_SUIUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
