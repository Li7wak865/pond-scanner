# Pond Scanner Report
**Scan time:** 2026-08-23 18:48 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PI_XRPUSD | -497.3% | $1,286,688 |
| 🟢 | PF_SOLUSD | +437.2% | $2,061,585 |
| 🟢 | PF_LINKUSD | -335.4% | $505,521 |
| 🟢 | PF_UNIUSD | +308.4% | $857,334 |
| 🟢 | PF_TRUMPUSD | +175.1% | $5,427,089 |
| 🟢 | PF_ACEUSD | -129.8% | $1,983,284 |
| 🟢 | PF_NEARUSD | +110.7% | $3,535,303 |
| 🟢 | PF_HFTUSD | +110.6% | $1,083,474 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (kraken → coinbase) — coinbase: $77,288.21, kraken: $77,277.40, gemini: $77,277.48
- ⚪ **ETH** gap **0.019%** (kraken → gemini) — coinbase: $2,445.65, kraken: $2,445.61, gemini: $2,446.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #464 | $47.5M | 3.16x | +25.6% |
| Spark (SPK) | #325 | $73.0M | 0.68x | +22.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 61% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.65, realized vol 10d 109% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9980 (-0.20% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 36% (0.9x)
- ⚪ **ETH** 24h vol 57% vs 30d norm 51% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 4 | -335.4% | 819.3% |
| PF_UNIUSD | 4 | +308.4% | 413.9% |
| PF_TRUMPUSD | 4 | +175.1% | 332.5% |
| PF_SYNUSD | 3 | +80.5% | 505.9% |
| PF_ACEUSD | 2 | -129.8% | 139.7% |
| PI_XRPUSD | 1 | -497.3% | 497.3% |
| PF_SOLUSD | 1 | +437.2% | 437.2% |
| PF_NEARUSD | 1 | +110.7% | 161.1% |
| PF_HFTUSD | 1 | +110.6% | 110.6% |
| PF_ZROUSD | 1 | +93.1% | 93.1% |
| PF_OGNUSD | 1 | +84.3% | 84.3% |
| PF_FETUSD | 1 | +70.1% | 95.8% |
| PF_RENDERUSD | 1 | +67.6% | 67.6% |
| PF_WLDUSD | 1 | +55.9% | 55.9% |
| PF_STXUSD | 1 | +35.5% | 35.5% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 2d, worst 93%), PF_XTZUSD (crowded 1d, worst 49%), PF_XRPUSD (crowded 1d, worst 56%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
