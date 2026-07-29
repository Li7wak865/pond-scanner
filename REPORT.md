# Pond Scanner Report
**Scan time:** 2026-07-29 19:44 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -597.1% | $919,790 |
| 🟢 | PF_KAITOUSD | -95.4% | $738,823 |
| 🟢 | PF_UNIUSD | -92.8% | $778,057 |
| 🟢 | PF_ATOMUSD | -77.0% | $693,917 |
| 🟢 | PF_SYNUSD | +59.6% | $1,448,311 |
| 🟢 | PF_SNXUSD | -33.0% | $599,280 |
| ⚪ | PF_JUPUSD | +24.0% | $694,644 |
| ⚪ | PF_TRXUSD | -19.3% | $625,376 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (kraken → gemini) — coinbase: $63,805.79, kraken: $63,800.10, gemini: $63,809.98
- ⚪ **ETH** gap **0.025%** (gemini → kraken) — coinbase: $1,897.61, kraken: $1,897.93, gemini: $1,897.46

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #429 | $47.9M | 2.96x | +28.0% |
| Lorenzo Protocol (BANK) | #329 | $68.5M | 2.71x | -25.6% |
| pipedog (PIPEDOG) | #461 | $43.1M | 1.93x | +314.6% |
| SOON (SOON) | #331 | $68.0M | 0.53x | -26.4% |
| RE (RE) | #284 | $84.2M | 0.50x | +16.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 41% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 40% vs 30d norm 34% (1.2x)
- ⚪ **ETH** 24h vol 50% vs 30d norm 46% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 3 | +59.6% | 79.8% |
| PF_DEXEUSD | 2 | -597.1% | 755.4% |
| PF_KAITOUSD | 1 | -95.4% | 306.5% |
| PF_UNIUSD | 1 | -92.8% | 150.7% |
| PF_ATOMUSD | 1 | -77.0% | 77.0% |
| PF_SNXUSD | 1 | -33.0% | 33.0% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 878%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
