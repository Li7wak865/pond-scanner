# Pond Scanner Report
**Scan time:** 2026-07-31 14:36 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -732.1% | $904,526 |
| 🟢 | PF_AGLDUSD | +643.0% | $625,193 |
| 🟢 | PF_HYPEUSD | -605.5% | $703,391 |
| 🟢 | PF_KAITOUSD | -135.6% | $765,252 |
| 🟢 | PF_UNIUSD | +90.7% | $2,429,120 |
| 🟢 | PF_NEARUSD | -58.3% | $1,152,317 |
| 🟢 | PF_APTUSD | -57.2% | $582,996 |
| 🟢 | PF_SYNUSD | +49.4% | $2,288,164 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (gemini → kraken) — coinbase: $62,691.97, kraken: $62,700.50, gemini: $62,684.79
- ⚪ **ETH** gap **0.026%** (gemini → coinbase) — coinbase: $1,864.37, kraken: $1,863.98, gemini: $1,863.88

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #369 | $59.7M | 0.55x | +21.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 28% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.11, realized vol 10d 42% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9968 (-0.32% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 45% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | -135.6% | 326.1% |
| PF_UNIUSD | 2 | +90.7% | 237.0% |
| PF_DEXEUSD | 1 | -732.1% | 732.1% |
| PF_AGLDUSD | 1 | +643.0% | 643.0% |
| PF_HYPEUSD | 1 | -605.5% | 605.5% |
| PF_NEARUSD | 1 | -58.3% | 58.3% |
| PF_APTUSD | 1 | -57.2% | 57.2% |
| PF_SYNUSD | 1 | +49.4% | 49.4% |

**Resolved since last scan:** PF_MUBARAKUSD (crowded 1d, worst 58%), PF_RAREUSD (crowded 1d, worst 52%), PF_SNXUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
