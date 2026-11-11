# Pond Scanner Report
**Scan time:** 2026-11-11 19:37 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -138.3% | $3,256,877 |
| 🟢 | PF_ZROUSD | +46.2% | $655,462 |
| 🟢 | PF_SUIUSD | -30.8% | $2,182,793 |
| ⚪ | PF_ASTERUSD | +21.4% | $986,703 |
| ⚪ | PF_ETHFIUSD | -18.0% | $627,661 |
| ⚪ | PF_FETUSD | +16.0% | $15,212,502 |
| ⚪ | PF_POLUSD | -14.2% | $14,701,976 |
| ⚪ | PF_CRVUSD | +12.2% | $6,063,509 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (kraken → gemini) — coinbase: $74,385.85, kraken: $74,383.40, gemini: $74,397.55
- ⚪ **ETH** gap **0.024%** (gemini → coinbase) — coinbase: $2,079.95, kraken: $2,079.95, gemini: $2,079.46

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Aria.AI (ARIA) | #455 | $47.5M | 1.75x | +20.7% |
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #296 | $80.6M | 1.06x | +23.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 46% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.35, realized vol 10d 72% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9965 (-0.35% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 36% (0.8x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 51% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -138.3% | 138.3% |
| PF_ZROUSD | 1 | +46.2% | 46.2% |
| PF_SUIUSD | 1 | -30.8% | 30.8% |

**Resolved since last scan:** PF_ZIGUSD (crowded 1d, worst 167%), PF_SOLUSD (crowded 2d, worst 731%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
