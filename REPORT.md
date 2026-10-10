# Pond Scanner Report
**Scan time:** 2026-10-10 05:54 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAIAUSD | -93.0% | $22,313,381 |
| 🟢 | PF_ZROUSD | +67.3% | $950,026 |
| 🟢 | PF_PONSUSD | +47.8% | $853,635 |
| 🟢 | PF_TIAUSD | +40.3% | $1,632,984 |
| 🟢 | PF_SUIUSD | +31.8% | $5,115,318 |
| ⚪ | PF_ASTERUSD | +25.6% | $607,639 |
| ⚪ | PF_WLDUSD | +21.1% | $1,580,743 |
| ⚪ | PF_ENAUSD | -19.3% | $20,561,021 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → gemini) — coinbase: $82,706.89, kraken: $82,706.10, gemini: $82,719.12
- ⚪ **ETH** gap **0.013%** (coinbase → gemini) — coinbase: $2,494.65, kraken: $2,494.73, gemini: $2,494.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Treasure (MAGIC) | #466 | $53.1M | 8.36x | +136.2% |
| iExec RLC (RLC) | #304 | $94.2M | 2.63x | +24.2% |
| Mina Protocol (MINA) | #259 | $119.5M | 0.61x | +20.0% |
| Talus (US) | #355 | $75.6M | 0.57x | +46.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 27% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 34% (0.7x)
- ⚪ **ETH** 24h vol 23% vs 30d norm 45% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 5 | +67.3% | 176.3% |
| PF_KAIAUSD | 2 | -93.0% | 250.9% |
| PF_PONSUSD | 2 | +47.8% | 47.8% |
| PF_TIAUSD | 2 | +40.3% | 40.3% |
| PF_SUIUSD | 2 | +31.8% | 41.5% |

**Resolved since last scan:** PF_ASTERUSD (crowded 2d, worst 70%), PF_ETHFIUSD (crowded 2d, worst 52%), PF_SAGAUSD (crowded 2d, worst 51%), PF_NEARUSD (crowded 5d, worst 418%), PF_STXUSD (crowded 2d, worst 36%), PF_XRPUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
