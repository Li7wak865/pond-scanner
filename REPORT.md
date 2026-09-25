# Pond Scanner Report
**Scan time:** 2026-09-25 11:52 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +404.8% | $5,458,984 |
| 🟢 | PF_ZROUSD | +230.0% | $710,224 |
| 🟢 | PF_LINKUSD | -118.1% | $971,802 |
| 🟢 | PF_LSKUSD | -108.3% | $2,375,950 |
| 🟢 | PF_UNIUSD | -67.0% | $828,332 |
| 🟢 | PF_SYNUSD | +43.5% | $1,518,904 |
| 🟢 | PF_TRXUSD | +37.9% | $6,909,622 |
| 🟢 | PF_TRUMPUSD | +37.3% | $816,334 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → gemini) — coinbase: $84,659.51, kraken: $84,654.70, gemini: $84,660.63
- ⚪ **ETH** gap **0.019%** (kraken → coinbase) — coinbase: $2,720.60, kraken: $2,720.07, gemini: $2,720.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #458 | $55.5M | 1.57x | +28.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 51% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 49% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 35% (0.9x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 47% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +404.8% | 404.8% |
| PF_TRUMPUSD | 3 | +37.3% | 372.6% |
| PF_LINKUSD | 2 | -118.1% | 482.7% |
| PF_ZROUSD | 1 | +230.0% | 230.0% |
| PF_LSKUSD | 1 | -108.3% | 108.3% |
| PF_UNIUSD | 1 | -67.0% | 84.4% |
| PF_SYNUSD | 1 | +43.5% | 43.5% |
| PF_TRXUSD | 1 | +37.9% | 37.9% |
| PF_KAITOUSD | 1 | -34.1% | 46.7% |
| PF_SPXUSD | 1 | -31.6% | 31.6% |

**Resolved since last scan:** PF_MINAUSD (crowded 1d, worst 433%), PF_OGNUSD (crowded 1d, worst 85%), PF_FILUSD (crowded 1d, worst 41%), PF_SOLUSD (crowded 1d, worst 36%), PF_VIRTUALUSD (crowded 2d, worst 57%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
