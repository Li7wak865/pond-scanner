# Pond Scanner Report
**Scan time:** 2026-09-07 04:43 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | -310.9% | $873,666 |
| 🟢 | PF_TRUMPUSD | +178.5% | $1,453,148 |
| 🟢 | PF_UNIUSD | +137.6% | $1,106,420 |
| 🟢 | PF_NEARUSD | +132.4% | $2,292,923 |
| 🟢 | PF_ACEUSD | -105.0% | $502,628 |
| 🟢 | PF_ASTERUSD | +70.3% | $800,357 |
| 🟢 | PF_CFGUSD | -61.6% | $1,571,550 |
| 🟢 | PF_LINKUSD | -40.2% | $926,164 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (gemini → kraken) — coinbase: $79,648.56, kraken: $79,649.30, gemini: $79,628.00
- ⚪ **ETH** gap **0.037%** (gemini → coinbase) — coinbase: $2,496.40, kraken: $2,496.35, gemini: $2,495.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| A Meme Coin (AMC) | #312 | $84.1M | 1.46x | +93.0% |
| 哈基米 (Hajimi) (哈基米) | #412 | $58.4M | 0.95x | +256.2% |
| Centrifuge (CFG) | #479 | $47.7M | 0.69x | +22.4% |
| Boner Coin (BONER) | #363 | $70.0M | 0.65x | +135.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.48, realized vol 10d 36% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 40% (0.4x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 54% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | +178.5% | 476.2% |
| PF_UNIUSD | 3 | +137.6% | 387.6% |
| PF_NEARUSD | 3 | +132.4% | 163.9% |
| PF_RAYUSD | 2 | -310.9% | 310.9% |
| PF_ACEUSD | 2 | -105.0% | 133.5% |
| PF_ASTERUSD | 1 | +70.3% | 70.3% |
| PF_CFGUSD | 1 | -61.6% | 61.6% |
| PF_LINKUSD | 1 | -40.2% | 40.2% |
| PF_XRPUSD | 1 | -31.5% | 31.5% |

**Resolved since last scan:** PF_COTIUSD (crowded 2d, worst 229%), PF_MINAUSD (crowded 2d, worst 199%), PF_HFTUSD (crowded 2d, worst 115%), PF_ICXUSD (crowded 2d, worst 36%), PF_JUPUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
