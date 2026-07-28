# Pond Scanner Report
**Scan time:** 2026-07-28 09:05 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -730.1% | $553,859 |
| 🟢 | PF_KAITOUSD | +177.8% | $883,928 |
| 🟢 | PF_LRCUSD | +47.4% | $605,294 |
| 🟢 | PF_SYNUSD | +47.0% | $3,207,345 |
| ⚪ | PF_SOONUSD | -25.8% | $1,220,190 |
| ⚪ | PF_GRASSUSD | -24.7% | $590,310 |
| ⚪ | PF_COTIUSD | -22.0% | $36,510,752 |
| ⚪ | PF_SUIUSD | +21.5% | $6,729,145 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (coinbase → kraken) — coinbase: $63,323.34, kraken: $63,341.40, gemini: $63,331.03
- ⚪ **ETH** gap **0.053%** (kraken → gemini) — coinbase: $1,878.99, kraken: $1,878.62, gemini: $1,879.62

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #353 | $61.6M | 1.01x | -19.0% |
| Espresso (ESP) | #448 | $46.2M | 0.52x | -23.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 45% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | +177.8% | 510.3% |
| PF_SYNUSD | 2 | +47.0% | 69.7% |
| PF_SOLUSD | 1 | -730.1% | 730.1% |
| PF_LRCUSD | 1 | +47.4% | 47.4% |

**Resolved since last scan:** PF_ZIGUSD (crowded 1d, worst 176%), PF_UNIUSD (crowded 1d, worst 80%), PF_VIRTUALUSD (crowded 1d, worst 43%), PF_SNXUSD (crowded 1d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
