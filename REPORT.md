# Pond Scanner Report
**Scan time:** 2026-08-26 07:09 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -820.8% | $1,027,834 |
| 🟢 | PF_TRUMPUSD | -417.1% | $1,554,831 |
| 🟢 | PF_ACEUSD | -155.0% | $3,005,546 |
| 🟢 | PF_SPXUSD | -99.7% | $907,385 |
| 🟢 | PF_HFTUSD | +85.9% | $2,820,126 |
| 🟢 | PF_COTIUSD | +60.9% | $3,436,199 |
| 🟢 | PF_LINKUSD | -54.8% | $505,562 |
| 🟢 | PF_VIRTUALUSD | -47.7% | $1,344,138 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (coinbase → kraken) — coinbase: $78,960.80, kraken: $78,979.40, gemini: $78,972.99
- ⚪ **ETH** gap **0.133%** (coinbase → gemini) — coinbase: $2,462.89, kraken: $2,463.28, gemini: $2,466.16

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.66, realized vol 10d 57% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.59, realized vol 10d 109% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 39% vs 30d norm 38% (1.0x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -155.0% | 241.7% |
| PF_LINKUSD | 3 | -54.8% | 477.7% |
| PF_SOLUSD | 2 | -820.8% | 820.8% |
| PF_TRUMPUSD | 2 | -417.1% | 417.1% |
| PF_SPXUSD | 2 | -99.7% | 128.1% |
| PF_NEARUSD | 2 | -33.9% | 121.5% |
| PF_HFTUSD | 1 | +85.9% | 103.9% |
| PF_COTIUSD | 1 | +60.9% | 60.9% |
| PF_VIRTUALUSD | 1 | -47.7% | 47.7% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 121%), PF_RENDERUSD (crowded 1d, worst 83%), PF_KAITOUSD (crowded 1d, worst 61%), PF_STXUSD (crowded 2d, worst 54%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
