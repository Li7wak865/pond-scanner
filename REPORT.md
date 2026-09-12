# Pond Scanner Report
**Scan time:** 2026-09-12 10:48 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +438.1% | $861,216 |
| 🟢 | PF_UNIUSD | +199.6% | $1,474,252 |
| 🟢 | PF_LSKUSD | -184.9% | $1,984,286 |
| 🟢 | PF_RIVERUSD | +56.3% | $1,167,189 |
| 🟢 | PF_RAYUSD | -53.3% | $1,137,593 |
| 🟢 | PF_ACEUSD | -52.5% | $2,810,772 |
| 🟢 | PF_NEARUSD | +41.4% | $2,732,025 |
| 🟢 | PF_MINAUSD | -34.4% | $3,289,333 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.044%** (kraken → gemini) — coinbase: $77,329.06, kraken: $77,327.60, gemini: $77,361.91
- ⚪ **ETH** gap **0.034%** (kraken → gemini) — coinbase: $2,532.47, kraken: $2,532.37, gemini: $2,533.22

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #445 | $51.2M | 2.17x | +59.9% |
| VeThor (VTHO) | #342 | $74.1M | 0.71x | +26.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 38% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 39% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 50% vs 30d norm 41% (1.2x)
- ⚪ **ETH** 24h vol 111% vs 30d norm 58% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +438.1% | 492.9% |
| PF_LSKUSD | 2 | -184.9% | 184.9% |
| PF_RAYUSD | 2 | -53.3% | 472.1% |
| PF_NEARUSD | 2 | +41.4% | 116.1% |
| PF_UNIUSD | 1 | +199.6% | 199.6% |
| PF_RIVERUSD | 1 | +56.3% | 56.3% |
| PF_ACEUSD | 1 | -52.5% | 62.9% |
| PF_MINAUSD | 1 | -34.4% | 34.4% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 2d, worst 109%), PF_HFTUSD (crowded 2d, worst 107%), PF_XRPUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
