# Pond Scanner Report
**Scan time:** 2026-08-02 03:54 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LPTUSD | -133.9% | $545,826 |
| 🟢 | PF_KAITOUSD | +119.5% | $932,949 |
| 🟢 | PF_NEARUSD | +56.9% | $952,265 |
| 🟢 | PF_SNXUSD | -43.2% | $3,306,125 |
| 🟢 | PF_AGLDUSD | -40.2% | $4,306,092 |
| 🟢 | PF_SYNUSD | -38.5% | $5,479,882 |
| 🟢 | PF_DOTUSD | +32.9% | $1,173,868 |
| ⚪ | PF_XRPUSD | +24.2% | $10,058,207 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (kraken → gemini) — coinbase: $63,369.44, kraken: $63,367.10, gemini: $63,374.99
- ⚪ **ETH** gap **0.049%** (kraken → gemini) — coinbase: $1,874.11, kraken: $1,874.08, gemini: $1,874.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #434 | $47.5M | 1.29x | +45.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 28% vs 60d 34%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 40% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 32% (0.6x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SNXUSD | 2 | -43.2% | 43.2% |
| PF_AGLDUSD | 2 | -40.2% | 526.7% |
| PF_LPTUSD | 1 | -133.9% | 133.9% |
| PF_KAITOUSD | 1 | +119.5% | 119.5% |
| PF_NEARUSD | 1 | +56.9% | 56.9% |
| PF_SYNUSD | 1 | -38.5% | 38.5% |
| PF_DOTUSD | 1 | +32.9% | 32.9% |

**Resolved since last scan:** PF_DEXEUSD (crowded 2d, worst 524%), PF_RENDERUSD (crowded 2d, worst 57%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
