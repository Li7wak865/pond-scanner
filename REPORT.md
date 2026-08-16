# Pond Scanner Report
**Scan time:** 2026-08-16 01:57 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -429.8% | $25,819,375 |
| 🟢 | PF_COWUSD | -295.5% | $1,211,716 |
| 🟢 | PF_LINKUSD | +156.8% | $889,230 |
| 🟢 | PF_HFTUSD | +117.4% | $7,120,550 |
| 🟢 | PF_AVAXUSD | -98.3% | $527,498 |
| 🟢 | PF_KAITOUSD | -46.2% | $603,004 |
| 🟢 | PF_ALICEUSD | -41.6% | $1,587,846 |
| 🟢 | PF_BICOUSD | -33.1% | $27,540,976 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $62,978.99, kraken: $62,986.00, gemini: $62,989.91
- ⚪ **ETH** gap **0.015%** (coinbase → gemini) — coinbase: $1,877.33, kraken: $1,877.53, gemini: $1,877.61

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| CoW Protocol (COW) | #311 | $71.9M | 1.54x | +34.7% |
| Capricorn (APR) | #453 | $44.3M | 1.16x | -71.6% |
| Walrus (WAL) | #380 | $58.0M | 0.63x | +18.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 13% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 8% vs 30d norm 26% (0.3x)
- ⚪ **ETH** 24h vol 10% vs 30d norm 35% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +156.8% | 190.8% |
| PF_ALICEUSD | 3 | -41.6% | 195.8% |
| PF_ACEUSD | 2 | -429.8% | 732.3% |
| PF_COWUSD | 2 | -295.5% | 603.4% |
| PF_HFTUSD | 1 | +117.4% | 117.4% |
| PF_AVAXUSD | 1 | -98.3% | 98.3% |
| PF_KAITOUSD | 1 | -46.2% | 46.2% |
| PF_BICOUSD | 1 | -33.1% | 33.1% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 3d, worst 121%), PF_JTOUSD (crowded 2d, worst 36%), PF_BIOUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
