# Pond Scanner Report
**Scan time:** 2026-09-23 17:01 UTC

**Flags this scan:** 21 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | +470.6% | $513,691 |
| 🟢 | PF_LINKUSD | -405.6% | $776,586 |
| 🟢 | PF_TRUMPUSD | -372.6% | $1,617,164 |
| 🟢 | PF_UNIUSD | -352.2% | $2,081,603 |
| 🟢 | PF_INJUSD | +223.5% | $514,038 |
| 🟢 | PF_AVAXUSD | +218.8% | $761,627 |
| 🟢 | PF_NEARUSD | -201.5% | $9,432,250 |
| 🟢 | PF_MINAUSD | -184.1% | $944,811 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (kraken → gemini) — coinbase: $84,098.92, kraken: $84,087.00, gemini: $84,108.23
- ⚪ **ETH** gap **0.062%** (gemini → kraken) — coinbase: $2,662.30, kraken: $2,662.33, gemini: $2,660.68

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #448 | $54.5M | 2.49x | -33.6% |
| Nillion (NIL) | #481 | $49.6M | 1.89x | +19.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.11, realized vol 10d 58% vs 60d 44%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.16, realized vol 10d 62% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 35% (1.1x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 47% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AVAXUSD | 2 | +218.8% | 218.8% |
| PF_RAYUSD | 1 | +470.6% | 470.6% |
| PF_LINKUSD | 1 | -405.6% | 405.6% |
| PF_TRUMPUSD | 1 | -372.6% | 372.6% |
| PF_UNIUSD | 1 | -352.2% | 352.2% |
| PF_INJUSD | 1 | +223.5% | 223.5% |
| PF_NEARUSD | 1 | -201.5% | 201.5% |
| PF_MINAUSD | 1 | -184.1% | 184.1% |
| PF_KAITOUSD | 1 | -166.8% | 166.8% |
| PF_HFTUSD | 1 | +107.9% | 112.1% |
| PF_JTOUSD | 1 | -91.0% | 91.0% |
| PF_BLURUSD | 1 | +86.9% | 91.5% |
| PF_FILUSD | 1 | -68.2% | 68.2% |
| PF_LDOUSD | 1 | -58.1% | 58.1% |
| PF_XRPUSD | 1 | +47.1% | 47.1% |
| PF_VIRTUALUSD | 1 | -41.2% | 53.9% |
| PF_SUPERUSD | 1 | -37.9% | 37.9% |
| PF_ACEUSD | 1 | -37.4% | 161.2% |
| PF_ZROUSD | 1 | +31.7% | 275.8% |

**Resolved since last scan:** PF_LSKUSD (crowded 2d, worst 303%), PF_SOLUSD (crowded 1d, worst 274%), PF_IOTAUSD (crowded 1d, worst 218%), PF_RUNEUSD (crowded 2d, worst 186%), PF_ETHFIUSD (crowded 2d, worst 137%), PF_APTUSD (crowded 1d, worst 50%), PF_TIAUSD (crowded 1d, worst 47%), PF_WLDUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
