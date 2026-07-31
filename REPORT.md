# Pond Scanner Report
**Scan time:** 2026-07-31 03:51 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -237.0% | $1,910,906 |
| 🟢 | PF_KAITOUSD | -113.8% | $1,034,806 |
| 🟢 | PF_MIRAUSD | -67.6% | $1,954,980 |
| ⚪ | PF_XRPUSD | -29.4% | $11,007,415 |
| ⚪ | PF_NEARUSD | +27.3% | $1,641,474 |
| ⚪ | PF_FLOWUSD | +23.6% | $3,016,502 |
| ⚪ | PF_FILUSD | +21.0% | $1,545,675 |
| ⚪ | PF_SUSHIUSD | -15.6% | $891,917 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (coinbase → gemini) — coinbase: $64,270.70, kraken: $64,277.40, gemini: $64,289.30
- ⚪ **ETH** gap **0.031%** (coinbase → gemini) — coinbase: $1,905.83, kraken: $1,905.90, gemini: $1,906.43

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #374 | $59.7M | 1.64x | +49.6% |
| Micron Technology (bStocks Tokenized Stock) (MUB) | #246 | $108.7M | 0.70x | +18.5% |
| Cap (CAP) | #384 | $56.6M | 0.63x | +38.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 23% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 39% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 34% (0.7x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 45% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | -113.8% | 326.1% |
| PF_UNIUSD | 2 | -237.0% | 237.0% |
| PF_MIRAUSD | 1 | -67.6% | 67.6% |

**Resolved since last scan:** PF_SUSHIUSD (crowded 2d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
