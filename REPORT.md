# Pond Scanner Report
**Scan time:** 2026-08-21 07:08 UTC

**Flags this scan:** 25 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +152.6% | $1,125,807 |
| 🟢 | PF_KAITOUSD | -137.5% | $1,142,662 |
| 🟢 | PF_LINKUSD | +118.4% | $565,444 |
| 🟢 | PF_ONTUSD | -103.2% | $1,452,162 |
| 🟢 | PF_JTOUSD | +76.6% | $605,648 |
| 🟢 | PF_PYTHUSD | -69.1% | $1,325,518 |
| 🟢 | PF_ACEUSD | +59.0% | $14,554,630 |
| 🟢 | PF_JUPUSD | +58.7% | $689,485 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (kraken → coinbase) — coinbase: $75,801.37, kraken: $75,789.90, gemini: $75,794.56
- ⚪ **ETH** gap **0.064%** (gemini → coinbase) — coinbase: $2,375.55, kraken: $2,375.22, gemini: $2,374.02

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| BOOK OF MEME (BOME) | #282 | $87.0M | 2.84x | +33.7% |
| ConstitutionDAO (PEOPLE) | #399 | $55.9M | 1.22x | +36.3% |
| Ontology (ONT) | #438 | $50.8M | 1.11x | +27.8% |
| Ontology Gas (ONG) | #385 | $59.2M | 0.95x | +104.5% |
| 牛来 (Niu Lai) (牛来) | #336 | $69.6M | 0.64x | +75.4% |
| Spark (SPK) | #413 | $53.6M | 0.59x | +18.3% |
| GALA (GALA) | #293 | $82.5M | 0.56x | +18.2% |
| ORDI (ORDI) | #277 | $89.1M | 0.53x | +15.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.72, realized vol 10d 50% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.75, realized vol 10d 98% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 66% vs 30d norm 32% (2.1x)
- ⚪ **ETH** 24h vol 61% vs 30d norm 47% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | +152.6% | 152.6% |
| PF_LINKUSD | 2 | +118.4% | 118.4% |
| PF_ACEUSD | 2 | +59.0% | 217.7% |
| PF_JUPUSD | 2 | +58.7% | 58.7% |
| PF_TRUMPUSD | 2 | -41.7% | 130.8% |
| PF_CATIUSD | 2 | -40.3% | 215.5% |
| PF_KAITOUSD | 1 | -137.5% | 137.5% |
| PF_ONTUSD | 1 | -103.2% | 103.2% |
| PF_JTOUSD | 1 | +76.6% | 76.6% |
| PF_PYTHUSD | 1 | -69.1% | 69.1% |
| PF_VIRTUALUSD | 1 | +50.9% | 50.9% |
| PF_LDOUSD | 1 | -49.1% | 49.1% |
| PF_TIAUSD | 1 | +43.0% | 43.0% |
| PF_ZKUSD | 1 | +39.5% | 39.5% |
| PF_SUIUSD | 1 | +33.3% | 33.3% |
| PF_STXUSD | 1 | -32.3% | 32.3% |

**Resolved since last scan:** PF_AVAXUSD (crowded 2d, worst 152%), PF_ETHFIUSD (crowded 2d, worst 155%), PF_SUSHIUSD (crowded 1d, worst 81%), PF_RAREUSD (crowded 1d, worst 55%), PF_HFTUSD (crowded 2d, worst 38%), PF_NEARUSD (crowded 2d, worst 71%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
