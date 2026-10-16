# Pond Scanner Report
**Scan time:** 2026-10-16 16:40 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -759.6% | $568,352 |
| 🟢 | PF_INJUSD | +608.3% | $567,738 |
| 🟢 | PF_ZROUSD | +219.7% | $524,565 |
| 🟢 | PF_TRUMPUSD | -64.1% | $666,236 |
| 🟢 | PF_FILUSD | -50.9% | $2,239,348 |
| ⚪ | PF_PONSUSD | -25.5% | $1,068,795 |
| ⚪ | PF_SUIUSD | +24.0% | $4,827,918 |
| ⚪ | PF_JUPUSD | -23.2% | $713,956 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (gemini → coinbase) — coinbase: $81,454.52, kraken: $81,453.70, gemini: $81,450.09
- ⚪ **ETH** gap **0.037%** (coinbase → gemini) — coinbase: $2,437.08, kraken: $2,437.31, gemini: $2,437.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Zilliqa (ZIL) | #452 | $50.9M | 0.67x | -20.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 29% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 45% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 35% (0.8x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | -759.6% | 759.6% |
| PF_INJUSD | 1 | +608.3% | 608.3% |
| PF_ZROUSD | 1 | +219.7% | 219.7% |
| PF_TRUMPUSD | 1 | -64.1% | 64.1% |
| PF_FILUSD | 1 | -50.9% | 50.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 179%), PF_TIAUSD (crowded 1d, worst 82%), PF_LINKUSD (crowded 3d, worst 403%), PF_GRASSUSD (crowded 1d, worst 51%), PF_STXUSD (crowded 1d, worst 49%), PF_XRPUSD (crowded 1d, worst 48%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
