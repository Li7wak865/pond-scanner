# Pond Scanner Report
**Scan time:** 2026-10-07 23:06 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | -825.8% | $701,267 |
| 🟢 | PF_AVAXUSD | -226.5% | $851,479 |
| 🟢 | PF_NEARUSD | -134.3% | $4,156,108 |
| 🟢 | PF_UNIUSD | -104.1% | $956,144 |
| 🟢 | PF_LINKUSD | +74.9% | $580,626 |
| 🟢 | PF_SPXUSD | +46.9% | $822,061 |
| 🟢 | PF_RENDERUSD | -45.5% | $1,083,240 |
| 🟢 | PF_ZROUSD | +43.1% | $1,324,137 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.035%** (coinbase → gemini) — coinbase: $83,164.09, kraken: $83,173.10, gemini: $83,193.45
- ⚪ **ETH** gap **0.023%** (kraken → gemini) — coinbase: $2,567.92, kraken: $2,567.83, gemini: $2,568.41

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mina Protocol (MINA) | #258 | $118.3M | 0.64x | -20.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 25% vs 60d 43%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.17, realized vol 10d 31% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9980 (-0.20% vs peg)
- ⚪ **PYUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 33% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 47% vs 30d norm 44% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -104.1% | 299.0% |
| PF_AVAXUSD | 2 | -226.5% | 288.5% |
| PF_NEARUSD | 2 | -134.3% | 178.3% |
| PF_ZROUSD | 2 | +43.1% | 99.2% |
| PF_RAYUSD | 1 | -825.8% | 825.8% |
| PF_LINKUSD | 1 | +74.9% | 395.8% |
| PF_SPXUSD | 1 | +46.9% | 46.9% |
| PF_RENDERUSD | 1 | -45.5% | 137.6% |
| PF_APTUSD | 1 | +36.6% | 36.6% |
| PF_ASTERUSD | 1 | +31.4% | 31.4% |
| PF_JTOUSD | 1 | -30.1% | 30.1% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 141%), PF_ETHFIUSD (crowded 1d, worst 77%), PF_XRPUSD (crowded 1d, worst 44%), PF_GRASSUSD (crowded 1d, worst 44%), PF_SUIUSD (crowded 2d, worst 45%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
