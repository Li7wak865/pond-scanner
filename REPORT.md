# Pond Scanner Report
**Scan time:** 2026-10-23 04:51 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_OPNUSD | +224.7% | $655,706 |
| 🟢 | PF_NEARUSD | -73.3% | $2,998,162 |
| 🟢 | PF_ATOMUSD | +60.6% | $589,680 |
| 🟢 | PF_FILUSD | +53.4% | $2,848,472 |
| 🟢 | PF_TRUMPUSD | +47.0% | $812,863 |
| 🟢 | PF_BATUSD | -35.7% | $3,630,608 |
| 🟢 | PF_PONSUSD | +32.1% | $852,615 |
| ⚪ | PF_ZROUSD | +27.8% | $573,674 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (kraken → coinbase) — coinbase: $81,561.54, kraken: $81,542.00, gemini: $81,557.43
- ⚪ **ETH** gap **0.036%** (coinbase → gemini) — coinbase: $2,393.83, kraken: $2,394.10, gemini: $2,394.70

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #418 | $53.7M | 2.66x | +23.8% |
| AltLayer (ALT) | #405 | $58.5M | 1.57x | -34.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 26% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.36, realized vol 10d 31% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 32% (0.8x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -73.3% | 175.8% |
| PF_TRUMPUSD | 2 | +47.0% | 47.0% |
| PF_BATUSD | 2 | -35.7% | 52.9% |
| PF_OPNUSD | 1 | +224.7% | 224.7% |
| PF_ATOMUSD | 1 | +60.6% | 60.6% |
| PF_FILUSD | 1 | +53.4% | 53.4% |
| PF_PONSUSD | 1 | +32.1% | 32.1% |

**Resolved since last scan:** PF_ZROUSD (crowded 3d, worst 148%), PF_TIAUSD (crowded 2d, worst 44%), PF_APTUSD (crowded 2d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
