# Pond Scanner Report
**Scan time:** 2026-10-13 14:13 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_OPNUSD | +274.0% | $609,950 |
| 🟢 | PF_INJUSD | -238.3% | $638,822 |
| 🟢 | PF_UNIUSD | -153.1% | $578,830 |
| 🟢 | PF_ZROUSD | -132.8% | $928,819 |
| 🟢 | PF_ATOMUSD | -125.0% | $694,409 |
| 🟢 | PF_RENDERUSD | -99.9% | $1,050,817 |
| 🟢 | PF_NEARUSD | -80.2% | $7,561,778 |
| 🟢 | PF_ICPUSD | -72.0% | $501,936 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → kraken) — coinbase: $83,549.70, kraken: $83,558.00, gemini: $83,550.92
- ⚪ **ETH** gap **0.052%** (coinbase → gemini) — coinbase: $2,516.08, kraken: $2,516.29, gemini: $2,517.39

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Wormhole (W) | #254 | $119.4M | 1.23x | -29.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 32% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.27, realized vol 10d 46% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 39% vs 30d norm 34% (1.1x)
- ⚪ **ETH** 24h vol 63% vs 30d norm 42% (1.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | -80.2% | 314.3% |
| PF_TIAUSD | 2 | -30.6% | 35.1% |
| PF_OPNUSD | 1 | +274.0% | 274.0% |
| PF_INJUSD | 1 | -238.3% | 238.3% |
| PF_UNIUSD | 1 | -153.1% | 153.1% |
| PF_ZROUSD | 1 | -132.8% | 132.8% |
| PF_ATOMUSD | 1 | -125.0% | 125.0% |
| PF_RENDERUSD | 1 | -99.9% | 99.9% |
| PF_ICPUSD | 1 | -72.0% | 72.0% |
| PF_APTUSD | 1 | -62.2% | 62.2% |
| PF_TRUMPUSD | 1 | -42.1% | 42.1% |
| PF_ONDOUSD | 1 | -40.4% | 40.4% |
| PF_STXUSD | 1 | -30.1% | 30.1% |

**Resolved since last scan:** PF_GRASSUSD (crowded 2d, worst 72%), PF_VIRTUALUSD (crowded 1d, worst 36%), PF_BATUSD (crowded 2d, worst 43%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
