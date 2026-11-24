# Pond Scanner Report
**Scan time:** 2026-11-24 09:55 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -727.7% | $810,169 |
| 🟢 | PF_HYPEUSD | -360.8% | $717,710 |
| 🟢 | PF_UNIUSD | -122.1% | $1,187,527 |
| 🟢 | PF_RENDERUSD | -86.3% | $516,226 |
| 🟢 | PF_ACEUSD | +78.3% | $9,951,337 |
| 🟢 | PF_INJUSD | +67.4% | $948,453 |
| 🟢 | PF_ZROUSD | -55.3% | $560,907 |
| 🟢 | PF_TRUMPUSD | -50.3% | $1,281,839 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $59,839.11, kraken: $59,843.70, gemini: $59,850.57
- 🟢 **ETH** gap **0.312%** (coinbase → gemini) — coinbase: $1,680.00, kraken: $1,680.21, gemini: $1,685.24

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lista DAO (LISTA) | #434 | $43.0M | 0.94x | +20.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.70, realized vol 10d 42% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.67, realized vol 10d 62% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9951 (-0.49% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 96% vs 30d norm 55% (1.8x)
- ⚪ **ETH** 24h vol 115% vs 30d norm 68% (1.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 8 | -122.1% | 222.0% |
| PF_ACEUSD | 3 | +78.3% | 786.5% |
| PF_HYPEUSD | 2 | -360.8% | 360.8% |
| PF_RENDERUSD | 2 | -86.3% | 86.3% |
| PF_INJUSD | 2 | +67.4% | 204.4% |
| PF_SOLUSD | 1 | -727.7% | 727.7% |
| PF_ZROUSD | 1 | -55.3% | 55.3% |
| PF_TRUMPUSD | 1 | -50.3% | 50.3% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 49%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
