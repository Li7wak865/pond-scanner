# Pond Scanner Report
**Scan time:** 2026-10-16 21:10 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | +410.6% | $506,868 |
| 🟢 | PF_ZROUSD | +99.2% | $586,722 |
| 🟢 | PF_ACEUSD | +79.2% | $1,853,128 |
| 🟢 | PF_NEARUSD | +73.9% | $4,187,623 |
| 🟢 | PF_TIAUSD | +55.2% | $6,703,476 |
| 🟢 | PF_GRASSUSD | +41.7% | $542,083 |
| 🟢 | PF_PONSUSD | +37.9% | $1,542,883 |
| ⚪ | PF_XRPUSD | +24.6% | $13,499,222 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → kraken) — coinbase: $81,563.27, kraken: $81,574.00, gemini: $81,573.01
- ⚪ **ETH** gap **0.008%** (gemini → coinbase) — coinbase: $2,412.90, kraken: $2,412.81, gemini: $2,412.70

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Zilliqa (ZIL) | #462 | $49.5M | 0.73x | -23.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 29% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 45% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 35% (0.8x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_INJUSD | 1 | +410.6% | 608.4% |
| PF_ZROUSD | 1 | +99.2% | 219.7% |
| PF_ACEUSD | 1 | +79.2% | 79.2% |
| PF_NEARUSD | 1 | +73.9% | 73.9% |
| PF_TIAUSD | 1 | +55.2% | 55.2% |
| PF_GRASSUSD | 1 | +41.7% | 41.7% |
| PF_PONSUSD | 1 | +37.9% | 37.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 760%), PF_TRUMPUSD (crowded 1d, worst 64%), PF_FILUSD (crowded 1d, worst 51%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
