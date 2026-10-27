# Pond Scanner Report
**Scan time:** 2026-10-27 18:02 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -92.6% | $2,274,122 |
| 🟢 | PF_ARCUSD | -34.5% | $3,011,232 |
| ⚪ | PF_SYNUSD | +26.0% | $3,463,207 |
| ⚪ | PF_XRPUSD | +23.8% | $9,806,246 |
| ⚪ | PF_SUIUSD | +16.2% | $2,989,291 |
| ⚪ | PF_TIAUSD | -15.3% | $1,005,003 |
| ⚪ | PF_BATUSD | +13.1% | $580,693 |
| ⚪ | PF_LDOUSD | +9.2% | $851,857 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $80,392.96, kraken: $80,394.10, gemini: $80,399.13
- ⚪ **ETH** gap **0.024%** (kraken → gemini) — coinbase: $2,341.64, kraken: $2,341.46, gemini: $2,342.03

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #449 | $49.7M | 1.32x | +34.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 24% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.34, realized vol 10d 27% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -92.6% | 303.9% |
| PF_ARCUSD | 1 | -34.5% | 34.5% |

**Resolved since last scan:** PF_XRPUSD (crowded 1d, worst 44%), PF_SYNUSD (crowded 2d, worst 52%), PF_TIAUSD (crowded 1d, worst 40%), PF_BBUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
