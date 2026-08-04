# Pond Scanner Report
**Scan time:** 2026-08-04 09:08 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | +135.4% | $1,282,954 |
| 🟢 | PF_SYNUSD | -69.5% | $1,662,783 |
| 🟢 | PF_COTIUSD | -62.8% | $14,673,608 |
| 🟢 | PF_ZEREBROUSD | -48.2% | $3,665,971 |
| 🟢 | PF_NEARUSD | -43.4% | $1,575,524 |
| 🟢 | PF_ATOMUSD | -37.7% | $581,322 |
| 🟢 | PF_ONDOUSD | -36.0% | $4,065,121 |
| ⚪ | PF_JTOUSD | -17.7% | $837,507 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → gemini) — coinbase: $63,497.64, kraken: $63,493.40, gemini: $63,501.75
- ⚪ **ETH** gap **0.067%** (kraken → gemini) — coinbase: $1,854.79, kraken: $1,854.78, gemini: $1,856.03

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SkyAI (SKYAI) | #441 | $45.4M | 0.50x | +37.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 27% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.11, realized vol 10d 41% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 36% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | +135.4% | 135.4% |
| PF_SYNUSD | 1 | -69.5% | 69.5% |
| PF_COTIUSD | 1 | -62.8% | 62.8% |
| PF_ZEREBROUSD | 1 | -48.2% | 48.2% |
| PF_NEARUSD | 1 | -43.4% | 43.4% |
| PF_ATOMUSD | 1 | -37.7% | 37.7% |
| PF_ONDOUSD | 1 | -36.0% | 36.0% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 97%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
