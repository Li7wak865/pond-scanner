# Pond Scanner Report
**Scan time:** 2026-10-27 05:07 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +60.9% | $2,126,175 |
| 🟢 | PF_APTUSD | -57.9% | $790,275 |
| 🟢 | PF_SYNUSD | +52.1% | $2,566,753 |
| 🟢 | PF_TIAUSD | +39.5% | $1,204,259 |
| ⚪ | PF_TRXUSD | -16.5% | $1,788,468 |
| ⚪ | PF_SUIUSD | -14.8% | $3,422,030 |
| ⚪ | PF_JUPUSD | -14.4% | $643,942 |
| ⚪ | PF_ARCUSD | +13.9% | $4,871,522 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $79,698.97, kraken: $79,705.30, gemini: $79,708.42
- ⚪ **ETH** gap **0.011%** (coinbase → gemini) — coinbase: $2,312.64, kraken: $2,312.80, gemini: $2,312.89

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 24% vs 60d 34%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9966 (-0.34% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9988 (-0.12% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 31% (0.9x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +60.9% | 129.3% |
| PF_SYNUSD | 2 | +52.1% | 52.1% |
| PF_APTUSD | 1 | -57.9% | 57.9% |
| PF_TIAUSD | 1 | +39.5% | 39.5% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 2d, worst 64%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
