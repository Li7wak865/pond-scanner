# Pond Scanner Report
**Scan time:** 2026-10-23 17:09 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | -40.1% | $610,021 |
| 🟢 | PF_NEARUSD | +39.0% | $3,967,449 |
| ⚪ | PF_XRPUSD | +28.3% | $15,062,169 |
| ⚪ | PF_TRUMPUSD | +26.9% | $922,491 |
| ⚪ | PF_WLDUSD | +22.2% | $8,180,465 |
| ⚪ | PF_BATUSD | -21.9% | $2,603,335 |
| ⚪ | PF_SUIUSD | +16.7% | $5,669,129 |
| ⚪ | PF_ATOMUSD | -15.2% | $614,288 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → gemini) — coinbase: $81,595.87, kraken: $81,600.10, gemini: $81,618.09
- ⚪ **ETH** gap **0.061%** (coinbase → gemini) — coinbase: $2,404.23, kraken: $2,404.40, gemini: $2,405.70

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #426 | $54.1M | 1.28x | +30.6% |
| Bifrost (BFC) | #477 | $49.0M | 1.06x | +63.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 26% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.35, realized vol 10d 31% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 42% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 1 | -40.1% | 40.1% |
| PF_NEARUSD | 1 | +39.0% | 39.0% |

**Resolved since last scan:** PF_BATUSD (crowded 2d, worst 53%), PF_XRPUSD (crowded 1d, worst 48%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
