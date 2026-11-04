# Pond Scanner Report
**Scan time:** 2026-11-04 19:46 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -726.0% | $999,262 |
| 🟢 | PF_TRUMPUSD | -178.3% | $5,402,001 |
| 🟢 | PF_NEARUSD | -126.6% | $6,842,545 |
| 🟢 | PF_ZROUSD | +39.5% | $615,527 |
| 🟢 | PF_WLDUSD | -33.4% | $6,412,905 |
| 🟢 | PF_RUNEUSD | -31.6% | $502,459 |
| ⚪ | PF_UNIUSD | -26.3% | $839,892 |
| ⚪ | PF_FILUSD | +25.6% | $1,028,212 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (coinbase → kraken) — coinbase: $79,984.38, kraken: $80,005.30, gemini: $80,000.01
- ⚪ **ETH** gap **0.023%** (coinbase → gemini) — coinbase: $2,413.40, kraken: $2,413.53, gemini: $2,413.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Janction (JCT) | #387 | $61.8M | 0.70x | +22.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.11, realized vol 10d 37% vs 60d 35%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 48% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9979 (-0.21% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 51% vs 30d norm 33% (1.5x)
- ⚪ **ETH** 24h vol 74% vs 30d norm 47% (1.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -126.6% | 126.6% |
| PF_RUNEUSD | 2 | -31.6% | 51.8% |
| PF_SOLUSD | 1 | -726.0% | 726.0% |
| PF_TRUMPUSD | 1 | -178.3% | 178.3% |
| PF_ZROUSD | 1 | +39.5% | 39.5% |
| PF_WLDUSD | 1 | -33.4% | 33.4% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
