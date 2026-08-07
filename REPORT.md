# Pond Scanner Report
**Scan time:** 2026-08-07 13:40 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -501.6% | $22,734,517 |
| 🟢 | PF_HFTUSD | -148.9% | $197,332,929 |
| 🟢 | PF_AIXBTUSD | +76.9% | $631,991 |
| 🟢 | PF_KAITOUSD | +55.0% | $504,793 |
| 🟢 | PF_NEARUSD | -54.7% | $2,263,470 |
| ⚪ | PF_BICOUSD | -26.1% | $50,049,343 |
| ⚪ | PF_ZBTUSD | -20.7% | $3,653,018 |
| ⚪ | PF_SYNUSD | +11.9% | $2,540,492 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.042%** (kraken → gemini) — coinbase: $65,267.12, kraken: $65,247.20, gemini: $65,274.59
- ⚪ **ETH** gap **0.078%** (kraken → coinbase) — coinbase: $1,933.24, kraken: $1,931.73, gemini: $1,932.68

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #554 | $50.1M | 5.99x | +57.9% |
| Cap (CAP) | #391 | $55.0M | 0.78x | +16.9% |
| Allora (ALLO) | #289 | $82.3M | 0.74x | +26.3% |
| Espresso (ESP) | #448 | $47.3M | 0.71x | +24.2% |
| SkyAI (SKYAI) | #245 | $108.5M | 0.62x | +33.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 24% vs 60d 31%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 29% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 29% (0.7x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 41% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 1 | -501.6% | 501.6% |
| PF_HFTUSD | 1 | -148.9% | 148.9% |
| PF_AIXBTUSD | 1 | +76.9% | 76.9% |
| PF_KAITOUSD | 1 | +55.0% | 124.5% |
| PF_NEARUSD | 1 | -54.7% | 54.7% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
