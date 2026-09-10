# Pond Scanner Report
**Scan time:** 2026-09-10 04:44 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BELUSD | -481.5% | $1,058,704 |
| 🟢 | PF_RAYUSD | -393.5% | $1,478,292 |
| 🟢 | PF_UNIUSD | -270.5% | $1,245,208 |
| 🟢 | PF_LINKUSD | +145.8% | $722,162 |
| 🟢 | PF_TRUMPUSD | +116.0% | $2,263,210 |
| 🟢 | PF_SOLUSD | -91.2% | $994,811 |
| 🟢 | PF_NEARUSD | +44.6% | $3,810,132 |
| 🟢 | PF_ASTERUSD | +41.0% | $746,495 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → gemini) — coinbase: $78,309.97, kraken: $78,310.80, gemini: $78,330.84
- ⚪ **ETH** gap **0.056%** (coinbase → gemini) — coinbase: $2,476.57, kraken: $2,477.12, gemini: $2,477.96

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 牛来 (Niu Lai) (牛来) | #317 | $81.3M | 1.22x | -24.1% |
| VeThor (VTHO) | #333 | $74.7M | 1.18x | +62.9% |
| MarsCoin (MARSCOIN) | #258 | $108.3M | 0.83x | -16.6% |
| A Meme Coin (AMC) | #400 | $61.2M | 0.57x | -24.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.00, realized vol 10d 36% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 37% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 40% (0.8x)
- ⚪ **ETH** 24h vol 41% vs 30d norm 54% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +44.6% | 246.3% |
| PF_RAYUSD | 2 | -393.5% | 657.3% |
| PF_UNIUSD | 2 | -270.5% | 361.6% |
| PF_LINKUSD | 2 | +145.8% | 350.9% |
| PF_TRUMPUSD | 2 | +116.0% | 507.7% |
| PF_SOLUSD | 2 | -91.2% | 597.5% |
| PF_ACEUSD | 2 | -40.0% | 64.2% |
| PF_BELUSD | 1 | -481.5% | 481.5% |
| PF_ASTERUSD | 1 | +41.0% | 41.0% |
| PF_APTUSD | 1 | -37.4% | 37.4% |

**Resolved since last scan:** PF_ATOMUSD (crowded 2d, worst 92%), PF_XTZUSD (crowded 2d, worst 32%), PF_SWARMSUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
