# Pond Scanner Report
**Scan time:** 2026-08-01 08:34 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +157.7% | $1,730,145 |
| 🟢 | PF_RENDERUSD | -32.4% | $672,918 |
| ⚪ | PF_SYNUSD | +28.9% | $3,036,090 |
| ⚪ | PF_NEARUSD | +26.8% | $1,240,322 |
| ⚪ | PF_COTIUSD | -16.3% | $85,264,721 |
| ⚪ | PF_ACEUSD | +14.7% | $1,008,902 |
| ⚪ | PF_SUSHIUSD | +12.0% | $698,861 |
| ⚪ | PF_MOODENGUSD | +9.8% | $987,922 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (kraken → gemini) — coinbase: $63,050.10, kraken: $63,048.20, gemini: $63,054.00
- ⚪ **ETH** gap **0.012%** (kraken → gemini) — coinbase: $1,867.04, kraken: $1,866.86, gemini: $1,867.09

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #470 | $42.1M | 4.41x | -29.3% |
| Giggle Fund (GIGGLE) | #431 | $49.1M | 3.11x | +38.9% |
| MEET48 (IDOL) | #447 | $46.2M | 0.80x | +43.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 28% vs 60d 35%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 42% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 32% (0.9x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 44% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +157.7% | 237.0% |
| PF_RENDERUSD | 1 | -32.4% | 32.4% |

**Resolved since last scan:** PF_AGLDUSD (crowded 2d, worst 645%), PF_KAITOUSD (crowded 4d, worst 326%), PF_SYNUSD (crowded 2d, worst 80%), PF_DEXEUSD (crowded 2d, worst 732%), PF_VIRTUALUSD (crowded 2d, worst 33%), PF_SWARMSUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
