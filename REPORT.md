# Pond Scanner Report
**Scan time:** 2026-11-25 08:36 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -849.1% | $596,320 |
| 🟢 | PF_ZROUSD | -50.4% | $725,819 |
| 🟢 | PF_ACEUSD | +38.0% | $2,702,762 |
| ⚪ | PF_RUNEUSD | -27.6% | $545,072 |
| ⚪ | PF_SUIUSD | -18.4% | $2,725,878 |
| ⚪ | PF_TRUMPUSD | -18.1% | $608,665 |
| ⚪ | PF_XLMUSD | -6.4% | $7,155,150 |
| ⚪ | PF_LDOUSD | -6.0% | $1,560,397 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.103%** (coinbase → gemini) — coinbase: $59,196.83, kraken: $59,204.60, gemini: $59,258.00
- ⚪ **ETH** gap **0.118%** (coinbase → gemini) — coinbase: $1,649.30, kraken: $1,649.31, gemini: $1,651.24

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #258 | $86.9M | 1.21x | -27.9% |
| OpenGradient (OPG) | #430 | $42.9M | 0.58x | +22.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 39% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.61, realized vol 10d 56% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9948 (-0.52% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 55% vs 30d norm 55% (1.0x)
- ⚪ **ETH** 24h vol 54% vs 30d norm 69% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | -849.1% | 849.1% |
| PF_ZROUSD | 2 | -50.4% | 55.3% |
| PF_ACEUSD | 1 | +38.0% | 38.0% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 2d, worst 50%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
