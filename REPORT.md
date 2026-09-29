# Pond Scanner Report
**Scan time:** 2026-09-29 22:16 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -804.0% | $687,557 |
| 🟢 | PF_2ZUSD | +285.5% | $2,546,279 |
| 🟢 | PF_UNIUSD | -215.8% | $621,612 |
| 🟢 | PF_AVAXUSD | +206.8% | $1,026,040 |
| 🟢 | PF_LINKUSD | +96.9% | $745,899 |
| 🟢 | PF_SPXUSD | -89.5% | $729,881 |
| 🟢 | PF_RAREUSD | +78.4% | $773,877 |
| 🟢 | PF_TRUMPUSD | +75.1% | $879,364 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → kraken) — coinbase: $83,539.58, kraken: $83,550.40, gemini: $83,548.04
- ⚪ **ETH** gap **0.024%** (kraken → gemini) — coinbase: $2,679.04, kraken: $2,678.91, gemini: $2,679.56

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
_Data source unavailable this run._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 43% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 34% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
_Data source unavailable this run._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 34% (0.9x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 46% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | -215.8% | 493.4% |
| PF_LINKUSD | 4 | +96.9% | 600.3% |
| PF_ETHFIUSD | 4 | -42.9% | 246.1% |
| PF_TRUMPUSD | 2 | +75.1% | 135.9% |
| PF_SOLUSD | 1 | -804.0% | 804.0% |
| PF_2ZUSD | 1 | +285.5% | 285.5% |
| PF_AVAXUSD | 1 | +206.8% | 289.8% |
| PF_SPXUSD | 1 | -89.5% | 109.2% |
| PF_RAREUSD | 1 | +78.4% | 78.4% |
| PF_RUNEUSD | 1 | +44.9% | 54.7% |
| PF_VETUSD | 1 | +38.6% | 38.6% |
| PF_SYRUPUSD | 1 | +35.6% | 35.6% |
| PF_SWARMSUSD | 1 | -35.4% | 35.4% |
| PF_SOONUSD | 1 | +33.3% | 33.3% |
| PF_VIRTUALUSD | 1 | -32.9% | 32.9% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 141%), PF_NIGHTUSD (crowded 1d, worst 44%), PF_ASTERUSD (crowded 1d, worst 44%), PF_CROUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

## Data issues this run
- small: HTTPError: 403 Client Error: Forbidden for url: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&price_change_percentage=24h
- stables: HTTPError: 403 Client Error: Forbidden for url: https://api.coingecko.com/api/v3/simple/price?ids=tether%2Cusd-coin%2Cdai%2Cfirst-digital-usd%2Cethena-usde%2Cpaypal-usd&vs_currencies=usd

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
