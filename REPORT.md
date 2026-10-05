# Pond Scanner Report
**Scan time:** 2026-10-05 05:42 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RUNEUSD | -84.2% | $1,080,527 |
| 🟢 | PF_TRUMPUSD | -71.2% | $919,813 |
| 🟢 | PF_NEARUSD | -56.4% | $2,726,711 |
| 🟢 | PF_PONSUSD | +51.2% | $686,811 |
| 🟢 | PF_ACEUSD | +44.4% | $1,012,657 |
| 🟢 | PF_ZROUSD | -33.7% | $680,325 |
| 🟢 | PF_TRXUSD | -30.6% | $844,244 |
| ⚪ | PF_EIGENUSD | -29.7% | $525,808 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.062%** (kraken → gemini) — coinbase: $85,631.00, kraken: $85,628.00, gemini: $85,680.73
- ⚪ **ETH** gap **0.011%** (gemini → kraken) — coinbase: $2,700.06, kraken: $2,700.11, gemini: $2,699.80

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #349 | $77.3M | 0.95x | +18.2% |
| Nillion (NIL) | #464 | $54.1M | 0.80x | +26.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 18% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 15% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 33% (0.7x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 43% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 3 | +51.2% | 111.2% |
| PF_TRUMPUSD | 2 | -71.2% | 99.1% |
| PF_NEARUSD | 2 | -56.4% | 255.9% |
| PF_RUNEUSD | 1 | -84.2% | 84.2% |
| PF_ACEUSD | 1 | +44.4% | 44.4% |
| PF_ZROUSD | 1 | -33.7% | 33.7% |
| PF_TRXUSD | 1 | -30.6% | 30.6% |

**Resolved since last scan:** PF_WLDUSD (crowded 2d, worst 48%), PF_XTZUSD (crowded 2d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
