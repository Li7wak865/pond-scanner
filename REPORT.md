# Pond Scanner Report
**Scan time:** 2026-11-09 06:33 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +64.0% | $648,137 |
| 🟢 | PF_TRUMPUSD | -49.1% | $3,332,705 |
| ⚪ | PF_ASTERUSD | +26.5% | $701,987 |
| ⚪ | PF_NEARUSD | +21.8% | $3,234,748 |
| ⚪ | PF_SUIUSD | +19.7% | $4,319,743 |
| ⚪ | PF_XTZUSD | -18.2% | $1,039,870 |
| ⚪ | PF_TRXUSD | -14.1% | $1,756,921 |
| ⚪ | PF_ACEUSD | +13.6% | $2,719,319 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.040%** (coinbase → gemini) — coinbase: $74,179.19, kraken: $74,189.90, gemini: $74,209.04
- ⚪ **ETH** gap **0.042%** (gemini → coinbase) — coinbase: $2,115.30, kraken: $2,115.17, gemini: $2,114.41

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Janction (JCT) | #266 | $102.0M | 2.23x | +198.0% |
| Holo (HOT) | #301 | $80.6M | 0.63x | +30.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.38, realized vol 10d 44% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 69% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9966 (-0.34% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 46% vs 30d norm 35% (1.3x)
- ⚪ **ETH** 24h vol 87% vs 30d norm 49% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 6 | -49.1% | 178.3% |
| PF_UNIUSD | 2 | +64.0% | 202.8% |

**Resolved since last scan:** PF_NEARUSD (crowded 3d, worst 198%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
