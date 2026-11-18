# Pond Scanner Report
**Scan time:** 2026-11-18 20:32 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +346.1% | $538,326 |
| 🟢 | PF_UNIUSD | -129.3% | $699,937 |
| 🟢 | PF_NEARUSD | -70.0% | $2,456,235 |
| ⚪ | PF_ZROUSD | -24.9% | $948,958 |
| ⚪ | PF_DOTUSD | -12.2% | $1,308,496 |
| ⚪ | PF_WLDUSD | -11.8% | $908,209 |
| ⚪ | PF_MELANIAUSD | -10.5% | $1,022,366 |
| ⚪ | PF_FILUSD | -9.4% | $1,045,992 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → gemini) — coinbase: $62,524.60, kraken: $62,527.80, gemini: $62,531.09
- ⚪ **ETH** gap **0.030%** (gemini → kraken) — coinbase: $1,748.83, kraken: $1,748.98, gemini: $1,748.45

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #396 | $50.6M | 4.64x | +76.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.53, realized vol 10d 47% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 61% vs 60d 49%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9951 (-0.49% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 39% vs 30d norm 43% (0.9x)
- ⚪ **ETH** 24h vol 48% vs 30d norm 58% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 5 | -70.0% | 245.2% |
| PF_UNIUSD | 2 | -129.3% | 129.3% |
| PF_SOLUSD | 1 | +346.1% | 346.1% |

**Resolved since last scan:** PF_KAVAUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
