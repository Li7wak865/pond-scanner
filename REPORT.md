# Pond Scanner Report
**Scan time:** 2026-08-04 19:57 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -71.3% | $1,105,494 |
| 🟢 | PF_KAITOUSD | -70.6% | $885,308 |
| 🟢 | PF_SOLUSD | -54.7% | $588,128 |
| 🟢 | PF_ZEREBROUSD | -41.5% | $3,895,142 |
| 🟢 | PF_SYNUSD | -31.0% | $2,704,506 |
| ⚪ | PF_ETHFIUSD | -26.6% | $986,832 |
| ⚪ | PF_COTIUSD | -23.3% | $31,505,276 |
| ⚪ | PF_JTOUSD | +22.6% | $508,411 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (gemini → kraken) — coinbase: $64,255.37, kraken: $64,265.20, gemini: $64,246.10
- ⚪ **ETH** gap **0.023%** (gemini → coinbase) — coinbase: $1,876.63, kraken: $1,876.32, gemini: $1,876.19

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #447 | $45.3M | 0.93x | +24.1% |
| SkyAI (SKYAI) | #403 | $52.7M | 0.82x | +35.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 28% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 42% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 32% (0.9x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -70.6% | 135.4% |
| PF_UNIUSD | 1 | -71.3% | 71.3% |
| PF_SOLUSD | 1 | -54.7% | 54.7% |
| PF_ZEREBROUSD | 1 | -41.5% | 41.5% |
| PF_SYNUSD | 1 | -31.0% | 69.5% |

**Resolved since last scan:** PF_ARCUSD (crowded 1d, worst 238%), PF_SUSD (crowded 1d, worst 99%), PF_COTIUSD (crowded 1d, worst 63%), PF_ETHFIUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
