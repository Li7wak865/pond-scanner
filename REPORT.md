# Pond Scanner Report
**Scan time:** 2026-11-26 21:33 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -248.8% | $1,221,326 |
| 🟢 | PF_NEARUSD | +48.4% | $2,244,324 |
| 🟢 | PF_RUNEUSD | -45.5% | $822,052 |
| 🟢 | PF_UNIUSD | -33.6% | $600,665 |
| ⚪ | PF_CRVUSD | +18.3% | $11,250,815 |
| ⚪ | PF_FILUSD | +13.3% | $1,119,093 |
| ⚪ | PF_XRPUSD | +13.1% | $10,629,380 |
| ⚪ | PF_MELANIAUSD | -9.3% | $563,228 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (gemini → coinbase) — coinbase: $60,870.64, kraken: $60,870.30, gemini: $60,868.38
- ⚪ **ETH** gap **0.076%** (gemini → kraken) — coinbase: $1,706.21, kraken: $1,706.53, gemini: $1,705.24

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #455 | $41.1M | 2.02x | -33.8% |
| SSV Network (SSV) | #442 | $42.3M | 1.00x | +25.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 42% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.55, realized vol 10d 57% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9950 (-0.50% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 56% (0.5x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 69% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 2 | -248.8% | 248.8% |
| PF_UNIUSD | 2 | -33.6% | 112.3% |
| PF_NEARUSD | 1 | +48.4% | 48.4% |
| PF_RUNEUSD | 1 | -45.5% | 46.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 91%), PF_ATOMUSD (crowded 1d, worst 48%), PF_TRUMPUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
