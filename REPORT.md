# Pond Scanner Report
**Scan time:** 2026-11-15 18:52 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +715.5% | $644,517 |
| 🟢 | PF_SOLUSD | -603.3% | $1,849,950 |
| 🟢 | PF_INJUSD | -331.9% | $582,365 |
| 🟢 | PF_NEARUSD | -245.2% | $2,538,196 |
| 🟢 | PF_KAVAUSD | -152.2% | $18,379,286 |
| 🟢 | PF_UNIUSD | -138.3% | $769,352 |
| 🟢 | PF_ZROUSD | -71.3% | $1,074,805 |
| 🟢 | PF_TRUMPUSD | -35.7% | $1,062,022 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (kraken → coinbase) — coinbase: $64,595.52, kraken: $64,584.80, gemini: $64,588.81
- ⚪ **ETH** gap **0.033%** (gemini → coinbase) — coinbase: $1,812.41, kraken: $1,812.04, gemini: $1,811.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Aria.AI (ARIA) | #429 | $47.1M | 0.74x | +29.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 43% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 59% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9956 (-0.44% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 100% vs 30d norm 41% (2.5x)
- 🟢 **ETH** 24h vol 132% vs 30d norm 56% (2.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_INJUSD | 3 | -331.9% | 746.6% |
| PF_NEARUSD | 2 | -245.2% | 245.2% |
| PF_KAVAUSD | 2 | -152.2% | 169.0% |
| PF_ZROUSD | 2 | -71.3% | 192.0% |
| PF_TRUMPUSD | 2 | -35.7% | 112.0% |
| PF_HYPEUSD | 1 | +715.5% | 715.5% |
| PF_SOLUSD | 1 | -603.3% | 603.3% |
| PF_UNIUSD | 1 | -138.3% | 138.3% |

**Resolved since last scan:** PF_AVAXUSD (crowded 1d, worst 180%), PF_APTUSD (crowded 2d, worst 57%), PF_ASTERUSD (crowded 1d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
