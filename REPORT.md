# Pond Scanner Report
**Scan time:** 2026-09-05 04:31 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SPXUSD | -119.5% | $782,676 |
| 🟢 | PF_HFTUSD | +113.6% | $10,470,858 |
| 🟢 | PF_ACEUSD | -90.8% | $910,924 |
| 🟢 | PF_TRUMPUSD | +71.3% | $1,162,058 |
| 🟢 | PF_ICXUSD | -63.5% | $1,851,896 |
| 🟢 | PF_BATUSD | +35.9% | $1,324,323 |
| ⚪ | PF_LDOUSD | +22.2% | $1,540,799 |
| ⚪ | PF_CRVUSD | +22.0% | $3,774,161 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $79,561.17, kraken: $79,566.90, gemini: $79,567.82
- ⚪ **ETH** gap **0.011%** (coinbase → gemini) — coinbase: $2,452.37, kraken: $2,452.42, gemini: $2,452.65

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 41% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 42% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 48% vs 30d norm 40% (1.2x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 54% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -90.8% | 304.8% |
| PF_SPXUSD | 2 | -119.5% | 209.6% |
| PF_HFTUSD | 2 | +113.6% | 113.6% |
| PF_TRUMPUSD | 2 | +71.3% | 196.2% |
| PF_ICXUSD | 1 | -63.5% | 63.5% |
| PF_BATUSD | 1 | +35.9% | 35.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 126%), PF_CRVUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
