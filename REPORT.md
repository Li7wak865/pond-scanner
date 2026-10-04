# Pond Scanner Report
**Scan time:** 2026-10-04 12:23 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +114.5% | $1,084,135 |
| 🟢 | PF_PONSUSD | +60.5% | $606,361 |
| 🟢 | PF_RUNEUSD | +56.2% | $674,716 |
| 🟢 | PF_ASTERUSD | +56.2% | $829,190 |
| 🟢 | PF_WLDUSD | +47.6% | $5,252,698 |
| 🟢 | PF_TRUMPUSD | -47.4% | $541,761 |
| 🟢 | PF_SYNUSD | +35.2% | $637,605 |
| 🟢 | PF_TIAUSD | +33.3% | $675,777 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (kraken → gemini) — coinbase: $85,280.01, kraken: $85,275.80, gemini: $85,301.02
- ⚪ **ETH** gap **0.032%** (gemini → kraken) — coinbase: $2,701.48, kraken: $2,701.85, gemini: $2,700.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.35, realized vol 10d 13% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 12% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 7% vs 30d norm 33% (0.2x)
- ⚪ **ETH** 24h vol 11% vs 30d norm 43% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 3 | +114.5% | 221.9% |
| PF_PONSUSD | 2 | +60.5% | 111.2% |
| PF_RUNEUSD | 1 | +56.2% | 56.2% |
| PF_ASTERUSD | 1 | +56.2% | 56.2% |
| PF_WLDUSD | 1 | +47.6% | 47.6% |
| PF_TRUMPUSD | 1 | -47.4% | 47.4% |
| PF_SYNUSD | 1 | +35.2% | 35.2% |
| PF_TIAUSD | 1 | +33.3% | 33.3% |
| PF_XRPUSD | 1 | +31.9% | 31.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 3d, worst 134%), PF_SUPERUSD (crowded 1d, worst 53%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
