# Pond Scanner Report
**Scan time:** 2026-11-28 07:51 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -122.2% | $2,479,025 |
| 🟢 | PF_NEARUSD | +120.5% | $2,201,560 |
| 🟢 | PF_SOLUSD | -109.4% | $625,784 |
| 🟢 | PF_CFGUSD | -90.6% | $8,700,880 |
| 🟢 | PF_UNIUSD | -67.9% | $622,812 |
| 🟢 | PF_WLFIUSD | -37.4% | $21,154,367 |
| ⚪ | PF_DOTUSD | -20.8% | $2,726,609 |
| ⚪ | PF_RUNEUSD | +20.4% | $871,673 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (coinbase → gemini) — coinbase: $59,762.37, kraken: $59,763.50, gemini: $59,771.70
- ⚪ **ETH** gap **0.029%** (kraken → gemini) — coinbase: $1,656.88, kraken: $1,656.86, gemini: $1,657.34

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 39% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.54, realized vol 10d 56% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9950 (-0.50% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 78% vs 30d norm 58% (1.4x)
- ⚪ **ETH** 24h vol 81% vs 30d norm 70% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | -67.9% | 112.3% |
| PF_TRUMPUSD | 1 | -122.2% | 122.2% |
| PF_NEARUSD | 1 | +120.5% | 120.5% |
| PF_SOLUSD | 1 | -109.4% | 109.4% |
| PF_CFGUSD | 1 | -90.6% | 90.6% |
| PF_WLFIUSD | 1 | -37.4% | 37.4% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
