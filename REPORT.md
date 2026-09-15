# Pond Scanner Report
**Scan time:** 2026-09-15 04:56 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -896.9% | $5,287,838 |
| 🟢 | PF_TRUMPUSD | -125.4% | $564,888 |
| 🟢 | PF_POWRUSD | -115.8% | $1,173,273 |
| 🟢 | PF_HFTUSD | +52.6% | $1,048,575 |
| ⚪ | PF_NEARUSD | -29.6% | $1,677,964 |
| ⚪ | PF_FILUSD | -25.6% | $4,100,300 |
| ⚪ | PF_DOTUSD | -19.6% | $1,771,290 |
| ⚪ | PF_MINAUSD | -19.1% | $1,833,795 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → gemini) — coinbase: $77,567.38, gemini: $77,583.51
- ⚪ **ETH** gap **0.006%** (kraken → gemini) — coinbase: $2,492.47, kraken: $2,492.46, gemini: $2,492.62

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #277 | $99.9M | 1.60x | +33.6% |
| Lisk (LSK) | #298 | $88.4M | 1.30x | -56.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 22% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 29% vs 60d 57%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 42% (0.7x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 59% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -896.9% | 896.9% |
| PF_HFTUSD | 2 | +52.6% | 65.1% |
| PF_TRUMPUSD | 1 | -125.4% | 125.4% |
| PF_POWRUSD | 1 | -115.8% | 115.8% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 170%), PF_STEEMUSD (crowded 3d, worst 188%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
