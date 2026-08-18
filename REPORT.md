# Pond Scanner Report
**Scan time:** 2026-08-18 13:08 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -173.9% | $18,417,379 |
| 🟢 | PF_ETHFIUSD | +135.5% | $677,954 |
| 🟢 | PF_RAREUSD | +52.8% | $2,398,406 |
| 🟢 | PF_HFTUSD | -46.2% | $4,937,962 |
| 🟢 | PF_KAITOUSD | -36.2% | $1,172,435 |
| ⚪ | PF_VIRTUALUSD | -28.0% | $637,160 |
| ⚪ | PF_APTUSD | -19.4% | $774,737 |
| ⚪ | PF_SUSHIUSD | -15.5% | $515,925 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (kraken → gemini) — coinbase: $64,123.25, kraken: $64,121.40, gemini: $64,126.75
- ⚪ **ETH** gap **0.034%** (kraken → gemini) — coinbase: $1,896.04, kraken: $1,895.63, gemini: $1,896.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RedStone (RED) | #429 | $47.4M | 0.76x | +18.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 19% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.04, realized vol 10d 19% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 26% (0.8x)
- ⚪ **ETH** 24h vol 21% vs 30d norm 35% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -173.9% | 732.3% |
| PF_ETHFIUSD | 1 | +135.5% | 135.5% |
| PF_RAREUSD | 1 | +52.8% | 52.8% |
| PF_HFTUSD | 1 | -46.2% | 46.2% |
| PF_KAITOUSD | 1 | -36.2% | 75.4% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 46%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
