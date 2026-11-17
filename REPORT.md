# Pond Scanner Report
**Scan time:** 2026-11-17 20:56 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +69.7% | $625,687 |
| 🟢 | PF_NEARUSD | -66.8% | $1,641,971 |
| 🟢 | PF_ZROUSD | -66.5% | $521,656 |
| 🟢 | PF_TRUMPUSD | -41.8% | $746,290 |
| ⚪ | PF_ASTERUSD | -17.1% | $3,088,151 |
| ⚪ | PF_KAVAUSD | -14.7% | $6,137,384 |
| ⚪ | PF_ONDOUSD | -14.0% | $2,025,807 |
| ⚪ | PF_MELANIAUSD | -13.4% | $801,467 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (gemini → kraken) — coinbase: $63,817.62, kraken: $63,817.70, gemini: $63,808.75
- ⚪ **ETH** gap **0.036%** (gemini → coinbase) — coinbase: $1,793.70, kraken: $1,793.35, gemini: $1,793.06

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.56, realized vol 10d 44% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.50, realized vol 10d 61% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9953 (-0.47% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 50% vs 30d norm 43% (1.2x)
- ⚪ **ETH** 24h vol 66% vs 30d norm 58% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | -66.8% | 245.2% |
| PF_ZROUSD | 4 | -66.5% | 192.0% |
| PF_UNIUSD | 1 | +69.7% | 69.7% |
| PF_TRUMPUSD | 1 | -41.8% | 41.8% |

**Resolved since last scan:** PF_ICPUSD (crowded 1d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
