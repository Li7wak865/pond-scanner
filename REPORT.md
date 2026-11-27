# Pond Scanner Report
**Scan time:** 2026-11-27 21:18 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +86.2% | $690,856 |
| ⚪ | PF_RUNEUSD | +28.8% | $961,876 |
| ⚪ | PF_CFGUSD | -25.6% | $6,581,590 |
| ⚪ | PF_TRUMPUSD | +24.8% | $593,367 |
| ⚪ | PF_GRASSUSD | +19.4% | $676,803 |
| ⚪ | PF_ALICEUSD | -18.0% | $899,874 |
| ⚪ | PF_TRXUSD | -16.1% | $1,389,551 |
| ⚪ | PF_XRPUSD | +12.4% | $12,845,628 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.048%** (coinbase → gemini) — coinbase: $59,801.49, kraken: $59,813.40, gemini: $59,830.00
- ⚪ **ETH** gap **0.001%** (coinbase → gemini) — coinbase: $1,666.69, kraken: $1,666.70, gemini: $1,666.71

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Portal (PORTAL) | #498 | $35.6M | 6.91x | +218.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.61, realized vol 10d 41% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.59, realized vol 10d 57% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9953 (-0.47% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 81% vs 30d norm 58% (1.4x)
- ⚪ **ETH** 24h vol 87% vs 30d norm 70% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +86.2% | 112.3% |

**Resolved since last scan:** PF_ACEUSD (crowded 3d, worst 249%), PF_NEARUSD (crowded 2d, worst 48%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
