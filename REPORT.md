# Pond Scanner Report
**Scan time:** 2026-09-15 11:45 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -812.2% | $5,752,061 |
| 🟢 | PF_INITUSD | +301.6% | $538,610 |
| 🟢 | PF_ACEUSD | -175.3% | $1,893,085 |
| 🟢 | PF_POWRUSD | -98.0% | $935,455 |
| 🟢 | PF_TRUMPUSD | -56.2% | $502,161 |
| ⚪ | PF_ASTRUSD | -24.8% | $17,091,273 |
| ⚪ | PF_UNIUSD | -17.8% | $1,103,159 |
| ⚪ | PF_MINAUSD | -17.6% | $832,078 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (kraken → gemini) — coinbase: $76,880.92, kraken: $76,879.30, gemini: $76,888.58
- ⚪ **ETH** gap **0.020%** (kraken → gemini) — coinbase: $2,474.44, kraken: $2,474.32, gemini: $2,474.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #290 | $90.9M | 1.43x | -50.5% |
| Threshold Network (T) | #429 | $53.0M | 1.16x | -16.5% |
| Astar (ASTR) | #390 | $61.6M | 1.11x | +15.6% |
| Teller (DEBIT) | #459 | $47.4M | 0.84x | -15.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 23% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 30% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 42% (0.7x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 59% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -812.2% | 896.9% |
| PF_INITUSD | 1 | +301.6% | 301.6% |
| PF_ACEUSD | 1 | -175.3% | 175.3% |
| PF_POWRUSD | 1 | -98.0% | 115.8% |
| PF_TRUMPUSD | 1 | -56.2% | 125.4% |

**Resolved since last scan:** PF_HFTUSD (crowded 2d, worst 65%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
