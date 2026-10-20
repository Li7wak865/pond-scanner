# Pond Scanner Report
**Scan time:** 2026-10-20 17:08 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | -249.4% | $595,619 |
| 🟢 | PF_NEARUSD | +174.4% | $4,232,165 |
| 🟢 | PF_ZROUSD | +165.8% | $726,009 |
| 🟢 | PF_FILUSD | -37.7% | $1,464,132 |
| 🟢 | PF_TIAUSD | -35.7% | $3,239,416 |
| 🟢 | PF_ASTERUSD | +35.4% | $513,401 |
| 🟢 | PF_ATOMUSD | -34.9% | $573,989 |
| ⚪ | PF_STXUSD | -20.5% | $650,197 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (kraken → gemini) — coinbase: $82,728.82, kraken: $82,717.80, gemini: $82,739.31
- ⚪ **ETH** gap **0.038%** (kraken → gemini) — coinbase: $2,450.31, kraken: $2,450.12, gemini: $2,451.04

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| AltLayer (ALT) | #338 | $74.9M | 0.86x | +17.2% |
| Janction (JCT) | #436 | $52.5M | 0.73x | +135.0% |
| Dolphin (POD) | #414 | $55.2M | 0.69x | +25.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 24% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.30, realized vol 10d 35% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9982 (-0.18% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 37% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 43% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +165.8% | 165.8% |
| PF_LINKUSD | 1 | -249.4% | 249.4% |
| PF_NEARUSD | 1 | +174.4% | 174.4% |
| PF_FILUSD | 1 | -37.7% | 37.7% |
| PF_TIAUSD | 1 | -35.7% | 35.7% |
| PF_ASTERUSD | 1 | +35.4% | 35.4% |
| PF_ATOMUSD | 1 | -34.9% | 34.9% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
