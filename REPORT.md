# Pond Scanner Report
**Scan time:** 2026-11-08 22:06 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -138.7% | $1,504,679 |
| 🟢 | PF_NEARUSD | -110.2% | $2,685,289 |
| 🟢 | PF_UNIUSD | -95.7% | $514,171 |
| ⚪ | PF_SUSHIUSD | -26.6% | $569,135 |
| ⚪ | PF_XRPUSD | +16.5% | $21,679,071 |
| ⚪ | PF_TIAUSD | +14.7% | $731,697 |
| ⚪ | PF_DOTUSD | -13.8% | $1,738,599 |
| ⚪ | PF_MELANIAUSD | -12.6% | $978,139 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.128%** (gemini → kraken) — coinbase: $73,977.00, kraken: $74,022.20, gemini: $73,927.74
- ⚪ **ETH** gap **0.139%** (gemini → kraken) — coinbase: $2,104.92, kraken: $2,105.37, gemini: $2,102.45

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Holo (HOT) | #332 | $71.5M | 0.52x | +15.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 46% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.33, realized vol 10d 72% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9968 (-0.32% vs peg)
- ⚪ **USDe** $0.9990 (-0.10% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 40% vs 30d norm 34% (1.2x)
- ⚪ **ETH** 24h vol 86% vs 30d norm 49% (1.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -138.7% | 178.3% |
| PF_NEARUSD | 2 | -110.2% | 198.4% |
| PF_UNIUSD | 1 | -95.7% | 202.8% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
