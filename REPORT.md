# Pond Scanner Report
**Scan time:** 2026-11-18 07:30 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -142.5% | $1,826,450 |
| 🟢 | PF_UNIUSD | -90.5% | $772,134 |
| 🟢 | PF_KAVAUSD | -31.7% | $5,671,012 |
| ⚪ | PF_RUNEUSD | -18.9% | $713,859 |
| ⚪ | PF_MELANIAUSD | -17.9% | $1,067,729 |
| ⚪ | PF_WLDUSD | -15.9% | $1,812,526 |
| ⚪ | PF_XRPUSD | -11.9% | $21,644,235 |
| ⚪ | PF_TRXUSD | +6.6% | $2,059,470 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.062%** (kraken → gemini) — coinbase: $64,652.63, kraken: $64,652.20, gemini: $64,692.27
- ⚪ **ETH** gap **0.151%** (kraken → gemini) — coinbase: $1,812.26, kraken: $1,811.99, gemini: $1,814.72

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #427 | $47.6M | 6.47x | +103.5% |
| Unitas (UP) | #410 | $49.2M | 0.92x | +22.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.49, realized vol 10d 46% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 60% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9957 (-0.43% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 43% (1.2x)
- ⚪ **ETH** 24h vol 66% vs 30d norm 58% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 5 | -142.5% | 245.2% |
| PF_UNIUSD | 2 | -90.5% | 90.5% |
| PF_KAVAUSD | 1 | -31.7% | 31.7% |

**Resolved since last scan:** PF_ZROUSD (crowded 5d, worst 192%), PF_TRUMPUSD (crowded 2d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
