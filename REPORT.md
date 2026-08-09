# Pond Scanner Report
**Scan time:** 2026-08-09 19:01 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -61.8% | $5,858,836 |
| 🟢 | PF_UNIUSD | +41.9% | $532,851 |
| 🟢 | PF_NEARUSD | +32.9% | $818,385 |
| ⚪ | PF_SYNUSD | -26.7% | $943,648 |
| ⚪ | PF_PNUTUSD | -19.6% | $1,023,570 |
| ⚪ | PF_COTIUSD | -14.8% | $16,780,825 |
| ⚪ | PF_HFTUSD | +14.5% | $3,823,784 |
| ⚪ | PF_XRPUSD | +14.2% | $8,160,441 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (kraken → gemini) — coinbase: $65,149.79, kraken: $65,139.30, gemini: $65,153.48
- ⚪ **ETH** gap **0.023%** (kraken → gemini) — coinbase: $1,920.27, kraken: $1,919.85, gemini: $1,920.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #607 | $44.5M | 5.82x | -22.2% |
| BOOK OF MEME (BOME) | #408 | $53.0M | 1.06x | +23.6% |
| ConstitutionDAO (PEOPLE) | #438 | $47.7M | 0.61x | +26.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 27% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 10% vs 30d norm 28% (0.4x)
- ⚪ **ETH** 24h vol 12% vs 30d norm 40% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -61.8% | 501.6% |
| PF_UNIUSD | 1 | +41.9% | 41.9% |
| PF_NEARUSD | 1 | +32.9% | 37.8% |

**Resolved since last scan:** PF_CATIUSD (crowded 1d, worst 103%), PF_SYNUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
