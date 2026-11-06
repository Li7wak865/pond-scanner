# Pond Scanner Report
**Scan time:** 2026-11-06 06:49 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -274.1% | $777,959 |
| 🟢 | PF_UNIUSD | -114.6% | $981,948 |
| 🟢 | PF_TRUMPUSD | -83.0% | $7,211,523 |
| 🟢 | PF_INJUSD | +64.9% | $638,081 |
| 🟢 | PF_ZROUSD | +39.5% | $940,547 |
| 🟢 | PF_NEARUSD | -34.9% | $7,387,586 |
| ⚪ | PF_STXUSD | -28.8% | $589,342 |
| ⚪ | PF_ATOMUSD | -28.7% | $662,094 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (coinbase → gemini) — coinbase: $75,654.96, kraken: $75,663.20, gemini: $75,671.73
- ⚪ **ETH** gap **0.079%** (gemini → kraken) — coinbase: $2,228.80, kraken: $2,229.25, gemini: $2,227.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #409 | $54.5M | 2.25x | -26.1% |
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #273 | $98.3M | 1.27x | -15.5% |
| UnifAI Network (UAI) | #476 | $44.3M | 0.83x | +74.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 50% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 68% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9965 (-0.35% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 68% vs 30d norm 35% (1.9x)
- ⚪ **ETH** 24h vol 86% vs 30d norm 49% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 3 | -274.1% | 987.6% |
| PF_TRUMPUSD | 3 | -83.0% | 178.3% |
| PF_UNIUSD | 2 | -114.6% | 229.5% |
| PF_ZROUSD | 2 | +39.5% | 123.9% |
| PF_INJUSD | 1 | +64.9% | 64.9% |
| PF_NEARUSD | 1 | -34.9% | 34.9% |

**Resolved since last scan:** PF_XTZUSD (crowded 2d, worst 74%), PF_STXUSD (crowded 2d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
