# Pond Scanner Report
**Scan time:** 2026-09-05 20:21 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +387.6% | $893,179 |
| 🟢 | PF_TRUMPUSD | -198.0% | $1,555,253 |
| 🟢 | PF_ACEUSD | -123.7% | $699,146 |
| 🟢 | PF_ASTERUSD | +83.8% | $1,911,222 |
| 🟢 | PF_NEARUSD | +72.1% | $1,863,629 |
| 🟢 | PF_HFTUSD | -65.8% | $10,408,676 |
| 🟢 | PF_SUSHIUSD | -34.8% | $3,905,389 |
| ⚪ | PF_SAGAUSD | -26.8% | $1,983,477 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $79,774.53, kraken: $79,780.20, gemini: $79,784.51
- ⚪ **ETH** gap **0.039%** (coinbase → gemini) — coinbase: $2,477.39, kraken: $2,477.83, gemini: $2,478.36

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Sushi (SUSHI) | #332 | $75.9M | 0.97x | +37.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.53, realized vol 10d 41% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 42% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 40% (0.3x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 53% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -123.7% | 304.8% |
| PF_TRUMPUSD | 2 | -198.0% | 256.3% |
| PF_HFTUSD | 2 | -65.8% | 113.8% |
| PF_UNIUSD | 1 | +387.6% | 387.6% |
| PF_ASTERUSD | 1 | +83.8% | 83.8% |
| PF_NEARUSD | 1 | +72.1% | 72.1% |
| PF_SUSHIUSD | 1 | -34.8% | 34.8% |

**Resolved since last scan:** PF_BELUSD (crowded 1d, worst 529%), PF_COTIUSD (crowded 1d, worst 122%), PF_ICXUSD (crowded 1d, worst 54%), PF_VIRTUALUSD (crowded 1d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
