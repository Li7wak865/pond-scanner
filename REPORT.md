# Pond Scanner Report
**Scan time:** 2026-07-28 19:53 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -359.3% | $1,100,490 |
| 🟢 | PF_UNIUSD | +171.4% | $865,886 |
| 🟢 | PF_NEARUSD | +91.4% | $1,278,700 |
| 🟢 | PF_KAITOUSD | +84.1% | $935,665 |
| 🟢 | PF_TRUMPUSD | -74.2% | $897,952 |
| 🟢 | PF_SOONUSD | -64.1% | $1,719,773 |
| 🟢 | PF_SYNUSD | +61.3% | $3,116,133 |
| 🟢 | PF_SPXUSD | -39.3% | $625,609 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (gemini → coinbase) — coinbase: $63,723.82, kraken: $63,719.80, gemini: $63,705.33
- ⚪ **ETH** gap **0.047%** (kraken → coinbase) — coinbase: $1,918.08, kraken: $1,917.17, gemini: $1,918.02

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #271 | $92.6M | 2.11x | -21.7% |
| Orochi Network (ON) | #415 | $50.1M | 1.08x | +73.2% |
| SOON (SOON) | #269 | $92.5M | 0.59x | +27.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 41% vs 30d norm 34% (1.2x)
- ⚪ **ETH** 24h vol 71% vs 30d norm 46% (1.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | +84.1% | 510.3% |
| PF_SYNUSD | 2 | +61.3% | 69.7% |
| PF_DEXEUSD | 1 | -359.3% | 755.4% |
| PF_UNIUSD | 1 | +171.4% | 171.4% |
| PF_NEARUSD | 1 | +91.4% | 91.4% |
| PF_TRUMPUSD | 1 | -74.2% | 74.2% |
| PF_SOONUSD | 1 | -64.1% | 69.2% |
| PF_SPXUSD | 1 | -39.3% | 39.3% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 730%), PF_RUNEUSD (crowded 1d, worst 63%), PF_LRCUSD (crowded 1d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
