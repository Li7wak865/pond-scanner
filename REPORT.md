# Pond Scanner Report
**Scan time:** 2026-08-01 13:56 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -327.8% | $653,971 |
| 🟢 | PF_RENDERUSD | -49.0% | $883,939 |
| 🟢 | PF_SYNUSD | -48.5% | $4,983,602 |
| 🟢 | PF_UNIUSD | -42.4% | $1,365,448 |
| 🟢 | PF_EIGENUSD | +35.5% | $4,380,556 |
| 🟢 | PF_AGLDUSD | +31.5% | $3,496,073 |
| ⚪ | PF_SNXUSD | -24.9% | $2,911,649 |
| ⚪ | PF_FILUSD | +24.6% | $997,486 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.006%** (gemini → kraken) — coinbase: $63,004.34, kraken: $63,004.70, gemini: $63,000.78
- ⚪ **ETH** gap **0.010%** (coinbase → gemini) — coinbase: $1,867.30, kraken: $1,867.32, gemini: $1,867.49

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #441 | $46.8M | 0.97x | +45.2% |
| ORDI (ORDI) | #299 | $77.5M | 0.71x | +15.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 28% vs 60d 35%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 42% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 32% (0.8x)
- ⚪ **ETH** 24h vol 16% vs 30d norm 43% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -42.4% | 237.0% |
| PF_DEXEUSD | 1 | -327.8% | 327.8% |
| PF_RENDERUSD | 1 | -49.0% | 49.0% |
| PF_SYNUSD | 1 | -48.5% | 48.5% |
| PF_EIGENUSD | 1 | +35.5% | 35.5% |
| PF_AGLDUSD | 1 | +31.5% | 31.5% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
