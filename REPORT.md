# Pond Scanner Report
**Scan time:** 2026-08-15 12:59 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -197.7% | $41,516,318 |
| 🟢 | PF_HFTUSD | +136.8% | $2,929,716 |
| 🟢 | PF_AXSUSD | -105.3% | $515,656 |
| 🟢 | PF_ALICEUSD | -103.7% | $4,611,370 |
| 🟢 | PF_ETHFIUSD | -95.1% | $676,662 |
| 🟢 | PF_LINKUSD | -54.5% | $937,588 |
| 🟢 | PF_KAITOUSD | -49.0% | $613,697 |
| 🟢 | PF_GRIFFAINUSD | -39.9% | $4,219,504 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (kraken → gemini) — coinbase: $62,985.93, kraken: $62,977.60, gemini: $62,995.99
- ⚪ **ETH** gap **0.050%** (kraken → gemini) — coinbase: $1,881.57, kraken: $1,881.24, gemini: $1,882.19

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Capricorn (APR) | #407 | $53.4M | 0.82x | -62.5% |
| Walrus (WAL) | #328 | $68.4M | 0.59x | +26.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.25, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 13% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 16% vs 30d norm 26% (0.6x)
- ⚪ **ETH** 24h vol 20% vs 30d norm 35% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALICEUSD | 2 | -103.7% | 195.8% |
| PF_ETHFIUSD | 2 | -95.1% | 120.5% |
| PF_LINKUSD | 2 | -54.5% | 102.8% |
| PF_KAITOUSD | 2 | -49.0% | 124.2% |
| PF_ACEUSD | 1 | -197.7% | 732.3% |
| PF_HFTUSD | 1 | +136.8% | 136.8% |
| PF_AXSUSD | 1 | -105.3% | 105.3% |
| PF_GRIFFAINUSD | 1 | -39.9% | 39.9% |
| PF_MONUSD | 1 | +36.3% | 91.3% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 142%), PF_TRUMPUSD (crowded 1d, worst 79%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
