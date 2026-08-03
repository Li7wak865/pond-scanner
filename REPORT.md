# Pond Scanner Report
**Scan time:** 2026-08-03 15:17 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -101.2% | $3,243,742 |
| ⚪ | PF_SUIUSD | +27.7% | $2,377,181 |
| ⚪ | PF_DOTUSD | +26.3% | $1,223,066 |
| ⚪ | PF_FILUSD | +23.2% | $661,187 |
| ⚪ | PF_BIGTIMEUSD | +21.3% | $1,087,439 |
| ⚪ | PF_IOTAUSD | +19.8% | $688,637 |
| ⚪ | PF_SNXUSD | -17.7% | $593,396 |
| ⚪ | PF_ACEUSD | -16.5% | $5,339,293 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.045%** (coinbase → gemini) — coinbase: $63,724.80, kraken: $63,742.70, gemini: $63,753.35
- ⚪ **ETH** gap **0.108%** (kraken → gemini) — coinbase: $1,863.10, kraken: $1,863.08, gemini: $1,865.09

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 28% vs 60d 34%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 41% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 39% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -101.2% | 101.2% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 844%), PF_SYNUSD (crowded 1d, worst 83%), PF_UNIUSD (crowded 2d, worst 116%), PF_ACEUSD (crowded 1d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
