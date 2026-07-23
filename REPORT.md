# Pond Scanner Report
**Scan time:** 2026-07-23 14:33 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -43.4% | $709,001 |
| 🟢 | PF_SUIUSD | -37.4% | $7,279,394 |
| ⚪ | PF_TRUMPUSD | -29.9% | $537,321 |
| ⚪ | PF_ACEUSD | -28.8% | $2,251,721 |
| ⚪ | PF_MIRAUSD | -28.5% | $2,814,721 |
| ⚪ | PF_SYNUSD | -28.4% | $3,869,711 |
| ⚪ | PF_ARCUSD | -21.0% | $646,687 |
| ⚪ | PF_ATHUSD | +20.2% | $2,441,380 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (gemini → coinbase) — coinbase: $65,008.85, kraken: $65,000.90, gemini: $65,000.01
- ⚪ **ETH** gap **0.022%** (coinbase → gemini) — coinbase: $1,900.19, kraken: $1,900.27, gemini: $1,900.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #254 | $106.8M | 1.62x | +40.0% |
| Zama (ZAMA) | #238 | $116.1M | 0.53x | +18.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 33% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
