# Pond Scanner Report
**Scan time:** 2026-08-30 05:25 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -144.1% | $521,382 |
| 🟢 | PF_ACEUSD | -80.7% | $1,680,104 |
| 🟢 | PF_NEARUSD | -52.4% | $668,949 |
| 🟢 | PF_SYNUSD | +43.7% | $516,980 |
| 🟢 | PF_TRUMPUSD | +31.8% | $1,851,082 |
| ⚪ | PF_HFTUSD | -27.9% | $1,807,715 |
| ⚪ | PF_BICOUSD | -26.2% | $12,174,088 |
| ⚪ | PF_CRVUSD | -21.8% | $3,560,836 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → gemini) — coinbase: $78,144.77, kraken: $78,140.70, gemini: $78,146.32
- ⚪ **ETH** gap **0.007%** (gemini → coinbase) — coinbase: $2,456.09, kraken: $2,455.96, gemini: $2,455.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 49% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.57, realized vol 10d 60% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (-0.00% vs peg)
- ⚪ **USDe** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 12% vs 30d norm 38% (0.3x)
- ⚪ **ETH** 24h vol 13% vs 30d norm 51% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 9 | -80.7% | 241.7% |
| PF_UNIUSD | 1 | -144.1% | 144.1% |
| PF_NEARUSD | 1 | -52.4% | 52.4% |
| PF_SYNUSD | 1 | +43.7% | 43.7% |
| PF_TRUMPUSD | 1 | +31.8% | 31.8% |

**Resolved since last scan:** PF_STXUSD (crowded 3d, worst 64%), PF_DEXEUSD (crowded 2d, worst 215%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
