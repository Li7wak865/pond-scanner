# Pond Scanner Report
**Scan time:** 2026-09-26 11:26 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +339.0% | $886,292 |
| 🟢 | PF_LINKUSD | +249.1% | $982,392 |
| 🟢 | PF_RAREUSD | -105.4% | $9,743,802 |
| 🟢 | PF_LSKUSD | -102.6% | $775,692 |
| 🟢 | PF_JTOUSD | +101.8% | $1,469,516 |
| 🟢 | PF_2ZUSD | -63.6% | $4,106,994 |
| 🟢 | PF_GRASSUSD | +55.7% | $704,032 |
| 🟢 | PF_KAITOUSD | -48.6% | $959,337 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (kraken → gemini) — coinbase: $84,165.39, kraken: $84,162.90, gemini: $84,170.06
- ⚪ **ETH** gap **0.006%** (coinbase → kraken) — coinbase: $2,688.75, kraken: $2,688.92, gemini: $2,688.82

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #397 | $68.5M | 3.18x | +27.8% |
| Mubarak (MUBARAK) | #449 | $57.1M | 2.09x | +26.9% |
| Nillion (NIL) | #463 | $54.9M | 0.76x | -15.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 35% (0.5x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 46% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | +339.0% | 372.6% |
| PF_LSKUSD | 2 | -102.6% | 191.7% |
| PF_JTOUSD | 2 | +101.8% | 101.8% |
| PF_GRASSUSD | 2 | +55.7% | 72.5% |
| PF_DOTUSD | 2 | +42.2% | 45.2% |
| PF_LINKUSD | 1 | +249.1% | 364.0% |
| PF_RAREUSD | 1 | -105.4% | 105.4% |
| PF_2ZUSD | 1 | -63.6% | 63.6% |
| PF_KAITOUSD | 1 | -48.6% | 50.3% |
| PF_ONDOUSD | 1 | +33.1% | 42.4% |
| PF_EIGENUSD | 1 | +30.1% | 30.1% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 537%), PF_ZROUSD (crowded 2d, worst 280%), PF_VIRTUALUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
