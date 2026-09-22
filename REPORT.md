# Pond Scanner Report
**Scan time:** 2026-09-22 04:58 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +346.5% | $633,482 |
| 🟢 | PF_NEARUSD | +337.5% | $9,300,278 |
| 🟢 | PF_UNIUSD | +266.4% | $932,777 |
| 🟢 | PF_RENDERUSD | +209.9% | $642,201 |
| 🟢 | PF_LSKUSD | -168.6% | $985,388 |
| 🟢 | PF_SPXUSD | +68.9% | $1,072,745 |
| 🟢 | PF_RUNEUSD | +66.1% | $505,133 |
| 🟢 | PF_SYNUSD | +42.3% | $2,875,514 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (gemini → coinbase) — coinbase: $85,435.85, kraken: $85,430.50, gemini: $85,411.47
- ⚪ **ETH** gap **0.022%** (kraken → gemini) — coinbase: $2,727.60, kraken: $2,727.15, gemini: $2,727.76

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #454 | $54.6M | 1.61x | +61.4% |
| Four (FORM) | #256 | $121.6M | 0.51x | +22.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.30, realized vol 10d 56% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.33, realized vol 10d 60% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 58% vs 30d norm 36% (1.6x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 48% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 6 | +266.4% | 624.1% |
| PF_NEARUSD | 3 | +337.5% | 457.9% |
| PF_LINKUSD | 2 | +346.5% | 725.7% |
| PF_RENDERUSD | 2 | +209.9% | 209.9% |
| PF_TRUMPUSD | 2 | +41.0% | 52.0% |
| PF_VIRTUALUSD | 2 | +38.3% | 41.2% |
| PF_XPLUSD | 2 | +33.0% | 37.4% |
| PF_LSKUSD | 1 | -168.6% | 168.6% |
| PF_SPXUSD | 1 | +68.9% | 68.9% |
| PF_RUNEUSD | 1 | +66.1% | 66.1% |
| PF_SYNUSD | 1 | +42.3% | 42.3% |

**Resolved since last scan:** PF_AVAXUSD (crowded 2d, worst 314%), PF_FILUSD (crowded 2d, worst 67%), PF_NIGHTUSD (crowded 2d, worst 60%), PF_ONDOUSD (crowded 2d, worst 93%), PF_WLDUSD (crowded 2d, worst 55%), PF_MOODENGUSD (crowded 2d, worst 52%), PF_HFTUSD (crowded 2d, worst 105%), PF_JTOUSD (crowded 2d, worst 61%), PF_APTUSD (crowded 2d, worst 49%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
