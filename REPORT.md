# Pond Scanner Report
**Scan time:** 2026-10-01 05:56 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -951.6% | $1,093,567 |
| 🟢 | PF_UNIUSD | +543.2% | $736,556 |
| 🟢 | PF_AVAXUSD | +153.8% | $664,020 |
| 🟢 | PF_PONSUSD | +92.7% | $871,413 |
| 🟢 | PF_TRUMPUSD | -80.6% | $1,037,122 |
| 🟢 | PF_NEARUSD | -51.8% | $5,870,336 |
| 🟢 | PF_SUIUSD | +37.7% | $13,997,906 |
| 🟢 | PF_ETHFIUSD | -37.5% | $1,090,851 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.034%** (coinbase → gemini) — coinbase: $84,263.54, kraken: $84,273.40, gemini: $84,292.48
- ⚪ **ETH** gap **0.015%** (kraken → coinbase) — coinbase: $2,716.96, kraken: $2,716.55, gemini: $2,716.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.35, realized vol 10d 15% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 17% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 47% vs 30d norm 35% (1.4x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 46% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AVAXUSD | 3 | +153.8% | 289.8% |
| PF_MOVRUSD | 2 | -951.6% | 951.6% |
| PF_UNIUSD | 2 | +543.2% | 543.2% |
| PF_PONSUSD | 2 | +92.7% | 92.7% |
| PF_TRUMPUSD | 2 | -80.6% | 80.6% |
| PF_NEARUSD | 2 | -51.8% | 372.8% |
| PF_WLDUSD | 2 | +36.2% | 41.5% |
| PF_LSKUSD | 2 | -35.3% | 73.2% |
| PF_SUIUSD | 1 | +37.7% | 37.7% |
| PF_ETHFIUSD | 1 | -37.5% | 37.5% |
| PF_DOTUSD | 1 | +33.0% | 33.0% |

**Resolved since last scan:** PF_SOONUSD (crowded 2d, worst 83%), PF_GRASSUSD (crowded 2d, worst 63%), PF_APTUSD (crowded 2d, worst 59%), PF_VIRTUALUSD (crowded 2d, worst 55%), PF_FILUSD (crowded 2d, worst 39%), PF_ASTERUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
