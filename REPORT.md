# Pond Scanner Report
**Scan time:** 2026-11-02 15:56 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_APTUSD | +40.5% | $501,763 |
| 🟢 | PF_FILUSD | +36.4% | $567,350 |
| ⚪ | PF_TIAUSD | +25.0% | $844,602 |
| ⚪ | PF_ACEUSD | +23.5% | $542,743 |
| ⚪ | PF_TRUMPUSD | -21.1% | $1,922,416 |
| ⚪ | PF_FARTCOINUSD | +14.3% | $3,879,506 |
| ⚪ | PF_CRVUSD | +13.3% | $3,094,823 |
| ⚪ | PF_MELANIAUSD | +12.1% | $1,195,681 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (coinbase → kraken) — coinbase: $77,613.78, kraken: $77,615.90, gemini: $77,615.00
- ⚪ **ETH** gap **0.012%** (coinbase → kraken) — coinbase: $2,278.76, kraken: $2,279.03, gemini: $2,278.80

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.33, realized vol 10d 28% vs 60d 34%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 30% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9965 (-0.35% vs peg)
- ⚪ **USDe** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 45% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_APTUSD | 1 | +40.5% | 40.5% |
| PF_FILUSD | 1 | +36.4% | 36.4% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 115%), PF_TIAUSD (crowded 1d, worst 38%), PF_SYNUSD (crowded 2d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
