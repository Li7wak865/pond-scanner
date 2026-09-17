# Pond Scanner Report
**Scan time:** 2026-09-17 04:54 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -848.4% | $3,748,364 |
| 🟢 | PF_UNIUSD | +187.1% | $1,397,097 |
| 🟢 | PF_NEARUSD | +109.5% | $3,494,941 |
| 🟢 | PF_TRUMPUSD | -95.6% | $742,807 |
| 🟢 | PF_SYNUSD | -75.2% | $12,250,724 |
| 🟢 | PF_ICXUSD | +48.3% | $5,058,624 |
| ⚪ | PF_XRPUSD | +29.4% | $60,208,170 |
| ⚪ | PF_ACEUSD | -28.8% | $1,342,909 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (coinbase → gemini) — coinbase: $76,377.63, kraken: $76,381.10, gemini: $76,399.80
- ⚪ **ETH** gap **0.078%** (kraken → gemini) — coinbase: $2,435.68, kraken: $2,435.21, gemini: $2,437.11

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 28% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9979 (-0.21% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 42% (0.6x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 60% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 4 | -848.4% | 896.9% |
| PF_NEARUSD | 2 | +109.5% | 109.5% |
| PF_TRUMPUSD | 2 | -95.6% | 95.6% |
| PF_SYNUSD | 2 | -75.2% | 75.2% |
| PF_ICXUSD | 2 | +48.3% | 48.3% |
| PF_UNIUSD | 1 | +187.1% | 187.1% |

**Resolved since last scan:** PF_HFTUSD (crowded 2d, worst 95%), PF_DOTUSD (crowded 2d, worst 58%), PF_ACEUSD (crowded 2d, worst 33%), PF_ETHFIUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
