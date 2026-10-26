# Pond Scanner Report
**Scan time:** 2026-10-26 22:40 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +129.3% | $2,863,954 |
| 🟢 | PF_TRUMPUSD | +63.9% | $538,708 |
| 🟢 | PF_SYNUSD | +33.5% | $2,035,722 |
| ⚪ | PF_PONSUSD | +18.7% | $2,583,746 |
| ⚪ | PF_XRPUSD | +17.5% | $8,560,473 |
| ⚪ | PF_MOODENGUSD | +12.4% | $905,655 |
| ⚪ | PF_DOTUSD | -11.5% | $977,021 |
| ⚪ | PF_TRXUSD | -10.7% | $1,915,794 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (kraken → coinbase) — coinbase: $79,833.31, kraken: $79,825.20, gemini: $79,831.83
- ⚪ **ETH** gap **0.004%** (coinbase → gemini) — coinbase: $2,307.45, kraken: $2,307.49, gemini: $2,307.55

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #409 | $56.1M | 2.08x | -27.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.30, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9966 (-0.34% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9988 (-0.12% vs peg)
- ⚪ **USDC** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 33% vs 30d norm 31% (1.1x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 43% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +129.3% | 129.3% |
| PF_TRUMPUSD | 1 | +63.9% | 63.9% |
| PF_SYNUSD | 1 | +33.5% | 33.5% |

**Resolved since last scan:** PF_GRASSUSD (crowded 1d, worst 68%), PF_FILUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
