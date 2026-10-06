# Pond Scanner Report
**Scan time:** 2026-10-06 18:23 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +299.0% | $759,917 |
| 🟢 | PF_AVAXUSD | -84.6% | $597,660 |
| 🟢 | PF_SPXUSD | +67.1% | $624,386 |
| 🟢 | PF_PONSUSD | +53.4% | $731,492 |
| 🟢 | PF_FILUSD | -46.1% | $1,397,575 |
| 🟢 | PF_ETHFIUSD | -45.5% | $1,757,760 |
| 🟢 | PF_SUIUSD | -44.5% | $6,891,156 |
| 🟢 | PF_NEARUSD | -39.0% | $3,315,621 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $85,645.91, kraken: $85,646.70, gemini: $85,657.77
- ⚪ **ETH** gap **0.023%** (coinbase → gemini) — coinbase: $2,696.40, kraken: $2,696.58, gemini: $2,697.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Numeraire (NMR) | #274 | $111.1M | 1.50x | +29.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.50, realized vol 10d 18% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 15% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 23% vs 30d norm 43% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 4 | +53.4% | 111.2% |
| PF_UNIUSD | 2 | +299.0% | 299.0% |
| PF_AVAXUSD | 1 | -84.6% | 84.6% |
| PF_SPXUSD | 1 | +67.1% | 76.2% |
| PF_FILUSD | 1 | -46.1% | 59.5% |
| PF_ETHFIUSD | 1 | -45.5% | 45.5% |
| PF_SUIUSD | 1 | -44.5% | 44.5% |
| PF_NEARUSD | 1 | -39.0% | 178.3% |
| PF_XRPUSD | 1 | -36.3% | 36.3% |
| PF_GRASSUSD | 1 | -35.8% | 35.8% |
| PF_ASTERUSD | 1 | -35.2% | 35.2% |
| PF_CROUSD | 1 | +34.9% | 34.9% |
| PF_ZROUSD | 1 | +31.7% | 80.1% |
| PF_DOTUSD | 1 | -30.8% | 61.0% |

**Resolved since last scan:** PF_MOVRUSD (crowded 2d, worst 542%), PF_LINKUSD (crowded 1d, worst 244%), PF_RUNEUSD (crowded 2d, worst 99%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
