# Pond Scanner Report
**Scan time:** 2026-08-13 02:48 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -441.8% | $2,013,970 |
| 🟢 | PF_HFTUSD | +137.2% | $2,652,656 |
| 🟢 | PF_AVAXUSD | +123.7% | $561,935 |
| 🟢 | PF_SAGAUSD | +62.1% | $6,333,812 |
| 🟢 | PF_RENDERUSD | +54.2% | $569,512 |
| 🟢 | PF_LSKUSD | -48.3% | $1,639,093 |
| 🟢 | PF_OPENUSD | +43.5% | $673,999 |
| 🟢 | PF_STORJUSD | -37.1% | $2,877,096 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → coinbase) — coinbase: $63,450.00, kraken: $63,439.80, gemini: $63,449.25
- ⚪ **ETH** gap **0.090%** (gemini → kraken) — coinbase: $1,875.85, kraken: $1,876.11, gemini: $1,874.42

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Babylon (BABY) | #460 | $44.2M | 4.30x | -20.6% |
| Prom (PROM) | #442 | $47.7M | 2.68x | +20.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 14% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 18% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 27% (0.8x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 39% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -441.8% | 946.7% |
| PF_COTIUSD | 2 | -33.7% | 57.5% |
| PF_HFTUSD | 1 | +137.2% | 137.2% |
| PF_AVAXUSD | 1 | +123.7% | 123.7% |
| PF_SAGAUSD | 1 | +62.1% | 62.1% |
| PF_RENDERUSD | 1 | +54.2% | 54.2% |
| PF_LSKUSD | 1 | -48.3% | 48.3% |
| PF_OPENUSD | 1 | +43.5% | 43.5% |
| PF_STORJUSD | 1 | -37.1% | 37.1% |
| PF_FILUSD | 1 | -34.9% | 34.9% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 108%), PF_RUNEUSD (crowded 2d, worst 54%), PF_ATOMUSD (crowded 2d, worst 58%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
