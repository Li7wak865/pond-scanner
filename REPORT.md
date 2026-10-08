# Pond Scanner Report
**Scan time:** 2026-10-08 23:21 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | -475.0% | $731,461 |
| 🟢 | PF_RENDERUSD | -203.4% | $1,092,354 |
| 🟢 | PF_NEARUSD | -93.2% | $8,300,848 |
| 🟢 | PF_ZROUSD | -78.7% | $1,035,400 |
| 🟢 | PF_AVAXUSD | -46.3% | $504,364 |
| 🟢 | PF_CTSIUSD | -41.2% | $5,788,654 |
| 🟢 | PF_FILUSD | -36.0% | $1,948,092 |
| 🟢 | PF_VIRTUALUSD | -34.9% | $1,417,503 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (kraken → gemini) — coinbase: $81,834.69, kraken: $81,833.70, gemini: $81,840.12
- ⚪ **ETH** gap **0.109%** (gemini → kraken) — coinbase: $2,477.18, kraken: $2,477.55, gemini: $2,474.85

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #351 | $75.2M | 1.77x | +27.2% |
| Amp (AMP) | #402 | $63.4M | 0.86x | +21.4% |
| Mina Protocol (MINA) | #289 | $99.6M | 0.63x | -16.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 25% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 36% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 35% (1.4x)
- ⚪ **ETH** 24h vol 82% vs 30d norm 46% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -93.2% | 391.2% |
| PF_ZROUSD | 3 | -78.7% | 139.5% |
| PF_LINKUSD | 1 | -475.0% | 475.0% |
| PF_RENDERUSD | 1 | -203.4% | 203.4% |
| PF_AVAXUSD | 1 | -46.3% | 157.3% |
| PF_CTSIUSD | 1 | -41.2% | 41.2% |
| PF_FILUSD | 1 | -36.0% | 36.0% |
| PF_VIRTUALUSD | 1 | -34.9% | 34.9% |
| PF_ASTERUSD | 1 | +34.8% | 34.8% |
| PF_JTOUSD | 1 | -31.2% | 37.9% |

**Resolved since last scan:** PF_RAYUSD (crowded 2d, worst 826%), PF_UNIUSD (crowded 4d, worst 299%), PF_APTUSD (crowded 2d, worst 51%), PF_ETHFIUSD (crowded 1d, worst 48%), PF_XRPUSD (crowded 1d, worst 40%), PF_SUIUSD (crowded 1d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
