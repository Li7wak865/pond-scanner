# Pond Scanner Report
**Scan time:** 2026-11-10 19:44 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +981.5% | $545,087 |
| 🟢 | PF_SOLUSD | +731.4% | $1,142,234 |
| 🟢 | PF_AVAXUSD | -101.2% | $509,559 |
| 🟢 | PF_TRUMPUSD | -85.1% | $591,534 |
| ⚪ | PF_ZROUSD | +28.3% | $611,137 |
| ⚪ | PF_SUIUSD | -22.5% | $6,040,729 |
| ⚪ | PF_NEARUSD | -18.4% | $2,483,181 |
| ⚪ | PF_DOTUSD | +16.1% | $1,031,642 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (coinbase → gemini) — coinbase: $73,304.87, kraken: $73,315.40, gemini: $73,323.75
- ⚪ **ETH** gap **0.018%** (kraken → gemini) — coinbase: $2,038.60, kraken: $2,038.56, gemini: $2,038.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Initia (INIT) | #346 | $68.8M | 2.40x | +97.3% |
| Janction (JCT) | #376 | $59.2M | 1.48x | -53.7% |
| Akedo (AKE) | #361 | $64.5M | 0.75x | -43.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.45, realized vol 10d 46% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 73% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9967 (-0.33% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 45% vs 30d norm 36% (1.2x)
- ⚪ **ETH** 24h vol 68% vs 30d norm 51% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 7 | -85.1% | 178.3% |
| PF_AVAXUSD | 2 | -101.2% | 211.0% |
| PF_HYPEUSD | 1 | +981.5% | 981.5% |
| PF_SOLUSD | 1 | +731.4% | 731.4% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 116%), PF_UNIUSD (crowded 3d, worst 203%), PF_ACEUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
