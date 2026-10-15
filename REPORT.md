# Pond Scanner Report
**Scan time:** 2026-10-15 21:23 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -581.9% | $565,029 |
| 🟢 | PF_LINKUSD | +216.3% | $864,473 |
| 🟢 | PF_NEARUSD | -178.9% | $5,137,883 |
| 🟢 | PF_ATOMUSD | -115.6% | $538,672 |
| 🟢 | PF_TRUMPUSD | -42.7% | $1,162,566 |
| 🟢 | PF_GRASSUSD | +41.3% | $784,976 |
| 🟢 | PF_BATUSD | +35.4% | $2,994,249 |
| 🟢 | PF_XRPUSD | +32.2% | $22,533,553 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → kraken) — coinbase: $82,205.15, kraken: $82,215.10, gemini: $82,213.93
- ⚪ **ETH** gap **0.024%** (coinbase → gemini) — coinbase: $2,454.14, kraken: $2,454.40, gemini: $2,454.72

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nexpace (NXPC) | #355 | $71.3M | 0.59x | +16.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.11, realized vol 10d 29% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.33, realized vol 10d 46% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 58% vs 30d norm 34% (1.7x)
- ⚪ **ETH** 24h vol 79% vs 30d norm 42% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | +216.3% | 403.5% |
| PF_SOLUSD | 1 | -581.9% | 581.9% |
| PF_NEARUSD | 1 | -178.9% | 178.9% |
| PF_ATOMUSD | 1 | -115.6% | 115.6% |
| PF_TRUMPUSD | 1 | -42.7% | 68.6% |
| PF_GRASSUSD | 1 | +41.3% | 41.3% |
| PF_BATUSD | 1 | +35.4% | 35.4% |
| PF_XRPUSD | 1 | +32.2% | 41.2% |

**Resolved since last scan:** PF_ZROUSD (crowded 1d, worst 247%), PF_TIAUSD (crowded 1d, worst 67%), PF_SUIUSD (crowded 1d, worst 41%), PF_STXUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
