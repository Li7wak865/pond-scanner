# Pond Scanner Report
**Scan time:** 2026-08-15 18:47 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_COWUSD | -603.4% | $960,670 |
| 🟢 | PF_ACEUSD | -377.9% | $34,572,004 |
| 🟢 | PF_LINKUSD | -190.8% | $985,396 |
| 🟢 | PF_ETHFIUSD | -91.3% | $717,350 |
| 🟢 | PF_ALICEUSD | -53.6% | $4,370,035 |
| 🟢 | PF_JTOUSD | +36.1% | $696,845 |
| 🟢 | PF_BIOUSD | +31.1% | $800,336 |
| ⚪ | PF_HFTUSD | -23.6% | $4,596,684 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.036%** (coinbase → kraken) — coinbase: $62,977.41, kraken: $63,000.10, gemini: $62,989.73
- ⚪ **ETH** gap **0.008%** (coinbase → gemini) — coinbase: $1,881.11, kraken: $1,881.14, gemini: $1,881.26

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| CoW Protocol (COW) | #288 | $82.6M | 1.32x | +35.6% |
| Capricorn (APR) | #453 | $45.4M | 1.00x | -69.3% |
| Walrus (WAL) | #355 | $63.6M | 0.60x | +22.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.25, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 13% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 26% (0.3x)
- ⚪ **ETH** 24h vol 10% vs 30d norm 35% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | -190.8% | 190.8% |
| PF_ETHFIUSD | 2 | -91.3% | 120.5% |
| PF_ALICEUSD | 2 | -53.6% | 195.8% |
| PF_COWUSD | 1 | -603.4% | 603.4% |
| PF_ACEUSD | 1 | -377.9% | 732.3% |
| PF_JTOUSD | 1 | +36.1% | 36.1% |
| PF_BIOUSD | 1 | +31.1% | 31.1% |

**Resolved since last scan:** PF_HFTUSD (crowded 1d, worst 137%), PF_AXSUSD (crowded 1d, worst 105%), PF_KAITOUSD (crowded 2d, worst 124%), PF_GRIFFAINUSD (crowded 1d, worst 40%), PF_MONUSD (crowded 1d, worst 91%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
