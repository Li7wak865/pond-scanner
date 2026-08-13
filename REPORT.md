# Pond Scanner Report
**Scan time:** 2026-08-13 19:26 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ETHFIUSD | -85.9% | $618,787 |
| 🟢 | PF_KAITOUSD | -65.1% | $1,718,667 |
| 🟢 | PF_GPSUSD | +46.8% | $9,339,046 |
| ⚪ | PF_VIRTUALUSD | +27.4% | $1,404,547 |
| ⚪ | PF_COTIUSD | -26.6% | $50,255,531 |
| ⚪ | PF_JTOUSD | -20.5% | $596,070 |
| ⚪ | PF_HFTUSD | -19.1% | $3,658,141 |
| ⚪ | PF_NEARUSD | -17.5% | $1,248,278 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.038%** (kraken → gemini) — coinbase: $63,358.64, kraken: $63,340.60, gemini: $63,364.79
- ⚪ **ETH** gap **0.024%** (gemini → coinbase) — coinbase: $1,886.03, kraken: $1,885.84, gemini: $1,885.57

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #389 | $55.4M | 2.50x | -17.6% |
| Acurast (ACU) | #458 | $45.5M | 0.65x | +35.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 14% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 18% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 27% (0.9x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 37% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -65.1% | 946.7% |
| PF_ETHFIUSD | 1 | -85.9% | 85.9% |
| PF_GPSUSD | 1 | +46.8% | 46.8% |

**Resolved since last scan:** PF_MONUSD (crowded 1d, worst 96%), PF_RENDERUSD (crowded 1d, worst 91%), PF_IOTAUSD (crowded 1d, worst 63%), PF_MOODENGUSD (crowded 1d, worst 59%), PF_COTIUSD (crowded 2d, worst 58%), PF_HFTUSD (crowded 1d, worst 137%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
