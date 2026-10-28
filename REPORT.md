# Pond Scanner Report
**Scan time:** 2026-10-28 12:57 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -141.8% | $2,060,090 |
| 🟢 | PF_GRASSUSD | +77.6% | $526,797 |
| 🟢 | PF_APTUSD | -52.9% | $941,130 |
| 🟢 | PF_ARCUSD | -42.9% | $984,273 |
| 🟢 | PF_SUIUSD | -34.1% | $2,876,459 |
| 🟢 | PF_SYNUSD | +30.1% | $1,418,955 |
| ⚪ | PF_DOTUSD | -27.3% | $1,655,464 |
| ⚪ | PF_SPXUSD | -22.7% | $519,051 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → kraken) — coinbase: $80,617.47, kraken: $80,632.90, gemini: $80,630.17
- ⚪ **ETH** gap **0.020%** (coinbase → gemini) — coinbase: $2,336.14, kraken: $2,336.35, gemini: $2,336.61

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Initia (INIT) | #473 | $48.5M | 1.13x | +39.3% |
| Dolphin (POD) | #480 | $48.0M | 0.89x | -15.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 24% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 27% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9993 (-0.07% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 31% (0.8x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -141.8% | 141.8% |
| PF_GRASSUSD | 1 | +77.6% | 77.6% |
| PF_APTUSD | 1 | -52.9% | 52.9% |
| PF_ARCUSD | 1 | -42.9% | 42.9% |
| PF_SUIUSD | 1 | -34.1% | 34.1% |
| PF_SYNUSD | 1 | +30.1% | 30.1% |

**Resolved since last scan:** PF_BBUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
