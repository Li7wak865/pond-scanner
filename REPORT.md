# Pond Scanner Report
**Scan time:** 2026-10-23 21:25 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | -38.2% | $574,474 |
| 🟢 | PF_NEARUSD | +33.0% | $4,282,153 |
| 🟢 | PF_XRPUSD | +30.6% | $13,117,752 |
| ⚪ | PF_WLDUSD | -16.6% | $7,522,671 |
| ⚪ | PF_ATOMUSD | +12.9% | $562,678 |
| ⚪ | PF_ARCUSD | -12.1% | $3,551,130 |
| ⚪ | PF_BATUSD | -11.4% | $1,597,318 |
| ⚪ | PF_FETUSD | +10.8% | $5,677,527 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (coinbase → gemini) — coinbase: $81,324.39, kraken: $81,333.60, gemini: $81,348.03
- ⚪ **ETH** gap **0.023%** (gemini → kraken) — coinbase: $2,400.03, kraken: $2,400.09, gemini: $2,399.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 26% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.35, realized vol 10d 31% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 1 | -38.2% | 40.1% |
| PF_NEARUSD | 1 | +33.0% | 39.0% |
| PF_XRPUSD | 1 | +30.6% | 30.6% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
