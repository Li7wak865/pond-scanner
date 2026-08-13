# Pond Scanner Report
**Scan time:** 2026-08-13 07:53 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -369.7% | $2,154,279 |
| 🟢 | PF_HFTUSD | +127.5% | $2,541,811 |
| 🟢 | PF_RENDERUSD | +90.5% | $562,250 |
| 🟢 | PF_VIRTUALUSD | +61.4% | $1,856,401 |
| 🟢 | PF_MOODENGUSD | +54.0% | $925,754 |
| 🟢 | PF_OPENUSD | +42.2% | $640,550 |
| 🟢 | PF_COTIUSD | -38.5% | $45,610,271 |
| 🟢 | PF_AVAXUSD | +31.8% | $601,031 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → gemini) — coinbase: $63,792.90, kraken: $63,788.90, gemini: $63,793.66
- ⚪ **ETH** gap **0.055%** (coinbase → gemini) — coinbase: $1,893.82, kraken: $1,894.01, gemini: $1,894.87

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Babylon (BABY) | #460 | $44.9M | 2.42x | -19.8% |
| DAPPOS (DOS) | #387 | $56.3M | 0.82x | -21.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 14% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 19% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 27% (0.8x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 39% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -369.7% | 946.7% |
| PF_COTIUSD | 2 | -38.5% | 57.5% |
| PF_HFTUSD | 1 | +127.5% | 137.2% |
| PF_RENDERUSD | 1 | +90.5% | 90.5% |
| PF_VIRTUALUSD | 1 | +61.4% | 61.4% |
| PF_MOODENGUSD | 1 | +54.0% | 54.0% |
| PF_OPENUSD | 1 | +42.2% | 43.5% |
| PF_AVAXUSD | 1 | +31.8% | 123.7% |

**Resolved since last scan:** PF_SAGAUSD (crowded 1d, worst 62%), PF_LSKUSD (crowded 1d, worst 48%), PF_STORJUSD (crowded 1d, worst 37%), PF_FILUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
