# Pond Scanner Report
**Scan time:** 2026-11-23 23:54 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -204.4% | $1,024,648 |
| 🟢 | PF_ACEUSD | +131.9% | $15,800,804 |
| 🟢 | PF_UNIUSD | +111.4% | $1,125,195 |
| 🟢 | PF_HYPEUSD | -58.6% | $775,022 |
| 🟢 | PF_NEARUSD | +48.5% | $2,836,198 |
| 🟢 | PF_RENDERUSD | -33.1% | $576,863 |
| ⚪ | PF_SPXUSD | -24.3% | $745,558 |
| ⚪ | PF_TRUMPUSD | -23.2% | $1,357,837 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (gemini → coinbase) — coinbase: $61,185.18, kraken: $61,181.70, gemini: $61,173.13
- ⚪ **ETH** gap **0.039%** (kraken → gemini) — coinbase: $1,708.48, kraken: $1,708.40, gemini: $1,709.07

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lista DAO (LISTA) | #450 | $40.5M | 0.81x | +22.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 52% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 76% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9953 (-0.47% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 94% vs 30d norm 54% (1.7x)
- ⚪ **ETH** 24h vol 117% vs 30d norm 68% (1.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 7 | +111.4% | 222.0% |
| PF_ACEUSD | 2 | +131.9% | 786.5% |
| PF_INJUSD | 1 | -204.4% | 204.4% |
| PF_HYPEUSD | 1 | -58.6% | 58.6% |
| PF_NEARUSD | 1 | +48.5% | 48.5% |
| PF_RENDERUSD | 1 | -33.1% | 33.1% |

**Resolved since last scan:** PF_JTOUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
