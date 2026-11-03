# Pond Scanner Report
**Scan time:** 2026-11-03 00:58 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +54.6% | $614,541 |
| 🟢 | PF_RUNEUSD | -52.8% | $900,404 |
| 🟢 | PF_TRUMPUSD | +48.9% | $1,244,127 |
| 🟢 | PF_STXUSD | +41.2% | $598,238 |
| 🟢 | PF_NEARUSD | +31.7% | $6,412,293 |
| 🟢 | PF_XRPUSD | +30.6% | $6,526,735 |
| ⚪ | PF_SUIUSD | +25.9% | $3,584,358 |
| ⚪ | PF_TIAUSD | +21.9% | $1,006,695 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.001%** (coinbase → gemini) — coinbase: $76,919.54, kraken: $76,920.10, gemini: $76,920.62
- ⚪ **ETH** gap **0.059%** (kraken → gemini) — coinbase: $2,253.59, kraken: $2,252.87, gemini: $2,254.20

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #482 | $44.2M | 0.59x | +15.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.28, realized vol 10d 30% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.33, realized vol 10d 30% vs 60d 38%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9958 (-0.42% vs peg)
- ⚪ **USDe** $0.9980 (-0.20% vs peg)
- ⚪ **USDT** $0.9988 (-0.12% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 45% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +54.6% | 54.6% |
| PF_RUNEUSD | 1 | -52.8% | 52.8% |
| PF_TRUMPUSD | 1 | +48.9% | 48.9% |
| PF_STXUSD | 1 | +41.2% | 41.2% |
| PF_NEARUSD | 1 | +31.7% | 31.7% |
| PF_XRPUSD | 1 | +30.6% | 30.6% |

**Resolved since last scan:** PF_APTUSD (crowded 2d, worst 40%), PF_FILUSD (crowded 2d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
