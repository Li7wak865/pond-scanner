# Pond Scanner Report
**Scan time:** 2026-08-14 07:51 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +236.7% | $529,159 |
| 🟢 | PF_UNIUSD | +129.8% | $557,544 |
| 🟢 | PF_KAITOUSD | -75.1% | $1,774,857 |
| 🟢 | PF_SAGAUSD | +56.1% | $7,436,766 |
| 🟢 | PF_VIRTUALUSD | +42.6% | $984,832 |
| 🟢 | PF_ACEUSD | -35.5% | $11,872,650 |
| ⚪ | PF_NEARUSD | +23.3% | $1,284,634 |
| ⚪ | PF_STORJUSD | -22.7% | $2,574,750 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.033%** (coinbase → kraken) — coinbase: $62,907.70, kraken: $62,928.30, gemini: $62,909.91
- ⚪ **ETH** gap **0.094%** (gemini → kraken) — coinbase: $1,873.34, kraken: $1,873.67, gemini: $1,871.91

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #445 | $46.6M | 2.35x | +15.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.13, realized vol 10d 13% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.00, realized vol 10d 18% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 27% (0.9x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 36% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +236.7% | 236.7% |
| PF_UNIUSD | 1 | +129.8% | 129.8% |
| PF_KAITOUSD | 1 | -75.1% | 75.1% |
| PF_SAGAUSD | 1 | +56.1% | 56.1% |
| PF_VIRTUALUSD | 1 | +42.6% | 42.6% |
| PF_ACEUSD | 1 | -35.5% | 35.5% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 2d, worst 86%), PF_HFTUSD (crowded 1d, worst 48%), PF_GRASSUSD (crowded 1d, worst 36%), PF_JUPUSD (crowded 1d, worst 34%), PF_NEARUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
