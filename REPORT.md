# Pond Scanner Report
**Scan time:** 2026-07-30 03:30 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | +132.4% | $710,692 |
| 🟢 | PF_SYNUSD | +66.8% | $1,141,875 |
| 🟢 | PF_SPXUSD | +47.8% | $542,301 |
| 🟢 | PF_XRPUSD | +30.1% | $22,092,334 |
| ⚪ | PF_SUSHIUSD | -17.2% | $690,624 |
| ⚪ | PF_UNIUSD | -17.0% | $863,412 |
| ⚪ | PF_SUIUSD | +15.0% | $4,263,574 |
| ⚪ | PF_ARCUSD | +14.4% | $752,766 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (coinbase → gemini) — coinbase: $64,175.99, kraken: $64,178.30, gemini: $64,186.14
- ⚪ **ETH** gap **0.018%** (kraken → gemini) — coinbase: $1,911.59, kraken: $1,911.39, gemini: $1,911.73

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #415 | $51.6M | 3.60x | +76.4% |
| Cash Cat (CASHCAT) | #413 | $51.2M | 0.60x | +19.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.00, realized vol 10d 26% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 39% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9965 (-0.35% vs peg)
- ⚪ **USDT** $0.9986 (-0.14% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 47% vs 30d norm 34% (1.4x)
- ⚪ **ETH** 24h vol 57% vs 30d norm 46% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 4 | +66.8% | 79.8% |
| PF_KAITOUSD | 2 | +132.4% | 306.5% |
| PF_SPXUSD | 1 | +47.8% | 47.8% |
| PF_XRPUSD | 1 | +30.1% | 30.1% |

**Resolved since last scan:** PF_DEXEUSD (crowded 3d, worst 755%), PF_UNIUSD (crowded 2d, worst 151%), PF_ATOMUSD (crowded 2d, worst 77%), PF_SNXUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
