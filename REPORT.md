# Pond Scanner Report
**Scan time:** 2026-08-11 02:28 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -439.0% | $636,077 |
| 🟢 | PF_UNIUSD | +66.9% | $545,214 |
| ⚪ | PF_DOTUSD | +27.2% | $687,295 |
| ⚪ | PF_SYNUSD | -26.3% | $700,457 |
| ⚪ | PF_EIGENUSD | +25.1% | $598,888 |
| ⚪ | PF_AXSUSD | +22.4% | $632,574 |
| ⚪ | PF_XRPUSD | -17.1% | $15,818,268 |
| ⚪ | PF_CATIUSD | +15.5% | $1,755,971 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → kraken) — coinbase: $63,988.62, kraken: $64,000.70, gemini: $63,997.89
- ⚪ **ETH** gap **0.022%** (coinbase → kraken) — coinbase: $1,875.45, kraken: $1,875.86, gemini: $1,875.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #269 | $93.9M | 1.35x | -42.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.18, realized vol 10d 15% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.11, realized vol 10d 23% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 28% (0.8x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 40% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | -439.0% | 439.0% |
| PF_UNIUSD | 1 | +66.9% | 66.9% |

**Resolved since last scan:** PF_BICOUSD (crowded 2d, worst 67%), PF_NEARUSD (crowded 2d, worst 52%), PF_FILUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
