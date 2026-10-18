# Pond Scanner Report
**Scan time:** 2026-10-18 04:35 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SANDUSD | -113.9% | $34,389,847 |
| 🟢 | PF_TIAUSD | +49.6% | $4,983,552 |
| ⚪ | PF_NEARUSD | -29.1% | $3,408,308 |
| ⚪ | PF_SPXUSD | +25.3% | $582,380 |
| ⚪ | PF_WLDUSD | -22.8% | $4,284,407 |
| ⚪ | PF_FILUSD | -16.3% | $1,739,243 |
| ⚪ | PF_XRPUSD | +16.3% | $9,950,704 |
| ⚪ | PF_BATUSD | -14.2% | $1,747,181 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (kraken → gemini) — coinbase: $81,715.95, kraken: $81,714.10, gemini: $81,717.02
- ⚪ **ETH** gap **0.005%** (kraken → gemini) — coinbase: $2,414.90, kraken: $2,414.82, gemini: $2,414.94

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 23% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 34% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 34% (0.5x)
- ⚪ **ETH** 24h vol 41% vs 30d norm 43% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SANDUSD | 1 | -113.9% | 113.9% |
| PF_TIAUSD | 1 | +49.6% | 49.6% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 136%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
