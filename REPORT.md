# Pond Scanner Report
**Scan time:** 2026-09-17 11:43 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -311.9% | $1,558,643 |
| 🟢 | PF_NEARUSD | +133.9% | $4,281,913 |
| 🟢 | PF_NATGASUSD | +100.5% | $593,744 |
| 🟢 | PF_SYNUSD | -85.8% | $9,477,392 |
| 🟢 | PF_TRUMPUSD | -54.1% | $544,294 |
| 🟢 | PF_ETHFIUSD | +41.9% | $530,449 |
| 🟢 | PF_SWARMSUSD | +30.7% | $890,845 |
| ⚪ | PF_KAITOUSD | +27.7% | $516,235 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $76,153.03, kraken: $76,156.50, gemini: $76,167.64
- ⚪ **ETH** gap **0.021%** (gemini → coinbase) — coinbase: $2,427.78, kraken: $2,427.70, gemini: $2,427.28

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #251 | $113.8M | 1.53x | -28.3% |
| Hunter Biden's Laptop (LAPTOP) | #459 | $47.2M | 0.50x | -38.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 27% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **PYUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 43% (0.6x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 60% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +133.9% | 133.9% |
| PF_SYNUSD | 2 | -85.8% | 85.8% |
| PF_TRUMPUSD | 2 | -54.1% | 95.6% |
| PF_UNIUSD | 1 | -311.9% | 311.9% |
| PF_NATGASUSD | 1 | +100.5% | 100.5% |
| PF_ETHFIUSD | 1 | +41.9% | 41.9% |
| PF_SWARMSUSD | 1 | +30.7% | 30.7% |

**Resolved since last scan:** PF_LSKUSD (crowded 4d, worst 897%), PF_ICXUSD (crowded 2d, worst 48%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
