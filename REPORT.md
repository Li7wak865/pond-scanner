# Pond Scanner Report
**Scan time:** 2026-10-18 20:45 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -80.6% | $5,040,484 |
| 🟢 | PF_TIAUSD | +30.6% | $2,497,307 |
| ⚪ | PF_PONSUSD | +24.8% | $1,019,317 |
| ⚪ | PF_POPCATUSD | -24.4% | $834,787 |
| ⚪ | PF_DOTUSD | -23.6% | $1,700,038 |
| ⚪ | PF_APTUSD | -23.2% | $587,992 |
| ⚪ | PF_SANDUSD | -20.5% | $37,841,669 |
| ⚪ | PF_FILUSD | -18.5% | $3,160,360 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (gemini → kraken) — coinbase: $80,765.36, kraken: $80,768.50, gemini: $80,764.42
- ⚪ **ETH** gap **0.023%** (gemini → kraken) — coinbase: $2,342.35, kraken: $2,342.82, gemini: $2,342.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 24% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 35% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 33% (0.7x)
- ⚪ **ETH** 24h vol 51% vs 30d norm 42% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -80.6% | 102.9% |
| PF_TIAUSD | 1 | +30.6% | 49.6% |

**Resolved since last scan:** PF_ZROUSD (crowded 1d, worst 88%), PF_FILUSD (crowded 1d, worst 52%), PF_APTUSD (crowded 1d, worst 41%), PF_SANDUSD (crowded 1d, worst 36%), PF_XRPUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
