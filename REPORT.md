# Pond Scanner Report
**Scan time:** 2026-09-12 04:36 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +492.9% | $864,625 |
| 🟢 | PF_RAYUSD | -472.1% | $1,402,299 |
| 🟢 | PF_LSKUSD | -156.9% | $1,320,491 |
| 🟢 | PF_UNIUSD | -108.0% | $1,450,100 |
| 🟢 | PF_TRUMPUSD | -89.6% | $886,322 |
| 🟢 | PF_NEARUSD | -71.0% | $3,027,319 |
| 🟢 | PF_ACEUSD | -62.9% | $2,775,377 |
| 🟢 | PF_HFTUSD | -33.6% | $672,491 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $77,268.78, kraken: $77,271.60, gemini: $77,282.63
- ⚪ **ETH** gap **0.005%** (kraken → coinbase) — coinbase: $2,513.34, kraken: $2,513.21, gemini: $2,513.22

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #460 | $48.8M | 1.67x | +67.3% |
| LAB (LAB) | #410 | $57.3M | 1.24x | +59.0% |
| VeThor (VTHO) | #403 | $61.0M | 0.56x | +15.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 38% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 39% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 51% vs 30d norm 41% (1.2x)
- ⚪ **ETH** 24h vol 112% vs 30d norm 58% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +492.9% | 492.9% |
| PF_RAYUSD | 2 | -472.1% | 472.1% |
| PF_LSKUSD | 2 | -156.9% | 156.9% |
| PF_TRUMPUSD | 2 | -89.6% | 108.6% |
| PF_NEARUSD | 2 | -71.0% | 116.1% |
| PF_HFTUSD | 2 | -33.6% | 106.8% |
| PF_UNIUSD | 1 | -108.0% | 108.0% |
| PF_ACEUSD | 1 | -62.9% | 62.9% |
| PF_XRPUSD | 1 | -30.4% | 30.4% |
| PF_MINAUSD | 1 | -30.4% | 30.4% |

**Resolved since last scan:** PF_RUNEUSD (crowded 2d, worst 67%), PF_ASTERUSD (crowded 2d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
