# Pond Scanner Report
**Scan time:** 2026-10-07 13:26 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +395.8% | $500,972 |
| 🟢 | PF_AVAXUSD | +288.5% | $877,437 |
| 🟢 | PF_UNIUSD | +285.6% | $869,085 |
| 🟢 | PF_NEARUSD | +142.5% | $3,494,995 |
| 🟢 | PF_RENDERUSD | -121.5% | $1,234,679 |
| 🟢 | PF_ZROUSD | -99.2% | $1,708,512 |
| 🟢 | PF_TRUMPUSD | +90.6% | $1,504,302 |
| 🟢 | PF_ETHFIUSD | -77.0% | $1,319,612 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $83,236.58, kraken: $83,237.50, gemini: $83,252.67
- ⚪ **ETH** gap **0.029%** (coinbase → gemini) — coinbase: $2,558.60, kraken: $2,558.80, gemini: $2,559.33

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #403 | $63.4M | 1.26x | -17.3% |
| Cap (CAP) | #267 | $112.2M | 1.12x | -26.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 24% vs 60d 43%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.15, realized vol 10d 33% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 44% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +285.6% | 299.0% |
| PF_AVAXUSD | 2 | +288.5% | 288.5% |
| PF_NEARUSD | 2 | +142.5% | 178.3% |
| PF_ZROUSD | 2 | -99.2% | 99.2% |
| PF_SUIUSD | 2 | +37.4% | 44.5% |
| PF_LINKUSD | 1 | +395.8% | 395.8% |
| PF_RENDERUSD | 1 | -121.5% | 137.6% |
| PF_TRUMPUSD | 1 | +90.6% | 141.5% |
| PF_ETHFIUSD | 1 | -77.0% | 77.0% |
| PF_XRPUSD | 1 | +44.1% | 44.1% |
| PF_GRASSUSD | 1 | +43.6% | 43.6% |
| PF_SPXUSD | 1 | +39.5% | 39.5% |

**Resolved since last scan:** PF_BATUSD (crowded 1d, worst 141%), PF_DOTUSD (crowded 2d, worst 61%), PF_PONSUSD (crowded 5d, worst 111%), PF_ASTERUSD (crowded 2d, worst 37%), PF_FILUSD (crowded 2d, worst 60%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
