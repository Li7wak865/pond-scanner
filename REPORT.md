# Pond Scanner Report
**Scan time:** 2026-09-09 20:56 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +597.5% | $1,026,269 |
| 🟢 | PF_LINKUSD | -226.7% | $662,425 |
| 🟢 | PF_TRUMPUSD | -177.0% | $1,446,670 |
| 🟢 | PF_UNIUSD | +170.0% | $949,664 |
| 🟢 | PF_RAYUSD | -112.5% | $1,355,335 |
| 🟢 | PF_ATOMUSD | -91.7% | $1,719,897 |
| 🟢 | PF_NEARUSD | -75.3% | $3,274,158 |
| 🟢 | PF_ACEUSD | -52.9% | $1,312,166 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (kraken → gemini) — coinbase: $78,268.79, kraken: $78,257.20, gemini: $78,277.51
- ⚪ **ETH** gap **0.019%** (kraken → coinbase) — coinbase: $2,469.04, kraken: $2,468.58, gemini: $2,468.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| IOST (IOST) | #333 | $77.1M | 3.28x | +147.8% |
| COTI (COTI) | #406 | $61.3M | 1.07x | +19.1% |
| Siacoin (SC) | #475 | $48.8M | 0.92x | +30.1% |
| 牛来 (Niu Lai) (牛来) | #316 | $82.6M | 0.71x | -15.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.22, realized vol 10d 37% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.15, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 40% (0.9x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 54% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -75.3% | 246.3% |
| PF_SOLUSD | 1 | +597.5% | 597.5% |
| PF_LINKUSD | 1 | -226.7% | 350.9% |
| PF_TRUMPUSD | 1 | -177.0% | 507.7% |
| PF_UNIUSD | 1 | +170.0% | 361.6% |
| PF_RAYUSD | 1 | -112.5% | 657.3% |
| PF_ATOMUSD | 1 | -91.7% | 91.7% |
| PF_ACEUSD | 1 | -52.9% | 64.2% |
| PF_XTZUSD | 1 | +32.1% | 32.1% |
| PF_SWARMSUSD | 1 | -30.8% | 31.4% |

**Resolved since last scan:** PF_ICXUSD (crowded 1d, worst 60%), PF_XRPUSD (crowded 1d, worst 51%), PF_BATUSD (crowded 1d, worst 45%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
