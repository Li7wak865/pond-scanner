# Pond Scanner Report
**Scan time:** 2026-09-10 16:25 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | +372.8% | $1,136,074 |
| 🟢 | PF_ATOMUSD | +122.6% | $714,056 |
| 🟢 | PF_NEARUSD | -118.3% | $2,977,705 |
| 🟢 | PF_UNIUSD | +110.0% | $1,471,945 |
| 🟢 | PF_TRUMPUSD | +79.8% | $1,867,273 |
| 🟢 | PF_SPXUSD | -71.8% | $534,637 |
| 🟢 | PF_DOTUSD | -58.4% | $1,600,522 |
| 🟢 | PF_ICXUSD | -53.6% | $960,725 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → kraken) — coinbase: $76,928.52, kraken: $76,938.80, gemini: $76,932.77
- ⚪ **ETH** gap **0.017%** (coinbase → kraken) — coinbase: $2,438.12, kraken: $2,438.54, gemini: $2,438.34

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Bifrost (BFC) | #400 | $59.0M | 2.15x | +273.5% |
| VeThor (VTHO) | #386 | $63.1M | 1.05x | +42.0% |
| A Meme Coin (AMC) | #415 | $56.2M | 0.54x | -23.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 38% vs 60d 40%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 38% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 41% (0.8x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 55% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -118.3% | 246.3% |
| PF_UNIUSD | 2 | +110.0% | 361.6% |
| PF_TRUMPUSD | 2 | +79.8% | 507.7% |
| PF_RAYUSD | 1 | +372.8% | 372.8% |
| PF_ATOMUSD | 1 | +122.6% | 122.6% |
| PF_SPXUSD | 1 | -71.8% | 124.2% |
| PF_DOTUSD | 1 | -58.4% | 58.4% |
| PF_ICXUSD | 1 | -53.6% | 53.6% |

**Resolved since last scan:** PF_BELUSD (crowded 1d, worst 497%), PF_SUSD (crowded 1d, worst 119%), PF_BLURUSD (crowded 1d, worst 74%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
