# Pond Scanner Report
**Scan time:** 2026-08-02 08:37 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LPTUSD | -209.0% | $537,574 |
| 🟢 | PF_UNIUSD | +96.8% | $784,716 |
| 🟢 | PF_KAITOUSD | +66.8% | $1,005,596 |
| 🟢 | PF_SYNUSD | -43.7% | $4,690,848 |
| 🟢 | PF_AGLDUSD | -30.0% | $4,362,824 |
| ⚪ | PF_SNXUSD | -22.7% | $3,158,014 |
| ⚪ | PF_XRPUSD | +21.6% | $11,504,206 |
| ⚪ | PF_DOTUSD | +16.2% | $1,271,264 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (kraken → gemini) — coinbase: $63,278.99, kraken: $63,275.00, gemini: $63,285.99
- ⚪ **ETH** gap **0.022%** (coinbase → gemini) — coinbase: $1,870.32, kraken: $1,870.50, gemini: $1,870.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 28% vs 60d 33%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 40% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AGLDUSD | 2 | -30.0% | 526.7% |
| PF_LPTUSD | 1 | -209.0% | 209.0% |
| PF_UNIUSD | 1 | +96.8% | 96.8% |
| PF_KAITOUSD | 1 | +66.8% | 119.5% |
| PF_SYNUSD | 1 | -43.7% | 43.7% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 57%), PF_SNXUSD (crowded 2d, worst 43%), PF_DOTUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
