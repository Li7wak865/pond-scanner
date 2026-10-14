# Pond Scanner Report
**Scan time:** 2026-10-14 17:11 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -477.6% | $511,006 |
| 🟢 | PF_INJUSD | +253.7% | $545,713 |
| 🟢 | PF_NEARUSD | +142.9% | $4,970,719 |
| 🟢 | PF_ZROUSD | -59.6% | $848,481 |
| 🟢 | PF_GRASSUSD | +41.1% | $563,064 |
| 🟢 | PF_JTOUSD | -38.6% | $1,355,512 |
| 🟢 | PF_PONSUSD | +36.1% | $3,009,286 |
| ⚪ | PF_WLDUSD | +27.9% | $3,004,785 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.046%** (kraken → gemini) — coinbase: $81,942.48, kraken: $81,928.90, gemini: $81,966.87
- ⚪ **ETH** gap **0.033%** (coinbase → gemini) — coinbase: $2,445.09, kraken: $2,445.12, gemini: $2,445.90

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #426 | $55.6M | 0.63x | -18.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 28% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 42% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 34% (0.9x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 42% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_INJUSD | 2 | +253.7% | 625.7% |
| PF_SOLUSD | 1 | -477.6% | 477.6% |
| PF_NEARUSD | 1 | +142.9% | 142.9% |
| PF_ZROUSD | 1 | -59.6% | 100.8% |
| PF_GRASSUSD | 1 | +41.1% | 41.1% |
| PF_JTOUSD | 1 | -38.6% | 38.6% |
| PF_PONSUSD | 1 | +36.1% | 36.1% |

**Resolved since last scan:** PF_BATUSD (crowded 2d, worst 133%), PF_XRPUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
