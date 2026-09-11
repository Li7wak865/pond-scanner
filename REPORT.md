# Pond Scanner Report
**Scan time:** 2026-09-11 16:29 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -285.6% | $1,437,072 |
| 🟢 | PF_NEARUSD | -116.1% | $2,342,527 |
| 🟢 | PF_HFTUSD | +106.8% | $528,681 |
| 🟢 | PF_TRUMPUSD | -73.9% | $1,058,580 |
| 🟢 | PF_RAYUSD | -70.9% | $1,497,212 |
| 🟢 | PF_RUNEUSD | -67.4% | $747,203 |
| 🟢 | PF_ATOMUSD | -54.6% | $510,730 |
| 🟢 | PF_ETHFIUSD | +41.9% | $1,179,607 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → kraken) — coinbase: $77,662.04, kraken: $77,673.00, gemini: $77,672.67
- ⚪ **ETH** gap **0.029%** (kraken → gemini) — coinbase: $2,563.61, kraken: $2,563.43, gemini: $2,564.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Blur (BLUR) | #414 | $56.6M | 0.85x | +21.7% |
| LAB (LAB) | #463 | $49.2M | 0.62x | +32.9% |
| Theta Fuel (TFUEL) | #310 | $83.0M | 0.57x | +22.0% |
| Bifrost (BFC) | #460 | $48.9M | 0.52x | -17.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 39% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.17, realized vol 10d 46% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 50% vs 30d norm 41% (1.2x)
- ⚪ **ETH** 24h vol 110% vs 30d norm 58% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -285.6% | 361.6% |
| PF_ATOMUSD | 2 | -54.6% | 122.6% |
| PF_NEARUSD | 1 | -116.1% | 116.1% |
| PF_HFTUSD | 1 | +106.8% | 106.8% |
| PF_TRUMPUSD | 1 | -73.9% | 73.9% |
| PF_RAYUSD | 1 | -70.9% | 260.9% |
| PF_RUNEUSD | 1 | -67.4% | 67.4% |
| PF_ETHFIUSD | 1 | +41.9% | 41.9% |
| PF_CROUSD | 1 | -33.9% | 33.9% |

**Resolved since last scan:** PF_LSKUSD (crowded 1d, worst 171%), PF_APTUSD (crowded 2d, worst 44%), PF_DOTUSD (crowded 1d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
