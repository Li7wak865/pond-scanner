# Pond Scanner Report
**Scan time:** 2026-08-16 06:59 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_COWUSD | -372.7% | $1,331,275 |
| 🟢 | PF_ACEUSD | -207.9% | $20,890,323 |
| 🟢 | PF_LINKUSD | +103.9% | $616,413 |
| 🟢 | PF_KAITOUSD | -99.7% | $1,003,853 |
| 🟢 | PF_HFTUSD | +91.7% | $7,274,932 |
| 🟢 | PF_ALICEUSD | -39.7% | $1,264,009 |
| 🟢 | PF_GRASSUSD | -35.8% | $560,936 |
| ⚪ | PF_ETHFIUSD | -23.8% | $613,352 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $62,992.21, kraken: $62,996.70, gemini: $63,003.81
- ⚪ **ETH** gap **0.007%** (kraken → gemini) — coinbase: $1,878.65, kraken: $1,878.61, gemini: $1,878.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| CoW Protocol (COW) | #303 | $75.0M | 1.77x | +32.2% |
| Capricorn (APR) | #432 | $49.8M | 0.95x | -38.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 13% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 7% vs 30d norm 26% (0.3x)
- ⚪ **ETH** 24h vol 9% vs 30d norm 34% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +103.9% | 190.8% |
| PF_ALICEUSD | 3 | -39.7% | 195.8% |
| PF_COWUSD | 2 | -372.7% | 603.4% |
| PF_ACEUSD | 2 | -207.9% | 732.3% |
| PF_KAITOUSD | 1 | -99.7% | 99.7% |
| PF_HFTUSD | 1 | +91.7% | 117.4% |
| PF_GRASSUSD | 1 | -35.8% | 35.8% |

**Resolved since last scan:** PF_AVAXUSD (crowded 1d, worst 98%), PF_BICOUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
