# Pond Scanner Report
**Scan time:** 2026-10-15 04:41 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | -403.5% | $746,359 |
| 🟢 | PF_ATOMUSD | -152.9% | $532,386 |
| 🟢 | PF_ZROUSD | -59.4% | $817,455 |
| 🟢 | PF_GRASSUSD | -53.1% | $856,976 |
| 🟢 | PF_FILUSD | +49.7% | $2,286,073 |
| 🟢 | PF_VIRTUALUSD | -49.5% | $836,576 |
| 🟢 | PF_PONSUSD | +38.0% | $4,585,296 |
| 🟢 | PF_TRUMPUSD | -34.2% | $851,090 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (kraken → gemini) — coinbase: $81,457.58, kraken: $81,456.20, gemini: $81,473.29
- ⚪ **ETH** gap **0.138%** (gemini → coinbase) — coinbase: $2,380.70, kraken: $2,380.57, gemini: $2,377.41

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 28% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 44% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 42% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | -403.5% | 403.5% |
| PF_ZROUSD | 2 | -59.4% | 100.8% |
| PF_GRASSUSD | 2 | -53.1% | 66.0% |
| PF_FILUSD | 2 | +49.7% | 49.7% |
| PF_ATOMUSD | 1 | -152.9% | 152.9% |
| PF_VIRTUALUSD | 1 | -49.5% | 49.5% |
| PF_PONSUSD | 1 | +38.0% | 38.0% |
| PF_TRUMPUSD | 1 | -34.2% | 34.2% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 602%), PF_NEARUSD (crowded 2d, worst 204%), PF_STXUSD (crowded 2d, worst 38%), PF_SUIUSD (crowded 2d, worst 32%), PF_JTOUSD (crowded 2d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
