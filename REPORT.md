# Pond Scanner Report
**Scan time:** 2026-11-09 22:22 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AVAXUSD | -211.0% | $605,776 |
| 🟢 | PF_SOLUSD | +200.6% | $772,421 |
| 🟢 | PF_RENDERUSD | +104.9% | $511,701 |
| 🟢 | PF_TRUMPUSD | -89.2% | $2,849,018 |
| 🟢 | PF_UNIUSD | +81.3% | $647,981 |
| 🟢 | PF_NEARUSD | -73.3% | $2,862,995 |
| ⚪ | PF_SUIUSD | -25.3% | $4,683,406 |
| ⚪ | PF_ASTERUSD | +16.2% | $741,308 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (coinbase → gemini) — coinbase: $74,923.28, kraken: $74,932.00, gemini: $74,938.59
- ⚪ **ETH** gap **0.046%** (coinbase → gemini) — coinbase: $2,123.28, kraken: $2,123.51, gemini: $2,124.25

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Initia (INIT) | #473 | $44.4M | 1.43x | +69.7% |
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #322 | $75.4M | 0.91x | +27.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.35, realized vol 10d 44% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 69% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9966 (-0.34% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 41% vs 30d norm 35% (1.2x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 50% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 6 | -89.2% | 178.3% |
| PF_UNIUSD | 2 | +81.3% | 202.8% |
| PF_AVAXUSD | 1 | -211.0% | 211.0% |
| PF_SOLUSD | 1 | +200.6% | 200.6% |
| PF_RENDERUSD | 1 | +104.9% | 104.9% |
| PF_NEARUSD | 1 | -73.3% | 73.3% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
