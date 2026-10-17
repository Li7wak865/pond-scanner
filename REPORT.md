# Pond Scanner Report
**Scan time:** 2026-10-17 15:36 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SANDUSD | -45.9% | $16,650,013 |
| 🟢 | PF_NEARUSD | +30.5% | $3,789,079 |
| 🟢 | PF_FILUSD | -30.2% | $1,299,423 |
| ⚪ | PF_WLDUSD | -23.6% | $6,218,744 |
| ⚪ | PF_TRXUSD | -19.2% | $7,757,675 |
| ⚪ | PF_FETUSD | -14.2% | $8,870,620 |
| ⚪ | PF_ACEUSD | -12.0% | $1,379,269 |
| ⚪ | PF_PONSUSD | -11.2% | $1,407,128 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → kraken) — coinbase: $81,378.00, kraken: $81,392.70, gemini: $81,387.09
- ⚪ **ETH** gap **0.070%** (gemini → kraken) — coinbase: $2,412.11, kraken: $2,413.17, gemini: $2,411.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Impossible Cloud Network Token (ICNT) | #463 | $48.7M | 0.80x | +19.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 26% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 39% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 34% (0.4x)
- ⚪ **ETH** 24h vol 23% vs 30d norm 42% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SANDUSD | 1 | -45.9% | 45.9% |
| PF_NEARUSD | 1 | +30.5% | 135.7% |
| PF_FILUSD | 1 | -30.2% | 30.2% |

**Resolved since last scan:** PF_TIAUSD (crowded 1d, worst 70%), PF_ZROUSD (crowded 2d, worst 220%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
