# Pond Scanner Report
**Scan time:** 2026-08-24 01:57 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PI_XRPUSD | -502.6% | $906,617 |
| 🟢 | PF_ACEUSD | -241.7% | $2,075,012 |
| 🟢 | PF_SOLUSD | -163.9% | $1,982,469 |
| 🟢 | PF_RENDERUSD | +152.2% | $605,687 |
| 🟢 | PF_UNIUSD | +110.6% | $984,395 |
| 🟢 | PF_ETHFIUSD | -73.3% | $844,655 |
| 🟢 | PF_STORJUSD | -71.1% | $636,984 |
| 🟢 | PF_GRASSUSD | +63.8% | $620,784 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.006%** (kraken → gemini) — coinbase: $77,001.97, kraken: $76,997.30, gemini: $77,002.15
- ⚪ **ETH** gap **0.019%** (kraken → coinbase) — coinbase: $2,430.31, kraken: $2,429.84, gemini: $2,430.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Spark (SPK) | #337 | $69.8M | 1.19x | +29.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 61% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.60, realized vol 10d 110% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 36% (1.0x)
- ⚪ **ETH** 24h vol 62% vs 30d norm 52% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | +110.6% | 413.9% |
| PF_TRUMPUSD | 5 | -60.8% | 332.5% |
| PF_ACEUSD | 3 | -241.7% | 241.7% |
| PI_XRPUSD | 2 | -502.6% | 502.6% |
| PF_SOLUSD | 2 | -163.9% | 437.2% |
| PF_RENDERUSD | 2 | +152.2% | 152.2% |
| PF_HFTUSD | 2 | -54.4% | 110.6% |
| PF_ZROUSD | 2 | +37.3% | 93.1% |
| PF_ETHFIUSD | 1 | -73.3% | 73.3% |
| PF_STORJUSD | 1 | -71.1% | 71.1% |
| PF_GRASSUSD | 1 | +63.8% | 63.8% |
| PF_LDOUSD | 1 | -54.4% | 54.4% |
| PF_CHILLGUYUSD | 1 | -51.7% | 51.7% |
| PF_EIGENUSD | 1 | +34.7% | 34.7% |

**Resolved since last scan:** PF_LINKUSD (crowded 5d, worst 819%), PF_NEARUSD (crowded 2d, worst 161%), PF_OGNUSD (crowded 2d, worst 84%), PF_SYNUSD (crowded 4d, worst 506%), PF_FETUSD (crowded 2d, worst 96%), PF_WLDUSD (crowded 2d, worst 56%), PF_STXUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
