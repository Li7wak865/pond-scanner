# Pond Scanner Report
**Scan time:** 2026-08-19 01:53 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -183.0% | $17,494,329 |
| 🟢 | PF_NEARUSD | -73.2% | $1,727,836 |
| 🟢 | PF_RAREUSD | +53.2% | $1,840,277 |
| ⚪ | PF_VIRTUALUSD | +19.2% | $815,286 |
| ⚪ | PF_ALICEUSD | -17.9% | $3,829,470 |
| ⚪ | PF_FILUSD | -15.8% | $1,167,231 |
| ⚪ | PF_ETHFIUSD | -13.5% | $663,071 |
| ⚪ | PF_SYNUSD | -13.3% | $704,420 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (kraken → gemini) — coinbase: $64,385.40, kraken: $64,376.50, gemini: $64,387.16
- ⚪ **ETH** gap **0.011%** (kraken → coinbase) — coinbase: $1,913.72, kraken: $1,913.51, gemini: $1,913.65

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 牛来 (Niu Lai) (牛来) | #462 | $42.5M | 1.28x | +22.6% |
| GALA (GALA) | #327 | $68.0M | 0.61x | -15.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 19% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 18% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 26% (0.8x)
- ⚪ **ETH** 24h vol 23% vs 30d norm 35% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -183.0% | 732.3% |
| PF_NEARUSD | 2 | -73.2% | 73.2% |
| PF_RAREUSD | 2 | +53.2% | 53.2% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 2d, worst 136%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
