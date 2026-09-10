# Pond Scanner Report
**Scan time:** 2026-09-10 20:52 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -564.9% | $553,212 |
| 🟢 | PF_RAYUSD | +190.6% | $754,908 |
| 🟢 | PF_OPNUSD | -121.6% | $4,292,268 |
| 🟢 | PF_TRUMPUSD | -110.4% | $1,888,234 |
| 🟢 | PF_ATOMUSD | +99.1% | $642,870 |
| 🟢 | PF_NEARUSD | -60.9% | $2,145,144 |
| 🟢 | PF_UNIUSD | +47.2% | $1,560,131 |
| 🟢 | PF_APTUSD | +42.7% | $980,819 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $77,252.57, kraken: $77,253.60, gemini: $77,261.81
- ⚪ **ETH** gap **0.020%** (kraken → coinbase) — coinbase: $2,461.88, kraken: $2,461.38, gemini: $2,461.88

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| VeThor (VTHO) | #388 | $62.5M | 3.13x | +40.4% |
| Bifrost (BFC) | #414 | $56.4M | 2.19x | +276.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 37% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 37% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 41% (0.7x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 55% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -60.9% | 246.3% |
| PF_TRUMPUSD | 2 | -110.4% | 507.7% |
| PF_UNIUSD | 2 | +47.2% | 361.6% |
| PF_SOLUSD | 1 | -564.9% | 564.9% |
| PF_RAYUSD | 1 | +190.6% | 372.8% |
| PF_OPNUSD | 1 | -121.6% | 121.6% |
| PF_ATOMUSD | 1 | +99.1% | 122.6% |
| PF_APTUSD | 1 | +42.7% | 42.7% |
| PF_DOTUSD | 1 | -42.3% | 58.4% |
| PF_RUNEUSD | 1 | +38.0% | 38.0% |
| PF_CATIUSD | 1 | +37.3% | 37.3% |
| PF_SWARMSUSD | 1 | +30.9% | 30.9% |

**Resolved since last scan:** PF_SPXUSD (crowded 1d, worst 124%), PF_ICXUSD (crowded 1d, worst 54%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
