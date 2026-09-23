# Pond Scanner Report
**Scan time:** 2026-09-23 04:46 UTC

**Flags this scan:** 22 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +857.3% | $1,838,482 |
| 🟢 | PF_LINKUSD | +325.4% | $565,537 |
| 🟢 | PF_NEARUSD | -244.2% | $6,156,828 |
| 🟢 | PF_ETHFIUSD | +137.0% | $818,398 |
| 🟢 | PF_TRUMPUSD | +136.4% | $1,481,359 |
| 🟢 | PF_LSKUSD | -111.6% | $950,500 |
| 🟢 | PF_HFTUSD | -110.3% | $1,318,120 |
| 🟢 | PF_AVAXUSD | -103.9% | $839,860 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (kraken → gemini) — coinbase: $87,150.52, kraken: $87,149.50, gemini: $87,160.01
- ⚪ **ETH** gap **0.008%** (kraken → gemini) — coinbase: $2,782.72, kraken: $2,782.70, gemini: $2,782.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #330 | $84.5M | 3.12x | +56.9% |
| Aurora (AURORA) | #413 | $64.6M | 0.61x | +79.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.25, realized vol 10d 54% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.30, realized vol 10d 56% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 36% (0.7x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 47% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 7 | +857.3% | 857.3% |
| PF_NEARUSD | 4 | -244.2% | 457.9% |
| PF_LINKUSD | 3 | +325.4% | 725.7% |
| PF_TRUMPUSD | 3 | +136.4% | 207.1% |
| PF_RENDERUSD | 3 | +35.1% | 209.9% |
| PF_ETHFIUSD | 2 | +137.0% | 137.0% |
| PF_LSKUSD | 2 | -111.6% | 290.1% |
| PF_AVAXUSD | 2 | -103.9% | 135.6% |
| PF_RUNEUSD | 2 | +30.3% | 43.6% |
| PF_HFTUSD | 1 | -110.3% | 110.3% |
| PF_BLURUSD | 1 | +90.5% | 90.5% |
| PF_TIAUSD | 1 | +47.4% | 47.4% |
| PF_EIGENUSD | 1 | +43.7% | 43.7% |
| PF_JTOUSD | 1 | +39.9% | 39.9% |
| PF_FETUSD | 1 | +35.0% | 35.0% |
| PF_SYNUSD | 1 | +34.5% | 34.5% |
| PF_VIRTUALUSD | 1 | +33.7% | 33.7% |
| PF_ZROUSD | 1 | +32.3% | 32.3% |
| PF_ASTRUSD | 1 | +32.2% | 32.2% |
| PF_MINAUSD | 1 | +30.0% | 30.0% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 92%), PF_FILUSD (crowded 2d, worst 71%), PF_SPXUSD (crowded 2d, worst 69%), PF_BIGTIMEUSD (crowded 2d, worst 37%), PF_ASTERUSD (crowded 2d, worst 34%), PF_DOTUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
