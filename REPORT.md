# Pond Scanner Report
**Scan time:** 2026-09-20 16:07 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +274.8% | $587,499 |
| 🟢 | PF_NEARUSD | +239.5% | $5,133,192 |
| 🟢 | PF_HFTUSD | +103.2% | $625,461 |
| 🟢 | PF_CATIUSD | +73.5% | $607,564 |
| 🟢 | PF_UNIUSD | +61.8% | $710,893 |
| 🟢 | PF_JTOUSD | -57.8% | $1,241,616 |
| 🟢 | PF_AVAXUSD | +47.9% | $2,389,451 |
| 🟢 | PF_FILUSD | -43.5% | $2,724,044 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (gemini → coinbase) — coinbase: $80,964.60, kraken: $80,957.00, gemini: $80,947.62
- ⚪ **ETH** gap **0.088%** (gemini → kraken) — coinbase: $2,614.73, kraken: $2,614.98, gemini: $2,612.69

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #476 | $49.2M | 6.90x | -31.9% |
| Harmony (ONE) | #425 | $57.6M | 2.95x | +15.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.11, realized vol 10d 42% vs 60d 41%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.16, realized vol 10d 55% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 35% (0.7x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 50% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +61.8% | 624.1% |
| PF_HFTUSD | 3 | +103.2% | 107.0% |
| PF_AVAXUSD | 2 | +47.9% | 168.4% |
| PF_SOLUSD | 1 | +274.8% | 274.8% |
| PF_NEARUSD | 1 | +239.5% | 239.5% |
| PF_CATIUSD | 1 | +73.5% | 73.5% |
| PF_JTOUSD | 1 | -57.8% | 57.8% |
| PF_FILUSD | 1 | -43.5% | 43.5% |
| PF_TRUMPUSD | 1 | -42.2% | 42.2% |

**Resolved since last scan:** PF_INJUSD (crowded 1d, worst 423%), PF_MINAUSD (crowded 2d, worst 73%), PF_WLDUSD (crowded 1d, worst 35%), PF_NIGHTUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
