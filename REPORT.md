# Pond Scanner Report
**Scan time:** 2026-07-28 03:36 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -510.3% | $959,632 |
| 🟢 | PF_ZIGUSD | -176.2% | $636,244 |
| 🟢 | PF_UNIUSD | -79.6% | $545,594 |
| 🟢 | PF_SYNUSD | +57.3% | $3,300,141 |
| 🟢 | PF_VIRTUALUSD | -43.5% | $521,068 |
| 🟢 | PF_SNXUSD | +39.9% | $630,262 |
| ⚪ | PF_TRUMPUSD | +29.6% | $853,083 |
| ⚪ | PF_XRPUSD | -26.3% | $17,083,718 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (coinbase → kraken) — coinbase: $63,229.76, kraken: $63,242.20, gemini: $63,232.25
- ⚪ **ETH** gap **0.053%** (gemini → coinbase) — coinbase: $1,876.32, kraken: $1,875.76, gemini: $1,875.32

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Espresso (ESP) | #438 | $46.3M | 0.88x | -29.7% |
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #374 | $58.4M | 0.83x | -16.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 59% vs 30d norm 45% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | -510.3% | 510.3% |
| PF_SYNUSD | 2 | +57.3% | 69.7% |
| PF_ZIGUSD | 1 | -176.2% | 176.2% |
| PF_UNIUSD | 1 | -79.6% | 79.6% |
| PF_VIRTUALUSD | 1 | -43.5% | 43.5% |
| PF_SNXUSD | 1 | +39.9% | 39.9% |

**Resolved since last scan:** PF_LRCUSD (crowded 2d, worst 49%), PF_SOONUSD (crowded 2d, worst 34%), PF_NEARUSD (crowded 2d, worst 33%), PF_DYMUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
