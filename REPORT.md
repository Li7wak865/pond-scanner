# Pond Scanner Report
**Scan time:** 2026-08-08 18:59 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -181.6% | $7,507,539 |
| 🟢 | PF_ZBTUSD | -49.3% | $720,908 |
| 🟢 | PF_NEARUSD | +37.8% | $1,153,823 |
| ⚪ | PF_HFTUSD | -29.2% | $9,757,325 |
| ⚪ | PF_SYNUSD | -23.4% | $2,174,380 |
| ⚪ | PF_COTIUSD | -21.2% | $13,274,327 |
| ⚪ | PF_LDOUSD | +20.8% | $517,330 |
| ⚪ | PF_DEEPUSD | +20.6% | $2,104,847 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $64,986.86, kraken: $64,997.60, gemini: $64,997.85
- ⚪ **ETH** gap **0.017%** (kraken → coinbase) — coinbase: $1,919.94, kraken: $1,919.62, gemini: $1,919.72

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #339 | $66.9M | 2.26x | +99.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 23% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 28% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 28% (0.3x)
- ⚪ **ETH** 24h vol 14% vs 30d norm 41% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 2 | -181.6% | 501.6% |
| PF_ZBTUSD | 1 | -49.3% | 49.3% |
| PF_NEARUSD | 1 | +37.8% | 55.1% |

**Resolved since last scan:** PF_KAITOUSD (crowded 2d, worst 608%), PF_DEEPUSD (crowded 1d, worst 75%), PF_UNIUSD (crowded 1d, worst 65%), PF_HFTUSD (crowded 1d, worst 210%), PF_SYNUSD (crowded 1d, worst 40%), PF_SNXUSD (crowded 1d, worst 38%), PF_XRPUSD (crowded 1d, worst 34%), PF_FILUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
