# Pond Scanner Report
**Scan time:** 2026-11-07 05:59 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +162.9% | $3,569,100 |
| 🟢 | PF_TRUMPUSD | -52.1% | $2,631,576 |
| ⚪ | PF_SUIUSD | -21.0% | $2,156,522 |
| ⚪ | PF_CRVUSD | +18.1% | $5,354,433 |
| ⚪ | PF_DOTUSD | -16.7% | $1,177,701 |
| ⚪ | PF_XTZUSD | -15.7% | $791,777 |
| ⚪ | PF_PONSUSD | +15.6% | $1,659,886 |
| ⚪ | PF_WLDUSD | +11.1% | $2,849,389 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $75,930.55, kraken: $75,934.00, gemini: $75,944.73
- ⚪ **ETH** gap **0.012%** (coinbase → kraken) — coinbase: $2,245.82, kraken: $2,246.08, gemini: $2,246.07

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.26, realized vol 10d 50% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 68% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 35% (0.6x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 49% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | -52.1% | 178.3% |
| PF_NEARUSD | 1 | +162.9% | 162.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 4d, worst 988%), PF_FILUSD (crowded 2d, worst 58%), PF_ZROUSD (crowded 3d, worst 124%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
