# Pond Scanner Report
**Scan time:** 2026-10-04 05:55 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -56.2% | $1,556,273 |
| 🟢 | PF_SUPERUSD | -53.3% | $505,520 |
| 🟢 | PF_ZROUSD | +45.3% | $1,206,229 |
| 🟢 | PF_WLDUSD | +37.4% | $7,290,688 |
| 🟢 | PF_PONSUSD | +34.5% | $777,320 |
| ⚪ | PF_JTOUSD | +26.2% | $555,353 |
| ⚪ | PF_FETUSD | +19.8% | $5,891,497 |
| ⚪ | PF_SANDUSD | -17.4% | $35,044,254 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $84,915.50, kraken: $84,920.60, gemini: $84,925.35
- ⚪ **ETH** gap **0.023%** (coinbase → gemini) — coinbase: $2,694.69, kraken: $2,695.00, gemini: $2,695.32

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #361 | $74.7M | 1.60x | +17.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.34, realized vol 10d 13% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 11% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 8% vs 30d norm 34% (0.2x)
- ⚪ **ETH** 24h vol 9% vs 30d norm 44% (0.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -56.2% | 134.3% |
| PF_ZROUSD | 3 | +45.3% | 221.9% |
| PF_PONSUSD | 2 | +34.5% | 111.2% |
| PF_SUPERUSD | 1 | -53.3% | 53.3% |
| PF_WLDUSD | 1 | +37.4% | 37.4% |

**Resolved since last scan:** PF_MOVRUSD (crowded 4d, worst 289%), PF_SANDUSD (crowded 3d, worst 148%), PF_UNIUSD (crowded 2d, worst 54%), PF_SYNUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
