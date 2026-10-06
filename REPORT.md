# Pond Scanner Report
**Scan time:** 2026-10-06 00:04 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -541.5% | $627,146 |
| 🟢 | PF_LINKUSD | +244.2% | $811,090 |
| 🟢 | PF_NEARUSD | -143.3% | $3,185,740 |
| 🟢 | PF_UNIUSD | +140.5% | $850,913 |
| 🟢 | PF_TRUMPUSD | +139.8% | $642,949 |
| 🟢 | PF_GRASSUSD | +72.4% | $545,863 |
| 🟢 | PF_RUNEUSD | -57.5% | $837,528 |
| 🟢 | PF_PONSUSD | +45.8% | $931,979 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $85,832.76, kraken: $85,836.80, gemini: $85,839.79
- ⚪ **ETH** gap **0.013%** (coinbase → gemini) — coinbase: $2,711.72, kraken: $2,712.00, gemini: $2,712.06

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #414 | $64.5M | 2.33x | +102.5% |
| Nillion (NIL) | #465 | $54.9M | 1.57x | +22.2% |
| Mubarak (MUBARAK) | #361 | $75.5M | 0.78x | +15.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 18% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 15% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 33% (1.0x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 4 | +45.8% | 111.2% |
| PF_MOVRUSD | 2 | -541.5% | 541.5% |
| PF_UNIUSD | 2 | +140.5% | 140.5% |
| PF_GRASSUSD | 2 | +72.4% | 84.4% |
| PF_RUNEUSD | 2 | -57.5% | 98.6% |
| PF_LINKUSD | 1 | +244.2% | 244.2% |
| PF_NEARUSD | 1 | -143.3% | 143.3% |
| PF_TRUMPUSD | 1 | +139.8% | 139.8% |
| PF_ATOMUSD | 1 | +45.1% | 45.1% |
| PF_FILUSD | 1 | +43.2% | 43.2% |
| PF_TIAUSD | 1 | +39.4% | 39.4% |
| PF_APTUSD | 1 | +39.1% | 39.1% |
| PF_FETUSD | 1 | +32.8% | 32.8% |

**Resolved since last scan:** PF_ACEUSD (crowded 2d, worst 84%), PF_VIRTUALUSD (crowded 2d, worst 39%), PF_DOTUSD (crowded 2d, worst 33%), PF_ZROUSD (crowded 2d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
