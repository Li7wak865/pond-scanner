# Pond Scanner Report
**Scan time:** 2026-09-20 11:26 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +200.5% | $584,890 |
| 🟢 | PF_INJUSD | -136.7% | $887,360 |
| 🟢 | PF_UNIUSD | +113.0% | $818,698 |
| 🟢 | PF_AVAXUSD | -108.8% | $2,123,882 |
| 🟢 | PF_HFTUSD | -88.9% | $943,692 |
| 🟢 | PF_MINAUSD | -53.6% | $553,504 |
| 🟢 | PF_CATIUSD | +48.3% | $795,151 |
| 🟢 | PF_JTOUSD | +37.2% | $1,109,176 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (coinbase → gemini) — coinbase: $80,316.15, kraken: $80,322.70, gemini: $80,333.89
- ⚪ **ETH** gap **0.025%** (coinbase → gemini) — coinbase: $2,570.80, kraken: $2,570.99, gemini: $2,571.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #462 | $50.5M | 7.21x | -19.9% |
| Harmony (ONE) | #392 | $65.4M | 3.40x | +76.8% |
| Cap (CAP) | #368 | $71.1M | 1.08x | -23.5% |
| COTI (COTI) | #446 | $52.8M | 0.90x | -16.3% |
| Zilliqa (ZIL) | #366 | $71.6M | 0.68x | +15.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 43% vs 60d 41%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.11, realized vol 10d 57% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 35% (0.7x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 50% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +113.0% | 624.1% |
| PF_HFTUSD | 3 | -88.9% | 107.0% |
| PF_AVAXUSD | 2 | -108.8% | 168.4% |
| PF_MINAUSD | 2 | -53.6% | 73.3% |
| PF_SOLUSD | 1 | +200.5% | 200.5% |
| PF_INJUSD | 1 | -136.7% | 423.0% |
| PF_CATIUSD | 1 | +48.3% | 48.3% |
| PF_JTOUSD | 1 | +37.2% | 37.2% |
| PF_WLDUSD | 1 | -35.5% | 35.5% |
| PF_NIGHTUSD | 1 | +33.7% | 33.7% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 196%), PF_NEARUSD (crowded 1d, worst 159%), PF_DOTUSD (crowded 2d, worst 47%), PF_FILUSD (crowded 1d, worst 38%), PF_JUPUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
