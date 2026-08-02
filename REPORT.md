# Pond Scanner Report
**Scan time:** 2026-08-02 19:35 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -144.0% | $2,061,124 |
| 🟢 | PF_UNIUSD | +35.6% | $709,172 |
| 🟢 | PF_AGLDUSD | +30.4% | $899,967 |
| ⚪ | PF_ACEUSD | -25.3% | $2,412,933 |
| ⚪ | PF_COTIUSD | -24.0% | $15,472,404 |
| ⚪ | PF_FILUSD | +22.5% | $689,112 |
| ⚪ | PF_EIGENUSD | -17.9% | $1,167,429 |
| ⚪ | PF_PORTALUSD | +17.5% | $3,059,680 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (coinbase → gemini) — coinbase: $63,267.99, kraken: $63,277.00, gemini: $63,286.66
- ⚪ **ETH** gap **0.005%** (gemini → kraken) — coinbase: $1,874.90, kraken: $1,874.99, gemini: $1,874.89

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 28% vs 60d 33%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 41% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AGLDUSD | 2 | +30.4% | 526.7% |
| PF_NEARUSD | 1 | -144.0% | 144.0% |
| PF_UNIUSD | 1 | +35.6% | 115.6% |

**Resolved since last scan:** PF_KAITOUSD (crowded 1d, worst 149%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
