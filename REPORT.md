# Pond Scanner Report
**Scan time:** 2026-08-18 07:05 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -459.2% | $15,179,792 |
| 🟢 | PF_NEARUSD | +45.9% | $1,897,860 |
| 🟢 | PF_KAITOUSD | -39.3% | $1,225,993 |
| ⚪ | PF_SAGAUSD | +25.9% | $7,792,417 |
| ⚪ | PF_ETHFIUSD | -24.4% | $706,826 |
| ⚪ | PF_HFTUSD | +22.9% | $6,032,573 |
| ⚪ | PF_FILUSD | -21.6% | $898,936 |
| ⚪ | PF_CATIUSD | -16.8% | $1,004,330 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.037%** (kraken → coinbase) — coinbase: $64,247.11, kraken: $64,223.30, gemini: $64,233.03
- ⚪ **ETH** gap **0.021%** (kraken → coinbase) — coinbase: $1,900.79, kraken: $1,900.40, gemini: $1,900.59

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cysic (CYS) | #277 | $85.2M | 0.63x | -19.4% |
| Audiera (BEAT) | #271 | $85.8M | 0.52x | -22.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 19% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 18% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 26% (0.9x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 35% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -459.2% | 732.3% |
| PF_NEARUSD | 1 | +45.9% | 45.9% |
| PF_KAITOUSD | 1 | -39.3% | 75.4% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 2d, worst 95%), PF_HFTUSD (crowded 2d, worst 58%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
