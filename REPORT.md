# Pond Scanner Report
**Scan time:** 2026-11-08 06:03 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -111.6% | $1,351,709 |
| 🟢 | PF_NEARUSD | -76.0% | $2,006,834 |
| ⚪ | PF_XRPUSD | +17.9% | $7,195,888 |
| ⚪ | PF_WLDUSD | -16.1% | $3,057,024 |
| ⚪ | PF_CRVUSD | +10.9% | $2,768,477 |
| ⚪ | PF_SUIUSD | -9.2% | $2,416,057 |
| ⚪ | PF_FARTCOINUSD | -9.1% | $1,822,881 |
| ⚪ | PF_XLMUSD | +8.3% | $6,061,099 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $75,695.07, kraken: $75,704.10, gemini: $75,704.98
- ⚪ **ETH** gap **0.013%** (kraken → coinbase) — coinbase: $2,231.15, kraken: $2,230.86, gemini: $2,230.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #333 | $71.5M | 0.73x | +36.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.27, realized vol 10d 44% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 63% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9967 (-0.33% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 47% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -111.6% | 178.3% |
| PF_NEARUSD | 2 | -76.0% | 98.3% |

**Resolved since last scan:** PF_SUIUSD (crowded 2d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
