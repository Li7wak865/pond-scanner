# Pond Scanner Report
**Scan time:** 2026-10-26 04:49 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| ⚪ | PF_SPXUSD | -29.0% | $536,324 |
| ⚪ | PF_TIAUSD | -25.1% | $871,948 |
| ⚪ | PF_FILUSD | +24.9% | $704,241 |
| ⚪ | PF_PONSUSD | +23.2% | $1,035,439 |
| ⚪ | PF_NEARUSD | +23.1% | $4,170,691 |
| ⚪ | PF_XRPUSD | +18.8% | $8,368,723 |
| ⚪ | PF_GRASSUSD | -16.7% | $1,097,702 |
| ⚪ | PF_ARCUSD | -9.5% | $2,530,264 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (kraken → gemini) — coinbase: $79,850.94, kraken: $79,849.40, gemini: $79,868.82
- ⚪ **ETH** gap **0.022%** (kraken → coinbase) — coinbase: $2,312.13, kraken: $2,311.62, gemini: $2,311.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #340 | $71.4M | 2.32x | -23.3% |
| Threshold Network (T) | #411 | $55.4M | 2.09x | -20.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.30, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
No perps currently crowded. ⚪

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
