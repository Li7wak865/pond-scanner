# Pond Scanner Report
**Scan time:** 2026-10-17 04:28 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +126.0% | $663,125 |
| 🟢 | PF_SOLUSD | +108.6% | $600,286 |
| 🟢 | PF_TRUMPUSD | -63.6% | $547,851 |
| 🟢 | PF_SUIUSD | +41.8% | $4,684,707 |
| 🟢 | PF_XRPUSD | +35.2% | $11,567,721 |
| 🟢 | PF_PONSUSD | +30.5% | $1,571,067 |
| ⚪ | PF_FILUSD | +29.2% | $1,682,213 |
| ⚪ | PF_CRVUSD | +22.6% | $3,558,872 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $81,416.81, kraken: $81,419.60, gemini: $81,423.31
- ⚪ **ETH** gap **0.021%** (coinbase → gemini) — coinbase: $2,423.75, kraken: $2,424.06, gemini: $2,424.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Impossible Cloud Network Token (ICNT) | #434 | $52.7M | 0.85x | +56.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 26% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.37, realized vol 10d 39% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 34% (0.8x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +126.0% | 219.7% |
| PF_PONSUSD | 2 | +30.5% | 37.9% |
| PF_SOLUSD | 1 | +108.6% | 108.6% |
| PF_TRUMPUSD | 1 | -63.6% | 63.6% |
| PF_SUIUSD | 1 | +41.8% | 41.8% |
| PF_XRPUSD | 1 | +35.2% | 35.2% |

**Resolved since last scan:** PF_INJUSD (crowded 2d, worst 608%), PF_ACEUSD (crowded 2d, worst 79%), PF_NEARUSD (crowded 2d, worst 74%), PF_TIAUSD (crowded 2d, worst 55%), PF_GRASSUSD (crowded 2d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
