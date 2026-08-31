# Pond Scanner Report
**Scan time:** 2026-08-31 22:51 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -229.5% | $962,881 |
| 🟢 | PF_LINKUSD | -182.4% | $570,440 |
| 🟢 | PF_SOLUSD | -128.2% | $756,895 |
| 🟢 | PF_UNIUSD | +88.0% | $522,385 |
| 🟢 | PF_NEARUSD | +63.2% | $788,980 |
| 🟢 | PF_ICXUSD | +46.9% | $2,148,422 |
| 🟢 | PF_HFTUSD | -42.7% | $2,095,160 |
| 🟢 | PF_STXUSD | -38.0% | $525,622 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.032%** (coinbase → kraken) — coinbase: $78,555.04, kraken: $78,580.40, gemini: $78,563.92
- ⚪ **ETH** gap **0.034%** (kraken → gemini) — coinbase: $2,468.23, kraken: $2,468.19, gemini: $2,469.03

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 0G (0G) | #447 | $50.1M | 2.62x | +39.9% |
| Ramses (RAM) | #370 | $65.6M | 0.87x | +3568.0% |
| Notcoin (NOT) | #475 | $47.2M | 0.76x | +16.2% |
| Useless Coin (USELESS) | #288 | $90.1M | 0.70x | +30.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.58, realized vol 10d 27% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.53, realized vol 10d 39% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 36% vs 30d norm 38% (1.0x)
- ⚪ **ETH** 24h vol 56% vs 30d norm 52% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 1 | -229.5% | 233.6% |
| PF_LINKUSD | 1 | -182.4% | 182.4% |
| PF_SOLUSD | 1 | -128.2% | 310.3% |
| PF_UNIUSD | 1 | +88.0% | 88.0% |
| PF_NEARUSD | 1 | +63.2% | 63.2% |
| PF_ICXUSD | 1 | +46.9% | 46.9% |
| PF_HFTUSD | 1 | -42.7% | 42.7% |
| PF_STXUSD | 1 | -38.0% | 38.0% |
| PF_MINAUSD | 1 | +35.9% | 35.9% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
