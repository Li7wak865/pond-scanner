# Pond Scanner Report
**Scan time:** 2026-09-06 20:25 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +476.2% | $1,756,871 |
| 🟢 | PF_UNIUSD | +383.9% | $1,285,858 |
| 🟢 | PF_RAYUSD | -252.1% | $770,340 |
| 🟢 | PF_COTIUSD | +229.4% | $8,242,653 |
| 🟢 | PF_MINAUSD | +198.6% | $725,913 |
| 🟢 | PF_NEARUSD | +153.7% | $2,020,613 |
| 🟢 | PF_HFTUSD | +114.6% | $4,184,982 |
| 🟢 | PF_ACEUSD | -98.0% | $536,112 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $79,926.27, kraken: $79,932.90, gemini: $79,936.61
- ⚪ **ETH** gap **0.025%** (kraken → coinbase) — coinbase: $2,495.87, kraken: $2,495.25, gemini: $2,495.40

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| A Meme Coin (AMC) | #262 | $109.7M | 1.51x | +303.7% |
| 哈基米 (Hajimi) (哈基米) | #414 | $57.5M | 0.87x | +220.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 40% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 42% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 40% (0.4x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 53% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +476.2% | 476.2% |
| PF_UNIUSD | 2 | +383.9% | 387.6% |
| PF_NEARUSD | 2 | +153.7% | 163.9% |
| PF_RAYUSD | 1 | -252.1% | 252.1% |
| PF_COTIUSD | 1 | +229.4% | 229.4% |
| PF_MINAUSD | 1 | +198.6% | 198.6% |
| PF_HFTUSD | 1 | +114.6% | 114.6% |
| PF_ACEUSD | 1 | -98.0% | 133.5% |
| PF_ICXUSD | 1 | -36.0% | 36.0% |
| PF_JUPUSD | 1 | +34.6% | 34.6% |

**Resolved since last scan:** PF_LINKUSD (crowded 1d, worst 561%), PF_SOLUSD (crowded 1d, worst 328%), PF_IOTAUSD (crowded 1d, worst 117%), PF_DOTUSD (crowded 1d, worst 91%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
