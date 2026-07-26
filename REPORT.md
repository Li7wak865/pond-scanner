# Pond Scanner Report
**Scan time:** 2026-07-26 03:56 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | -112.3% | $3,489,120 |
| 🟢 | PF_LUNA2USD | +102.9% | $577,777 |
| 🟢 | PF_AVAXUSD | +96.5% | $670,419 |
| ⚪ | PF_STXUSD | -25.8% | $633,965 |
| ⚪ | PF_PNUTUSD | +23.6% | $1,054,374 |
| ⚪ | PF_SUIUSD | -16.1% | $4,069,806 |
| ⚪ | PF_LDOUSD | -13.4% | $653,727 |
| ⚪ | PF_ONDOUSD | -8.8% | $3,038,241 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $64,476.35, kraken: $64,481.20, gemini: $64,488.63
- ⚪ **ETH** gap **0.015%** (coinbase → gemini) — coinbase: $1,880.40, kraken: $1,880.51, gemini: $1,880.69

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #397 | $60.8M | 2.90x | +81.7% |
| Allora (ALLO) | #290 | $81.5M | 1.44x | -33.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 21% vs 60d 37%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 25% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 14% vs 30d norm 45% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 3 | -112.3% | 112.3% |
| PF_LUNA2USD | 1 | +102.9% | 102.9% |
| PF_AVAXUSD | 1 | +96.5% | 96.5% |

**Resolved since last scan:** PF_EIGENUSD (crowded 2d, worst 51%), PF_ACEUSD (crowded 3d, worst 192%), PF_ONDOUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
