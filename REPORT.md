# Pond Scanner Report
**Scan time:** 2026-10-21 21:43 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +83.7% | $1,011,571 |
| 🟢 | PF_NEARUSD | +46.6% | $4,718,659 |
| 🟢 | PF_ZROUSD | +39.4% | $617,792 |
| 🟢 | PF_BATUSD | -31.1% | $3,568,514 |
| ⚪ | PF_APTUSD | -21.6% | $687,113 |
| ⚪ | PF_JUPUSD | +16.8% | $566,880 |
| ⚪ | PF_FILUSD | -16.7% | $3,044,194 |
| ⚪ | PF_TRXUSD | -13.6% | $2,685,123 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.048%** (coinbase → gemini) — coinbase: $84,740.24, kraken: $84,751.70, gemini: $84,780.70
- ⚪ **ETH** gap **0.041%** (coinbase → gemini) — coinbase: $2,496.85, kraken: $2,497.09, gemini: $2,497.87

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| IOST (IOST) | #404 | $61.9M | 4.53x | +62.5% |
| AltLayer (ALT) | #296 | $97.7M | 1.21x | +35.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 27% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 36% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 32% (0.7x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 2 | +83.7% | 93.4% |
| PF_NEARUSD | 1 | +46.6% | 116.8% |
| PF_ZROUSD | 1 | +39.4% | 39.4% |
| PF_BATUSD | 1 | -31.1% | 31.1% |

**Resolved since last scan:** PF_UNIUSD (crowded 1d, worst 141%), PF_SUSHIUSD (crowded 1d, worst 42%), PF_POLUSD (crowded 1d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
