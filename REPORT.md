# Pond Scanner Report
**Scan time:** 2026-08-14 19:14 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALICEUSD | -195.8% | $673,698 |
| 🟢 | PF_KAITOUSD | -124.2% | $977,612 |
| 🟢 | PF_ETHFIUSD | +120.5% | $776,627 |
| 🟢 | PF_LINKUSD | +75.0% | $563,298 |
| 🟢 | PF_HFTUSD | -71.0% | $3,797,933 |
| 🟢 | PF_UNIUSD | -62.0% | $2,265,599 |
| 🟢 | PF_SAGAUSD | +57.9% | $9,965,652 |
| 🟢 | PF_MONUSD | +36.1% | $1,492,144 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (coinbase → gemini) — coinbase: $62,792.79, kraken: $62,793.40, gemini: $62,794.17
- ⚪ **ETH** gap **0.016%** (gemini → kraken) — coinbase: $1,872.36, kraken: $1,872.54, gemini: $1,872.24

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| LAB (LAB) | #650 | $66.4M | 0.59x | -23.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 14% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.00, realized vol 10d 19% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9968 (-0.32% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 26% (0.8x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 36% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALICEUSD | 1 | -195.8% | 195.8% |
| PF_KAITOUSD | 1 | -124.2% | 124.2% |
| PF_ETHFIUSD | 1 | +120.5% | 120.5% |
| PF_LINKUSD | 1 | +75.0% | 75.0% |
| PF_HFTUSD | 1 | -71.0% | 71.0% |
| PF_UNIUSD | 1 | -62.0% | 129.8% |
| PF_SAGAUSD | 1 | +57.9% | 57.9% |
| PF_MONUSD | 1 | +36.1% | 36.1% |
| PF_NEARUSD | 1 | +34.8% | 34.8% |
| PF_FILUSD | 1 | +31.8% | 31.8% |

**Resolved since last scan:** PF_ACEUSD (crowded 1d, worst 148%), PF_ATOMUSD (crowded 1d, worst 66%), PF_2ZUSD (crowded 1d, worst 53%), PF_GRASSUSD (crowded 1d, worst 48%), PF_GPSUSD (crowded 1d, worst 44%), PF_VIRTUALUSD (crowded 1d, worst 43%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
