# Pond Scanner Report
**Scan time:** 2026-11-10 07:20 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +116.2% | $2,090,223 |
| 🟢 | PF_TRUMPUSD | -89.9% | $1,211,693 |
| 🟢 | PF_AVAXUSD | -88.9% | $658,879 |
| 🟢 | PF_UNIUSD | +49.3% | $516,772 |
| 🟢 | PF_ACEUSD | +35.7% | $2,392,123 |
| ⚪ | PF_XRPUSD | +29.4% | $19,464,005 |
| ⚪ | PF_XTZUSD | +19.1% | $595,592 |
| ⚪ | PF_SUSHIUSD | -16.0% | $516,277 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (kraken → gemini) — coinbase: $74,646.68, kraken: $74,646.30, gemini: $74,656.45
- ⚪ **ETH** gap **0.015%** (gemini → kraken) — coinbase: $2,116.92, kraken: $2,117.07, gemini: $2,116.76

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Initia (INIT) | #428 | $51.2M | 2.19x | +84.0% |
| Akedo (AKE) | #392 | $57.2M | 0.74x | -45.8% |
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #358 | $66.0M | 0.65x | +25.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.41, realized vol 10d 45% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.41, realized vol 10d 69% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9965 (-0.35% vs peg)
- ⚪ **USDe** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 37% vs 30d norm 35% (1.0x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 50% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 7 | -89.9% | 178.3% |
| PF_UNIUSD | 3 | +49.3% | 202.8% |
| PF_NEARUSD | 2 | +116.2% | 116.2% |
| PF_AVAXUSD | 2 | -88.9% | 211.0% |
| PF_ACEUSD | 1 | +35.7% | 35.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 201%), PF_RENDERUSD (crowded 2d, worst 105%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
