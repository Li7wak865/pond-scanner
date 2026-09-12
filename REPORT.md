# Pond Scanner Report
**Scan time:** 2026-09-12 20:34 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RIVERUSD | +238.3% | $1,165,633 |
| 🟢 | PF_LSKUSD | -156.1% | $4,785,786 |
| 🟢 | PF_RAYUSD | -66.9% | $504,221 |
| 🟢 | PF_HFTUSD | -60.2% | $649,235 |
| 🟢 | PF_ALCHUSD | +59.2% | $2,567,375 |
| 🟢 | PF_ACEUSD | -54.2% | $1,552,063 |
| 🟢 | PF_NEARUSD | +44.2% | $1,541,112 |
| ⚪ | PF_UNIUSD | -28.3% | $1,335,010 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → gemini) — coinbase: $77,158.35, kraken: $77,158.90, gemini: $77,167.06
- ⚪ **ETH** gap **0.050%** (coinbase → gemini) — coinbase: $2,521.50, kraken: $2,521.74, gemini: $2,522.75

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #434 | $53.1M | 1.29x | +73.5% |
| VeThor (VTHO) | #362 | $68.6M | 0.65x | +15.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 38% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 39% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 41% (0.2x)
- ⚪ **ETH** 24h vol 20% vs 30d norm 58% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -156.1% | 451.6% |
| PF_RIVERUSD | 1 | +238.3% | 238.3% |
| PF_RAYUSD | 1 | -66.9% | 66.9% |
| PF_HFTUSD | 1 | -60.2% | 60.2% |
| PF_ALCHUSD | 1 | +59.2% | 59.2% |
| PF_ACEUSD | 1 | -54.2% | 62.9% |
| PF_NEARUSD | 1 | +44.2% | 44.2% |

**Resolved since last scan:** PF_UNIUSD (crowded 1d, worst 200%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
