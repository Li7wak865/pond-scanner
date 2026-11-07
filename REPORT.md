# Pond Scanner Report
**Scan time:** 2026-11-07 21:52 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -148.0% | $2,006,036 |
| 🟢 | PF_NEARUSD | +98.3% | $1,719,260 |
| 🟢 | PF_SUIUSD | -30.2% | $1,627,477 |
| ⚪ | PF_TIAUSD | +14.2% | $752,387 |
| ⚪ | PF_XRPUSD | +12.1% | $8,493,685 |
| ⚪ | PF_CRVUSD | +10.0% | $2,753,274 |
| ⚪ | PF_ONDOUSD | -7.5% | $1,115,442 |
| ⚪ | PF_ARCUSD | +6.2% | $654,398 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (kraken → gemini) — coinbase: $75,601.82, kraken: $75,600.80, gemini: $75,603.00
- ⚪ **ETH** gap **0.009%** (coinbase → gemini) — coinbase: $2,227.15, kraken: $2,227.19, gemini: $2,227.34

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #327 | $73.2M | 0.65x | +30.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.28, realized vol 10d 50% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 68% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDe** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 10% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 47% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | -148.0% | 178.3% |
| PF_NEARUSD | 1 | +98.3% | 98.3% |
| PF_SUIUSD | 1 | -30.2% | 30.2% |

**Resolved since last scan:** PF_XTZUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
