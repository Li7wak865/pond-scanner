# Pond Scanner Report
**Scan time:** 2026-08-06 09:06 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +120.7% | $2,207,725 |
| 🟢 | PF_ETHFIUSD | +67.6% | $810,047 |
| 🟢 | PF_MOODENGUSD | +48.3% | $1,078,749 |
| 🟢 | PF_GRIFFAINUSD | +41.3% | $763,252 |
| 🟢 | PF_AXSUSD | +37.5% | $582,237 |
| 🟢 | PF_FILUSD | -33.0% | $815,753 |
| ⚪ | PF_APTUSD | +26.8% | $554,448 |
| ⚪ | PF_NEARUSD | -24.7% | $1,331,475 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → kraken) — coinbase: $64,784.04, kraken: $64,791.10, gemini: $64,787.37
- ⚪ **ETH** gap **0.049%** (kraken → gemini) — coinbase: $1,911.66, kraken: $1,911.25, gemini: $1,912.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Bless (BLESS) | #423 | $49.8M | 0.91x | +56.8% |
| SkyAI (SKYAI) | #295 | $77.9M | 0.71x | +43.1% |
| COTI (COTI) | #453 | $45.5M | 0.58x | +16.8% |
| Orochi Network (ON) | #464 | $44.4M | 0.51x | +25.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 29% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 16% vs 30d norm 30% (0.5x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 1 | +120.7% | 120.7% |
| PF_ETHFIUSD | 1 | +67.6% | 67.6% |
| PF_MOODENGUSD | 1 | +48.3% | 48.3% |
| PF_GRIFFAINUSD | 1 | +41.3% | 41.3% |
| PF_AXSUSD | 1 | +37.5% | 37.5% |
| PF_FILUSD | 1 | -33.0% | 33.0% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 766%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
