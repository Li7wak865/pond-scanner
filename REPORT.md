# Pond Scanner Report
**Scan time:** 2026-11-22 06:50 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -42.7% | $650,216 |
| 🟢 | PF_UNIUSD | -32.3% | $681,692 |
| ⚪ | PF_ETHFIUSD | +28.7% | $2,057,459 |
| ⚪ | PF_FETUSD | -17.9% | $6,659,551 |
| ⚪ | PF_NEARUSD | +17.9% | $2,586,323 |
| ⚪ | PF_TRXUSD | -13.2% | $1,903,890 |
| ⚪ | PF_XRPUSD | -11.6% | $13,589,415 |
| ⚪ | PF_DOTUSD | -9.9% | $1,696,482 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.077%** (kraken → gemini) — coinbase: $59,037.51, kraken: $59,036.30, gemini: $59,081.54
- ⚪ **ETH** gap **0.017%** (coinbase → gemini) — coinbase: $1,660.24, kraken: $1,660.32, gemini: $1,660.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #405 | $45.6M | 1.21x | -21.5% |
| Akedo (AKE) | #326 | $63.8M | 0.77x | -45.5% |
| Momentum (MMT) | #420 | $43.6M | 0.60x | -17.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.56, realized vol 10d 51% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 75% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9946 (-0.54% vs peg)
- ⚪ **USDT** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9986 (-0.14% vs peg)
- ⚪ **USDC** $0.9992 (-0.08% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 68% vs 30d norm 51% (1.3x)
- ⚪ **ETH** 24h vol 59% vs 30d norm 65% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 6 | -32.3% | 220.1% |
| PF_TRUMPUSD | 1 | -42.7% | 42.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 365%), PF_NEARUSD (crowded 2d, worst 67%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
