# Pond Scanner Report
**Scan time:** 2026-09-29 05:45 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +197.4% | $898,068 |
| 🟢 | PF_TRUMPUSD | -135.9% | $1,167,396 |
| 🟢 | PF_SPXUSD | -109.2% | $578,531 |
| 🟢 | PF_GRASSUSD | +99.7% | $939,578 |
| 🟢 | PF_ETHFIUSD | +57.9% | $701,284 |
| 🟢 | PF_CFGUSD | +53.1% | $683,380 |
| 🟢 | PF_RUNEUSD | -53.1% | $1,451,332 |
| 🟢 | PF_ZROUSD | +52.9% | $1,069,725 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.049%** (coinbase → gemini) — coinbase: $83,256.23, kraken: $83,257.80, gemini: $83,297.29
- ⚪ **ETH** gap **0.064%** (coinbase → gemini) — coinbase: $2,667.19, kraken: $2,667.74, gemini: $2,668.91

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Numeraire (NMR) | #287 | $100.5M | 1.50x | +38.2% |
| 0G (0G) | #398 | $65.5M | 1.11x | +20.8% |
| Quack AI (Q) | #283 | $101.4M | 0.93x | -28.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.22, realized vol 10d 43% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 34% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 34% (0.9x)
- ⚪ **ETH** 24h vol 41% vs 30d norm 46% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +197.4% | 493.4% |
| PF_ETHFIUSD | 4 | +57.9% | 137.8% |
| PF_LINKUSD | 4 | +47.5% | 600.3% |
| PF_NEARUSD | 4 | +45.2% | 285.8% |
| PF_TRUMPUSD | 2 | -135.9% | 135.9% |
| PF_GRASSUSD | 2 | +99.7% | 101.2% |
| PF_ZROUSD | 2 | +52.9% | 141.3% |
| PF_FILUSD | 2 | +34.6% | 73.0% |
| PF_TIAUSD | 2 | -31.4% | 35.3% |
| PF_SPXUSD | 1 | -109.2% | 109.2% |
| PF_CFGUSD | 1 | +53.1% | 53.1% |
| PF_RUNEUSD | 1 | -53.1% | 53.1% |
| PF_ASTERUSD | 1 | +41.0% | 41.0% |
| PF_NIGHTUSD | 1 | -35.9% | 35.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 698%), PF_AVAXUSD (crowded 4d, worst 167%), PF_SUIUSD (crowded 2d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
