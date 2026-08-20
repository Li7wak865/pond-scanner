# Pond Scanner Report
**Scan time:** 2026-08-20 18:59 UTC

**Flags this scan:** 23 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +819.3% | $1,275,554 |
| 🟢 | PF_ACEUSD | -217.7% | $14,559,760 |
| 🟢 | PF_CATIUSD | +215.5% | $995,382 |
| 🟢 | PF_AVAXUSD | +151.8% | $1,169,345 |
| 🟢 | PF_IOTAUSD | +131.0% | $1,530,495 |
| 🟢 | PF_TRUMPUSD | +130.8% | $2,699,114 |
| 🟢 | PF_ETHFIUSD | -111.5% | $889,278 |
| 🟢 | PF_UNIUSD | +106.1% | $1,234,873 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → kraken) — coinbase: $72,415.33, kraken: $72,430.70, gemini: $72,419.60
- ⚪ **ETH** gap **0.116%** (coinbase → gemini) — coinbase: $2,316.06, kraken: $2,316.41, gemini: $2,318.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| BOOK OF MEME (BOME) | #298 | $78.9M | 2.34x | +31.3% |
| ConstitutionDAO (PEOPLE) | #417 | $52.2M | 0.73x | +31.0% |
| Peanut the Squirrel (PNUT) | #421 | $51.3M | 0.67x | +18.4% |
| 牛来 (Niu Lai) (牛来) | #379 | $60.1M | 0.64x | +47.4% |
| ORDI (ORDI) | #277 | $87.3M | 0.54x | +19.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 48% vs 60d 34%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.69, realized vol 10d 99% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 61% vs 30d norm 30% (2.0x)
- 🟢 **ETH** 24h vol 133% vs 30d norm 47% (2.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_HYPEUSD | 1 | +819.3% | 819.3% |
| PF_ACEUSD | 1 | -217.7% | 217.7% |
| PF_CATIUSD | 1 | +215.5% | 215.5% |
| PF_AVAXUSD | 1 | +151.8% | 151.8% |
| PF_IOTAUSD | 1 | +131.0% | 131.0% |
| PF_TRUMPUSD | 1 | +130.8% | 130.8% |
| PF_ETHFIUSD | 1 | -111.5% | 154.6% |
| PF_UNIUSD | 1 | +106.1% | 106.1% |
| PF_NEARUSD | 1 | +71.2% | 71.2% |
| PF_LINKUSD | 1 | +67.6% | 67.6% |
| PF_GOATUSD | 1 | +66.5% | 66.5% |
| PF_CHILLGUYUSD | 1 | +52.4% | 52.4% |
| PF_JUPUSD | 1 | +46.7% | 54.3% |
| PF_GRASSUSD | 1 | +45.3% | 52.8% |
| PF_XRPUSD | 1 | -37.7% | 37.7% |
| PF_HFTUSD | 1 | -31.5% | 32.1% |
| PF_SUIUSD | 1 | +31.1% | 37.6% |

**Resolved since last scan:** PF_ZEREBROUSD (crowded 1d, worst 192%), PF_MOODENGUSD (crowded 1d, worst 79%), PF_VIRTUALUSD (crowded 1d, worst 55%), PF_RAREUSD (crowded 1d, worst 53%), PF_DOTUSD (crowded 1d, worst 40%), PF_WLDUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
