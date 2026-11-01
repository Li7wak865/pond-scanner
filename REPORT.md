# Pond Scanner Report
**Scan time:** 2026-11-01 06:07 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -70.6% | $2,229,710 |
| 🟢 | PF_STXUSD | -33.7% | $2,174,733 |
| ⚪ | PF_TIAUSD | -16.1% | $576,583 |
| ⚪ | PF_FARTCOINUSD | +15.9% | $1,475,978 |
| ⚪ | PF_SUIUSD | +15.8% | $1,246,876 |
| ⚪ | PF_WLDUSD | +13.1% | $1,353,941 |
| ⚪ | PF_TRXUSD | +12.6% | $44,132,050 |
| ⚪ | PF_CRVUSD | +8.9% | $1,277,384 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → gemini) — coinbase: $77,812.33, kraken: $77,820.20, gemini: $77,833.64
- ⚪ **ETH** gap **0.026%** (kraken → gemini) — coinbase: $2,268.59, kraken: $2,268.53, gemini: $2,269.11

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 27% vs 60d 36%
- 🟡 **ETH: MIXED** — efficiency ratio 0.29, realized vol 10d 30% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **DAI** $1.0010 (+0.10% vs peg)
- ⚪ **USDe** $0.9990 (-0.10% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 10% vs 30d norm 32% (0.3x)
- ⚪ **ETH** 24h vol 14% vs 30d norm 45% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -70.6% | 70.6% |
| PF_STXUSD | 1 | -33.7% | 33.7% |

**Resolved since last scan:** PF_BATUSD (crowded 2d, worst 138%), PF_TRXUSD (crowded 2d, worst 55%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
