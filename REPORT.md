# Pond Scanner Report
**Scan time:** 2026-09-26 16:24 UTC

**Flags this scan:** 18 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +316.9% | $679,912 |
| 🟢 | PF_LINKUSD | -255.9% | $938,538 |
| 🟢 | PF_TRUMPUSD | +238.4% | $936,787 |
| 🟢 | PF_ETHFIUSD | +137.8% | $1,255,601 |
| 🟢 | PF_WLDUSD | +93.0% | $8,676,922 |
| 🟢 | PF_2ZUSD | -92.0% | $3,998,545 |
| 🟢 | PF_DOTUSD | +89.2% | $1,562,086 |
| 🟢 | PF_GRASSUSD | +81.0% | $634,874 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $84,098.00, kraken: $84,101.00, gemini: $84,107.81
- ⚪ **ETH** gap **0.007%** (coinbase → gemini) — coinbase: $2,689.81, kraken: $2,689.81, gemini: $2,690.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| ARK (ARK) | #479 | $52.7M | 1.24x | +15.8% |
| Amp (AMP) | #444 | $59.1M | 0.73x | +31.2% |
| Nillion (NIL) | #471 | $53.9M | 0.55x | -16.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 14% vs 30d norm 34% (0.4x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 46% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | +238.4% | 372.6% |
| PF_DOTUSD | 2 | +89.2% | 89.2% |
| PF_GRASSUSD | 2 | +81.0% | 81.0% |
| PF_LSKUSD | 2 | -80.8% | 191.7% |
| PF_UNIUSD | 1 | +316.9% | 316.9% |
| PF_LINKUSD | 1 | -255.9% | 364.0% |
| PF_ETHFIUSD | 1 | +137.8% | 137.8% |
| PF_WLDUSD | 1 | +93.0% | 93.0% |
| PF_2ZUSD | 1 | -92.0% | 92.0% |
| PF_NEARUSD | 1 | +78.2% | 78.2% |
| PF_RAREUSD | 1 | -64.8% | 105.4% |
| PF_KAITOUSD | 1 | -47.2% | 50.3% |
| PF_SUIUSD | 1 | +45.0% | 45.0% |
| PF_FILUSD | 1 | +34.1% | 34.1% |
| PF_EIGENUSD | 1 | +30.0% | 30.1% |

**Resolved since last scan:** PF_JTOUSD (crowded 2d, worst 102%), PF_ONDOUSD (crowded 1d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
