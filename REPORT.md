# Pond Scanner Report
**Scan time:** 2026-08-16 18:47 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -151.4% | $11,508,675 |
| 🟢 | PF_ALICEUSD | -93.9% | $1,282,824 |
| 🟢 | PF_ZEREBROUSD | +52.9% | $665,847 |
| 🟢 | PF_HFTUSD | +46.9% | $5,731,646 |
| 🟢 | PF_ETHFIUSD | -42.4% | $928,374 |
| 🟢 | PF_LINKUSD | +38.4% | $524,735 |
| ⚪ | PF_COWUSD | -22.6% | $872,552 |
| ⚪ | PF_NEARUSD | +19.2% | $1,156,358 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → kraken) — coinbase: $63,077.99, kraken: $63,090.00, gemini: $63,080.20
- ⚪ **ETH** gap **0.032%** (kraken → gemini) — coinbase: $1,884.14, kraken: $1,883.65, gemini: $1,884.26

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 13% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 7% vs 30d norm 25% (0.3x)
- ⚪ **ETH** 24h vol 10% vs 30d norm 34% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALICEUSD | 3 | -93.9% | 195.8% |
| PF_LINKUSD | 3 | +38.4% | 227.6% |
| PF_ACEUSD | 2 | -151.4% | 732.3% |
| PF_ZEREBROUSD | 1 | +52.9% | 52.9% |
| PF_HFTUSD | 1 | +46.9% | 117.4% |
| PF_ETHFIUSD | 1 | -42.4% | 42.4% |

**Resolved since last scan:** PF_COWUSD (crowded 2d, worst 603%), PF_MONUSD (crowded 1d, worst 91%), PF_KAITOUSD (crowded 1d, worst 100%), PF_BICOUSD (crowded 1d, worst 60%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
