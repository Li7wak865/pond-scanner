# Pond Scanner Report
**Scan time:** 2026-08-22 18:49 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +600.0% | $1,327,649 |
| 🟢 | PF_UNIUSD | +371.9% | $1,328,125 |
| 🟢 | PF_FETUSD | +146.4% | $14,135,861 |
| 🟢 | PF_JUPUSD | +97.3% | $976,217 |
| 🟢 | PF_NEARUSD | +84.2% | $4,656,966 |
| 🟢 | PF_ETHFIUSD | +61.4% | $1,072,979 |
| 🟢 | PF_SYNUSD | +50.9% | $832,277 |
| 🟢 | PF_PNUTUSD | +49.5% | $4,608,742 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (kraken → gemini) — coinbase: $77,208.49, kraken: $77,206.30, gemini: $77,217.96
- ⚪ **ETH** gap **0.045%** (gemini → kraken) — coinbase: $2,426.01, kraken: $2,426.13, gemini: $2,425.04

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 61% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.61, realized vol 10d 109% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 45% vs 30d norm 36% (1.2x)
- ⚪ **ETH** 24h vol 88% vs 30d norm 50% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +600.0% | 819.3% |
| PF_UNIUSD | 3 | +371.9% | 371.9% |
| PF_TRUMPUSD | 3 | +36.7% | 332.5% |
| PF_SYNUSD | 2 | +50.9% | 505.9% |
| PF_XRPUSD | 2 | +34.4% | 76.9% |
| PF_FETUSD | 1 | +146.4% | 146.4% |
| PF_JUPUSD | 1 | +97.3% | 97.3% |
| PF_NEARUSD | 1 | +84.2% | 142.8% |
| PF_ETHFIUSD | 1 | +61.4% | 92.6% |
| PF_PNUTUSD | 1 | +49.5% | 49.5% |
| PF_WUSD | 1 | +41.7% | 41.7% |
| PF_ICPUSD | 1 | -36.9% | 36.9% |
| PF_ACEUSD | 1 | -36.7% | 36.7% |
| PF_FARTCOINUSD | 1 | +33.6% | 33.6% |
| PF_GOATUSD | 1 | -32.7% | 32.7% |
| PF_MELANIAUSD | 1 | +31.3% | 31.3% |
| PF_APTUSD | 1 | +31.1% | 31.1% |

**Resolved since last scan:** PF_POPCATUSD (crowded 1d, worst 246%), PF_ZIGUSD (crowded 2d, worst 187%), PF_AVAXUSD (crowded 2d, worst 441%), PF_RIVERUSD (crowded 1d, worst 82%), PF_GRIFFAINUSD (crowded 1d, worst 57%), PF_RAREUSD (crowded 1d, worst 56%), PF_LDOUSD (crowded 2d, worst 118%), PF_ARCUSD (crowded 1d, worst 46%), PF_MOODENGUSD (crowded 1d, worst 63%), PF_EIGENUSD (crowded 1d, worst 37%), PF_ONDOUSD (crowded 1d, worst 34%), PF_COTIUSD (crowded 1d, worst 141%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
