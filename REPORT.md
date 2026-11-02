# Pond Scanner Report
**Scan time:** 2026-11-02 06:06 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +115.4% | $2,298,046 |
| 🟢 | PF_TIAUSD | +38.0% | $586,552 |
| 🟢 | PF_SYNUSD | +30.4% | $1,021,562 |
| ⚪ | PF_XRPUSD | +26.2% | $4,800,026 |
| ⚪ | PF_CRVUSD | +14.3% | $2,525,671 |
| ⚪ | PF_FILUSD | +12.6% | $813,112 |
| ⚪ | PF_FETUSD | +10.5% | $5,294,187 |
| ⚪ | PF_WIFUSD | +9.7% | $2,937,590 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (coinbase → gemini) — coinbase: $78,221.34, kraken: $78,239.40, gemini: $78,245.11
- ⚪ **ETH** gap **0.006%** (coinbase → gemini) — coinbase: $2,287.78, kraken: $2,287.82, gemini: $2,287.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.30, realized vol 10d 28% vs 60d 34%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 31% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9967 (-0.33% vs peg)
- ⚪ **USDe** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 45% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 2 | +30.4% | 43.9% |
| PF_TRUMPUSD | 1 | +115.4% | 115.4% |
| PF_TIAUSD | 1 | +38.0% | 38.0% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 71%), PF_STXUSD (crowded 2d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
