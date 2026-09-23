# Pond Scanner Report
**Scan time:** 2026-09-23 21:30 UTC

**Flags this scan:** 21 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MINAUSD | +623.5% | $1,312,207 |
| 🟢 | PF_UNIUSD | -486.3% | $1,984,718 |
| 🟢 | PF_TRUMPUSD | -338.1% | $1,449,138 |
| 🟢 | PF_NEARUSD | -294.7% | $8,479,876 |
| 🟢 | PF_SOLUSD | +255.1% | $551,156 |
| 🟢 | PF_LINKUSD | -196.6% | $686,664 |
| 🟢 | PF_AVAXUSD | -97.9% | $690,639 |
| 🟢 | PF_JTOUSD | -94.2% | $789,098 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (kraken → coinbase) — coinbase: $84,422.59, kraken: $84,414.70, gemini: $84,420.23
- ⚪ **ETH** gap **0.007%** (kraken → gemini) — coinbase: $2,675.23, kraken: $2,675.18, gemini: $2,675.36

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #488 | $48.1M | 2.01x | +20.1% |
| Mubarak (MUBARAK) | #454 | $53.0M | 2.00x | -31.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.13, realized vol 10d 57% vs 60d 44%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.17, realized vol 10d 61% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 39% vs 30d norm 35% (1.1x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 47% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AVAXUSD | 2 | -97.9% | 218.8% |
| PF_MINAUSD | 1 | +623.5% | 623.5% |
| PF_UNIUSD | 1 | -486.3% | 486.3% |
| PF_TRUMPUSD | 1 | -338.1% | 372.6% |
| PF_NEARUSD | 1 | -294.7% | 294.7% |
| PF_SOLUSD | 1 | +255.1% | 255.1% |
| PF_LINKUSD | 1 | -196.6% | 405.6% |
| PF_JTOUSD | 1 | -94.2% | 94.2% |
| PF_RAYUSD | 1 | -91.8% | 470.6% |
| PF_ZROUSD | 1 | -79.6% | 275.8% |
| PF_APTUSD | 1 | -61.2% | 61.2% |
| PF_ACEUSD | 1 | -58.8% | 161.2% |
| PF_HFTUSD | 1 | +58.3% | 112.1% |
| PF_KAITOUSD | 1 | -52.0% | 166.8% |
| PF_SPXUSD | 1 | -45.2% | 45.2% |
| PF_FETUSD | 1 | -42.3% | 42.3% |
| PF_FILUSD | 1 | -40.6% | 68.2% |
| PF_SWARMSUSD | 1 | -33.9% | 33.9% |
| PF_DOTUSD | 1 | +32.2% | 32.2% |

**Resolved since last scan:** PF_INJUSD (crowded 1d, worst 224%), PF_BLURUSD (crowded 1d, worst 92%), PF_LDOUSD (crowded 1d, worst 58%), PF_XRPUSD (crowded 1d, worst 47%), PF_VIRTUALUSD (crowded 1d, worst 54%), PF_SUPERUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
