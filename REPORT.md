# Pond Scanner Report
**Scan time:** 2026-08-25 18:57 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +477.7% | $518,472 |
| 🟢 | PF_SOLUSD | +476.0% | $2,076,233 |
| 🟢 | PF_SPXUSD | -128.1% | $704,257 |
| 🟢 | PF_TRUMPUSD | -66.4% | $1,608,443 |
| 🟢 | PF_NEARUSD | -62.5% | $2,269,719 |
| 🟢 | PF_STORJUSD | -59.7% | $1,011,042 |
| 🟢 | PF_STXUSD | -53.8% | $2,673,512 |
| 🟢 | PF_ZROUSD | -48.1% | $660,538 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (kraken → gemini) — coinbase: $79,085.51, kraken: $79,071.90, gemini: $79,086.18
- ⚪ **ETH** gap **0.006%** (gemini → coinbase) — coinbase: $2,466.00, kraken: $2,465.96, gemini: $2,465.84

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #474 | $47.1M | 2.02x | +28.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.66, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.62, realized vol 10d 109% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 47% vs 30d norm 38% (1.2x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -37.7% | 241.7% |
| PF_LINKUSD | 2 | +477.7% | 477.7% |
| PF_STORJUSD | 2 | -59.7% | 214.3% |
| PF_SOLUSD | 1 | +476.0% | 476.0% |
| PF_SPXUSD | 1 | -128.1% | 128.1% |
| PF_TRUMPUSD | 1 | -66.4% | 89.5% |
| PF_NEARUSD | 1 | -62.5% | 121.5% |
| PF_STXUSD | 1 | -53.8% | 53.8% |
| PF_ZROUSD | 1 | -48.1% | 48.1% |
| PF_JTOUSD | 1 | -35.5% | 35.5% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 129%), PF_HFTUSD (crowded 2d, worst 110%), PF_BBUSD (crowded 1d, worst 44%), PF_SAGAUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
