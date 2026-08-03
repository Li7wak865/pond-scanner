# Pond Scanner Report
**Scan time:** 2026-08-03 03:55 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | +141.7% | $1,131,546 |
| 🟢 | PF_UNIUSD | -109.9% | $887,792 |
| 🟢 | PF_NEARUSD | +76.4% | $2,847,442 |
| 🟢 | PF_SYNUSD | -35.8% | $3,859,646 |
| ⚪ | PF_ACEUSD | -29.5% | $2,471,675 |
| ⚪ | PF_COTIUSD | -24.1% | $15,533,542 |
| ⚪ | PF_XRPUSD | +18.5% | $20,004,904 |
| ⚪ | PF_SUIUSD | -13.3% | $2,040,815 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $62,860.98, kraken: $62,864.00, gemini: $62,868.64
- ⚪ **ETH** gap **0.033%** (kraken → gemini) — coinbase: $1,857.82, kraken: $1,857.50, gemini: $1,858.12

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 28% vs 60d 34%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 42% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -109.9% | 115.6% |
| PF_NEARUSD | 2 | +76.4% | 144.0% |
| PF_KAITOUSD | 1 | +141.7% | 141.7% |
| PF_SYNUSD | 1 | -35.8% | 35.8% |

**Resolved since last scan:** PF_AGLDUSD (crowded 3d, worst 527%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
