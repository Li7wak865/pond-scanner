# Pond Scanner Report
**Scan time:** 2026-08-30 16:41 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -109.7% | $1,246,373 |
| 🟢 | PF_SAGAUSD | +67.8% | $3,333,302 |
| 🟢 | PF_BBUSD | +41.2% | $600,294 |
| ⚪ | PF_XRPUSD | +26.2% | $33,776,214 |
| ⚪ | PF_VELOUSD | -21.7% | $2,857,260 |
| ⚪ | PF_WLDUSD | -19.5% | $1,409,946 |
| ⚪ | PF_DOTUSD | +17.8% | $614,646 |
| ⚪ | PF_UNIUSD | +16.7% | $984,577 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (kraken → gemini) — coinbase: $79,196.64, kraken: $79,192.40, gemini: $79,209.44
- ⚪ **ETH** gap **0.024%** (coinbase → kraken) — coinbase: $2,531.05, kraken: $2,531.66, gemini: $2,531.19

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 49% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.60, realized vol 10d 61% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 37% (0.5x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 51% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 9 | -109.7% | 241.7% |
| PF_SAGAUSD | 1 | +67.8% | 67.8% |
| PF_BBUSD | 1 | +41.2% | 41.2% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 98%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
