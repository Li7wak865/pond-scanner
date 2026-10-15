# Pond Scanner Report
**Scan time:** 2026-10-15 17:02 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +246.9% | $575,626 |
| 🟢 | PF_TIAUSD | -67.3% | $1,770,091 |
| 🟢 | PF_TRUMPUSD | -62.7% | $1,131,020 |
| 🟢 | PF_LINKUSD | +62.3% | $965,004 |
| 🟢 | PF_XRPUSD | +41.2% | $24,398,719 |
| 🟢 | PF_SUIUSD | +40.6% | $6,426,956 |
| 🟢 | PF_STXUSD | +33.1% | $1,288,835 |
| ⚪ | PF_JUPUSD | -25.2% | $1,894,629 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (kraken → gemini) — coinbase: $82,048.00, kraken: $82,039.00, gemini: $82,060.09
- ⚪ **ETH** gap **0.012%** (kraken → gemini) — coinbase: $2,431.69, kraken: $2,431.68, gemini: $2,431.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Zerebro (ZEREBRO) | #440 | $53.0M | 0.98x | +36.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 29% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 45% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 57% vs 30d norm 35% (1.6x)
- ⚪ **ETH** 24h vol 79% vs 30d norm 43% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | +62.3% | 403.5% |
| PF_ZROUSD | 1 | +246.9% | 246.9% |
| PF_TIAUSD | 1 | -67.3% | 67.3% |
| PF_TRUMPUSD | 1 | -62.7% | 68.6% |
| PF_XRPUSD | 1 | +41.2% | 41.2% |
| PF_SUIUSD | 1 | +40.6% | 40.6% |
| PF_STXUSD | 1 | +33.1% | 34.3% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 383%), PF_NEARUSD (crowded 1d, worst 89%), PF_FILUSD (crowded 2d, worst 50%), PF_XTZUSD (crowded 1d, worst 33%), PF_ACEUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
