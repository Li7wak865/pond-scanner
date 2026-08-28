# Pond Scanner Report
**Scan time:** 2026-08-28 22:21 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +218.5% | $756,394 |
| 🟢 | PF_RUNEUSD | -102.4% | $604,151 |
| 🟢 | PF_ACEUSD | -89.5% | $1,026,656 |
| 🟢 | PF_STXUSD | -60.2% | $1,169,859 |
| ⚪ | PF_NEARUSD | -21.3% | $697,600 |
| ⚪ | PF_TRUMPUSD | +18.9% | $4,245,926 |
| ⚪ | PF_SUSHIUSD | +17.7% | $783,992 |
| ⚪ | PF_XRPUSD | +17.2% | $34,506,696 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (gemini → kraken) — coinbase: $77,466.97, kraken: $77,479.00, gemini: $77,463.82
- ⚪ **ETH** gap **0.030%** (gemini → kraken) — coinbase: $2,428.43, kraken: $2,429.00, gemini: $2,428.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DeXe (DEXE) | #294 | $86.7M | 1.20x | +28.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.49, realized vol 10d 66% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 114% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 37% vs 30d norm 38% (1.0x)
- ⚪ **ETH** 24h vol 48% vs 30d norm 51% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 7 | -89.5% | 241.7% |
| PF_SOLUSD | 1 | +218.5% | 218.5% |
| PF_RUNEUSD | 1 | -102.4% | 102.4% |
| PF_STXUSD | 1 | -60.2% | 60.2% |

**Resolved since last scan:** PF_MOVRUSD (crowded 2d, worst 328%), PF_TRUMPUSD (crowded 4d, worst 417%), PF_UNIUSD (crowded 1d, worst 94%), PF_SPXUSD (crowded 3d, worst 201%), PF_NEARUSD (crowded 3d, worst 75%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
