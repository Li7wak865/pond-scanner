# Pond Scanner Report
**Scan time:** 2026-10-14 11:54 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | +625.7% | $504,366 |
| 🟢 | PF_ZROUSD | -100.8% | $745,161 |
| 🟢 | PF_NEARUSD | +79.1% | $3,954,365 |
| 🟢 | PF_BATUSD | -48.6% | $5,992,428 |
| 🟢 | PF_XRPUSD | -34.3% | $11,401,403 |
| ⚪ | PF_STXUSD | +28.0% | $985,932 |
| ⚪ | PF_TRUMPUSD | +26.7% | $663,654 |
| ⚪ | PF_STRKUSD | +15.4% | $54,248,138 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → gemini) — coinbase: $83,397.82, kraken: $83,395.50, gemini: $83,401.47
- ⚪ **ETH** gap **0.020%** (coinbase → gemini) — coinbase: $2,500.82, kraken: $2,500.87, gemini: $2,501.32

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Wormhole (W) | #276 | $104.3M | 0.68x | -16.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 27% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.30, realized vol 10d 42% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 34% (0.6x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 41% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_INJUSD | 2 | +625.7% | 625.7% |
| PF_BATUSD | 2 | -48.6% | 132.6% |
| PF_ZROUSD | 1 | -100.8% | 100.8% |
| PF_NEARUSD | 1 | +79.1% | 79.1% |
| PF_XRPUSD | 1 | -34.3% | 34.3% |

**Resolved since last scan:** PF_RENDERUSD (crowded 2d, worst 134%), PF_APTUSD (crowded 2d, worst 62%), PF_STXUSD (crowded 2d, worst 42%), PF_TIAUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
