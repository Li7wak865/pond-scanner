# Pond Scanner Report
**Scan time:** 2026-10-04 21:26 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -256.0% | $2,672,023 |
| 🟢 | PF_TRUMPUSD | +99.1% | $616,408 |
| 🟢 | PF_PONSUSD | +72.1% | $560,941 |
| 🟢 | PF_WLDUSD | +34.0% | $3,416,462 |
| 🟢 | PF_XTZUSD | +33.5% | $599,979 |
| ⚪ | PF_GOATUSD | -25.4% | $1,031,364 |
| ⚪ | PF_SUIUSD | -25.0% | $9,950,932 |
| ⚪ | PF_EIGENUSD | -22.1% | $613,663 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (coinbase → gemini) — coinbase: $85,849.72, kraken: $85,851.10, gemini: $85,853.57
- ⚪ **ETH** gap **0.011%** (coinbase → kraken) — coinbase: $2,704.24, kraken: $2,704.55, gemini: $2,704.50

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.37, realized vol 10d 14% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 12% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 33% (0.3x)
- ⚪ **ETH** 24h vol 11% vs 30d norm 43% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 2 | +72.1% | 111.2% |
| PF_NEARUSD | 1 | -256.0% | 256.0% |
| PF_TRUMPUSD | 1 | +99.1% | 99.1% |
| PF_WLDUSD | 1 | +34.0% | 47.6% |
| PF_XTZUSD | 1 | +33.5% | 33.5% |

**Resolved since last scan:** PF_ZROUSD (crowded 3d, worst 222%), PF_RUNEUSD (crowded 1d, worst 56%), PF_ASTERUSD (crowded 1d, worst 56%), PF_SYNUSD (crowded 1d, worst 35%), PF_TIAUSD (crowded 1d, worst 33%), PF_XRPUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
