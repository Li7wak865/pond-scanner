# Pond Scanner Report
**Scan time:** 2026-10-10 12:33 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAIAUSD | -68.8% | $18,182,761 |
| 🟢 | PF_DOTUSD | +53.0% | $2,684,491 |
| 🟢 | PF_WLDUSD | +36.4% | $1,810,883 |
| ⚪ | PF_XRPUSD | +29.4% | $7,301,328 |
| ⚪ | PF_ZROUSD | -26.0% | $914,988 |
| ⚪ | PF_NEARUSD | +22.8% | $3,297,875 |
| ⚪ | PF_FILUSD | -18.8% | $1,937,619 |
| ⚪ | PF_EIGENUSD | -17.0% | $595,004 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $82,776.17, kraken: $82,779.00, gemini: $82,792.31
- ⚪ **ETH** gap **0.005%** (coinbase → kraken) — coinbase: $2,494.93, kraken: $2,495.06, gemini: $2,494.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 27% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 34% (0.5x)
- ⚪ **ETH** 24h vol 17% vs 30d norm 45% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAIAUSD | 2 | -68.8% | 250.9% |
| PF_DOTUSD | 1 | +53.0% | 53.0% |
| PF_WLDUSD | 1 | +36.4% | 36.4% |

**Resolved since last scan:** PF_ZROUSD (crowded 5d, worst 176%), PF_PONSUSD (crowded 2d, worst 48%), PF_TIAUSD (crowded 2d, worst 40%), PF_SUIUSD (crowded 2d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
