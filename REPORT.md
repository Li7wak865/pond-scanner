# Pond Scanner Report
**Scan time:** 2026-09-25 21:35 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -691.6% | $879,315 |
| 🟢 | PF_UNIUSD | +537.1% | $1,145,975 |
| 🟢 | PF_ZROUSD | +266.4% | $821,695 |
| 🟢 | PF_LSKUSD | -186.5% | $872,925 |
| 🟢 | PF_TRUMPUSD | +134.0% | $550,918 |
| 🟢 | PF_GRASSUSD | +71.2% | $644,791 |
| 🟢 | PF_JTOUSD | -61.8% | $2,331,408 |
| 🟢 | PF_NEARUSD | -49.3% | $4,848,419 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (coinbase → gemini) — coinbase: $83,807.49, kraken: $83,809.90, gemini: $83,810.79
- ⚪ **ETH** gap **0.004%** (kraken → coinbase) — coinbase: $2,680.40, kraken: $2,680.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #369 | $74.0M | 2.76x | +69.9% |
| Mubarak (MUBARAK) | #465 | $53.8M | 1.68x | +18.4% |
| Lisk (LSK) | #342 | $79.3M | 0.58x | -23.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 35% (0.6x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 47% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +134.0% | 372.6% |
| PF_NEARUSD | 3 | -49.3% | 404.8% |
| PF_SOLUSD | 1 | -691.6% | 691.6% |
| PF_UNIUSD | 1 | +537.1% | 537.1% |
| PF_ZROUSD | 1 | +266.4% | 266.4% |
| PF_LSKUSD | 1 | -186.5% | 186.5% |
| PF_GRASSUSD | 1 | +71.2% | 71.2% |
| PF_JTOUSD | 1 | -61.8% | 61.8% |
| PF_ASTERUSD | 1 | +48.0% | 63.1% |
| PF_WLDUSD | 1 | +45.1% | 45.1% |
| PF_XPLUSD | 1 | +43.9% | 43.9% |
| PF_DOTUSD | 1 | +40.7% | 40.7% |
| PF_NIGHTUSD | 1 | +31.7% | 31.7% |

**Resolved since last scan:** PF_RUNEUSD (crowded 1d, worst 116%), PF_LINKUSD (crowded 2d, worst 483%), PF_RAREUSD (crowded 1d, worst 72%), PF_MINAUSD (crowded 1d, worst 62%), PF_XRPUSD (crowded 1d, worst 50%), PF_SPXUSD (crowded 1d, worst 44%), PF_SUIUSD (crowded 1d, worst 38%), PF_BLURUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
