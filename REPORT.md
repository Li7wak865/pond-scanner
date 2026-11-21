# Pond Scanner Report
**Scan time:** 2026-11-21 07:10 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | -527.0% | $803,399 |
| 🟢 | PF_INJUSD | -445.8% | $592,416 |
| 🟢 | PF_UNIUSD | -218.0% | $610,346 |
| 🟢 | PF_ZROUSD | -107.2% | $633,346 |
| 🟢 | PF_RUNEUSD | -48.8% | $545,604 |
| 🟢 | PF_SPXUSD | -35.8% | $560,141 |
| ⚪ | PF_TRUMPUSD | -29.1% | $1,868,462 |
| ⚪ | PF_SUIUSD | -29.0% | $9,886,582 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.043%** (coinbase → kraken) — coinbase: $58,442.72, kraken: $58,467.60, gemini: $58,467.48
- ⚪ **ETH** gap **0.057%** (gemini → kraken) — coinbase: $1,638.19, kraken: $1,638.85, gemini: $1,637.92

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #265 | $83.3M | 2.48x | -22.9% |
| EVAA Protocol (EVAA) | #440 | $40.7M | 0.96x | +15.8% |
| DODO (DODO) | #492 | $35.2M | 0.51x | +15.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.63, realized vol 10d 45% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.53, realized vol 10d 69% vs 60d 50%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9948 (-0.52% vs peg)
- ⚪ **USDe** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 130% vs 30d norm 50% (2.6x)
- 🟢 **ETH** 24h vol 154% vs 30d norm 64% (2.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | -218.0% | 220.1% |
| PF_INJUSD | 2 | -445.8% | 445.8% |
| PF_ZROUSD | 2 | -107.2% | 107.2% |
| PF_RUNEUSD | 2 | -48.8% | 48.8% |
| PF_SPXUSD | 2 | -35.8% | 53.5% |
| PF_HYPEUSD | 1 | -527.0% | 527.0% |

**Resolved since last scan:** PF_SOLUSD (crowded 4d, worst 769%), PF_TRUMPUSD (crowded 3d, worst 41%), PF_NEARUSD (crowded 2d, worst 37%), PF_TRXUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
