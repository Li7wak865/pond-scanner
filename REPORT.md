# Pond Scanner Report
**Scan time:** 2026-07-28 14:38 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -755.4% | $1,161,679 |
| 🟢 | PF_SOLUSD | -616.4% | $555,865 |
| 🟢 | PF_UNIUSD | +89.0% | $867,725 |
| 🟢 | PF_KAITOUSD | +84.0% | $891,642 |
| 🟢 | PF_SOONUSD | -69.2% | $1,776,325 |
| 🟢 | PF_RUNEUSD | -63.1% | $548,439 |
| 🟢 | PF_LRCUSD | +47.1% | $647,225 |
| 🟢 | PF_SYNUSD | +39.5% | $3,816,301 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (kraken → gemini) — coinbase: $63,232.55, kraken: $63,232.20, gemini: $63,241.21
- ⚪ **ETH** gap **0.004%** (kraken → gemini) — coinbase: $1,883.38, kraken: $1,883.32, gemini: $1,883.39

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #342 | $62.2M | 1.07x | -26.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 59% vs 30d norm 45% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | +84.0% | 510.3% |
| PF_SYNUSD | 2 | +39.5% | 69.7% |
| PF_DEXEUSD | 1 | -755.4% | 755.4% |
| PF_SOLUSD | 1 | -616.4% | 730.1% |
| PF_UNIUSD | 1 | +89.0% | 89.0% |
| PF_SOONUSD | 1 | -69.2% | 69.2% |
| PF_RUNEUSD | 1 | -63.1% | 63.1% |
| PF_LRCUSD | 1 | +47.1% | 47.4% |
| PF_NEARUSD | 1 | +33.8% | 33.8% |
| PF_TRUMPUSD | 1 | -32.6% | 32.6% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
