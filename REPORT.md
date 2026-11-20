# Pond Scanner Report
**Scan time:** 2026-11-20 07:17 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -220.1% | $524,503 |
| 🟢 | PF_SOLUSD | -36.8% | $526,326 |
| 🟢 | PF_TRUMPUSD | -35.3% | $879,537 |
| 🟢 | PF_JUPUSD | -31.6% | $737,471 |
| ⚪ | PF_SUIUSD | -28.1% | $3,972,091 |
| ⚪ | PF_NEARUSD | -18.2% | $3,708,476 |
| ⚪ | PF_CFGUSD | -12.1% | $1,086,620 |
| ⚪ | PF_TIAUSD | -10.9% | $743,562 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.090%** (coinbase → gemini) — coinbase: $61,890.39, kraken: $61,897.10, gemini: $61,946.00
- ⚪ **ETH** gap **0.108%** (coinbase → gemini) — coinbase: $1,745.77, kraken: $1,746.08, gemini: $1,747.65

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #393 | $49.9M | 3.22x | +25.0% |
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #282 | $79.4M | 0.96x | -20.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.54, realized vol 10d 45% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 57% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9955 (-0.45% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 53% vs 30d norm 44% (1.2x)
- ⚪ **ETH** 24h vol 59% vs 30d norm 58% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | -220.1% | 220.1% |
| PF_SOLUSD | 3 | -36.8% | 768.6% |
| PF_TRUMPUSD | 2 | -35.3% | 38.8% |
| PF_JUPUSD | 1 | -31.6% | 31.6% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 162%), PF_NEARUSD (crowded 7d, worst 245%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
