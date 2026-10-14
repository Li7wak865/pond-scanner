# Pond Scanner Report
**Scan time:** 2026-10-14 04:55 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -547.4% | $567,688 |
| 🟢 | PF_RENDERUSD | -134.3% | $643,334 |
| 🟢 | PF_BATUSD | -54.3% | $6,794,404 |
| 🟢 | PF_APTUSD | -49.1% | $757,138 |
| 🟢 | PF_STXUSD | +40.1% | $1,313,701 |
| 🟢 | PF_TIAUSD | +31.9% | $2,477,098 |
| ⚪ | PF_ZROUSD | +27.0% | $529,188 |
| ⚪ | PF_NEARUSD | +23.2% | $5,221,386 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → coinbase) — coinbase: $83,687.11, kraken: $83,675.90, gemini: $83,677.99
- ⚪ **ETH** gap **0.033%** (gemini → kraken) — coinbase: $2,512.58, kraken: $2,512.68, gemini: $2,511.85

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Amp (AMP) | #362 | $71.0M | 0.91x | +24.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 28% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.28, realized vol 10d 43% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 34% (0.6x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 41% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_INJUSD | 2 | -547.4% | 547.4% |
| PF_RENDERUSD | 2 | -134.3% | 134.3% |
| PF_BATUSD | 2 | -54.3% | 132.6% |
| PF_APTUSD | 2 | -49.1% | 62.2% |
| PF_STXUSD | 2 | +40.1% | 41.8% |
| PF_TIAUSD | 1 | +31.9% | 31.9% |

**Resolved since last scan:** PF_ATOMUSD (crowded 2d, worst 161%), PF_UNIUSD (crowded 2d, worst 153%), PF_NEARUSD (crowded 5d, worst 314%), PF_ZROUSD (crowded 2d, worst 133%), PF_XTZUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
