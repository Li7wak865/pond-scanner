# Pond Scanner Report
**Scan time:** 2026-07-31 19:53 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AGLDUSD | +644.9% | $678,832 |
| 🟢 | PF_HYPEUSD | -447.4% | $762,127 |
| 🟢 | PF_UNIUSD | +198.2% | $2,250,253 |
| 🟢 | PF_DEXEUSD | -198.1% | $964,621 |
| 🟢 | PF_KAITOUSD | -84.8% | $650,779 |
| 🟢 | PF_APTUSD | -50.2% | $611,036 |
| 🟢 | PF_SYNUSD | +43.0% | $2,560,948 |
| 🟢 | PF_VIRTUALUSD | -30.5% | $550,144 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → kraken) — coinbase: $62,929.63, kraken: $62,936.10, gemini: $62,935.82
- ⚪ **ETH** gap **0.017%** (coinbase → gemini) — coinbase: $1,865.72, kraken: $1,866.02, gemini: $1,866.03

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Giggle Fund (GIGGLE) | #447 | $45.6M | 2.34x | +45.6% |
| Cap (CAP) | #354 | $62.8M | 0.63x | +18.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 27% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 42% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 33% (0.9x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 45% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | -84.8% | 326.1% |
| PF_UNIUSD | 2 | +198.2% | 237.0% |
| PF_AGLDUSD | 1 | +644.9% | 644.9% |
| PF_HYPEUSD | 1 | -447.4% | 605.5% |
| PF_DEXEUSD | 1 | -198.1% | 732.1% |
| PF_APTUSD | 1 | -50.2% | 57.2% |
| PF_SYNUSD | 1 | +43.0% | 49.4% |
| PF_VIRTUALUSD | 1 | -30.5% | 30.5% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 58%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
