# Pond Scanner Report
**Scan time:** 2026-08-19 13:09 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +405.0% | $531,084 |
| 🟢 | PF_ETHFIUSD | +154.5% | $780,913 |
| 🟢 | PF_UNIUSD | +131.9% | $593,824 |
| 🟢 | PF_ACEUSD | -110.9% | $16,348,970 |
| 🟢 | PF_LINKUSD | -51.1% | $743,311 |
| 🟢 | PF_NEARUSD | -30.3% | $1,728,135 |
| ⚪ | PF_ALICEUSD | -27.9% | $1,681,223 |
| ⚪ | PF_APTUSD | +24.6% | $949,420 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → coinbase) — coinbase: $64,821.81, kraken: $64,817.00, gemini: $64,820.00
- ⚪ **ETH** gap **0.031%** (coinbase → gemini) — coinbase: $1,934.20, kraken: $1,934.49, gemini: $1,934.80

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| GoPlus Security (GPS) | #306 | $71.7M | 0.80x | -33.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 19% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 19% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 25% (0.9x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 34% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -110.9% | 732.3% |
| PF_SOLUSD | 1 | +405.0% | 405.0% |
| PF_ETHFIUSD | 1 | +154.5% | 154.5% |
| PF_UNIUSD | 1 | +131.9% | 131.9% |
| PF_LINKUSD | 1 | -51.1% | 51.1% |
| PF_NEARUSD | 1 | -30.3% | 30.3% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
