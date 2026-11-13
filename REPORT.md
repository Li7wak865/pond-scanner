# Pond Scanner Report
**Scan time:** 2026-11-13 19:43 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +822.3% | $913,572 |
| 🟢 | PF_HYPEUSD | +713.9% | $692,845 |
| 🟢 | PF_ZROUSD | -187.3% | $1,098,273 |
| 🟢 | PF_AVAXUSD | -175.5% | $558,204 |
| 🟢 | PF_INJUSD | -154.5% | $582,341 |
| 🟢 | PF_UNIUSD | -148.0% | $761,980 |
| ⚪ | PF_IMXUSD | -22.6% | $706,021 |
| ⚪ | PF_TIAUSD | -15.7% | $2,339,746 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → gemini) — coinbase: $69,016.07, kraken: $69,013.50, gemini: $69,024.76
- ⚪ **ETH** gap **0.009%** (kraken → gemini) — coinbase: $1,949.89, kraken: $1,949.83, gemini: $1,950.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Sanctum (SANC) | #465 | $44.2M | 0.68x | +102.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.46, realized vol 10d 48% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 71% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9959 (-0.41% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 57% vs 30d norm 37% (1.5x)
- ⚪ **ETH** 24h vol 72% vs 30d norm 51% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -148.0% | 273.6% |
| PF_SOLUSD | 1 | +822.3% | 822.3% |
| PF_HYPEUSD | 1 | +713.9% | 713.9% |
| PF_ZROUSD | 1 | -187.3% | 187.3% |
| PF_AVAXUSD | 1 | -175.5% | 175.5% |
| PF_INJUSD | 1 | -154.5% | 154.5% |

**Resolved since last scan:** PF_RENDERUSD (crowded 1d, worst 123%), PF_NEARUSD (crowded 3d, worst 138%), PF_SPXUSD (crowded 1d, worst 72%), PF_ZIGUSD (crowded 2d, worst 102%), PF_TRUMPUSD (crowded 2d, worst 57%), PF_SUIUSD (crowded 1d, worst 34%), PF_XRPUSD (crowded 1d, worst 34%), PF_STXUSD (crowded 1d, worst 33%), PF_DOTUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
