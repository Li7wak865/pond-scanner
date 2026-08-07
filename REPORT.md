# Pond Scanner Report
**Scan time:** 2026-08-07 00:16 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -358.3% | $13,972,871 |
| 🟢 | PF_KAITOUSD | +124.5% | $586,599 |
| 🟢 | PF_UNIUSD | -53.5% | $1,638,458 |
| 🟢 | PF_SYNUSD | -53.4% | $2,459,681 |
| 🟢 | PF_BICOUSD | +51.5% | $32,154,084 |
| 🟢 | PF_GRIFFAINUSD | +42.4% | $1,957,994 |
| ⚪ | PF_NEARUSD | +28.4% | $2,130,158 |
| ⚪ | PF_ZBTUSD | -25.1% | $3,225,239 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (gemini → kraken) — coinbase: $64,196.24, kraken: $64,198.30, gemini: $64,183.95
- ⚪ **ETH** gap **0.053%** (gemini → coinbase) — coinbase: $1,899.54, kraken: $1,898.82, gemini: $1,898.54

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| ZEROBASE (ZBT) | #390 | $55.4M | 3.11x | +45.1% |
| SkyAI (SKYAI) | #249 | $103.6M | 0.67x | +62.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 27% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 30% (0.6x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 41% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -53.5% | 144.4% |
| PF_SYNUSD | 2 | -53.4% | 53.5% |
| PF_ACEUSD | 1 | -358.3% | 358.3% |
| PF_KAITOUSD | 1 | +124.5% | 124.5% |
| PF_BICOUSD | 1 | +51.5% | 51.5% |
| PF_GRIFFAINUSD | 1 | +42.4% | 42.4% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 458%), PF_ZIGUSD (crowded 2d, worst 84%), PF_SUSD (crowded 2d, worst 68%), PF_MOODENGUSD (crowded 2d, worst 53%), PF_AXSUSD (crowded 2d, worst 44%), PF_HFTUSD (crowded 2d, worst 38%), PF_NEARUSD (crowded 2d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
