# Pond Scanner Report
**Scan time:** 2026-08-16 13:01 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -268.0% | $13,522,077 |
| 🟢 | PF_LINKUSD | +227.6% | $531,898 |
| 🟢 | PF_COWUSD | -156.4% | $1,275,622 |
| 🟢 | PF_HFTUSD | +93.6% | $5,475,637 |
| 🟢 | PF_MONUSD | +91.5% | $1,469,683 |
| 🟢 | PF_KAITOUSD | -75.7% | $1,131,132 |
| 🟢 | PF_ALICEUSD | -60.3% | $1,035,430 |
| 🟢 | PF_BICOUSD | -60.0% | $46,104,942 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (kraken → gemini) — coinbase: $62,948.00, kraken: $62,939.90, gemini: $62,955.74
- ⚪ **ETH** gap **0.009%** (coinbase → gemini) — coinbase: $1,877.76, kraken: $1,877.87, gemini: $1,877.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| CoW Protocol (COW) | #311 | $71.8M | 1.13x | -24.4% |
| USD.AI (CHIP) | #386 | $56.8M | 1.03x | +19.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 13% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 5% vs 30d norm 25% (0.2x)
- ⚪ **ETH** 24h vol 7% vs 30d norm 34% (0.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +227.6% | 227.6% |
| PF_ALICEUSD | 3 | -60.3% | 195.8% |
| PF_ACEUSD | 2 | -268.0% | 732.3% |
| PF_COWUSD | 2 | -156.4% | 603.4% |
| PF_HFTUSD | 1 | +93.6% | 117.4% |
| PF_MONUSD | 1 | +91.5% | 91.5% |
| PF_KAITOUSD | 1 | -75.7% | 99.7% |
| PF_BICOUSD | 1 | -60.0% | 60.0% |

**Resolved since last scan:** PF_GRASSUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
