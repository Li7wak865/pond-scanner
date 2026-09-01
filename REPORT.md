# Pond Scanner Report
**Scan time:** 2026-09-01 11:40 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +419.4% | $649,256 |
| 🟢 | PF_UNIUSD | +137.8% | $882,458 |
| 🟢 | PF_TRUMPUSD | -68.0% | $707,671 |
| 🟢 | PF_TRXUSD | -48.7% | $1,800,907 |
| 🟢 | PF_FILUSD | +35.6% | $807,975 |
| ⚪ | PF_NEARUSD | +24.0% | $1,122,156 |
| ⚪ | PF_MINAUSD | -21.1% | $974,070 |
| ⚪ | PF_ACEUSD | -18.5% | $1,308,927 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.036%** (gemini → kraken) — coinbase: $78,154.96, kraken: $78,163.30, gemini: $78,135.16
- ⚪ **ETH** gap **0.035%** (gemini → coinbase) — coinbase: $2,462.48, kraken: $2,462.00, gemini: $2,461.62

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Siacoin (SC) | #476 | $46.4M | 1.76x | +53.7% |
| Ontology Gas (ONG) | #419 | $53.8M | 0.91x | +18.2% |
| Cysic (CYS) | #334 | $73.5M | 0.77x | -47.1% |
| Ramses (RAM) | #354 | $68.3M | 0.77x | +2298.2% |
| Useless Coin (USELESS) | #259 | $104.3M | 0.76x | +52.5% |
| Prom (PROM) | #271 | $98.9M | 0.57x | -21.5% |
| MarsCoin (MARSCOIN) | #306 | $82.8M | 0.57x | +90.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.56, realized vol 10d 25% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.53, realized vol 10d 32% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 38% (0.9x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +419.4% | 893.2% |
| PF_UNIUSD | 2 | +137.8% | 137.8% |
| PF_TRUMPUSD | 2 | -68.0% | 233.6% |
| PF_TRXUSD | 1 | -48.7% | 48.7% |
| PF_FILUSD | 1 | +35.6% | 35.6% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 182%), PF_NEARUSD (crowded 2d, worst 63%), PF_STXUSD (crowded 2d, worst 45%), PF_RAREUSD (crowded 1d, worst 42%), PF_MIRAUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
