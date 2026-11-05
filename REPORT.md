# Pond Scanner Report
**Scan time:** 2026-11-05 06:48 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +617.3% | $641,729 |
| 🟢 | PF_UNIUSD | -229.5% | $1,081,928 |
| 🟢 | PF_SOLUSD | -200.2% | $905,031 |
| 🟢 | PF_NEARUSD | -158.3% | $5,124,081 |
| 🟢 | PF_TRUMPUSD | -113.3% | $7,955,606 |
| 🟢 | PF_SYNUSD | +33.5% | $798,667 |
| 🟢 | PF_BBUSD | +30.2% | $1,881,413 |
| ⚪ | PF_XRPUSD | +22.6% | $8,977,348 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (coinbase → gemini) — coinbase: $80,608.46, kraken: $80,621.40, gemini: $80,621.53
- ⚪ **ETH** gap **0.059%** (gemini → kraken) — coinbase: $2,430.19, kraken: $2,430.49, gemini: $2,429.05

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #427 | $53.1M | 1.12x | -18.4% |
| Janction (JCT) | #309 | $80.9M | 0.69x | +81.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 39% vs 60d 35%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 50% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9978 (-0.22% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 69% vs 30d norm 47% (1.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -158.3% | 158.3% |
| PF_SOLUSD | 2 | -200.2% | 726.0% |
| PF_TRUMPUSD | 2 | -113.3% | 178.3% |
| PF_HYPEUSD | 1 | +617.3% | 617.3% |
| PF_UNIUSD | 1 | -229.5% | 229.5% |
| PF_SYNUSD | 1 | +33.5% | 33.5% |
| PF_BBUSD | 1 | +30.2% | 30.2% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 40%), PF_WLDUSD (crowded 2d, worst 33%), PF_RUNEUSD (crowded 3d, worst 52%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
