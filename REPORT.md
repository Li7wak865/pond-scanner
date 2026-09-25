# Pond Scanner Report
**Scan time:** 2026-09-25 04:59 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MINAUSD | +432.8% | $706,414 |
| 🟢 | PF_LINKUSD | +152.0% | $695,984 |
| 🟢 | PF_TRUMPUSD | +130.4% | $1,099,333 |
| 🟢 | PF_OGNUSD | +85.5% | $807,173 |
| 🟢 | PF_UNIUSD | +84.4% | $641,342 |
| 🟢 | PF_NEARUSD | +72.8% | $5,408,714 |
| 🟢 | PF_LSKUSD | -61.3% | $3,422,450 |
| 🟢 | PF_KAITOUSD | -46.7% | $664,326 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (gemini → coinbase) — coinbase: $84,183.50, kraken: $84,180.50, gemini: $84,163.61
- ⚪ **ETH** gap **0.034%** (gemini → coinbase) — coinbase: $2,679.35, kraken: $2,679.18, gemini: $2,678.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #429 | $58.5M | 1.64x | -16.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.19, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 40% vs 30d norm 35% (1.1x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 47% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +130.4% | 372.6% |
| PF_NEARUSD | 3 | +72.8% | 343.9% |
| PF_LINKUSD | 2 | +152.0% | 482.7% |
| PF_VIRTUALUSD | 2 | -36.0% | 57.1% |
| PF_MINAUSD | 1 | +432.8% | 432.8% |
| PF_OGNUSD | 1 | +85.5% | 85.5% |
| PF_UNIUSD | 1 | +84.4% | 84.4% |
| PF_LSKUSD | 1 | -61.3% | 61.3% |
| PF_KAITOUSD | 1 | -46.7% | 46.7% |
| PF_FILUSD | 1 | +40.7% | 40.7% |
| PF_SOLUSD | 1 | +36.3% | 36.3% |

**Resolved since last scan:** PF_HFTUSD (crowded 3d, worst 112%), PF_SPXUSD (crowded 3d, worst 83%), PF_ZROUSD (crowded 2d, worst 70%), PF_XPLUSD (crowded 2d, worst 54%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
