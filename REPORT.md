# Pond Scanner Report
**Scan time:** 2026-07-24 16:46 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALCHUSD | -127.9% | $736,414 |
| 🟢 | PF_LRCUSD | +52.6% | $854,331 |
| 🟢 | PF_UNIUSD | -50.9% | $1,023,364 |
| 🟢 | PF_ACEUSD | -40.1% | $1,484,661 |
| 🟢 | PF_STXUSD | -33.6% | $1,173,734 |
| 🟢 | PF_SYNUSD | +32.5% | $3,936,003 |
| ⚪ | PF_SUIUSD | +21.1% | $7,336,551 |
| ⚪ | PF_EIGENUSD | -17.5% | $724,669 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (kraken → gemini) — coinbase: $63,901.43, kraken: $63,896.90, gemini: $63,909.04
- ⚪ **ETH** gap **0.032%** (gemini → coinbase) — coinbase: $1,855.92, kraken: $1,855.38, gemini: $1,855.32

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #361 | $63.3M | 4.67x | +24.5% |
| RE (RE) | #264 | $98.3M | 1.45x | +24.2% |
| Cap (CAP) | #472 | $43.2M | 0.54x | +23.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 23% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 31% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 41% (0.7x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 53% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALCHUSD | 1 | -127.9% | 127.9% |
| PF_LRCUSD | 1 | +52.6% | 52.6% |
| PF_UNIUSD | 1 | -50.9% | 50.9% |
| PF_ACEUSD | 1 | -40.1% | 40.1% |
| PF_STXUSD | 1 | -33.6% | 33.6% |
| PF_SYNUSD | 1 | +32.5% | 32.5% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
