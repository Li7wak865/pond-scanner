# Pond Scanner Report
**Scan time:** 2026-09-23 11:38 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -303.3% | $738,425 |
| 🟢 | PF_ZROUSD | +275.8% | $973,830 |
| 🟢 | PF_SOLUSD | -274.3% | $601,455 |
| 🟢 | PF_IOTAUSD | +218.4% | $624,861 |
| 🟢 | PF_RUNEUSD | +185.8% | $608,980 |
| 🟢 | PF_ACEUSD | +161.2% | $1,531,071 |
| 🟢 | PF_AVAXUSD | +155.1% | $633,515 |
| 🟢 | PF_HFTUSD | -112.1% | $1,103,427 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (kraken → gemini) — coinbase: $85,471.36, kraken: $85,468.70, gemini: $85,483.09
- ⚪ **ETH** gap **0.015%** (coinbase → gemini) — coinbase: $2,717.63, kraken: $2,717.89, gemini: $2,718.04

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| OVERTAKE (TAKE) | #388 | $69.5M | 0.95x | +240.1% |
| Aurora (AURORA) | #416 | $62.6M | 0.59x | +30.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.18, realized vol 10d 55% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 58% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 36% (0.7x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 47% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -303.3% | 303.3% |
| PF_RUNEUSD | 2 | +185.8% | 185.8% |
| PF_AVAXUSD | 2 | +155.1% | 155.1% |
| PF_ETHFIUSD | 2 | +90.2% | 137.0% |
| PF_ZROUSD | 1 | +275.8% | 275.8% |
| PF_SOLUSD | 1 | -274.3% | 274.3% |
| PF_IOTAUSD | 1 | +218.4% | 218.4% |
| PF_ACEUSD | 1 | +161.2% | 161.2% |
| PF_HFTUSD | 1 | -112.1% | 112.1% |
| PF_BLURUSD | 1 | +91.5% | 91.5% |
| PF_MINAUSD | 1 | -61.6% | 61.6% |
| PF_VIRTUALUSD | 1 | +53.9% | 53.9% |
| PF_APTUSD | 1 | +49.8% | 49.8% |
| PF_TIAUSD | 1 | +45.1% | 47.4% |
| PF_WLDUSD | 1 | +35.8% | 35.8% |

**Resolved since last scan:** PF_UNIUSD (crowded 7d, worst 857%), PF_LINKUSD (crowded 3d, worst 726%), PF_NEARUSD (crowded 4d, worst 458%), PF_TRUMPUSD (crowded 3d, worst 207%), PF_EIGENUSD (crowded 1d, worst 44%), PF_JTOUSD (crowded 1d, worst 40%), PF_RENDERUSD (crowded 3d, worst 210%), PF_FETUSD (crowded 1d, worst 35%), PF_SYNUSD (crowded 1d, worst 34%), PF_ASTRUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
