# Pond Scanner Report
**Scan time:** 2026-08-04 03:38 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -63.1% | $1,357,064 |
| 🟢 | PF_KAITOUSD | +36.2% | $1,484,785 |
| ⚪ | PF_ACEUSD | -29.2% | $4,859,172 |
| ⚪ | PF_ETHFIUSD | -29.1% | $559,222 |
| ⚪ | PF_COTIUSD | -23.0% | $9,307,547 |
| ⚪ | PF_SNXUSD | -21.7% | $512,732 |
| ⚪ | PF_XCNUSD | -13.9% | $1,715,550 |
| ⚪ | PF_FILUSD | +13.2% | $739,039 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (gemini → coinbase) — coinbase: $63,770.36, kraken: $63,761.50, gemini: $63,758.18
- ⚪ **ETH** gap **0.010%** (kraken → coinbase) — coinbase: $1,863.07, kraken: $1,862.89, gemini: $1,862.94

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 28% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 41% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 36% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -63.1% | 96.9% |
| PF_KAITOUSD | 2 | +36.2% | 81.5% |

**Resolved since last scan:** PF_XRPUSD (crowded 2d, worst 37%), PF_ACEUSD (crowded 2d, worst 32%), PF_NEARUSD (crowded 2d, worst 101%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
