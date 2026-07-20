# Pond Scanner Report
**Scan time:** 2026-07-20 13:10 UTC

**Flags this scan:** 110 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUUSD | -4526.6% | $12,081,434 |
| 🟢 | PF_VELOUSD | +4421.6% | $838,030 |
| 🟢 | PF_SPKUSD | -4409.9% | $166,413 |
| 🟢 | PF_DOGUSD | -4385.8% | $1,654,931 |
| 🟢 | PF_BBUSD | +4373.6% | $953,061 |
| 🟢 | PF_LRCUSD | +4158.6% | $3,455,244 |
| 🟢 | PF_BEAMUSD | +2086.6% | $2,649,100 |
| 🟢 | PF_ZEREBROUSD | -1888.2% | $3,705,911 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (coinbase → gemini) — coinbase: $64,646.99, kraken: $64,650.00, gemini: $64,650.46
- ⚪ **ETH** gap **0.069%** (kraken → gemini) — coinbase: $1,872.01, kraken: $1,871.74, gemini: $1,873.04

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.38, realized vol 10d 33% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 46% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
