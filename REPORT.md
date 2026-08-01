# Pond Scanner Report
**Scan time:** 2026-08-01 19:35 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AGLDUSD | +526.7% | $3,763,925 |
| 🟢 | PF_DEXEUSD | -523.7% | $519,361 |
| 🟢 | PF_RENDERUSD | +56.6% | $820,717 |
| 🟢 | PF_SNXUSD | -36.5% | $3,217,981 |
| ⚪ | PF_EIGENUSD | +29.5% | $4,756,729 |
| ⚪ | PF_GRASSUSD | -27.9% | $1,035,471 |
| ⚪ | PF_NEARUSD | -27.6% | $1,041,215 |
| ⚪ | PF_SYNUSD | -20.3% | $5,454,897 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → kraken) — coinbase: $62,448.85, kraken: $62,456.20, gemini: $62,454.50
- ⚪ **ETH** gap **0.036%** (kraken → gemini) — coinbase: $1,836.12, kraken: $1,835.84, gemini: $1,836.50

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #440 | $46.5M | 1.29x | +48.5% |
| COTI (COTI) | #451 | $44.3M | 0.98x | -16.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 28% vs 60d 35%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 42% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 32% (0.4x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AGLDUSD | 1 | +526.7% | 526.7% |
| PF_DEXEUSD | 1 | -523.7% | 523.7% |
| PF_RENDERUSD | 1 | +56.6% | 56.6% |
| PF_SNXUSD | 1 | -36.5% | 36.5% |

**Resolved since last scan:** PF_SYNUSD (crowded 1d, worst 49%), PF_UNIUSD (crowded 3d, worst 237%), PF_EIGENUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
