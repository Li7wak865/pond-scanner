# Pond Scanner Report
**Scan time:** 2026-09-05 10:36 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BELUSD | +528.8% | $560,034 |
| 🟢 | PF_UNIUSD | +269.5% | $843,298 |
| 🟢 | PF_HFTUSD | +112.0% | $10,372,484 |
| 🟢 | PF_TRUMPUSD | -109.1% | $1,405,726 |
| 🟢 | PF_SPXUSD | -107.8% | $625,304 |
| 🟢 | PF_ACEUSD | -93.5% | $919,361 |
| 🟢 | PF_LDOUSD | -36.6% | $1,791,472 |
| 🟢 | PF_NEARUSD | +35.8% | $2,307,929 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → kraken) — coinbase: $79,607.00, kraken: $79,614.70, gemini: $79,613.63
- ⚪ **ETH** gap **0.004%** (coinbase → kraken) — coinbase: $2,454.75, kraken: $2,454.85, gemini: $2,454.78

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.53, realized vol 10d 41% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 42% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 46% vs 30d norm 40% (1.2x)
- ⚪ **ETH** 24h vol 57% vs 30d norm 54% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -93.5% | 304.8% |
| PF_HFTUSD | 2 | +112.0% | 113.6% |
| PF_TRUMPUSD | 2 | -109.1% | 196.2% |
| PF_SPXUSD | 2 | -107.8% | 209.6% |
| PF_BELUSD | 1 | +528.8% | 528.8% |
| PF_UNIUSD | 1 | +269.5% | 269.5% |
| PF_LDOUSD | 1 | -36.6% | 36.6% |
| PF_NEARUSD | 1 | +35.8% | 35.8% |

**Resolved since last scan:** PF_ICXUSD (crowded 1d, worst 64%), PF_BATUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
