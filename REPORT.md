# Pond Scanner Report
**Scan time:** 2026-10-18 15:53 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -102.9% | $4,242,283 |
| 🟢 | PF_ZROUSD | -74.1% | $698,251 |
| 🟢 | PF_FILUSD | -51.5% | $2,208,676 |
| 🟢 | PF_APTUSD | -41.1% | $547,462 |
| 🟢 | PF_TIAUSD | +37.1% | $3,258,814 |
| 🟢 | PF_SANDUSD | -36.2% | $41,315,755 |
| 🟢 | PF_XRPUSD | -30.3% | $10,706,664 |
| ⚪ | PF_BATUSD | -24.4% | $1,167,443 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → gemini) — coinbase: $81,026.58, kraken: $81,031.80, gemini: $81,035.65
- ⚪ **ETH** gap **0.019%** (coinbase → kraken) — coinbase: $2,374.96, kraken: $2,375.42, gemini: $2,375.20

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 23% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.41, realized vol 10d 33% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 33% (0.7x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 42% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -102.9% | 102.9% |
| PF_ZROUSD | 1 | -74.1% | 88.1% |
| PF_FILUSD | 1 | -51.5% | 51.5% |
| PF_APTUSD | 1 | -41.1% | 41.1% |
| PF_TIAUSD | 1 | +37.1% | 49.6% |
| PF_SANDUSD | 1 | -36.2% | 36.2% |
| PF_XRPUSD | 1 | -30.3% | 30.3% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
