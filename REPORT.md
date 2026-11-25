# Pond Scanner Report
**Scan time:** 2026-11-25 21:42 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +183.9% | $2,558,876 |
| 🟢 | PF_UNIUSD | +112.3% | $947,329 |
| 🟢 | PF_ACEUSD | +94.5% | $4,189,922 |
| ⚪ | PF_TRUMPUSD | -26.7% | $759,179 |
| ⚪ | PF_CFGUSD | -20.6% | $1,029,670 |
| ⚪ | PF_SPXUSD | +16.1% | $786,083 |
| ⚪ | PF_TRXUSD | -14.8% | $1,099,621 |
| ⚪ | PF_XRPUSD | +14.5% | $10,517,251 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.034%** (kraken → gemini) — coinbase: $60,226.80, kraken: $60,224.70, gemini: $60,245.00
- ⚪ **ETH** gap **0.040%** (kraken → gemini) — coinbase: $1,687.84, kraken: $1,687.66, gemini: $1,688.34

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #332 | $62.6M | 1.32x | +39.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.62, realized vol 10d 41% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.58, realized vol 10d 56% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9949 (-0.51% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **USDe** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 56% vs 30d norm 56% (1.0x)
- ⚪ **ETH** 24h vol 62% vs 30d norm 69% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +183.9% | 183.9% |
| PF_UNIUSD | 1 | +112.3% | 112.3% |
| PF_ACEUSD | 1 | +94.5% | 94.5% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 849%), PF_ZROUSD (crowded 2d, worst 55%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
