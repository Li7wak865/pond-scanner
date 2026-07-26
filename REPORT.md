# Pond Scanner Report
**Scan time:** 2026-07-26 13:57 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -155.2% | $531,587 |
| 🟢 | PF_AVAXUSD | +40.5% | $707,486 |
| 🟢 | PF_PNUTUSD | +37.1% | $2,389,890 |
| 🟢 | PF_ACEUSD | -34.0% | $1,297,382 |
| 🟢 | PF_XRPUSD | +31.9% | $14,984,076 |
| ⚪ | PF_STXUSD | -13.6% | $636,992 |
| ⚪ | PF_SYNUSD | +12.2% | $3,878,086 |
| ⚪ | PF_SUSHIUSD | -11.2% | $554,304 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → kraken) — coinbase: $64,459.10, kraken: $64,467.90, gemini: $64,462.01
- ⚪ **ETH** gap **0.040%** (coinbase → gemini) — coinbase: $1,884.36, kraken: $1,884.80, gemini: $1,885.12

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #371 | $60.9M | 3.09x | +49.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 21% vs 60d 37%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.15, realized vol 10d 25% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 33% (0.3x)
- ⚪ **ETH** 24h vol 12% vs 30d norm 44% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 1 | -155.2% | 155.2% |
| PF_AVAXUSD | 1 | +40.5% | 96.5% |
| PF_PNUTUSD | 1 | +37.1% | 37.1% |
| PF_ACEUSD | 1 | -34.0% | 34.0% |
| PF_XRPUSD | 1 | +31.9% | 31.9% |

**Resolved since last scan:** PF_SYNUSD (crowded 3d, worst 113%), PF_NEARUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
