# Pond Scanner Report
**Scan time:** 2026-08-12 19:26 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -348.3% | $1,986,449 |
| 🟢 | PF_LINKUSD | +107.5% | $520,670 |
| 🟢 | PF_COTIUSD | -57.5% | $33,230,720 |
| 🟢 | PF_RUNEUSD | +53.6% | $524,577 |
| 🟢 | PF_ATOMUSD | +34.6% | $529,865 |
| ⚪ | PF_VIRTUALUSD | -26.3% | $1,514,509 |
| ⚪ | PF_STORJUSD | -23.2% | $2,444,592 |
| ⚪ | PF_ARCUSD | -20.2% | $1,318,459 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.034%** (kraken → gemini) — coinbase: $63,270.00, kraken: $63,250.10, gemini: $63,271.86
- ⚪ **ETH** gap **0.060%** (gemini → coinbase) — coinbase: $1,881.58, kraken: $1,881.37, gemini: $1,880.46

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Babylon (BABY) | #449 | $45.7M | 4.69x | -16.9% |
| Prom (PROM) | #441 | $47.9M | 2.41x | +31.1% |
| Tutorial (TUT) | #360 | $62.8M | 1.85x | -26.1% |
| COTI (COTI) | #484 | $43.1M | 0.84x | +27.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 14% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 20% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 27% (0.8x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 39% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 1 | -348.3% | 946.7% |
| PF_LINKUSD | 1 | +107.5% | 107.5% |
| PF_COTIUSD | 1 | -57.5% | 57.5% |
| PF_RUNEUSD | 1 | +53.6% | 53.6% |
| PF_ATOMUSD | 1 | +34.6% | 58.0% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 156%), PF_STORJUSD (crowded 1d, worst 47%), PF_APTUSD (crowded 1d, worst 41%), PF_USUALUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
