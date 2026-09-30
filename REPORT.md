# Pond Scanner Report
**Scan time:** 2026-09-30 22:17 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -372.8% | $5,331,899 |
| 🟢 | PF_MOVRUSD | +226.7% | $870,658 |
| 🟢 | PF_AVAXUSD | -219.2% | $623,145 |
| 🟢 | PF_UNIUSD | +123.8% | $666,214 |
| 🟢 | PF_SOONUSD | +82.6% | $1,093,407 |
| 🟢 | PF_LSKUSD | +73.1% | $869,447 |
| 🟢 | PF_GRASSUSD | +63.3% | $569,737 |
| 🟢 | PF_APTUSD | -58.3% | $531,211 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.028%** (kraken → gemini) — coinbase: $83,699.50, kraken: $83,698.00, gemini: $83,721.37
- ⚪ **ETH** gap **0.015%** (kraken → gemini) — coinbase: $2,682.26, kraken: $2,682.15, gemini: $2,682.56

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.35, realized vol 10d 43% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.30, realized vol 10d 34% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 47% vs 30d norm 35% (1.3x)
- ⚪ **ETH** 24h vol 45% vs 30d norm 46% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AVAXUSD | 2 | -219.2% | 289.8% |
| PF_NEARUSD | 1 | -372.8% | 372.8% |
| PF_MOVRUSD | 1 | +226.7% | 242.9% |
| PF_UNIUSD | 1 | +123.8% | 123.8% |
| PF_SOONUSD | 1 | +82.6% | 82.6% |
| PF_LSKUSD | 1 | +73.1% | 73.1% |
| PF_GRASSUSD | 1 | +63.3% | 63.3% |
| PF_APTUSD | 1 | -58.3% | 58.9% |
| PF_VIRTUALUSD | 1 | +54.5% | 54.5% |
| PF_PONSUSD | 1 | +48.5% | 48.5% |
| PF_TRUMPUSD | 1 | -47.3% | 47.3% |
| PF_WLDUSD | 1 | +41.5% | 41.5% |
| PF_FILUSD | 1 | -39.1% | 39.1% |
| PF_ASTERUSD | 1 | +34.9% | 34.9% |

**Resolved since last scan:** PF_ARCUSD (crowded 1d, worst 312%), PF_RAREUSD (crowded 2d, worst 80%), PF_ETHFIUSD (crowded 5d, worst 246%), PF_XRPUSD (crowded 1d, worst 50%), PF_VETUSD (crowded 2d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
