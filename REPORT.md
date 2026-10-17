# Pond Scanner Report
**Scan time:** 2026-10-17 10:46 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +135.7% | $3,894,886 |
| 🟢 | PF_TIAUSD | +70.4% | $6,084,909 |
| 🟢 | PF_ZROUSD | +38.0% | $564,169 |
| ⚪ | PF_FILUSD | +20.6% | $1,669,928 |
| ⚪ | PF_PONSUSD | +18.1% | $1,367,281 |
| ⚪ | PF_ARCUSD | +15.6% | $3,337,877 |
| ⚪ | PF_JUPUSD | -14.1% | $510,010 |
| ⚪ | PF_SUIUSD | +14.1% | $4,178,201 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (gemini → coinbase) — coinbase: $81,532.16, kraken: $81,528.00, gemini: $81,525.12
- ⚪ **ETH** gap **0.064%** (gemini → kraken) — coinbase: $2,436.14, kraken: $2,436.21, gemini: $2,434.66

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Impossible Cloud Network Token (ICNT) | #478 | $47.6M | 0.99x | +31.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 26% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.35, realized vol 10d 40% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 34% (0.8x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +38.0% | 219.7% |
| PF_NEARUSD | 1 | +135.7% | 135.7% |
| PF_TIAUSD | 1 | +70.4% | 70.4% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 109%), PF_TRUMPUSD (crowded 1d, worst 64%), PF_SUIUSD (crowded 1d, worst 42%), PF_XRPUSD (crowded 1d, worst 35%), PF_PONSUSD (crowded 2d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
