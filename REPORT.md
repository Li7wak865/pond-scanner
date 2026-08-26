# Pond Scanner Report
**Scan time:** 2026-08-26 13:17 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALCHUSD | -125.6% | $519,230 |
| 🟢 | PF_ACEUSD | -106.4% | $2,651,196 |
| 🟢 | PF_HFTUSD | +106.1% | $2,152,705 |
| 🟢 | PF_STXUSD | -74.2% | $2,023,514 |
| 🟢 | PF_TRUMPUSD | -55.6% | $1,499,290 |
| 🟢 | PF_LINKUSD | -52.9% | $504,186 |
| 🟢 | PF_ZROUSD | +47.8% | $787,888 |
| 🟢 | PF_RENDERUSD | +41.8% | $535,438 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (coinbase → kraken) — coinbase: $78,153.06, kraken: $78,157.00, gemini: $78,153.90
- ⚪ **ETH** gap **0.045%** (kraken → gemini) — coinbase: $2,447.39, kraken: $2,446.81, gemini: $2,447.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PolySwarm (NCT) | #487 | $44.7M | 2.66x | +408.8% |
| 牛来 (Niu Lai) (牛来) | #484 | $44.9M | 0.55x | +28.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.62, realized vol 10d 59% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.59, realized vol 10d 109% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 38% (0.9x)
- ⚪ **ETH** 24h vol 39% vs 30d norm 52% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -106.4% | 241.7% |
| PF_LINKUSD | 3 | -52.9% | 477.7% |
| PF_TRUMPUSD | 2 | -55.6% | 417.1% |
| PF_ALCHUSD | 1 | -125.6% | 125.6% |
| PF_HFTUSD | 1 | +106.1% | 106.1% |
| PF_STXUSD | 1 | -74.2% | 74.2% |
| PF_ZROUSD | 1 | +47.8% | 47.8% |
| PF_RENDERUSD | 1 | +41.8% | 41.8% |
| PF_FETUSD | 1 | +40.1% | 40.1% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 821%), PF_SPXUSD (crowded 2d, worst 128%), PF_COTIUSD (crowded 1d, worst 61%), PF_VIRTUALUSD (crowded 1d, worst 48%), PF_NEARUSD (crowded 2d, worst 122%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
