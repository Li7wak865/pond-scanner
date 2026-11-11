# Pond Scanner Report
**Scan time:** 2026-11-11 06:24 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZIGUSD | -166.6% | $645,016 |
| 🟢 | PF_ZROUSD | +44.2% | $603,643 |
| 🟢 | PF_SOLUSD | -36.9% | $1,202,047 |
| ⚪ | PF_TIAUSD | -19.0% | $1,025,691 |
| ⚪ | PF_XRPUSD | +14.4% | $20,779,547 |
| ⚪ | PF_AVAXUSD | +13.9% | $510,331 |
| ⚪ | PF_LDOUSD | +10.0% | $1,363,133 |
| ⚪ | PF_NEARUSD | -9.7% | $2,611,237 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (kraken → gemini) — coinbase: $73,754.55, kraken: $73,753.80, gemini: $73,773.02
- ⚪ **ETH** gap **0.068%** (coinbase → gemini) — coinbase: $2,063.74, kraken: $2,063.90, gemini: $2,065.14

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Initia (INIT) | #355 | $67.9M | 2.24x | +39.6% |
| Janction (JCT) | #275 | $92.0M | 1.53x | +17.1% |
| Aria.AI (ARIA) | #498 | $41.1M | 0.97x | +22.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.36, realized vol 10d 45% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 71% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9966 (-0.34% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 44% vs 30d norm 36% (1.2x)
- ⚪ **ETH** 24h vol 70% vs 30d norm 51% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | -36.9% | 731.4% |
| PF_ZIGUSD | 1 | -166.6% | 166.6% |
| PF_ZROUSD | 1 | +44.2% | 44.2% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 981%), PF_AVAXUSD (crowded 3d, worst 211%), PF_TRUMPUSD (crowded 8d, worst 178%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
