# Pond Scanner Report
**Scan time:** 2026-09-15 17:00 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -674.5% | $759,396 |
| 🟢 | PF_LSKUSD | -600.4% | $2,997,338 |
| 🟢 | PF_ACEUSD | -152.6% | $2,356,495 |
| 🟢 | PF_TRUMPUSD | +123.3% | $702,720 |
| 🟢 | PF_NEARUSD | -91.9% | $2,514,835 |
| 🟢 | PF_ICPUSD | -64.7% | $505,054 |
| 🟢 | PF_HFTUSD | -55.5% | $612,165 |
| 🟢 | PF_DOTUSD | +30.5% | $1,684,131 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → gemini) — coinbase: $76,324.07, kraken: $76,327.30, gemini: $76,335.15
- ⚪ **ETH** gap **0.053%** (coinbase → gemini) — coinbase: $2,420.02, kraken: $2,420.09, gemini: $2,421.30

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.13, realized vol 10d 25% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.10, realized vol 10d 36% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 42% (0.7x)
- ⚪ **ETH** 24h vol 56% vs 30d norm 60% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -600.4% | 896.9% |
| PF_SOLUSD | 1 | -674.5% | 674.5% |
| PF_ACEUSD | 1 | -152.6% | 175.3% |
| PF_TRUMPUSD | 1 | +123.3% | 125.4% |
| PF_NEARUSD | 1 | -91.9% | 91.9% |
| PF_ICPUSD | 1 | -64.7% | 64.7% |
| PF_HFTUSD | 1 | -55.5% | 55.5% |
| PF_DOTUSD | 1 | +30.5% | 30.5% |

**Resolved since last scan:** PF_INITUSD (crowded 1d, worst 302%), PF_POWRUSD (crowded 1d, worst 116%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
