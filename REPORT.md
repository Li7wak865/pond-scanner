# Pond Scanner Report
**Scan time:** 2026-09-20 04:55 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +624.1% | $1,012,559 |
| 🟢 | PF_INJUSD | +423.0% | $1,047,271 |
| 🟢 | PF_TRUMPUSD | +195.8% | $757,604 |
| 🟢 | PF_NEARUSD | +159.2% | $3,988,054 |
| 🟢 | PF_HFTUSD | -104.8% | $1,142,777 |
| 🟢 | PF_MINAUSD | -46.9% | $1,040,224 |
| 🟢 | PF_DOTUSD | +44.0% | $1,432,646 |
| 🟢 | PF_AVAXUSD | +41.0% | $2,218,390 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.006%** (coinbase → gemini) — coinbase: $80,396.49, kraken: $80,398.00, gemini: $80,400.95
- ⚪ **ETH** gap **0.033%** (kraken → gemini) — coinbase: $2,579.27, kraken: $2,579.24, gemini: $2,580.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #302 | $94.2M | 4.68x | +60.6% |
| Harmony (ONE) | #433 | $56.6M | 3.07x | +67.2% |
| Cap (CAP) | #366 | $72.5M | 1.10x | -16.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 43% vs 60d 41%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 57% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 39% (0.6x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 51% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +624.1% | 624.1% |
| PF_HFTUSD | 3 | -104.8% | 107.0% |
| PF_MINAUSD | 2 | -46.9% | 73.3% |
| PF_DOTUSD | 2 | +44.0% | 47.4% |
| PF_AVAXUSD | 2 | +41.0% | 168.4% |
| PF_INJUSD | 1 | +423.0% | 423.0% |
| PF_TRUMPUSD | 1 | +195.8% | 195.8% |
| PF_NEARUSD | 1 | +159.2% | 159.2% |
| PF_FILUSD | 1 | +38.2% | 38.2% |
| PF_JTOUSD | 1 | +36.4% | 36.4% |
| PF_WLDUSD | 1 | +35.4% | 35.4% |
| PF_JUPUSD | 1 | +32.8% | 32.8% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 985%), PF_SYNUSD (crowded 2d, worst 128%), PF_ASTERUSD (crowded 2d, worst 65%), PF_STXUSD (crowded 2d, worst 58%), PF_ACEUSD (crowded 2d, worst 57%), PF_XRPUSD (crowded 2d, worst 45%), PF_XTZUSD (crowded 2d, worst 219%), PF_APTUSD (crowded 2d, worst 33%), PF_KAITOUSD (crowded 2d, worst 50%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
