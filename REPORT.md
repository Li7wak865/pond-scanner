# Pond Scanner Report
**Scan time:** 2026-11-16 06:31 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +836.9% | $1,130,336 |
| 🟢 | PF_KAVAUSD | -156.9% | $13,605,961 |
| 🟢 | PF_ZROUSD | -117.6% | $595,622 |
| 🟢 | PF_NEARUSD | -88.6% | $1,457,261 |
| 🟢 | PF_TRUMPUSD | -39.3% | $574,327 |
| ⚪ | PF_FILUSD | -25.7% | $604,260 |
| ⚪ | PF_TRXUSD | -23.3% | $2,652,412 |
| ⚪ | PF_SUIUSD | -17.9% | $2,491,977 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (kraken → gemini) — coinbase: $64,449.71, kraken: $64,446.00, gemini: $64,452.22
- ⚪ **ETH** gap **0.019%** (coinbase → gemini) — coinbase: $1,809.72, kraken: $1,809.85, gemini: $1,810.07

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.53, realized vol 10d 45% vs 60d 42%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 62% vs 60d 52%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9957 (-0.43% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 55% vs 30d norm 41% (1.3x)
- ⚪ **ETH** 24h vol 61% vs 30d norm 56% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAVAUSD | 3 | -156.9% | 169.0% |
| PF_ZROUSD | 3 | -117.6% | 192.0% |
| PF_NEARUSD | 3 | -88.6% | 245.2% |
| PF_TRUMPUSD | 3 | -39.3% | 112.0% |
| PF_SOLUSD | 2 | +836.9% | 836.9% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 716%), PF_INJUSD (crowded 4d, worst 747%), PF_UNIUSD (crowded 2d, worst 138%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
