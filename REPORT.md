# Pond Scanner Report
**Scan time:** 2026-08-27 22:16 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -328.0% | $513,237 |
| 🟢 | PF_SPXUSD | +178.1% | $1,401,732 |
| 🟢 | PF_RUNEUSD | -169.6% | $823,341 |
| 🟢 | PF_ACEUSD | -107.1% | $1,089,064 |
| 🟢 | PF_TRUMPUSD | -74.3% | $1,996,283 |
| 🟢 | PF_HFTUSD | -56.4% | $7,312,952 |
| 🟢 | PF_STXUSD | -55.1% | $794,718 |
| 🟢 | PF_NEARUSD | -45.1% | $1,430,493 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.049%** (kraken → gemini) — coinbase: $80,410.40, kraken: $80,385.10, gemini: $80,424.15
- ⚪ **ETH** gap **0.004%** (kraken → coinbase) — coinbase: $2,515.55, kraken: $2,515.44, gemini: $2,515.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #388 | $61.1M | 2.43x | -44.3% |
| Beam (BEAM) | #286 | $91.5M | 1.00x | +23.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.67, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.61, realized vol 10d 109% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **USDe** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 51% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 6 | -107.1% | 241.7% |
| PF_TRUMPUSD | 3 | -74.3% | 417.1% |
| PF_SPXUSD | 2 | +178.1% | 201.0% |
| PF_HFTUSD | 2 | -56.4% | 106.1% |
| PF_NEARUSD | 2 | -45.1% | 75.4% |
| PF_MOVRUSD | 1 | -328.0% | 328.0% |
| PF_RUNEUSD | 1 | -169.6% | 169.6% |
| PF_STXUSD | 1 | -55.1% | 55.1% |

**Resolved since last scan:** PF_SUSD (crowded 2d, worst 138%), PF_MINAUSD (crowded 1d, worst 55%), PF_DOTUSD (crowded 1d, worst 36%), PF_ONTUSD (crowded 2d, worst 39%), PF_POPCATUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
