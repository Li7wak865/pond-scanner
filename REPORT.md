# Pond Scanner Report
**Scan time:** 2026-07-21 08:46 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -328.1% | $670,634 |
| 🟢 | PF_ALCHUSD | +120.7% | $622,400 |
| 🟢 | PF_ETHFIUSD | -96.8% | $516,873 |
| 🟢 | PF_SPXUSD | +43.1% | $546,765 |
| 🟢 | PF_SXTUSD | +32.0% | $664,278 |
| ⚪ | PF_ZKUSD | +29.8% | $1,411,548 |
| ⚪ | PF_TRUMPUSD | -27.0% | $841,522 |
| ⚪ | PF_ONDOUSD | -17.4% | $5,357,775 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (kraken → coinbase) — coinbase: $66,227.20, kraken: $66,212.50, gemini: $66,214.76
- ⚪ **ETH** gap **0.016%** (coinbase → kraken) — coinbase: $1,939.88, kraken: $1,940.20, gemini: $1,939.89

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #385 | $61.2M | 2.09x | -44.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.39, realized vol 10d 33% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.49, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
