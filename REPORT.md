# Pond Scanner Report
**Scan time:** 2026-09-07 21:31 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -289.3% | $1,916,578 |
| 🟢 | PF_INJUSD | +145.3% | $665,569 |
| 🟢 | PF_TRUMPUSD | -129.5% | $981,497 |
| 🟢 | PF_UNIUSD | +106.4% | $764,096 |
| 🟢 | PF_ICPUSD | +74.1% | $502,849 |
| 🟢 | PF_CFGUSD | -60.2% | $1,585,170 |
| 🟢 | PF_SUIUSD | +33.7% | $7,800,265 |
| 🟢 | PF_LINKUSD | -32.9% | $705,883 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $79,213.41, kraken: $79,218.30, gemini: $79,226.67
- ⚪ **ETH** gap **0.019%** (coinbase → gemini) — coinbase: $2,492.95, kraken: $2,492.97, gemini: $2,493.42

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.46, realized vol 10d 37% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.42, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 40% (0.5x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 54% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | -129.5% | 476.2% |
| PF_UNIUSD | 3 | +106.4% | 387.6% |
| PF_ACEUSD | 1 | -289.3% | 289.3% |
| PF_INJUSD | 1 | +145.3% | 145.3% |
| PF_ICPUSD | 1 | +74.1% | 74.1% |
| PF_CFGUSD | 1 | -60.2% | 74.8% |
| PF_SUIUSD | 1 | +33.7% | 33.7% |
| PF_LINKUSD | 1 | -32.9% | 236.7% |
| PF_APTUSD | 1 | +31.9% | 31.9% |

**Resolved since last scan:** PF_RAYUSD (crowded 2d, worst 311%), PF_ASTERUSD (crowded 1d, worst 74%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
