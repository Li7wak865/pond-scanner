# Pond Scanner Report
**Scan time:** 2026-09-17 17:00 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +137.4% | $5,077,064 |
| 🟢 | PF_ETHFIUSD | +109.4% | $655,336 |
| 🟢 | PF_NATGASUSD | +71.9% | $607,631 |
| 🟢 | PF_SYNUSD | -66.7% | $7,188,902 |
| 🟢 | PF_UNIUSD | +50.6% | $1,767,040 |
| 🟢 | PF_SUIUSD | +48.8% | $7,711,706 |
| 🟢 | PF_DOTUSD | -38.7% | $1,956,669 |
| 🟢 | PF_ASTERUSD | -31.4% | $699,922 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $76,693.28, kraken: $76,696.70, gemini: $76,707.23
- ⚪ **ETH** gap **0.025%** (gemini → kraken) — coinbase: $2,468.47, kraken: $2,468.53, gemini: $2,467.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #257 | $108.9M | 1.15x | -43.3% |
| MarsCoin (MARSCOIN) | #252 | $112.7M | 0.64x | +22.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 28% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 41% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9978 (-0.22% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **PYUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 42% (0.6x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 60% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +137.4% | 137.4% |
| PF_SYNUSD | 2 | -66.7% | 85.8% |
| PF_ETHFIUSD | 1 | +109.4% | 109.4% |
| PF_NATGASUSD | 1 | +71.9% | 100.5% |
| PF_UNIUSD | 1 | +50.6% | 311.9% |
| PF_SUIUSD | 1 | +48.8% | 48.8% |
| PF_DOTUSD | 1 | -38.7% | 38.7% |
| PF_ASTERUSD | 1 | -31.4% | 31.4% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 2d, worst 96%), PF_SWARMSUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
