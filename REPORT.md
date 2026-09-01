# Pond Scanner Report
**Scan time:** 2026-09-01 05:10 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +893.2% | $639,415 |
| 🟢 | PF_LINKUSD | +127.5% | $526,316 |
| 🟢 | PF_TRUMPUSD | -105.7% | $727,566 |
| 🟢 | PF_UNIUSD | +76.8% | $572,992 |
| 🟢 | PF_NEARUSD | +56.4% | $881,119 |
| 🟢 | PF_STXUSD | -44.5% | $644,735 |
| 🟢 | PF_RAREUSD | +42.4% | $1,010,540 |
| 🟢 | PF_MIRAUSD | -31.3% | $1,844,561 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (kraken → gemini) — coinbase: $78,864.03, kraken: $78,858.90, gemini: $78,864.84
- ⚪ **ETH** gap **0.059%** (kraken → gemini) — coinbase: $2,474.02, kraken: $2,473.82, gemini: $2,475.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 0G (0G) | #429 | $52.4M | 4.90x | +28.9% |
| Bitlayer (BTR) | #472 | $47.2M | 2.32x | +20.4% |
| Ramses (RAM) | #356 | $67.7M | 0.80x | +3543.9% |
| Useless Coin (USELESS) | #281 | $94.8M | 0.66x | +42.5% |
| Cysic (CYS) | #307 | $82.6M | 0.58x | -39.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 25% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.54, realized vol 10d 32% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 38% (0.7x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 52% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +893.2% | 893.2% |
| PF_LINKUSD | 2 | +127.5% | 182.3% |
| PF_TRUMPUSD | 2 | -105.7% | 233.6% |
| PF_UNIUSD | 2 | +76.8% | 88.0% |
| PF_NEARUSD | 2 | +56.4% | 63.2% |
| PF_STXUSD | 2 | -44.5% | 44.5% |
| PF_RAREUSD | 1 | +42.4% | 42.4% |
| PF_MIRAUSD | 1 | -31.3% | 31.3% |

**Resolved since last scan:** PF_ICXUSD (crowded 2d, worst 47%), PF_HFTUSD (crowded 2d, worst 43%), PF_MINAUSD (crowded 2d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
