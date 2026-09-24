# Pond Scanner Report
**Scan time:** 2026-09-24 17:12 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MINAUSD | -659.6% | $1,590,272 |
| 🟢 | PF_LINKUSD | +482.7% | $520,149 |
| 🟢 | PF_UNIUSD | +231.8% | $867,951 |
| 🟢 | PF_TRUMPUSD | +208.5% | $1,633,977 |
| 🟢 | PF_LSKUSD | -171.7% | $2,789,480 |
| 🟢 | PF_NEARUSD | -115.5% | $5,331,760 |
| 🟢 | PF_HFTUSD | -104.1% | $2,808,701 |
| 🟢 | PF_SPXUSD | +81.4% | $881,032 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (gemini → coinbase) — coinbase: $84,391.17, kraken: $84,378.00, gemini: $84,377.39
- ⚪ **ETH** gap **0.026%** (kraken → coinbase) — coinbase: $2,681.51, kraken: $2,680.80, gemini: $2,680.84

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #422 | $59.8M | 2.40x | +23.1% |
| Lisk (LSK) | #304 | $93.7M | 1.35x | +34.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 57% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 60% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 40% vs 30d norm 35% (1.1x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 47% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | +231.8% | 545.8% |
| PF_TRUMPUSD | 2 | +208.5% | 372.6% |
| PF_NEARUSD | 2 | -115.5% | 343.9% |
| PF_HFTUSD | 2 | -104.1% | 112.1% |
| PF_SPXUSD | 2 | +81.4% | 81.4% |
| PF_MINAUSD | 1 | -659.6% | 659.6% |
| PF_LINKUSD | 1 | +482.7% | 482.7% |
| PF_LSKUSD | 1 | -171.7% | 171.7% |
| PF_JTOUSD | 1 | +74.4% | 74.4% |
| PF_ZROUSD | 1 | +69.9% | 69.9% |
| PF_VIRTUALUSD | 1 | +57.1% | 57.1% |
| PF_XPLUSD | 1 | +40.3% | 40.3% |

**Resolved since last scan:** PF_RAYUSD (crowded 1d, worst 119%), PF_AVAXUSD (crowded 3d, worst 219%), PF_APTUSD (crowded 1d, worst 40%), PF_SUIUSD (crowded 1d, worst 34%), PF_DOTUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
