# Pond Scanner Report
**Scan time:** 2026-09-13 04:49 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -166.2% | $1,237,013 |
| 🟢 | PF_POWRUSD | -137.7% | $3,570,324 |
| 🟢 | PF_HFTUSD | +106.1% | $1,326,132 |
| 🟢 | PF_ETHFIUSD | -49.1% | $936,481 |
| 🟢 | PF_ACEUSD | -35.7% | $1,226,033 |
| 🟢 | PF_NEARUSD | +33.4% | $1,124,723 |
| 🟢 | PF_SWARMSUSD | -32.6% | $1,936,811 |
| ⚪ | PF_ALCHUSD | +24.6% | $3,776,234 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $77,195.04, kraken: $77,196.30, gemini: $77,209.78
- ⚪ **ETH** gap **0.014%** (coinbase → gemini) — coinbase: $2,519.17, kraken: $2,519.39, gemini: $2,519.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| VeThor (VTHO) | #287 | $96.2M | 1.93x | +58.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 20% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 27% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 7% vs 30d norm 41% (0.2x)
- ⚪ **ETH** 24h vol 16% vs 30d norm 58% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_HFTUSD | 2 | +106.1% | 106.1% |
| PF_ACEUSD | 2 | -35.7% | 62.9% |
| PF_NEARUSD | 2 | +33.4% | 44.2% |
| PF_UNIUSD | 1 | -166.2% | 166.2% |
| PF_POWRUSD | 1 | -137.7% | 137.7% |
| PF_ETHFIUSD | 1 | -49.1% | 49.1% |
| PF_SWARMSUSD | 1 | -32.6% | 32.6% |

**Resolved since last scan:** PF_RIVERUSD (crowded 2d, worst 238%), PF_LSKUSD (crowded 3d, worst 452%), PF_RAYUSD (crowded 2d, worst 67%), PF_ALCHUSD (crowded 2d, worst 59%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
