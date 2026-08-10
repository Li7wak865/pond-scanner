# Pond Scanner Report
**Scan time:** 2026-08-10 13:45 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AXSUSD | +36.4% | $555,259 |
| 🟢 | PF_UNIUSD | -34.1% | $537,635 |
| 🟢 | PF_MONUSD | +32.6% | $10,845,071 |
| ⚪ | PF_SYNUSD | -28.1% | $558,053 |
| ⚪ | PF_HFTUSD | -25.1% | $3,110,283 |
| ⚪ | PF_CATIUSD | +19.5% | $4,049,138 |
| ⚪ | PF_BICOUSD | +17.9% | $113,190,412 |
| ⚪ | PF_POPCATUSD | +15.0% | $884,270 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (gemini → coinbase) — coinbase: $64,615.25, kraken: $64,600.00, gemini: $64,595.92
- ⚪ **ETH** gap **0.053%** (kraken → coinbase) — coinbase: $1,901.01, kraken: $1,900.00, gemini: $1,900.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #262 | $94.7M | 2.22x | -31.2% |
| Cap (CAP) | #335 | $69.9M | 1.13x | +15.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 11% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.06, realized vol 10d 21% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 28% (0.6x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 40% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AXSUSD | 1 | +36.4% | 36.4% |
| PF_UNIUSD | 1 | -34.1% | 50.1% |
| PF_MONUSD | 1 | +32.6% | 32.6% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 949%), PF_HFTUSD (crowded 1d, worst 170%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
