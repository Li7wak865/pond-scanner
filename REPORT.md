# Pond Scanner Report
**Scan time:** 2026-10-09 06:10 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +417.9% | $18,343,035 |
| 🟢 | PF_LINKUSD | +295.2% | $621,588 |
| 🟢 | PF_ZROUSD | -159.3% | $1,175,102 |
| 🟢 | PF_RENDERUSD | -125.6% | $1,045,793 |
| 🟢 | PF_UNIUSD | +123.6% | $826,372 |
| 🟢 | PF_ASTERUSD | +56.5% | $1,929,173 |
| 🟢 | PF_TRUMPUSD | -54.4% | $736,831 |
| 🟢 | PF_PONSUSD | +53.8% | $1,370,944 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (gemini → coinbase) — coinbase: $82,395.39, kraken: $82,392.50, gemini: $82,389.05
- ⚪ **ETH** gap **0.018%** (gemini → kraken) — coinbase: $2,492.84, kraken: $2,492.95, gemini: $2,492.49

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #276 | $107.4M | 1.92x | +75.2% |
| Amp (AMP) | #418 | $60.1M | 0.95x | +17.2% |
| Talus (US) | #427 | $57.7M | 0.58x | +32.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 26% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 35% (1.4x)
- ⚪ **ETH** 24h vol 82% vs 30d norm 46% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | +417.9% | 417.9% |
| PF_ZROUSD | 4 | -159.3% | 159.3% |
| PF_LINKUSD | 2 | +295.2% | 475.0% |
| PF_RENDERUSD | 2 | -125.6% | 203.4% |
| PF_ASTERUSD | 2 | +56.5% | 56.5% |
| PF_CTSIUSD | 2 | -36.0% | 41.2% |
| PF_AVAXUSD | 2 | +34.0% | 157.3% |
| PF_UNIUSD | 1 | +123.6% | 123.6% |
| PF_TRUMPUSD | 1 | -54.4% | 54.4% |
| PF_PONSUSD | 1 | +53.8% | 53.8% |
| PF_XRPUSD | 1 | +47.1% | 47.1% |
| PF_JUPUSD | 1 | -41.5% | 41.5% |
| PF_WLDUSD | 1 | +40.1% | 40.1% |

**Resolved since last scan:** PF_FILUSD (crowded 2d, worst 36%), PF_VIRTUALUSD (crowded 2d, worst 35%), PF_JTOUSD (crowded 2d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
