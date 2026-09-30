# Pond Scanner Report
**Scan time:** 2026-09-30 12:36 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ARCUSD | -312.4% | $848,287 |
| 🟢 | PF_NEARUSD | +265.3% | $5,117,679 |
| 🟢 | PF_MOVRUSD | +242.9% | $532,311 |
| 🟢 | PF_AVAXUSD | +143.7% | $617,462 |
| 🟢 | PF_RAREUSD | +79.7% | $647,534 |
| 🟢 | PF_SOONUSD | -73.9% | $802,746 |
| 🟢 | PF_ETHFIUSD | +70.3% | $842,910 |
| 🟢 | PF_APTUSD | +58.9% | $528,917 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.051%** (coinbase → gemini) — coinbase: $84,620.80, kraken: $84,627.40, gemini: $84,663.90
- ⚪ **ETH** gap **0.022%** (kraken → gemini) — coinbase: $2,722.69, kraken: $2,722.35, gemini: $2,722.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #485 | $50.0M | 0.79x | +18.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.38, realized vol 10d 43% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.34, realized vol 10d 35% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 46% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ETHFIUSD | 5 | +70.3% | 246.1% |
| PF_AVAXUSD | 2 | +143.7% | 289.8% |
| PF_RAREUSD | 2 | +79.7% | 79.7% |
| PF_VETUSD | 2 | +39.5% | 39.5% |
| PF_ARCUSD | 1 | -312.4% | 312.4% |
| PF_NEARUSD | 1 | +265.3% | 265.3% |
| PF_MOVRUSD | 1 | +242.9% | 242.9% |
| PF_SOONUSD | 1 | -73.9% | 73.9% |
| PF_APTUSD | 1 | +58.9% | 58.9% |
| PF_XRPUSD | 1 | +49.8% | 49.8% |
| PF_VIRTUALUSD | 1 | +36.4% | 36.4% |

**Resolved since last scan:** PF_2ZUSD (crowded 2d, worst 285%), PF_UNIUSD (crowded 5d, worst 493%), PF_ENJUSD (crowded 1d, worst 129%), PF_SOLUSD (crowded 2d, worst 804%), PF_SPXUSD (crowded 2d, worst 109%), PF_RUNEUSD (crowded 2d, worst 55%), PF_GRASSUSD (crowded 1d, worst 45%), PF_GMTUSD (crowded 1d, worst 37%), PF_SWARMSUSD (crowded 2d, worst 35%), PF_LINKUSD (crowded 5d, worst 600%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
