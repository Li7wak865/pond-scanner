# Pond Scanner Report
**Scan time:** 2026-11-13 06:47 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -273.6% | $738,240 |
| 🟢 | PF_RENDERUSD | -122.5% | $876,862 |
| 🟢 | PF_NEARUSD | +93.6% | $4,038,290 |
| 🟢 | PF_SPXUSD | -72.1% | $564,218 |
| 🟢 | PF_ZIGUSD | -65.3% | $522,065 |
| 🟢 | PF_ZROUSD | -52.0% | $881,238 |
| 🟢 | PF_TRUMPUSD | -38.5% | $965,616 |
| 🟢 | PF_SUIUSD | -34.3% | $2,503,243 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.067%** (coinbase → gemini) — coinbase: $68,738.16, kraken: $68,750.10, gemini: $68,783.94
- ⚪ **ETH** gap **0.023%** (coinbase → gemini) — coinbase: $1,928.00, kraken: $1,928.20, gemini: $1,928.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lombard (BARD) | #396 | $54.0M | 2.10x | +66.2% |
| Magma Finance (MAGMA) | #358 | $64.2M | 0.70x | +22.1% |
| Akedo (AKE) | #276 | $92.6M | 0.68x | +64.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.47, realized vol 10d 49% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 72% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9958 (-0.42% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 51% vs 30d norm 37% (1.4x)
- ⚪ **ETH** 24h vol 65% vs 30d norm 51% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +93.6% | 138.3% |
| PF_UNIUSD | 2 | -273.6% | 273.6% |
| PF_ZIGUSD | 2 | -65.3% | 102.4% |
| PF_TRUMPUSD | 2 | -38.5% | 57.2% |
| PF_RENDERUSD | 1 | -122.5% | 122.5% |
| PF_SPXUSD | 1 | -72.1% | 72.1% |
| PF_ZROUSD | 1 | -52.0% | 52.0% |
| PF_SUIUSD | 1 | -34.3% | 34.3% |
| PF_XRPUSD | 1 | -33.9% | 33.9% |
| PF_STXUSD | 1 | -33.4% | 33.4% |
| PF_DOTUSD | 1 | -30.6% | 30.6% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 744%), PF_SOLUSD (crowded 2d, worst 638%), PF_ETHFIUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
