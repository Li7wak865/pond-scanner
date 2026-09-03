# Pond Scanner Report
**Scan time:** 2026-09-03 04:34 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -190.2% | $2,384,642 |
| 🟢 | PF_UNIUSD | +86.3% | $1,602,289 |
| 🟢 | PF_XRPUSD | +35.9% | $42,288,561 |
| 🟢 | PF_HFTUSD | +32.0% | $1,312,839 |
| ⚪ | PF_DOTUSD | +24.8% | $1,492,614 |
| ⚪ | PF_VELOUSD | -21.4% | $2,342,400 |
| ⚪ | PF_VIRTUALUSD | +20.6% | $1,067,521 |
| ⚪ | PF_APTUSD | +17.9% | $547,177 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.045%** (kraken → gemini) — coinbase: $77,570.01, kraken: $77,563.40, gemini: $77,598.00
- ⚪ **ETH** gap **0.053%** (kraken → gemini) — coinbase: $2,397.85, kraken: $2,397.82, gemini: $2,399.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #416 | $54.0M | 3.15x | +27.0% |
| Ankr Network (ANKR) | #476 | $46.4M | 1.34x | +17.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.54, realized vol 10d 25% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 32% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 41% vs 30d norm 52% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +86.3% | 280.5% |
| PF_ACEUSD | 3 | -190.2% | 304.8% |
| PF_HFTUSD | 2 | +32.0% | 108.4% |
| PF_XRPUSD | 1 | +35.9% | 35.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 64%), PF_SYRUPUSD (crowded 2d, worst 186%), PF_ICXUSD (crowded 2d, worst 38%), PF_VIRTUALUSD (crowded 2d, worst 38%), PF_ASTERUSD (crowded 2d, worst 82%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
