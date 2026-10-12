# Pond Scanner Report
**Scan time:** 2026-10-12 06:00 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ATOMUSD | -56.9% | $609,778 |
| 🟢 | PF_NEARUSD | -48.6% | $3,542,323 |
| 🟢 | PF_APTUSD | +30.2% | $751,757 |
| ⚪ | PF_BATUSD | +25.9% | $3,841,653 |
| ⚪ | PF_STXUSD | +25.0% | $1,046,841 |
| ⚪ | PF_XTZUSD | +18.9% | $748,852 |
| ⚪ | PF_LDOUSD | -18.9% | $564,184 |
| ⚪ | PF_GRASSUSD | -17.7% | $1,447,263 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.038%** (gemini → coinbase) — coinbase: $83,928.50, kraken: $83,917.80, gemini: $83,896.79
- ⚪ **ETH** gap **0.002%** (coinbase → kraken) — coinbase: $2,562.45, kraken: $2,562.49, gemini: $2,562.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nervos Network (CKB) | #327 | $86.0M | 1.14x | +21.5% |
| io.net (IO) | #339 | $80.0M | 0.75x | +26.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 26% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.34, realized vol 10d 39% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 40% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -48.6% | 142.6% |
| PF_ATOMUSD | 2 | -56.9% | 57.6% |
| PF_APTUSD | 2 | +30.2% | 66.3% |

**Resolved since last scan:** PF_GRASSUSD (crowded 2d, worst 68%), PF_XRPUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
