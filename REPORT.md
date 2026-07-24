# Pond Scanner Report
**Scan time:** 2026-07-24 19:47 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -192.1% | $2,007,048 |
| 🟢 | PF_UNIUSD | -135.5% | $1,046,965 |
| 🟢 | PF_KAITOUSD | -127.6% | $620,134 |
| 🟢 | PF_SYNUSD | -34.5% | $3,418,149 |
| ⚪ | PF_XTZUSD | -18.6% | $1,108,848 |
| ⚪ | PF_STXUSD | -13.2% | $1,231,207 |
| ⚪ | PF_FARTCOINUSD | -12.2% | $8,450,700 |
| ⚪ | PF_DYDXUSD | -8.5% | $2,828,248 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (kraken → coinbase) — coinbase: $64,175.87, kraken: $64,172.80, gemini: $64,175.35
- ⚪ **ETH** gap **0.025%** (kraken → gemini) — coinbase: $1,861.22, kraken: $1,861.01, gemini: $1,861.47

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #381 | $57.0M | 4.42x | +19.7% |
| RE (RE) | #273 | $94.0M | 1.40x | +18.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 22% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 31% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 41% (0.7x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 53% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 1 | -192.1% | 192.1% |
| PF_UNIUSD | 1 | -135.5% | 135.5% |
| PF_KAITOUSD | 1 | -127.6% | 127.6% |
| PF_SYNUSD | 1 | -34.5% | 34.5% |

**Resolved since last scan:** PF_ALCHUSD (crowded 1d, worst 128%), PF_LRCUSD (crowded 1d, worst 53%), PF_STXUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
