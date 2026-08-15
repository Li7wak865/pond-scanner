# Pond Scanner Report
**Scan time:** 2026-08-15 01:49 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALICEUSD | -185.9% | $3,478,382 |
| 🟢 | PF_LINKUSD | +102.8% | $617,287 |
| 🟢 | PF_KAITOUSD | -65.7% | $862,846 |
| 🟢 | PF_ACEUSD | -58.0% | $46,756,361 |
| 🟢 | PF_ETHFIUSD | +52.2% | $584,707 |
| 🟢 | PF_UNIUSD | +37.3% | $2,323,904 |
| 🟢 | PF_NEARUSD | +36.1% | $1,903,333 |
| 🟢 | PF_ATOMUSD | +33.1% | $778,760 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → kraken) — coinbase: $62,953.83, kraken: $62,965.30, gemini: $62,964.18
- ⚪ **ETH** gap **0.020%** (coinbase → kraken) — coinbase: $1,882.23, kraken: $1,882.61, gemini: $1,882.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.25, realized vol 10d 11% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 13% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 26% (0.8x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 36% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALICEUSD | 2 | -185.9% | 195.8% |
| PF_LINKUSD | 2 | +102.8% | 102.8% |
| PF_KAITOUSD | 2 | -65.7% | 124.2% |
| PF_ETHFIUSD | 2 | +52.2% | 120.5% |
| PF_UNIUSD | 2 | +37.3% | 129.8% |
| PF_NEARUSD | 2 | +36.1% | 36.1% |
| PF_ACEUSD | 1 | -58.0% | 58.0% |
| PF_ATOMUSD | 1 | +33.1% | 33.1% |

**Resolved since last scan:** PF_HFTUSD (crowded 2d, worst 71%), PF_SAGAUSD (crowded 2d, worst 58%), PF_MONUSD (crowded 2d, worst 36%), PF_FILUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
