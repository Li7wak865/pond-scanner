# Pond Scanner Report
**Scan time:** 2026-11-24 22:28 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +310.2% | $592,059 |
| 🟢 | PF_ZROUSD | +37.0% | $716,877 |
| 🟢 | PF_TRUMPUSD | -30.5% | $580,919 |
| ⚪ | PF_NEARUSD | +25.0% | $4,011,391 |
| ⚪ | PF_JUPUSD | -18.1% | $694,003 |
| ⚪ | PF_DOTUSD | -12.7% | $1,270,390 |
| ⚪ | PF_SUIUSD | -9.8% | $3,368,085 |
| ⚪ | PF_XRPUSD | +9.5% | $8,119,952 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → kraken) — coinbase: $59,918.84, kraken: $59,924.80, gemini: $59,922.20
- ⚪ **ETH** gap **0.025%** (kraken → gemini) — coinbase: $1,682.08, kraken: $1,682.00, gemini: $1,682.42

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lista DAO (LISTA) | #412 | $46.3M | 1.05x | +16.7% |
| aelf (ELF) | #399 | $47.8M | 0.78x | +34.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.70, realized vol 10d 42% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.67, realized vol 10d 62% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9949 (-0.51% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 58% vs 30d norm 55% (1.0x)
- ⚪ **ETH** 24h vol 51% vs 30d norm 68% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +310.2% | 727.7% |
| PF_ZROUSD | 1 | +37.0% | 55.3% |
| PF_TRUMPUSD | 1 | -30.5% | 50.3% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 361%), PF_UNIUSD (crowded 8d, worst 222%), PF_RENDERUSD (crowded 2d, worst 86%), PF_ACEUSD (crowded 3d, worst 786%), PF_INJUSD (crowded 2d, worst 204%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
