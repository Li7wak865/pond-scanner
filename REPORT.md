# Pond Scanner Report
**Scan time:** 2026-07-26 19:35 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | +103.5% | $728,954 |
| 🟢 | PF_SYNUSD | -51.0% | $3,240,460 |
| ⚪ | PF_ACEUSD | -28.9% | $868,181 |
| ⚪ | PF_NEARUSD | +26.3% | $633,061 |
| ⚪ | PF_STXUSD | -24.1% | $613,112 |
| ⚪ | PF_DOTUSD | +23.5% | $853,533 |
| ⚪ | PF_SUSHIUSD | -13.8% | $707,842 |
| ⚪ | PF_MOODENGUSD | +12.9% | $2,153,568 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.035%** (kraken → gemini) — coinbase: $64,681.47, kraken: $64,677.50, gemini: $64,699.82
- ⚪ **ETH** gap **0.033%** (kraken → gemini) — coinbase: $1,913.88, kraken: $1,913.65, gemini: $1,914.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #396 | $62.6M | 2.88x | +50.0% |
| Espresso (ESP) | #365 | $64.7M | 0.97x | +29.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 21% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 28% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 10% vs 30d norm 33% (0.3x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 44% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 1 | +103.5% | 155.2% |
| PF_SYNUSD | 1 | -51.0% | 51.0% |

**Resolved since last scan:** PF_AVAXUSD (crowded 1d, worst 96%), PF_PNUTUSD (crowded 1d, worst 37%), PF_ACEUSD (crowded 1d, worst 34%), PF_XRPUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
