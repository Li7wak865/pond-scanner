# Pond Scanner Report
**Scan time:** 2026-09-12 15:32 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -451.6% | $3,032,381 |
| 🟢 | PF_RIVERUSD | -132.0% | $1,148,233 |
| 🟢 | PF_UNIUSD | -48.0% | $1,150,340 |
| 🟢 | PF_ACEUSD | -33.4% | $2,126,789 |
| ⚪ | PF_RAYUSD | -27.0% | $671,168 |
| ⚪ | PF_HFTUSD | -23.7% | $668,525 |
| ⚪ | PF_JUPUSD | -18.5% | $855,486 |
| ⚪ | PF_ETHFIUSD | +18.3% | $1,245,428 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $77,434.21, kraken: $77,434.90, gemini: $77,447.47
- ⚪ **ETH** gap **0.018%** (coinbase → gemini) — coinbase: $2,540.24, kraken: $2,540.25, gemini: $2,540.69

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #410 | $57.6M | 1.16x | +103.5% |
| LAB (LAB) | #413 | $57.0M | 1.12x | +20.0% |
| Blur (BLUR) | #454 | $50.2M | 0.81x | -15.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 38% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.10, realized vol 10d 39% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 41% (0.4x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 58% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 2 | -451.6% | 451.6% |
| PF_RIVERUSD | 1 | -132.0% | 132.0% |
| PF_UNIUSD | 1 | -48.0% | 199.6% |
| PF_ACEUSD | 1 | -33.4% | 62.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 493%), PF_RAYUSD (crowded 2d, worst 472%), PF_NEARUSD (crowded 2d, worst 116%), PF_MINAUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
