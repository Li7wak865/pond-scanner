# Pond Scanner Report
**Scan time:** 2026-10-16 11:26 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +217.1% | $547,383 |
| 🟢 | PF_NEARUSD | +153.4% | $4,328,943 |
| 🟢 | PF_TIAUSD | +82.4% | $5,051,943 |
| 🟢 | PF_LINKUSD | +64.1% | $535,442 |
| 🟢 | PF_GRASSUSD | +51.2% | $642,329 |
| 🟢 | PF_STXUSD | -49.1% | $851,725 |
| 🟢 | PF_XRPUSD | +48.2% | $19,345,431 |
| ⚪ | PF_INJUSD | -29.8% | $563,955 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.038%** (coinbase → kraken) — coinbase: $82,738.49, kraken: $82,769.90, gemini: $82,764.77
- ⚪ **ETH** gap **0.026%** (coinbase → gemini) — coinbase: $2,483.99, kraken: $2,484.00, gemini: $2,484.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 30% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.28, realized vol 10d 48% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 34% (1.4x)
- ⚪ **ETH** 24h vol 63% vs 30d norm 42% (1.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +64.1% | 403.5% |
| PF_NEARUSD | 2 | +153.4% | 178.9% |
| PF_ZROUSD | 1 | +217.1% | 217.1% |
| PF_TIAUSD | 1 | +82.4% | 82.4% |
| PF_GRASSUSD | 1 | +51.2% | 51.2% |
| PF_STXUSD | 1 | -49.1% | 49.1% |
| PF_XRPUSD | 1 | +48.2% | 48.2% |

**Resolved since last scan:** PF_INJUSD (crowded 1d, worst 402%), PF_BATUSD (crowded 2d, worst 45%), PF_FILUSD (crowded 1d, worst 37%), PF_WLDUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
