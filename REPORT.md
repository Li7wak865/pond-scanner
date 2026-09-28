# Pond Scanner Report
**Scan time:** 2026-09-28 13:57 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | -298.7% | $956,244 |
| 🟢 | PF_ZROUSD | +141.3% | $701,077 |
| 🟢 | PF_ETHFIUSD | +108.7% | $1,490,253 |
| 🟢 | PF_UNIUSD | -104.1% | $1,055,376 |
| 🟢 | PF_GRASSUSD | +101.2% | $821,631 |
| 🟢 | PF_NEARUSD | -80.8% | $3,957,590 |
| 🟢 | PF_RUNEUSD | +71.4% | $991,898 |
| 🟢 | PF_VIRTUALUSD | -53.6% | $1,150,688 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (kraken → gemini) — coinbase: $83,639.36, kraken: $83,638.00, gemini: $83,642.12
- ⚪ **ETH** gap **0.053%** (gemini → kraken) — coinbase: $2,691.11, kraken: $2,691.25, gemini: $2,689.83

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Quack AI (Q) | #264 | $116.7M | 0.58x | -50.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 42% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 34% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 34% (0.9x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 46% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | -298.7% | 600.3% |
| PF_ETHFIUSD | 3 | +108.7% | 137.8% |
| PF_UNIUSD | 3 | -104.1% | 479.0% |
| PF_NEARUSD | 3 | -80.8% | 285.8% |
| PF_AVAXUSD | 3 | +45.2% | 167.3% |
| PF_SAGAUSD | 2 | -30.3% | 36.7% |
| PF_ZROUSD | 1 | +141.3% | 141.3% |
| PF_GRASSUSD | 1 | +101.2% | 101.2% |
| PF_RUNEUSD | 1 | +71.4% | 71.4% |
| PF_VIRTUALUSD | 1 | -53.6% | 53.6% |
| PF_TRUMPUSD | 1 | -40.1% | 40.1% |
| PF_XRPUSD | 1 | -33.9% | 33.9% |

**Resolved since last scan:** PF_ENJUSD (crowded 1d, worst 131%), PF_PONSUSD (crowded 1d, worst 79%), PF_SUIUSD (crowded 1d, worst 42%), PF_DOTUSD (crowded 1d, worst 37%), PF_FILUSD (crowded 1d, worst 34%), PF_HFTUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
