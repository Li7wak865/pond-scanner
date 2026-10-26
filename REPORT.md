# Pond Scanner Report
**Scan time:** 2026-10-26 13:05 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_GRASSUSD | +68.4% | $908,685 |
| 🟢 | PF_FILUSD | +31.0% | $1,189,571 |
| ⚪ | PF_SUIUSD | +25.1% | $4,512,822 |
| ⚪ | PF_PONSUSD | +22.0% | $1,316,879 |
| ⚪ | PF_TIAUSD | +14.3% | $1,144,177 |
| ⚪ | PF_WLDUSD | +11.7% | $3,900,677 |
| ⚪ | PF_XRPUSD | +9.6% | $8,023,615 |
| ⚪ | PF_SPXUSD | +8.9% | $529,158 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → coinbase) — coinbase: $80,104.88, kraken: $80,092.10, gemini: $80,102.09
- ⚪ **ETH** gap **0.058%** (gemini → coinbase) — coinbase: $2,316.36, kraken: $2,315.56, gemini: $2,315.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #419 | $53.2M | 0.77x | -18.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.29, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 31% (0.8x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_GRASSUSD | 1 | +68.4% | 68.4% |
| PF_FILUSD | 1 | +31.0% | 31.0% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
