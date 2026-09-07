# Pond Scanner Report
**Scan time:** 2026-09-07 12:34 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +236.7% | $1,132,412 |
| 🟢 | PF_UNIUSD | +193.0% | $990,506 |
| 🟢 | PF_TRUMPUSD | +155.0% | $1,177,623 |
| 🟢 | PF_RAYUSD | -135.7% | $726,615 |
| 🟢 | PF_CFGUSD | -74.8% | $1,760,700 |
| 🟢 | PF_ASTERUSD | +73.6% | $1,182,563 |
| ⚪ | PF_XRPUSD | +29.6% | $22,084,766 |
| ⚪ | PF_VELOUSD | -21.0% | $759,810 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (coinbase → kraken) — coinbase: $79,494.29, kraken: $79,500.10, gemini: $79,496.67
- ⚪ **ETH** gap **0.003%** (gemini → kraken) — coinbase: $2,493.21, kraken: $2,493.27, gemini: $2,493.20

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| A Meme Coin (AMC) | #259 | $109.4M | 1.50x | +192.6% |
| Centrifuge (CFG) | #481 | $47.6M | 1.19x | +15.9% |
| STONK (STONK) | #302 | $88.8M | 0.78x | -15.8% |
| Boner Coin (BONER) | #408 | $59.3M | 0.66x | +117.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.47, realized vol 10d 36% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 40% (0.5x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 54% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | +155.0% | 476.2% |
| PF_UNIUSD | 3 | +193.0% | 387.6% |
| PF_RAYUSD | 2 | -135.7% | 310.9% |
| PF_LINKUSD | 1 | +236.7% | 236.7% |
| PF_CFGUSD | 1 | -74.8% | 74.8% |
| PF_ASTERUSD | 1 | +73.6% | 73.6% |

**Resolved since last scan:** PF_NEARUSD (crowded 3d, worst 164%), PF_ACEUSD (crowded 2d, worst 134%), PF_XRPUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
