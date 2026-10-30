# Pond Scanner Report
**Scan time:** 2026-10-30 22:21 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +235.7% | $1,554,415 |
| 🟢 | PF_LINKUSD | +235.0% | $1,138,392 |
| 🟢 | PF_ATOMUSD | -203.8% | $2,664,053 |
| 🟢 | PF_ZROUSD | -97.2% | $725,415 |
| 🟢 | PF_VIRTUALUSD | +69.2% | $848,569 |
| 🟢 | PF_XTZUSD | -37.1% | $1,229,670 |
| 🟢 | PF_NEARUSD | -33.9% | $5,393,604 |
| 🟢 | PF_ASTERUSD | -31.7% | $552,720 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → kraken) — coinbase: $76,563.01, kraken: $76,578.80, gemini: $76,575.23
- ⚪ **ETH** gap **0.027%** (coinbase → gemini) — coinbase: $2,230.03, kraken: $2,230.11, gemini: $2,230.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #455 | $48.6M | 1.13x | +54.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 33% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 34% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDe** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 52% vs 30d norm 33% (1.6x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 45% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -33.9% | 141.8% |
| PF_UNIUSD | 2 | +235.7% | 486.9% |
| PF_LINKUSD | 1 | +235.0% | 235.0% |
| PF_ATOMUSD | 1 | -203.8% | 550.1% |
| PF_ZROUSD | 1 | -97.2% | 393.1% |
| PF_VIRTUALUSD | 1 | +69.2% | 72.5% |
| PF_XTZUSD | 1 | -37.1% | 42.5% |
| PF_ASTERUSD | 1 | -31.7% | 52.7% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 949%), PF_INJUSD (crowded 2d, worst 684%), PF_ETHFIUSD (crowded 1d, worst 73%), PF_SUSHIUSD (crowded 2d, worst 144%), PF_FLOWUSD (crowded 1d, worst 47%), PF_JTOUSD (crowded 2d, worst 123%), PF_GRASSUSD (crowded 1d, worst 64%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
