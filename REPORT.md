# Pond Scanner Report
**Scan time:** 2026-11-08 13:26 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -202.8% | $526,332 |
| 🟢 | PF_NEARUSD | -198.4% | $1,516,081 |
| 🟢 | PF_TRUMPUSD | -67.4% | $1,141,281 |
| ⚪ | PF_DOTUSD | -28.9% | $1,376,888 |
| ⚪ | PF_TIAUSD | -10.8% | $637,944 |
| ⚪ | PF_XRPUSD | +10.5% | $4,864,224 |
| ⚪ | PF_ACEUSD | +10.3% | $1,276,713 |
| ⚪ | PF_ONDOUSD | -9.5% | $1,185,215 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → gemini) — coinbase: $75,951.99, kraken: $75,957.60, gemini: $75,969.32
- ⚪ **ETH** gap **0.011%** (coinbase → gemini) — coinbase: $2,238.27, kraken: $2,238.50, gemini: $2,238.52

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.26, realized vol 10d 44% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 63% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9967 (-0.33% vs peg)
- ⚪ **USDe** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 47% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -67.4% | 178.3% |
| PF_NEARUSD | 2 | -198.4% | 198.4% |
| PF_UNIUSD | 1 | -202.8% | 202.8% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
