# Pond Scanner Report
**Scan time:** 2026-08-04 14:39 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ARCUSD | +237.7% | $629,206 |
| 🟢 | PF_KAITOUSD | +116.7% | $1,061,808 |
| 🟢 | PF_SUSD | +99.1% | $595,818 |
| 🟢 | PF_SYNUSD | -60.9% | $1,497,565 |
| 🟢 | PF_COTIUSD | -48.4% | $21,343,339 |
| 🟢 | PF_ETHFIUSD | +31.2% | $958,492 |
| ⚪ | PF_ZEREBROUSD | +23.1% | $2,889,179 |
| ⚪ | PF_JTOUSD | +20.4% | $772,351 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (kraken → gemini) — coinbase: $63,926.04, kraken: $63,923.70, gemini: $63,935.50
- ⚪ **ETH** gap **0.029%** (kraken → coinbase) — coinbase: $1,869.43, kraken: $1,868.89, gemini: $1,869.35

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| HOME (HOME) | #438 | $46.8M | 3.15x | +76.3% |
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #327 | $68.2M | 1.13x | +19.7% |
| SkyAI (SKYAI) | #399 | $53.8M | 0.85x | +43.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 28% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 42% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 32% (0.8x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | +116.7% | 135.4% |
| PF_ARCUSD | 1 | +237.7% | 237.7% |
| PF_SUSD | 1 | +99.1% | 99.1% |
| PF_SYNUSD | 1 | -60.9% | 69.5% |
| PF_COTIUSD | 1 | -48.4% | 62.8% |
| PF_ETHFIUSD | 1 | +31.2% | 31.2% |

**Resolved since last scan:** PF_ZEREBROUSD (crowded 1d, worst 48%), PF_NEARUSD (crowded 1d, worst 43%), PF_ATOMUSD (crowded 1d, worst 38%), PF_ONDOUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
