# Pond Scanner Report
**Scan time:** 2026-09-02 04:35 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +456.0% | $595,746 |
| 🟢 | PF_ACEUSD | -225.0% | $4,004,203 |
| 🟢 | PF_UNIUSD | +69.4% | $1,346,575 |
| 🟢 | PF_RENDERUSD | +60.3% | $688,246 |
| 🟢 | PF_NEARUSD | -42.3% | $1,820,384 |
| 🟢 | PF_DOTUSD | +39.3% | $2,250,695 |
| 🟢 | PF_LDOUSD | +35.9% | $917,135 |
| 🟢 | PF_POPCATUSD | +31.1% | $959,535 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (coinbase → gemini) — coinbase: $77,435.93, kraken: $77,441.80, gemini: $77,451.04
- ⚪ **ETH** gap **0.005%** (coinbase → kraken) — coinbase: $2,412.98, kraken: $2,413.11, gemini: $2,413.02

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MarsCoin (MARSCOIN) | #337 | $72.2M | 0.72x | +35.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 26% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 32% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +69.4% | 150.3% |
| PF_SOLUSD | 2 | +456.0% | 456.0% |
| PF_ACEUSD | 2 | -225.0% | 304.8% |
| PF_RENDERUSD | 2 | +60.3% | 175.0% |
| PF_NEARUSD | 2 | -42.3% | 57.5% |
| PF_DOTUSD | 1 | +39.3% | 39.3% |
| PF_LDOUSD | 1 | +35.9% | 35.9% |
| PF_POPCATUSD | 1 | +31.1% | 31.1% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 3d, worst 234%), PF_TRXUSD (crowded 2d, worst 71%), PF_FILUSD (crowded 2d, worst 51%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
