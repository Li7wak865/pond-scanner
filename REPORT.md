# Pond Scanner Report
**Scan time:** 2026-09-29 12:55 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AVAXUSD | +289.8% | $953,538 |
| 🟢 | PF_ETHFIUSD | -246.1% | $823,676 |
| 🟢 | PF_TRUMPUSD | +106.7% | $960,722 |
| 🟢 | PF_ZROUSD | -64.6% | $594,785 |
| 🟢 | PF_LINKUSD | +58.3% | $1,225,450 |
| 🟢 | PF_RUNEUSD | -54.7% | $1,026,770 |
| 🟢 | PF_SPXUSD | -49.0% | $621,313 |
| 🟢 | PF_NIGHTUSD | +44.2% | $6,406,223 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.057%** (gemini → coinbase) — coinbase: $84,330.55, kraken: $84,328.00, gemini: $84,282.60
- ⚪ **ETH** gap **0.005%** (coinbase → gemini) — coinbase: $2,735.65, gemini: $2,735.80

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
_Data source unavailable this run._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.27, realized vol 10d 43% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.31, realized vol 10d 35% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
_Data source unavailable this run._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 46% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ETHFIUSD | 4 | -246.1% | 246.1% |
| PF_LINKUSD | 4 | +58.3% | 600.3% |
| PF_UNIUSD | 4 | +41.8% | 493.4% |
| PF_TRUMPUSD | 2 | +106.7% | 135.9% |
| PF_ZROUSD | 2 | -64.6% | 141.3% |
| PF_AVAXUSD | 1 | +289.8% | 289.8% |
| PF_RUNEUSD | 1 | -54.7% | 54.7% |
| PF_SPXUSD | 1 | -49.0% | 109.2% |
| PF_NIGHTUSD | 1 | +44.2% | 44.2% |
| PF_ASTERUSD | 1 | +44.0% | 44.0% |
| PF_CROUSD | 1 | +32.1% | 32.1% |

**Resolved since last scan:** PF_GRASSUSD (crowded 2d, worst 101%), PF_CFGUSD (crowded 1d, worst 53%), PF_NEARUSD (crowded 4d, worst 286%), PF_FILUSD (crowded 2d, worst 73%), PF_TIAUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

## Data issues this run
- small: HTTPError: 403 Client Error: Forbidden for url: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&price_change_percentage=24h
- stables: HTTPError: 403 Client Error: Forbidden for url: https://api.coingecko.com/api/v3/simple/price?ids=tether%2Cusd-coin%2Cdai%2Cfirst-digital-usd%2Cethena-usde%2Cpaypal-usd&vs_currencies=usd

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
