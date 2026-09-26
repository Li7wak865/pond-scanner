# Pond Scanner Report
**Scan time:** 2026-09-26 05:00 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +435.3% | $1,248,896 |
| 🟢 | PF_LINKUSD | -364.0% | $924,084 |
| 🟢 | PF_ZROUSD | +280.0% | $771,854 |
| 🟢 | PF_LSKUSD | -191.7% | $648,619 |
| 🟢 | PF_TRUMPUSD | +99.9% | $593,166 |
| 🟢 | PF_GRASSUSD | +72.5% | $746,673 |
| 🟢 | PF_JTOUSD | -53.7% | $2,159,914 |
| 🟢 | PF_KAITOUSD | -50.3% | $838,824 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (kraken → gemini) — coinbase: $83,975.53, kraken: $83,975.30, gemini: $83,977.22
- ⚪ **ETH** gap **0.003%** (coinbase → kraken) — coinbase: $2,689.13, kraken: $2,689.21, gemini: $2,689.19

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #377 | $72.5M | 3.45x | +68.9% |
| Mubarak (MUBARAK) | #449 | $57.0M | 1.76x | +31.3% |
| ARK (ARK) | #482 | $51.2M | 1.60x | +32.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 35% (0.6x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 47% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | +99.9% | 372.6% |
| PF_UNIUSD | 2 | +435.3% | 537.1% |
| PF_ZROUSD | 2 | +280.0% | 280.0% |
| PF_LSKUSD | 2 | -191.7% | 191.7% |
| PF_GRASSUSD | 2 | +72.5% | 72.5% |
| PF_JTOUSD | 2 | -53.7% | 61.8% |
| PF_DOTUSD | 2 | +45.2% | 45.2% |
| PF_LINKUSD | 1 | -364.0% | 364.0% |
| PF_KAITOUSD | 1 | -50.3% | 50.3% |
| PF_ONDOUSD | 1 | +42.4% | 42.4% |
| PF_VIRTUALUSD | 1 | +38.3% | 38.3% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 692%), PF_NEARUSD (crowded 4d, worst 405%), PF_ASTERUSD (crowded 2d, worst 63%), PF_WLDUSD (crowded 2d, worst 45%), PF_XPLUSD (crowded 2d, worst 44%), PF_NIGHTUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
