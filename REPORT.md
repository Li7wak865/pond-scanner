# Pond Scanner Report
**Scan time:** 2026-09-13 20:51 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_POWRUSD | -175.7% | $8,961,780 |
| 🟢 | PF_UNIUSD | -164.0% | $623,949 |
| 🟢 | PF_STEEMUSD | -87.0% | $3,729,047 |
| 🟢 | PF_CATIUSD | +85.9% | $2,472,952 |
| 🟢 | PF_ACEUSD | -45.2% | $788,383 |
| 🟢 | PF_FILUSD | +34.8% | $2,054,313 |
| ⚪ | PF_NEARUSD | -25.8% | $1,170,974 |
| ⚪ | PF_HFTUSD | +21.9% | $1,690,641 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → gemini) — coinbase: $77,303.74, kraken: $77,301.50, gemini: $77,314.16
- ⚪ **ETH** gap **0.056%** (kraken → gemini) — coinbase: $2,512.98, kraken: $2,512.79, gemini: $2,514.20

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Teller (DEBIT) | #375 | $65.8M | 2.07x | +93.2% |
| VeThor (VTHO) | #306 | $83.9M | 1.29x | +22.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 20% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 28% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 41% (0.4x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 58% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_POWRUSD | 1 | -175.7% | 195.0% |
| PF_UNIUSD | 1 | -164.0% | 247.8% |
| PF_STEEMUSD | 1 | -87.0% | 93.4% |
| PF_CATIUSD | 1 | +85.9% | 85.9% |
| PF_ACEUSD | 1 | -45.2% | 59.5% |
| PF_FILUSD | 1 | +34.8% | 80.8% |

**Resolved since last scan:** PF_ALCHUSD (crowded 1d, worst 154%), PF_DYMUSD (crowded 1d, worst 65%), PF_DOTUSD (crowded 1d, worst 50%), PF_RIVERUSD (crowded 1d, worst 103%), PF_ICXUSD (crowded 1d, worst 36%), PF_VIRTUALUSD (crowded 1d, worst 53%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
