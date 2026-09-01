# Pond Scanner Report
**Scan time:** 2026-09-01 16:41 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -203.9% | $2,428,152 |
| 🟢 | PF_RENDERUSD | +175.0% | $645,084 |
| 🟢 | PF_UNIUSD | -150.3% | $966,448 |
| 🟢 | PF_TRXUSD | -71.2% | $5,522,313 |
| 🟢 | PF_NEARUSD | -57.5% | $1,784,069 |
| 🟢 | PF_STXUSD | -47.5% | $941,758 |
| 🟢 | PF_TRUMPUSD | -44.2% | $574,642 |
| ⚪ | PF_VELOUSD | -23.8% | $2,586,830 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (kraken → coinbase) — coinbase: $77,491.45, kraken: $77,489.70, gemini: $77,490.01
- ⚪ **ETH** gap **0.029%** (coinbase → gemini) — coinbase: $2,430.42, kraken: $2,430.65, gemini: $2,431.13

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #427 | $52.5M | 1.06x | +16.6% |
| Useless Coin (USELESS) | #265 | $102.1M | 0.80x | +27.8% |
| Cysic (CYS) | #344 | $70.8M | 0.76x | -34.2% |
| MarsCoin (MARSCOIN) | #378 | $64.2M | 0.68x | +42.7% |
| 牛来 (Niu Lai) (牛来) | #310 | $82.8M | 0.53x | -25.6% |
| Siacoin (SC) | #475 | $45.7M | 0.53x | +53.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 27% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.49, realized vol 10d 33% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -150.3% | 150.3% |
| PF_TRUMPUSD | 2 | -44.2% | 233.6% |
| PF_ACEUSD | 1 | -203.9% | 203.9% |
| PF_RENDERUSD | 1 | +175.0% | 175.0% |
| PF_TRXUSD | 1 | -71.2% | 71.2% |
| PF_NEARUSD | 1 | -57.5% | 57.5% |
| PF_STXUSD | 1 | -47.5% | 47.5% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 893%), PF_FILUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
