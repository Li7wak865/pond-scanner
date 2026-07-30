# Pond Scanner Report
**Scan time:** 2026-07-30 19:53 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -276.7% | $973,007 |
| 🟢 | PF_UNIUSD | -80.0% | $1,393,689 |
| 🟢 | PF_SUSHIUSD | +36.7% | $759,454 |
| ⚪ | PF_DOTUSD | -26.5% | $1,232,030 |
| ⚪ | PF_SYNUSD | -20.1% | $1,152,567 |
| ⚪ | PF_XTZUSD | -19.9% | $657,914 |
| ⚪ | PF_XRPUSD | +19.7% | $13,198,498 |
| ⚪ | PF_FETUSD | -16.5% | $8,796,386 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (gemini → kraken) — coinbase: $64,775.56, kraken: $64,777.10, gemini: $64,775.21
- ⚪ **ETH** gap **0.034%** (kraken → gemini) — coinbase: $1,923.25, kraken: $1,922.94, gemini: $1,923.59

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Espresso (ESP) | #445 | $47.8M | 1.29x | +21.8% |
| Momentum (MMT) | #414 | $52.6M | 1.06x | +40.7% |
| Cash Cat (CASHCAT) | #441 | $46.5M | 0.60x | +30.2% |
| Cap (CAP) | #380 | $58.4M | 0.53x | +32.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 27% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 34% (0.8x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 45% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -276.7% | 326.1% |
| PF_UNIUSD | 1 | -80.0% | 80.0% |
| PF_SUSHIUSD | 1 | +36.7% | 36.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 421%), PF_SOONUSD (crowded 1d, worst 53%), PF_SYNUSD (crowded 4d, worst 80%), PF_COTIUSD (crowded 1d, worst 59%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
