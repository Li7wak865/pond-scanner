# Pond Scanner Report
**Scan time:** 2026-09-10 11:21 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BELUSD | -497.2% | $1,113,482 |
| 🟢 | PF_UNIUSD | -187.9% | $1,298,620 |
| 🟢 | PF_SPXUSD | -124.2% | $521,846 |
| 🟢 | PF_SUSD | +118.9% | $632,190 |
| 🟢 | PF_TRUMPUSD | -81.6% | $2,300,851 |
| 🟢 | PF_BLURUSD | +74.3% | $917,525 |
| 🟢 | PF_NEARUSD | +57.3% | $3,331,509 |
| 🟢 | PF_ICXUSD | -42.7% | $1,627,203 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (kraken → gemini) — coinbase: $77,966.99, kraken: $77,966.10, gemini: $77,980.20
- ⚪ **ETH** gap **0.012%** (gemini → kraken) — coinbase: $2,466.02, kraken: $2,466.27, gemini: $2,465.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| VeThor (VTHO) | #378 | $66.3M | 2.11x | +46.1% |
| 牛来 (Niu Lai) (牛来) | #324 | $77.8M | 1.25x | -18.1% |
| Bifrost (BFC) | #449 | $50.2M | 1.24x | +234.5% |
| MarsCoin (MARSCOIN) | #264 | $104.1M | 0.70x | -24.5% |
| A Meme Coin (AMC) | #417 | $56.3M | 0.55x | -35.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 36% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.06, realized vol 10d 37% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 40% (0.6x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 54% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +57.3% | 246.3% |
| PF_UNIUSD | 2 | -187.9% | 361.6% |
| PF_TRUMPUSD | 2 | -81.6% | 507.7% |
| PF_BELUSD | 1 | -497.2% | 497.2% |
| PF_SPXUSD | 1 | -124.2% | 124.2% |
| PF_SUSD | 1 | +118.9% | 118.9% |
| PF_BLURUSD | 1 | +74.3% | 74.3% |
| PF_ICXUSD | 1 | -42.7% | 42.7% |
| PF_ATOMUSD | 1 | +30.3% | 30.3% |

**Resolved since last scan:** PF_RAYUSD (crowded 2d, worst 657%), PF_LINKUSD (crowded 2d, worst 351%), PF_SOLUSD (crowded 2d, worst 597%), PF_ASTERUSD (crowded 1d, worst 41%), PF_ACEUSD (crowded 2d, worst 64%), PF_APTUSD (crowded 1d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
