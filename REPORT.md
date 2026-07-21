# Pond Scanner Report
**Scan time:** 2026-07-21 19:52 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | -453.3% | $643,994 |
| 🟢 | PF_SOLUSD | -164.3% | $531,581 |
| 🟢 | PF_NEARUSD | -67.9% | $1,669,843 |
| 🟢 | PF_TRUMPUSD | +54.7% | $542,366 |
| 🟢 | PF_SPXUSD | +51.5% | $604,254 |
| 🟢 | PF_MOVEUSD | +47.5% | $2,439,773 |
| 🟢 | PF_JTOUSD | -35.7% | $569,108 |
| 🟢 | PF_GRIFFAINUSD | +35.1% | $726,999 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (kraken → gemini) — coinbase: $66,462.77, kraken: $66,462.40, gemini: $66,465.72
- ⚪ **ETH** gap **0.010%** (kraken → gemini) — coinbase: $1,923.42, kraken: $1,923.37, gemini: $1,923.56

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #329 | $73.2M | 2.68x | -39.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.40, realized vol 10d 34% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
