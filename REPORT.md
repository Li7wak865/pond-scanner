# Pond Scanner Report
**Scan time:** 2026-07-27 19:56 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -184.4% | $542,593 |
| 🟢 | PF_SYNUSD | -69.7% | $2,860,509 |
| 🟢 | PF_LRCUSD | +48.8% | $800,154 |
| 🟢 | PF_SOONUSD | +33.5% | $702,258 |
| 🟢 | PF_NEARUSD | -33.4% | $964,659 |
| 🟢 | PF_DYMUSD | +32.5% | $1,012,404 |
| ⚪ | PF_VIRTUALUSD | -29.5% | $548,029 |
| ⚪ | PF_JUPUSD | +28.9% | $777,544 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (gemini → kraken) — coinbase: $64,904.73, kraken: $64,904.90, gemini: $64,888.00
- ⚪ **ETH** gap **0.003%** (gemini → coinbase) — coinbase: $1,948.16, kraken: $1,948.16, gemini: $1,948.10

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #477 | $47.7M | 1.36x | -24.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 23% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.29, realized vol 10d 34% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 33% (0.9x)
- ⚪ **ETH** 24h vol 48% vs 30d norm 44% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -184.4% | 248.3% |
| PF_SYNUSD | 1 | -69.7% | 69.7% |
| PF_LRCUSD | 1 | +48.8% | 48.8% |
| PF_SOONUSD | 1 | +33.5% | 33.5% |
| PF_NEARUSD | 1 | -33.4% | 33.4% |
| PF_DYMUSD | 1 | +32.5% | 32.5% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 67%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
