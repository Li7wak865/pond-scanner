# Pond Scanner Report
**Scan time:** 2026-08-13 13:48 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -234.4% | $1,574,587 |
| 🟢 | PF_MONUSD | +95.6% | $3,392,995 |
| 🟢 | PF_RENDERUSD | +87.8% | $572,038 |
| 🟢 | PF_IOTAUSD | +63.1% | $1,719,891 |
| 🟢 | PF_MOODENGUSD | +58.7% | $1,098,456 |
| 🟢 | PF_COTIUSD | -57.7% | $54,608,817 |
| 🟢 | PF_HFTUSD | -33.3% | $2,719,733 |
| ⚪ | PF_VIRTUALUSD | -26.6% | $1,740,483 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.056%** (coinbase → gemini) — coinbase: $63,741.88, kraken: $63,760.10, gemini: $63,777.52
- ⚪ **ETH** gap **0.060%** (gemini → kraken) — coinbase: $1,889.86, kraken: $1,890.92, gemini: $1,889.79

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Prom (PROM) | #464 | $43.9M | 1.36x | -31.8% |
| Tutorial (TUT) | #458 | $45.1M | 1.18x | -24.0% |
| DAPPOS (DOS) | #389 | $56.3M | 1.07x | -20.0% |
| HOME (HOME) | #441 | $47.8M | 1.00x | +19.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 14% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.06, realized vol 10d 18% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 27% (0.8x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 37% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -234.4% | 946.7% |
| PF_COTIUSD | 2 | -57.7% | 57.7% |
| PF_MONUSD | 1 | +95.6% | 95.6% |
| PF_RENDERUSD | 1 | +87.8% | 90.5% |
| PF_IOTAUSD | 1 | +63.1% | 63.1% |
| PF_MOODENGUSD | 1 | +58.7% | 58.7% |
| PF_HFTUSD | 1 | -33.3% | 137.2% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 1d, worst 61%), PF_OPENUSD (crowded 1d, worst 44%), PF_AVAXUSD (crowded 1d, worst 124%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
