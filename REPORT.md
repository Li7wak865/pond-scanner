# Pond Scanner Report
**Scan time:** 2026-09-24 04:53 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MINAUSD | -628.4% | $1,819,638 |
| 🟢 | PF_UNIUSD | -323.1% | $1,435,675 |
| 🟢 | PF_LINKUSD | -291.1% | $703,149 |
| 🟢 | PF_TRUMPUSD | -271.9% | $1,898,935 |
| 🟢 | PF_NEARUSD | -206.5% | $8,293,579 |
| 🟢 | PF_AVAXUSD | -87.6% | $580,597 |
| 🟢 | PF_HFTUSD | -85.7% | $3,102,324 |
| 🟢 | PF_JTOUSD | -69.2% | $908,014 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (gemini → kraken) — coinbase: $83,840.10, kraken: $83,840.90, gemini: $83,839.14
- ⚪ **ETH** gap **0.083%** (gemini → coinbase) — coinbase: $2,677.02, kraken: $2,676.88, gemini: $2,674.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #383 | $68.8M | 2.57x | +42.4% |
| Mubarak (MUBARAK) | #454 | $53.6M | 1.90x | -38.4% |
| Lisk (LSK) | #319 | $84.5M | 0.60x | +15.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.18, realized vol 10d 58% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 60% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 37% vs 30d norm 35% (1.1x)
- ⚪ **ETH** 24h vol 39% vs 30d norm 47% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AVAXUSD | 3 | -87.6% | 218.8% |
| PF_MINAUSD | 2 | -628.4% | 628.4% |
| PF_UNIUSD | 2 | -323.1% | 486.3% |
| PF_LINKUSD | 2 | -291.1% | 405.6% |
| PF_TRUMPUSD | 2 | -271.9% | 372.6% |
| PF_NEARUSD | 2 | -206.5% | 294.7% |
| PF_HFTUSD | 2 | -85.7% | 112.1% |
| PF_JTOUSD | 2 | -69.2% | 94.2% |
| PF_SPXUSD | 2 | -58.4% | 58.4% |
| PF_KAITOUSD | 2 | -57.8% | 166.8% |
| PF_SWARMSUSD | 2 | -35.0% | 35.0% |
| PF_FETUSD | 2 | -31.2% | 42.3% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 255%), PF_RAYUSD (crowded 2d, worst 471%), PF_ZROUSD (crowded 2d, worst 276%), PF_APTUSD (crowded 2d, worst 61%), PF_ACEUSD (crowded 2d, worst 161%), PF_FILUSD (crowded 2d, worst 68%), PF_DOTUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
