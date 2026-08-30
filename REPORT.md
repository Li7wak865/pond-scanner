# Pond Scanner Report
**Scan time:** 2026-08-30 21:07 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_VIRTUALUSD | -99.2% | $531,394 |
| 🟢 | PF_ACEUSD | -85.1% | $1,367,328 |
| 🟢 | PF_SAGAUSD | +67.7% | $3,639,943 |
| 🟢 | PF_UNIUSD | -59.0% | $1,198,683 |
| ⚪ | PF_TRUMPUSD | +29.4% | $1,357,112 |
| ⚪ | PF_WLDUSD | -23.3% | $1,956,363 |
| ⚪ | PF_VELOUSD | -22.2% | $3,747,050 |
| ⚪ | PF_FARTCOINUSD | +19.2% | $5,269,395 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (kraken → gemini) — coinbase: $78,445.19, kraken: $78,436.50, gemini: $78,449.92
- ⚪ **ETH** gap **0.013%** (gemini → coinbase) — coinbase: $2,472.60, kraken: $2,472.39, gemini: $2,472.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.58, realized vol 10d 49% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.58, realized vol 10d 59% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 37% (0.6x)
- ⚪ **ETH** 24h vol 47% vs 30d norm 51% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 9 | -85.1% | 241.7% |
| PF_VIRTUALUSD | 1 | -99.2% | 99.2% |
| PF_SAGAUSD | 1 | +67.7% | 67.8% |
| PF_UNIUSD | 1 | -59.0% | 59.0% |

**Resolved since last scan:** PF_BBUSD (crowded 1d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
