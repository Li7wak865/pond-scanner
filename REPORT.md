# Pond Scanner Report
**Scan time:** 2026-08-03 10:06 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | -844.3% | $505,399 |
| 🟢 | PF_SYNUSD | -82.6% | $3,666,638 |
| 🟢 | PF_UNIUSD | -62.2% | $834,038 |
| 🟢 | PF_ACEUSD | -39.3% | $5,527,051 |
| ⚪ | PF_KAITOUSD | +23.1% | $1,450,476 |
| ⚪ | PF_APTUSD | +22.4% | $500,434 |
| ⚪ | PF_COTIUSD | -14.5% | $15,520,661 |
| ⚪ | PF_SNXUSD | -14.1% | $617,591 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $62,687.48, kraken: $62,688.80, gemini: $62,696.51
- ⚪ **ETH** gap **0.070%** (kraken → gemini) — coinbase: $1,848.38, kraken: $1,848.26, gemini: $1,849.55

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 28% vs 60d 34%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 42% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -62.2% | 115.6% |
| PF_HYPEUSD | 1 | -844.3% | 844.3% |
| PF_SYNUSD | 1 | -82.6% | 82.6% |
| PF_ACEUSD | 1 | -39.3% | 39.3% |

**Resolved since last scan:** PF_KAITOUSD (crowded 1d, worst 142%), PF_NEARUSD (crowded 2d, worst 144%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
