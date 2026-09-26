# Pond Scanner Report
**Scan time:** 2026-09-26 21:11 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -323.6% | $846,770 |
| 🟢 | PF_LINKUSD | +293.4% | $1,033,359 |
| 🟢 | PF_NEARUSD | +255.3% | $1,660,381 |
| 🟢 | PF_UNIUSD | +142.4% | $576,222 |
| 🟢 | PF_TRUMPUSD | +113.6% | $1,050,525 |
| 🟢 | PF_NIGHTUSD | +111.1% | $2,155,356 |
| 🟢 | PF_AVAXUSD | +91.7% | $562,669 |
| 🟢 | PF_2ZUSD | -75.1% | $3,336,458 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $84,076.61, kraken: $84,077.60, gemini: $84,087.29
- ⚪ **ETH** gap **0.024%** (gemini → coinbase) — coinbase: $2,678.81, kraken: $2,678.46, gemini: $2,678.16

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Amp (AMP) | #377 | $72.5M | 1.45x | +59.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 52% vs 60d 43%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 13% vs 30d norm 34% (0.4x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 46% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | +113.6% | 372.6% |
| PF_LSKUSD | 2 | -323.6% | 323.6% |
| PF_LINKUSD | 1 | +293.4% | 364.0% |
| PF_NEARUSD | 1 | +255.3% | 255.3% |
| PF_UNIUSD | 1 | +142.4% | 316.9% |
| PF_NIGHTUSD | 1 | +111.1% | 111.1% |
| PF_AVAXUSD | 1 | +91.7% | 91.7% |
| PF_2ZUSD | 1 | -75.1% | 92.0% |
| PF_VIRTUALUSD | 1 | -58.6% | 58.6% |
| PF_ETHFIUSD | 1 | +57.6% | 137.8% |
| PF_WLDUSD | 1 | +37.4% | 93.0% |
| PF_BLURUSD | 1 | +34.1% | 34.1% |
| PF_FILUSD | 1 | +32.9% | 34.1% |

**Resolved since last scan:** PF_DOTUSD (crowded 2d, worst 89%), PF_GRASSUSD (crowded 2d, worst 81%), PF_RAREUSD (crowded 1d, worst 105%), PF_KAITOUSD (crowded 1d, worst 50%), PF_SUIUSD (crowded 1d, worst 45%), PF_EIGENUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
