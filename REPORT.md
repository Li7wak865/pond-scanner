# Pond Scanner Report
**Scan time:** 2026-09-15 21:22 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -508.0% | $2,532,519 |
| 🟢 | PF_SOLUSD | +457.1% | $831,568 |
| 🟢 | PF_ICPUSD | -151.6% | $526,983 |
| 🟢 | PF_HFTUSD | -54.2% | $648,908 |
| 🟢 | PF_TRUMPUSD | +54.2% | $1,039,075 |
| 🟢 | PF_ACEUSD | -42.0% | $2,661,820 |
| 🟢 | PF_XRPUSD | +41.2% | $57,634,277 |
| 🟢 | PF_FILUSD | -37.6% | $2,357,160 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $75,719.68, kraken: $75,720.70, gemini: $75,732.93
- ⚪ **ETH** gap **0.052%** (gemini → coinbase) — coinbase: $2,398.68, kraken: $2,398.36, gemini: $2,397.43

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| VeThor (VTHO) | #319 | $78.3M | 0.57x | +17.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 27% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9980 (-0.20% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 40% vs 30d norm 42% (0.9x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 60% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -508.0% | 896.9% |
| PF_SOLUSD | 1 | +457.1% | 674.5% |
| PF_ICPUSD | 1 | -151.6% | 151.6% |
| PF_HFTUSD | 1 | -54.2% | 55.5% |
| PF_TRUMPUSD | 1 | +54.2% | 125.4% |
| PF_ACEUSD | 1 | -42.0% | 175.3% |
| PF_XRPUSD | 1 | +41.2% | 41.2% |
| PF_FILUSD | 1 | -37.6% | 37.6% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 92%), PF_DOTUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
