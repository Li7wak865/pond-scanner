# Pond Scanner Report
**Scan time:** 2026-08-05 03:33 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +437.6% | $676,095 |
| 🟢 | PF_TRUMPUSD | -157.2% | $772,532 |
| 🟢 | PF_UNIUSD | -94.4% | $1,187,314 |
| 🟢 | PF_KAITOUSD | +73.3% | $769,362 |
| 🟢 | PF_ACEUSD | -52.0% | $2,133,476 |
| ⚪ | PF_ARCUSD | -24.8% | $1,176,518 |
| ⚪ | PF_SYNUSD | -22.3% | $3,920,623 |
| ⚪ | PF_ETHFIUSD | -11.9% | $1,000,350 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (kraken → coinbase) — coinbase: $64,056.44, kraken: $64,054.80, gemini: $64,055.12
- ⚪ **ETH** gap **0.028%** (kraken → coinbase) — coinbase: $1,864.76, kraken: $1,864.24, gemini: $1,864.45

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| HOME (HOME) | #456 | $43.3M | 4.42x | +29.1% |
| Cysic (CYS) | #269 | $91.5M | 1.10x | +100.0% |
| SkyAI (SKYAI) | #348 | $62.5M | 0.82x | +45.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 26% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.00, realized vol 10d 31% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 32% (0.9x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | +73.3% | 135.4% |
| PF_SOLUSD | 2 | +437.6% | 437.6% |
| PF_UNIUSD | 2 | -94.4% | 94.4% |
| PF_TRUMPUSD | 1 | -157.2% | 157.2% |
| PF_ACEUSD | 1 | -52.0% | 52.0% |

**Resolved since last scan:** PF_ZEREBROUSD (crowded 2d, worst 42%), PF_SYNUSD (crowded 2d, worst 70%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
