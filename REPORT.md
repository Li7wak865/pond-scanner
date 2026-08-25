# Pond Scanner Report
**Scan time:** 2026-08-25 13:11 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_STORJUSD | -141.1% | $1,961,456 |
| 🟢 | PF_HYPEUSD | -129.1% | $525,252 |
| 🟢 | PF_LINKUSD | -128.1% | $701,401 |
| 🟢 | PF_NEARUSD | -121.5% | $3,311,965 |
| 🟢 | PF_HFTUSD | +94.0% | $3,917,239 |
| 🟢 | PF_ACEUSD | -90.5% | $2,037,884 |
| 🟢 | PF_TRUMPUSD | -89.5% | $1,647,206 |
| 🟢 | PF_BBUSD | +43.5% | $1,993,500 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (kraken → gemini) — coinbase: $78,787.27, kraken: $78,769.10, gemini: $78,788.61
- ⚪ **ETH** gap **0.049%** (gemini → kraken) — coinbase: $2,467.84, kraken: $2,468.14, gemini: $2,466.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #445 | $50.6M | 1.63x | +46.3% |
| Amp (AMP) | #491 | $44.7M | 1.42x | +17.2% |
| DGrid AI (DGAI) | #254 | $104.9M | 1.26x | +81.5% |
| Velvet (VELVET) | #354 | $67.8M | 0.71x | -30.7% |
| Ontology (ONT) | #403 | $57.2M | 0.51x | +15.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.64, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.62, realized vol 10d 108% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 38% (1.3x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 52% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -90.5% | 241.7% |
| PF_STORJUSD | 2 | -141.1% | 214.3% |
| PF_LINKUSD | 2 | -128.1% | 223.0% |
| PF_HFTUSD | 2 | +94.0% | 110.1% |
| PF_HYPEUSD | 1 | -129.1% | 129.1% |
| PF_NEARUSD | 1 | -121.5% | 121.5% |
| PF_TRUMPUSD | 1 | -89.5% | 89.5% |
| PF_BBUSD | 1 | +43.5% | 44.4% |
| PF_STXUSD | 1 | -41.2% | 41.2% |
| PF_SAGAUSD | 1 | +32.9% | 32.9% |

**Resolved since last scan:** PF_SUPERUSD (crowded 1d, worst 149%), PF_SUSD (crowded 1d, worst 129%), PF_XRPUSD (crowded 2d, worst 51%), PF_ETHFIUSD (crowded 1d, worst 40%), PF_GRASSUSD (crowded 1d, worst 38%), PF_APTUSD (crowded 1d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
