# Pond Scanner Report
**Scan time:** 2026-07-25 03:38 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | +823.5% | $643,590 |
| 🟢 | PF_KAITOUSD | -178.9% | $608,784 |
| 🟢 | PF_UNIUSD | -144.5% | $1,107,409 |
| 🟢 | PF_ACEUSD | -122.6% | $2,605,604 |
| 🟢 | PF_SYNUSD | +76.6% | $2,453,798 |
| 🟢 | PF_STXUSD | -41.4% | $1,436,877 |
| 🟢 | PF_GRASSUSD | +30.3% | $678,532 |
| ⚪ | PF_EIGENUSD | -17.5% | $735,173 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → kraken) — coinbase: $64,020.86, kraken: $64,032.80, gemini: $64,026.76
- ⚪ **ETH** gap **0.007%** (kraken → gemini) — coinbase: $1,857.25, kraken: $1,857.18, gemini: $1,857.31

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #368 | $61.6M | 3.05x | +20.4% |
| ETHGas (GWEI) | #384 | $57.7M | 0.70x | +35.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 22% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 30% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 41% (0.6x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 52% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -178.9% | 178.9% |
| PF_UNIUSD | 2 | -144.5% | 144.5% |
| PF_ACEUSD | 2 | -122.6% | 192.2% |
| PF_SYNUSD | 2 | +76.6% | 76.6% |
| PF_DEXEUSD | 1 | +823.5% | 823.5% |
| PF_STXUSD | 1 | -41.4% | 41.4% |
| PF_GRASSUSD | 1 | +30.3% | 30.3% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
