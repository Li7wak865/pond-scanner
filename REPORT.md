# Pond Scanner Report
**Scan time:** 2026-08-26 01:58 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -219.7% | $1,633,528 |
| 🟢 | PF_LINKUSD | -141.0% | $541,897 |
| 🟢 | PF_ACEUSD | -122.7% | $3,179,657 |
| 🟢 | PF_ZROUSD | -121.1% | $776,617 |
| 🟢 | PF_HFTUSD | +103.9% | $2,792,323 |
| 🟢 | PF_RENDERUSD | -83.4% | $642,160 |
| 🟢 | PF_SPXUSD | +82.4% | $930,302 |
| 🟢 | PF_NEARUSD | +62.2% | $2,241,712 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (kraken → coinbase) — coinbase: $78,791.55, kraken: $78,770.00, gemini: $78,788.25
- ⚪ **ETH** gap **0.037%** (kraken → gemini) — coinbase: $2,455.13, kraken: $2,454.78, gemini: $2,455.69

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #456 | $48.9M | 1.99x | +20.4% |
| Prom (PROM) | #302 | $81.8M | 1.76x | +19.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.59, realized vol 10d 109% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 48% vs 30d norm 38% (1.3x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 52% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -122.7% | 241.7% |
| PF_LINKUSD | 3 | -141.0% | 477.7% |
| PF_SOLUSD | 2 | -219.7% | 476.0% |
| PF_ZROUSD | 2 | -121.1% | 121.1% |
| PF_SPXUSD | 2 | +82.4% | 128.1% |
| PF_NEARUSD | 2 | +62.2% | 121.5% |
| PF_TRUMPUSD | 2 | -50.5% | 89.5% |
| PF_STXUSD | 2 | -30.3% | 53.8% |
| PF_HFTUSD | 1 | +103.9% | 103.9% |
| PF_RENDERUSD | 1 | -83.4% | 83.4% |
| PF_KAITOUSD | 1 | -60.6% | 60.6% |

**Resolved since last scan:** PF_STORJUSD (crowded 3d, worst 214%), PF_JTOUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
