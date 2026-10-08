# Pond Scanner Report
**Scan time:** 2026-10-08 13:31 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | -614.1% | $589,887 |
| 🟢 | PF_NEARUSD | +391.2% | $5,807,439 |
| 🟢 | PF_UNIUSD | +172.1% | $644,460 |
| 🟢 | PF_AVAXUSD | +157.3% | $506,210 |
| 🟢 | PF_ZROUSD | +71.9% | $657,686 |
| 🟢 | PF_APTUSD | +51.1% | $514,565 |
| 🟢 | PF_ETHFIUSD | -48.4% | $641,006 |
| 🟢 | PF_XRPUSD | +40.4% | $38,206,892 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (gemini → coinbase) — coinbase: $82,295.23, kraken: $82,293.90, gemini: $82,293.87
- ⚪ **ETH** gap **0.037%** (coinbase → gemini) — coinbase: $2,532.98, kraken: $2,533.11, gemini: $2,533.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| WINkLink (WIN) | #417 | $59.4M | 1.09x | +15.9% |
| Wormhole (W) | #276 | $107.9M | 0.88x | +19.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 24% vs 60d 44%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 31% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **PYUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 34% (0.7x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 44% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +172.1% | 299.0% |
| PF_NEARUSD | 3 | +391.2% | 391.2% |
| PF_ZROUSD | 3 | +71.9% | 139.5% |
| PF_RAYUSD | 2 | -614.1% | 825.8% |
| PF_APTUSD | 2 | +51.1% | 51.1% |
| PF_AVAXUSD | 1 | +157.3% | 157.3% |
| PF_ETHFIUSD | 1 | -48.4% | 48.4% |
| PF_XRPUSD | 1 | +40.4% | 40.4% |
| PF_SUIUSD | 1 | +39.3% | 39.3% |
| PF_JTOUSD | 1 | +37.9% | 37.9% |
| PF_FILUSD | 1 | +32.4% | 32.4% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 396%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
