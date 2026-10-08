# Pond Scanner Report
**Scan time:** 2026-10-08 06:06 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | -415.6% | $769,907 |
| 🟢 | PF_LINKUSD | -266.9% | $603,405 |
| 🟢 | PF_NEARUSD | -152.7% | $4,382,982 |
| 🟢 | PF_ZROUSD | -139.5% | $836,939 |
| 🟢 | PF_UNIUSD | +91.0% | $678,551 |
| 🟢 | PF_APTUSD | +47.1% | $533,541 |
| 🟢 | PF_SUIUSD | +32.1% | $8,938,999 |
| ⚪ | PF_ASTERUSD | +29.8% | $1,418,337 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → kraken) — coinbase: $82,794.40, kraken: $82,813.60, gemini: $82,808.17
- ⚪ **ETH** gap **0.026%** (gemini → kraken) — coinbase: $2,567.25, kraken: $2,567.34, gemini: $2,566.67

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Numeraire (NMR) | #292 | $99.5M | 0.64x | -18.6% |
| Wormhole (W) | #258 | $118.5M | 0.56x | +23.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.11, realized vol 10d 24% vs 60d 43%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 30% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **PYUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 34% (0.6x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 44% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +91.0% | 299.0% |
| PF_NEARUSD | 3 | -152.7% | 178.3% |
| PF_ZROUSD | 3 | -139.5% | 139.5% |
| PF_RAYUSD | 2 | -415.6% | 825.8% |
| PF_LINKUSD | 2 | -266.9% | 395.8% |
| PF_APTUSD | 2 | +47.1% | 47.1% |
| PF_SUIUSD | 1 | +32.1% | 32.1% |

**Resolved since last scan:** PF_AVAXUSD (crowded 3d, worst 289%), PF_SPXUSD (crowded 2d, worst 47%), PF_RENDERUSD (crowded 2d, worst 138%), PF_ASTERUSD (crowded 2d, worst 31%), PF_JTOUSD (crowded 2d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
