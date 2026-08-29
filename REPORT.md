# Pond Scanner Report
**Scan time:** 2026-08-29 16:44 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | +214.7% | $1,116,894 |
| 🟢 | PF_SPXUSD | -73.9% | $509,908 |
| 🟢 | PF_STXUSD | -52.9% | $784,411 |
| 🟢 | PF_ACEUSD | -45.8% | $1,356,150 |
| 🟢 | PF_FETUSD | +34.6% | $10,642,925 |
| ⚪ | PF_TRUMPUSD | -29.0% | $2,632,846 |
| ⚪ | PF_HFTUSD | -26.9% | $4,355,735 |
| ⚪ | PF_DOTUSD | +19.8% | $789,331 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → kraken) — coinbase: $78,003.96, kraken: $78,016.00, gemini: $78,009.20
- ⚪ **ETH** gap **0.020%** (coinbase → gemini) — coinbase: $2,449.82, kraken: $2,450.23, gemini: $2,450.31

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Helium (HNT) | #373 | $64.1M | 0.93x | +61.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 56% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.52, realized vol 10d 61% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **USDe** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 38% (0.5x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 51% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 8 | -45.8% | 241.7% |
| PF_STXUSD | 2 | -52.9% | 60.2% |
| PF_DEXEUSD | 1 | +214.7% | 214.7% |
| PF_SPXUSD | 1 | -73.9% | 73.9% |
| PF_FETUSD | 1 | +34.6% | 34.6% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 547%), PF_TRUMPUSD (crowded 1d, worst 232%), PF_NEARUSD (crowded 1d, worst 113%), PF_HFTUSD (crowded 1d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
