# Pond Scanner Report
**Scan time:** 2026-09-04 16:22 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SPXUSD | +209.6% | $814,231 |
| 🟢 | PF_TRUMPUSD | +107.1% | $1,922,666 |
| 🟢 | PF_SAGAUSD | +63.9% | $3,035,774 |
| 🟢 | PF_HFTUSD | -54.5% | $4,977,281 |
| 🟢 | PF_ACEUSD | -49.5% | $817,716 |
| ⚪ | PF_CRVUSD | +25.3% | $5,384,672 |
| ⚪ | PF_ASTERUSD | -24.4% | $784,258 |
| ⚪ | PF_FARTCOINUSD | +23.0% | $10,200,886 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → kraken) — coinbase: $79,454.88, kraken: $79,476.30, gemini: $79,467.59
- ⚪ **ETH** gap **0.061%** (coinbase → gemini) — coinbase: $2,451.76, kraken: $2,451.84, gemini: $2,453.26

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 42% vs 60d 40%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 45% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 51% vs 30d norm 40% (1.3x)
- ⚪ **ETH** 24h vol 62% vs 30d norm 54% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -49.5% | 304.8% |
| PF_SPXUSD | 1 | +209.6% | 209.6% |
| PF_TRUMPUSD | 1 | +107.1% | 196.2% |
| PF_SAGAUSD | 1 | +63.9% | 63.9% |
| PF_HFTUSD | 1 | -54.5% | 54.5% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 439%), PF_ZIGUSD (crowded 2d, worst 180%), PF_COTIUSD (crowded 1d, worst 179%), PF_BATUSD (crowded 1d, worst 109%), PF_NEARUSD (crowded 1d, worst 67%), PF_UNIUSD (crowded 2d, worst 247%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
