# Pond Scanner Report
**Scan time:** 2026-07-30 14:32 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +421.2% | $502,958 |
| 🟢 | PF_KAITOUSD | -56.8% | $1,041,283 |
| 🟢 | PF_SOONUSD | +52.5% | $961,965 |
| 🟢 | PF_UNIUSD | +44.9% | $1,061,448 |
| 🟢 | PF_SYNUSD | +41.8% | $1,214,206 |
| 🟢 | PF_COTIUSD | -37.3% | $129,417,400 |
| ⚪ | PF_XRPUSD | +28.8% | $18,825,432 |
| ⚪ | PF_ETHFIUSD | +17.2% | $876,654 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.006%** (coinbase → kraken) — coinbase: $64,768.47, kraken: $64,772.60, gemini: $64,769.03
- ⚪ **ETH** gap **0.013%** (kraken → gemini) — coinbase: $1,921.97, kraken: $1,921.91, gemini: $1,922.16

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Espresso (ESP) | #442 | $46.5M | 1.27x | +21.2% |
| Semicon Bull 3X ETF (bStocks Tokenized Stock) (SOXLB) | #455 | $44.1M | 1.26x | +16.7% |
| Cash Cat (CASHCAT) | #460 | $43.4M | 0.67x | +25.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 27% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 42% vs 30d norm 34% (1.2x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 45% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 4 | +41.8% | 79.8% |
| PF_KAITOUSD | 2 | -56.8% | 326.1% |
| PF_SOLUSD | 1 | +421.2% | 421.2% |
| PF_SOONUSD | 1 | +52.5% | 52.5% |
| PF_UNIUSD | 1 | +44.9% | 61.1% |
| PF_COTIUSD | 1 | -37.3% | 59.3% |

**Resolved since last scan:** PF_CTSIUSD (crowded 1d, worst 71%), PF_SPXUSD (crowded 1d, worst 67%), PF_SAGAUSD (crowded 1d, worst 54%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
