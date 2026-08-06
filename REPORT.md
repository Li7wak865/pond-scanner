# Pond Scanner Report
**Scan time:** 2026-08-06 03:39 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +766.4% | $937,799 |
| 🟢 | PF_AXSUSD | +30.2% | $619,972 |
| ⚪ | PF_XRPUSD | -22.1% | $35,390,233 |
| ⚪ | PF_SYNUSD | -21.5% | $7,071,867 |
| ⚪ | PF_APTUSD | +21.5% | $573,188 |
| ⚪ | PF_APEUSD | +21.2% | $681,647 |
| ⚪ | PF_NEARUSD | -16.6% | $1,205,751 |
| ⚪ | PF_ETHFIUSD | -16.4% | $780,959 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → gemini) — coinbase: $64,482.19, kraken: $64,479.50, gemini: $64,490.00
- ⚪ **ETH** gap **0.028%** (gemini → coinbase) — coinbase: $1,896.40, kraken: $1,896.15, gemini: $1,895.86

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Bless (BLESS) | #459 | $43.9M | 0.94x | +112.2% |
| Cap (CAP) | #418 | $50.2M | 0.61x | +22.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.10, realized vol 10d 29% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 30% (0.5x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +766.4% | 766.4% |
| PF_AXSUSD | 1 | +30.2% | 30.2% |

**Resolved since last scan:** PF_ZIGUSD (crowded 2d, worst 192%), PF_KAITOUSD (crowded 2d, worst 81%), PF_SYNUSD (crowded 2d, worst 61%), PF_XRPUSD (crowded 2d, worst 40%), PF_APTUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
