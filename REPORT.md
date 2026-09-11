# Pond Scanner Report
**Scan time:** 2026-09-11 20:59 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +329.7% | $856,620 |
| 🟢 | PF_RAYUSD | +167.8% | $1,472,433 |
| 🟢 | PF_NEARUSD | -109.4% | $2,833,692 |
| 🟢 | PF_TRUMPUSD | -108.6% | $984,893 |
| 🟢 | PF_LSKUSD | -76.4% | $926,570 |
| 🟢 | PF_HFTUSD | +72.2% | $552,924 |
| 🟢 | PF_RUNEUSD | -43.0% | $548,909 |
| 🟢 | PF_ASTERUSD | +40.9% | $760,373 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $77,310.13, kraken: $77,315.40, gemini: $77,321.14
- ⚪ **ETH** gap **0.055%** (gemini → coinbase) — coinbase: $2,529.50, kraken: $2,529.00, gemini: $2,528.10

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| LAB (LAB) | #412 | $57.5M | 0.56x | +62.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 38% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 41% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 53% vs 30d norm 41% (1.3x)
- ⚪ **ETH** 24h vol 113% vs 30d norm 58% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +329.7% | 329.7% |
| PF_RAYUSD | 1 | +167.8% | 260.9% |
| PF_NEARUSD | 1 | -109.4% | 116.1% |
| PF_TRUMPUSD | 1 | -108.6% | 108.6% |
| PF_LSKUSD | 1 | -76.4% | 76.4% |
| PF_HFTUSD | 1 | +72.2% | 106.8% |
| PF_RUNEUSD | 1 | -43.0% | 67.4% |
| PF_ASTERUSD | 1 | +40.9% | 40.9% |

**Resolved since last scan:** PF_UNIUSD (crowded 3d, worst 362%), PF_ATOMUSD (crowded 2d, worst 123%), PF_ETHFIUSD (crowded 1d, worst 42%), PF_CROUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
