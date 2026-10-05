# Pond Scanner Report
**Scan time:** 2026-10-05 14:42 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -236.6% | $533,056 |
| 🟢 | PF_RUNEUSD | +98.6% | $1,259,139 |
| 🟢 | PF_GRASSUSD | +84.4% | $508,513 |
| 🟢 | PF_ACEUSD | +83.7% | $681,299 |
| 🟢 | PF_PONSUSD | +68.1% | $960,427 |
| 🟢 | PF_UNIUSD | -59.1% | $545,512 |
| 🟢 | PF_VIRTUALUSD | +38.7% | $945,604 |
| 🟢 | PF_DOTUSD | +33.0% | $1,513,030 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.054%** (kraken → gemini) — coinbase: $85,758.87, kraken: $85,752.00, gemini: $85,798.56
- ⚪ **ETH** gap **0.047%** (coinbase → gemini) — coinbase: $2,704.80, kraken: $2,705.05, gemini: $2,706.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 18% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 15% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 33% vs 30d norm 33% (1.0x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 3 | +68.1% | 111.2% |
| PF_MOVRUSD | 1 | -236.6% | 236.6% |
| PF_RUNEUSD | 1 | +98.6% | 98.6% |
| PF_GRASSUSD | 1 | +84.4% | 84.4% |
| PF_ACEUSD | 1 | +83.7% | 83.7% |
| PF_UNIUSD | 1 | -59.1% | 59.1% |
| PF_VIRTUALUSD | 1 | +38.7% | 38.7% |
| PF_DOTUSD | 1 | +33.0% | 33.0% |
| PF_ZROUSD | 1 | +31.0% | 33.7% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 2d, worst 99%), PF_NEARUSD (crowded 2d, worst 256%), PF_TRXUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
