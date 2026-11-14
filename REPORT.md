# Pond Scanner Report
**Scan time:** 2026-11-14 22:25 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +944.9% | $1,001,243 |
| 🟢 | PF_INJUSD | -746.6% | $662,145 |
| 🟢 | PF_NEARUSD | -210.0% | $3,095,381 |
| 🟢 | PF_ZROUSD | -192.0% | $1,015,405 |
| 🟢 | PF_KAVAUSD | -169.0% | $36,806,211 |
| 🟢 | PF_TRUMPUSD | -89.7% | $929,436 |
| 🟢 | PF_UNIUSD | -82.4% | $853,325 |
| 🟢 | PF_APTUSD | -57.4% | $1,763,679 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.044%** (coinbase → gemini) — coinbase: $64,220.99, kraken: $64,235.50, gemini: $64,249.40
- ⚪ **ETH** gap **0.075%** (coinbase → gemini) — coinbase: $1,766.48, kraken: $1,766.77, gemini: $1,767.80

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Kava (KAVA) | #473 | $38.9M | 1.40x | -47.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.54, realized vol 10d 45% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.52, realized vol 10d 60% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9950 (-0.50% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 55% vs 30d norm 37% (1.5x)
- ⚪ **ETH** 24h vol 81% vs 30d norm 52% (1.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -82.4% | 273.6% |
| PF_INJUSD | 2 | -746.6% | 746.6% |
| PF_HYPEUSD | 1 | +944.9% | 944.9% |
| PF_NEARUSD | 1 | -210.0% | 210.0% |
| PF_ZROUSD | 1 | -192.0% | 192.0% |
| PF_KAVAUSD | 1 | -169.0% | 169.0% |
| PF_TRUMPUSD | 1 | -89.7% | 89.7% |
| PF_APTUSD | 1 | -57.4% | 57.4% |
| PF_SUIUSD | 1 | -45.5% | 45.5% |
| PF_GRASSUSD | 1 | -39.2% | 39.2% |

**Resolved since last scan:** PF_XRPUSD (crowded 1d, worst 40%), PF_ASTERUSD (crowded 1d, worst 35%), PF_TRXUSD (crowded 1d, worst 30%), PF_DOTUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
