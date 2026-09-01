# Pond Scanner Report
**Scan time:** 2026-09-01 21:02 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +438.2% | $580,675 |
| 🟢 | PF_ACEUSD | -304.8% | $3,223,904 |
| 🟢 | PF_TRUMPUSD | +158.4% | $646,092 |
| 🟢 | PF_UNIUSD | -101.0% | $1,145,595 |
| 🟢 | PF_RENDERUSD | +69.5% | $683,019 |
| 🟢 | PF_TRXUSD | -61.1% | $6,779,919 |
| 🟢 | PF_FILUSD | +51.1% | $2,224,739 |
| 🟢 | PF_NEARUSD | +32.1% | $2,017,186 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (kraken → gemini) — coinbase: $77,432.40, kraken: $77,431.30, gemini: $77,442.67
- ⚪ **ETH** gap **0.009%** (gemini → coinbase) — coinbase: $2,420.00, kraken: $2,419.99, gemini: $2,419.78

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Siacoin (SC) | #485 | $44.7M | 2.10x | +49.3% |
| Cysic (CYS) | #339 | $71.9M | 0.82x | -30.0% |
| MarsCoin (MARSCOIN) | #351 | $68.7M | 0.70x | +57.1% |
| 牛来 (Niu Lai) (牛来) | #305 | $82.8M | 0.58x | -21.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 27% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 34% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 2 | +158.4% | 233.6% |
| PF_UNIUSD | 2 | -101.0% | 150.3% |
| PF_SOLUSD | 1 | +438.2% | 438.2% |
| PF_ACEUSD | 1 | -304.8% | 304.8% |
| PF_RENDERUSD | 1 | +69.5% | 175.0% |
| PF_TRXUSD | 1 | -61.1% | 71.2% |
| PF_FILUSD | 1 | +51.1% | 51.1% |
| PF_NEARUSD | 1 | +32.1% | 57.5% |

**Resolved since last scan:** PF_STXUSD (crowded 1d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
