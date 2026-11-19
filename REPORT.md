# Pond Scanner Report
**Scan time:** 2026-11-19 20:38 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -582.5% | $558,380 |
| 🟢 | PF_ZROUSD | -162.1% | $1,177,906 |
| 🟢 | PF_UNIUSD | -123.7% | $637,522 |
| 🟢 | PF_TRUMPUSD | -38.8% | $735,426 |
| 🟢 | PF_NEARUSD | -35.8% | $3,605,183 |
| ⚪ | PF_CFGUSD | -19.7% | $1,199,810 |
| ⚪ | PF_DOTUSD | -19.2% | $1,749,030 |
| ⚪ | PF_JUPUSD | -14.5% | $713,912 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (gemini → kraken) — coinbase: $61,976.37, kraken: $61,978.80, gemini: $61,965.73
- ⚪ **ETH** gap **0.038%** (coinbase → gemini) — coinbase: $1,757.74, kraken: $1,758.12, gemini: $1,758.41

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #428 | $44.8M | 3.13x | +29.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.53, realized vol 10d 43% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 58% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9951 (-0.49% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 43% (1.1x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 58% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 6 | -35.8% | 245.2% |
| PF_UNIUSD | 3 | -123.7% | 175.8% |
| PF_SOLUSD | 2 | -582.5% | 768.6% |
| PF_ZROUSD | 1 | -162.1% | 162.1% |
| PF_TRUMPUSD | 1 | -38.8% | 38.8% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
