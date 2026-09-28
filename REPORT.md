# Pond Scanner Report
**Scan time:** 2026-09-28 05:25 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +228.8% | $641,203 |
| 🟢 | PF_ENJUSD | +131.2% | $954,401 |
| 🟢 | PF_UNIUSD | +125.6% | $852,687 |
| 🟢 | PF_PONSUSD | +79.2% | $524,858 |
| 🟢 | PF_AVAXUSD | -71.9% | $688,910 |
| 🟢 | PF_NEARUSD | -58.5% | $3,824,381 |
| 🟢 | PF_VIRTUALUSD | +50.6% | $809,581 |
| 🟢 | PF_SUIUSD | +41.8% | $16,574,415 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (kraken → gemini) — coinbase: $83,065.19, kraken: $83,060.00, gemini: $83,078.12
- ⚪ **ETH** gap **0.026%** (kraken → gemini) — coinbase: $2,646.55, kraken: $2,646.27, gemini: $2,646.96

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SOON (SOON) | #261 | $120.4M | 1.55x | +16.4% |
| PHALA (PHA) | #473 | $51.6M | 0.75x | -17.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 43% vs 60d 43%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 36% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 34% (0.8x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 46% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +228.8% | 600.3% |
| PF_UNIUSD | 3 | +125.6% | 479.0% |
| PF_AVAXUSD | 3 | -71.9% | 167.3% |
| PF_NEARUSD | 3 | -58.5% | 285.8% |
| PF_ETHFIUSD | 3 | +31.4% | 137.8% |
| PF_SAGAUSD | 2 | -33.2% | 36.7% |
| PF_HFTUSD | 2 | -31.1% | 32.4% |
| PF_ENJUSD | 1 | +131.2% | 131.2% |
| PF_PONSUSD | 1 | +79.2% | 79.2% |
| PF_VIRTUALUSD | 1 | +50.6% | 50.6% |
| PF_SUIUSD | 1 | +41.8% | 41.8% |
| PF_DOTUSD | 1 | +36.9% | 36.9% |
| PF_FILUSD | 1 | +34.1% | 34.1% |

**Resolved since last scan:** PF_XRPUSD (crowded 2d, worst 58%), PF_GRASSUSD (crowded 2d, worst 46%), PF_ONDOUSD (crowded 2d, worst 44%), PF_RUNEUSD (crowded 2d, worst 102%), PF_XPLUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
