# Pond Scanner Report
**Scan time:** 2026-08-27 09:50 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SPXUSD | +201.0% | $1,317,196 |
| 🟢 | PF_SUSD | +138.4% | $1,873,450 |
| 🟢 | PF_ACEUSD | -78.5% | $870,304 |
| 🟢 | PF_TRUMPUSD | -75.9% | $1,130,144 |
| 🟢 | PF_NEARUSD | +75.5% | $1,753,548 |
| 🟢 | PF_MINAUSD | -55.4% | $1,121,934 |
| 🟢 | PF_HFTUSD | -55.1% | $2,759,659 |
| 🟢 | PF_DOTUSD | +35.9% | $891,899 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.072%** (coinbase → gemini) — coinbase: $80,142.19, kraken: $80,151.40, gemini: $80,200.06
- ⚪ **ETH** gap **0.087%** (kraken → gemini) — coinbase: $2,539.22, kraken: $2,539.08, gemini: $2,541.30

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #404 | $57.0M | 4.35x | +17.9% |
| Ontology (ONT) | #389 | $59.7M | 1.97x | +15.6% |
| 牛来 (Niu Lai) (牛来) | #397 | $58.1M | 0.52x | +32.9% |
| Beam (BEAM) | #259 | $106.4M | 0.51x | +46.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.67, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.62, realized vol 10d 108% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 38% (0.9x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 52% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 6 | -78.5% | 241.7% |
| PF_TRUMPUSD | 3 | -75.9% | 417.1% |
| PF_SPXUSD | 2 | +201.0% | 201.0% |
| PF_SUSD | 2 | +138.4% | 138.4% |
| PF_NEARUSD | 2 | +75.5% | 75.5% |
| PF_HFTUSD | 2 | -55.1% | 106.1% |
| PF_ONTUSD | 2 | -35.3% | 39.2% |
| PF_MINAUSD | 1 | -55.4% | 55.4% |
| PF_DOTUSD | 1 | +35.9% | 35.9% |
| PF_POPCATUSD | 1 | -30.0% | 30.0% |

**Resolved since last scan:** PF_STXUSD (crowded 2d, worst 74%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
