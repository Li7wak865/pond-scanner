# Pond Scanner Report
**Scan time:** 2026-09-27 05:19 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +127.3% | $1,016,719 |
| 🟢 | PF_NEARUSD | -122.9% | $2,592,712 |
| 🟢 | PF_RUNEUSD | +102.5% | $1,143,392 |
| 🟢 | PF_AVAXUSD | +78.8% | $567,514 |
| 🟢 | PF_2ZUSD | -69.1% | $2,246,142 |
| 🟢 | PF_LINKUSD | -61.8% | $1,019,805 |
| 🟢 | PF_UNIUSD | +38.9% | $657,059 |
| 🟢 | PF_VIRTUALUSD | +37.8% | $589,151 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → gemini) — coinbase: $84,379.94, kraken: $84,379.40, gemini: $84,388.47
- ⚪ **ETH** gap **0.027%** (gemini → coinbase) — coinbase: $2,695.70, kraken: $2,695.34, gemini: $2,694.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Amp (AMP) | #430 | $61.3M | 1.83x | +35.2% |
| SOON (SOON) | #284 | $105.2M | 0.69x | +50.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 13% vs 30d norm 34% (0.4x)
- ⚪ **ETH** 24h vol 16% vs 30d norm 46% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | +127.3% | 372.6% |
| PF_NEARUSD | 2 | -122.9% | 255.3% |
| PF_AVAXUSD | 2 | +78.8% | 91.6% |
| PF_2ZUSD | 2 | -69.1% | 92.0% |
| PF_LINKUSD | 2 | -61.8% | 364.0% |
| PF_UNIUSD | 2 | +38.9% | 316.9% |
| PF_VIRTUALUSD | 2 | +37.8% | 58.6% |
| PF_ETHFIUSD | 2 | +32.6% | 137.8% |
| PF_WLDUSD | 2 | +31.9% | 93.0% |
| PF_RUNEUSD | 1 | +102.5% | 102.5% |
| PF_XPLUSD | 1 | +31.4% | 31.4% |

**Resolved since last scan:** PF_LSKUSD (crowded 3d, worst 324%), PF_NIGHTUSD (crowded 2d, worst 111%), PF_BLURUSD (crowded 2d, worst 34%), PF_FILUSD (crowded 2d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
