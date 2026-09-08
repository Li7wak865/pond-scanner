# Pond Scanner Report
**Scan time:** 2026-09-08 16:39 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +215.3% | $673,851 |
| 🟢 | PF_VIRTUALUSD | +91.0% | $694,857 |
| 🟢 | PF_INJUSD | -85.4% | $720,371 |
| 🟢 | PF_ACEUSD | -80.6% | $2,692,089 |
| 🟢 | PF_JTOUSD | +50.1% | $1,385,129 |
| 🟢 | PF_XRPUSD | +47.1% | $28,887,079 |
| 🟢 | PF_SUIUSD | +44.8% | $6,749,170 |
| 🟢 | PF_TRUMPUSD | +36.0% | $757,736 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (kraken → coinbase) — coinbase: $78,859.99, kraken: $78,845.40, gemini: $78,853.24
- ⚪ **ETH** gap **0.084%** (gemini → coinbase) — coinbase: $2,500.79, kraken: $2,500.33, gemini: $2,498.68

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.35, realized vol 10d 37% vs 60d 39%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 40% (0.7x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 54% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | +36.0% | 476.2% |
| PF_INJUSD | 2 | -85.4% | 604.5% |
| PF_ACEUSD | 2 | -80.6% | 289.3% |
| PF_UNIUSD | 1 | +215.3% | 215.3% |
| PF_VIRTUALUSD | 1 | +91.0% | 91.0% |
| PF_JTOUSD | 1 | +50.1% | 50.1% |
| PF_XRPUSD | 1 | +47.1% | 47.1% |
| PF_SUIUSD | 1 | +44.8% | 44.8% |
| PF_DOTUSD | 1 | -30.4% | 54.6% |

**Resolved since last scan:** PF_ASTERUSD (crowded 1d, worst 62%), PF_NEARUSD (crowded 1d, worst 34%), PF_KAITOUSD (crowded 1d, worst 33%), PF_HFTUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
