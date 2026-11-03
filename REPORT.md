# Pond Scanner Report
**Scan time:** 2026-11-03 23:24 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RUNEUSD | +51.8% | $1,056,337 |
| 🟢 | PF_NEARUSD | +41.7% | $6,434,307 |
| ⚪ | PF_XRPUSD | +29.7% | $7,057,210 |
| ⚪ | PF_CRVUSD | -18.5% | $7,065,074 |
| ⚪ | PF_TRUMPUSD | -17.9% | $748,794 |
| ⚪ | PF_ACEUSD | +16.7% | $701,058 |
| ⚪ | PF_DYDXUSD | +15.1% | $644,801 |
| ⚪ | PF_SUSHIUSD | +12.4% | $520,894 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (kraken → gemini) — coinbase: $77,832.01, kraken: $77,829.20, gemini: $77,844.43
- ⚪ **ETH** gap **0.080%** (gemini → coinbase) — coinbase: $2,288.51, kraken: $2,288.48, gemini: $2,286.68

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Holo (HOT) | #271 | $99.7M | 0.64x | +27.6% |
| MEET48 (IDOL) | #483 | $44.7M | 0.54x | +21.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.22, realized vol 10d 32% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 32% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9967 (-0.33% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 32% (0.7x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 45% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_RUNEUSD | 1 | +51.8% | 51.8% |
| PF_NEARUSD | 1 | +41.7% | 74.3% |

**Resolved since last scan:** PF_ACEUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
