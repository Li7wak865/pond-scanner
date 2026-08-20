# Pond Scanner Report
**Scan time:** 2026-08-20 01:52 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +322.6% | $1,622,326 |
| 🟢 | PF_NEARUSD | +151.8% | $2,303,827 |
| 🟢 | PF_GRASSUSD | +78.4% | $982,061 |
| 🟢 | PF_ETHFIUSD | -63.1% | $1,295,170 |
| 🟢 | PF_AVAXUSD | +55.1% | $698,561 |
| 🟢 | PF_ACEUSD | -55.0% | $17,584,429 |
| 🟢 | PF_RAREUSD | +54.6% | $959,462 |
| 🟢 | PF_ASTERUSD | -49.3% | $571,875 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (gemini → coinbase) — coinbase: $69,741.61, kraken: $69,738.50, gemini: $69,734.58
- ⚪ **ETH** gap **0.096%** (kraken → gemini) — coinbase: $2,267.40, kraken: $2,267.22, gemini: $2,269.39

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RE (RE) | #275 | $86.8M | 1.59x | +36.6% |
| Audiera (BEAT) | #425 | $49.6M | 0.67x | -34.6% |
| GoPlus Security (GPS) | #326 | $68.8M | 0.59x | -34.2% |
| Bio Protocol (BIO) | #371 | $60.6M | 0.58x | +15.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 43% vs 60d 33%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.66, realized vol 10d 99% vs 60d 57%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 83% vs 30d norm 29% (2.9x)
- 🟢 **ETH** 24h vol 160% vs 30d norm 45% (3.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 6 | -55.0% | 732.3% |
| PF_UNIUSD | 2 | +322.6% | 322.6% |
| PF_GRASSUSD | 2 | +78.4% | 78.4% |
| PF_ETHFIUSD | 2 | -63.1% | 154.5% |
| PF_NEARUSD | 1 | +151.8% | 151.8% |
| PF_AVAXUSD | 1 | +55.1% | 55.1% |
| PF_RAREUSD | 1 | +54.6% | 54.6% |
| PF_ASTERUSD | 1 | -49.3% | 49.3% |
| PF_DYMUSD | 1 | +37.8% | 37.8% |
| PF_TRUMPUSD | 1 | -35.2% | 35.2% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 112%), PF_VIRTUALUSD (crowded 2d, worst 63%), PF_BBUSD (crowded 2d, worst 50%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
