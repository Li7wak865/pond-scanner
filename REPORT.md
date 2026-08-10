# Pond Scanner Report
**Scan time:** 2026-08-10 02:35 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -742.4% | $1,922,507 |
| 🟢 | PF_SOLUSD | +274.3% | $528,566 |
| 🟢 | PF_HFTUSD | +170.5% | $3,124,946 |
| ⚪ | PF_SYNUSD | -25.9% | $897,842 |
| ⚪ | PF_DOTUSD | -25.0% | $724,332 |
| ⚪ | PF_UNIUSD | -14.0% | $553,505 |
| ⚪ | PF_BIOUSD | +11.4% | $572,318 |
| ⚪ | PF_CTSIUSD | -11.2% | $10,352,514 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (coinbase → gemini) — coinbase: $64,917.47, kraken: $64,923.70, gemini: $64,932.04
- ⚪ **ETH** gap **0.031%** (kraken → gemini) — coinbase: $1,914.40, kraken: $1,914.30, gemini: $1,914.89

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #617 | $43.6M | 5.74x | -30.6% |
| BOOK OF MEME (BOME) | #405 | $52.3M | 1.58x | +23.1% |
| ConstitutionDAO (PEOPLE) | #448 | $46.6M | 0.60x | +20.1% |
| Cap (CAP) | #317 | $73.5M | 0.59x | +26.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 11% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 20% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 28% (0.5x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 40% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 1 | -742.4% | 742.4% |
| PF_SOLUSD | 1 | +274.3% | 274.3% |
| PF_HFTUSD | 1 | +170.5% | 170.5% |

**Resolved since last scan:** PF_ACEUSD (crowded 4d, worst 502%), PF_UNIUSD (crowded 2d, worst 42%), PF_NEARUSD (crowded 2d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
