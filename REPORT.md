# Pond Scanner Report
**Scan time:** 2026-11-17 07:56 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | -90.7% | $810,114 |
| 🟢 | PF_NEARUSD | +48.8% | $1,974,729 |
| 🟢 | PF_ICPUSD | -41.9% | $560,336 |
| ⚪ | PF_KAVAUSD | -27.2% | $9,670,466 |
| ⚪ | PF_FILUSD | -15.9% | $603,738 |
| ⚪ | PF_CRVUSD | -13.8% | $2,747,277 |
| ⚪ | PF_SUIUSD | -13.1% | $2,017,299 |
| ⚪ | PF_WLDUSD | -10.9% | $2,431,775 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.039%** (gemini → kraken) — coinbase: $64,652.71, kraken: $64,657.00, gemini: $64,631.77
- ⚪ **ETH** gap **0.059%** (gemini → kraken) — coinbase: $1,831.21, kraken: $1,831.22, gemini: $1,830.14

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.55, realized vol 10d 45% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 63% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9961 (-0.39% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 51% vs 30d norm 42% (1.2x)
- ⚪ **ETH** 24h vol 65% vs 30d norm 57% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 4 | -90.7% | 192.0% |
| PF_NEARUSD | 4 | +48.8% | 245.2% |
| PF_ICPUSD | 1 | -41.9% | 41.9% |

**Resolved since last scan:** PF_KAVAUSD (crowded 4d, worst 169%), PF_SPXUSD (crowded 2d, worst 77%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
