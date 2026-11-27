# Pond Scanner Report
**Scan time:** 2026-11-27 08:36 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -148.3% | $1,097,221 |
| 🟢 | PF_NEARUSD | +46.7% | $2,242,951 |
| 🟢 | PF_UNIUSD | +34.1% | $662,791 |
| ⚪ | PF_PONSUSD | +11.6% | $3,823,071 |
| ⚪ | PF_TIAUSD | +11.6% | $1,713,992 |
| ⚪ | PF_WLDUSD | -10.9% | $6,737,443 |
| ⚪ | PF_CRVUSD | +10.4% | $14,888,195 |
| ⚪ | PF_XRPUSD | -10.2% | $12,679,208 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $61,718.89, kraken: $61,719.80, gemini: $61,726.19
- ⚪ **ETH** gap **0.008%** (kraken → coinbase) — coinbase: $1,728.88, kraken: $1,728.75, gemini: $1,728.80

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #491 | $36.3M | 2.23x | -25.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 44% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.52, realized vol 10d 59% vs 60d 52%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9953 (-0.47% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 56% (0.5x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 69% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -148.3% | 248.7% |
| PF_UNIUSD | 3 | +34.1% | 112.3% |
| PF_NEARUSD | 2 | +46.7% | 48.4% |

**Resolved since last scan:** PF_RUNEUSD (crowded 2d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
