# Pond Scanner Report
**Scan time:** 2026-07-23 08:45 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | -68.4% | $2,304,820 |
| 🟢 | PF_VIRTUALUSD | -66.2% | $731,720 |
| 🟢 | PF_NEARUSD | -45.2% | $778,255 |
| 🟢 | PF_MIRAUSD | -43.1% | $2,767,241 |
| 🟢 | PF_ACEUSD | -35.2% | $2,390,643 |
| ⚪ | PF_EIGENUSD | -28.4% | $723,007 |
| ⚪ | PF_SUIUSD | -26.2% | $7,204,009 |
| ⚪ | PF_UNIUSD | -24.8% | $896,033 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (kraken → gemini) — coinbase: $65,592.28, kraken: $65,590.50, gemini: $65,596.38
- ⚪ **ETH** gap **0.097%** (gemini → coinbase) — coinbase: $1,924.88, kraken: $1,924.40, gemini: $1,923.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #255 | $108.8M | 1.96x | +77.3% |
| Zama (ZAMA) | #252 | $109.0M | 0.51x | +22.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 31% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.32, realized vol 10d 44% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
