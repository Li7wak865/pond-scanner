# Pond Scanner Report
**Scan time:** 2026-10-09 13:19 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -404.2% | $18,121,642 |
| 🟢 | PF_KAIAUSD | -250.9% | $10,088,094 |
| 🟢 | PF_ZROUSD | -176.3% | $1,141,691 |
| 🟢 | PF_LINKUSD | +167.5% | $559,832 |
| 🟢 | PF_AVAXUSD | -139.1% | $553,239 |
| 🟢 | PF_RENDERUSD | -137.9% | $1,104,029 |
| 🟢 | PF_OPNUSD | -41.6% | $671,979 |
| 🟢 | PF_UNIUSD | +38.7% | $835,244 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (coinbase → gemini) — coinbase: $83,033.12, kraken: $83,036.30, gemini: $83,052.98
- ⚪ **ETH** gap **0.015%** (coinbase → kraken) — coinbase: $2,496.11, kraken: $2,496.49, gemini: $2,496.13

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #306 | $92.7M | 2.76x | +48.0% |
| Talus (US) | #297 | $96.9M | 1.37x | +135.1% |
| Amp (AMP) | #409 | $62.7M | 1.34x | +19.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 28% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 50% vs 30d norm 34% (1.5x)
- ⚪ **ETH** 24h vol 82% vs 30d norm 46% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | -404.2% | 417.9% |
| PF_ZROUSD | 4 | -176.3% | 176.3% |
| PF_LINKUSD | 2 | +167.5% | 475.0% |
| PF_AVAXUSD | 2 | -139.1% | 157.3% |
| PF_RENDERUSD | 2 | -137.9% | 203.4% |
| PF_CTSIUSD | 2 | -32.4% | 41.2% |
| PF_KAIAUSD | 1 | -250.9% | 250.9% |
| PF_OPNUSD | 1 | -41.6% | 41.6% |
| PF_UNIUSD | 1 | +38.7% | 123.6% |

**Resolved since last scan:** PF_ASTERUSD (crowded 2d, worst 56%), PF_TRUMPUSD (crowded 1d, worst 54%), PF_PONSUSD (crowded 1d, worst 54%), PF_XRPUSD (crowded 1d, worst 47%), PF_JUPUSD (crowded 1d, worst 41%), PF_WLDUSD (crowded 1d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
