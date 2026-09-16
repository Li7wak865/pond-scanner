# Pond Scanner Report
**Scan time:** 2026-09-16 16:57 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +492.4% | $710,448 |
| 🟢 | PF_LSKUSD | -254.8% | $3,137,366 |
| 🟢 | PF_TRUMPUSD | -83.8% | $1,016,161 |
| 🟢 | PF_IDUSD | +70.4% | $784,116 |
| 🟢 | PF_SYNUSD | -61.9% | $9,405,453 |
| 🟢 | PF_STEEMUSD | -59.9% | $531,774 |
| 🟢 | PF_FILUSD | -55.9% | $2,331,052 |
| 🟢 | PF_HFTUSD | -45.5% | $3,372,257 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (coinbase → gemini) — coinbase: $75,718.14, kraken: $75,721.60, gemini: $75,722.23
- ⚪ **ETH** gap **0.077%** (kraken → gemini) — coinbase: $2,391.41, kraken: $2,391.16, gemini: $2,392.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Canopy (CNPY) | #483 | $43.4M | 0.98x | +19.2% |
| Teller (DEBIT) | #463 | $46.5M | 0.73x | +25.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.22, realized vol 10d 27% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 38% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 42% (0.9x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 60% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 3 | -254.8% | 896.9% |
| PF_SOLUSD | 1 | +492.4% | 492.4% |
| PF_TRUMPUSD | 1 | -83.8% | 83.8% |
| PF_IDUSD | 1 | +70.4% | 70.4% |
| PF_SYNUSD | 1 | -61.9% | 61.9% |
| PF_STEEMUSD | 1 | -59.9% | 205.3% |
| PF_FILUSD | 1 | -55.9% | 55.9% |
| PF_HFTUSD | 1 | -45.5% | 45.5% |
| PF_APTUSD | 1 | -38.3% | 38.3% |
| PF_UNIUSD | 1 | +36.6% | 212.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 79%), PF_ACEUSD (crowded 2d, worst 175%), PF_ICXUSD (crowded 1d, worst 46%), PF_RAREUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
