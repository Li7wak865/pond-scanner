# Pond Scanner Report
**Scan time:** 2026-09-27 12:04 UTC

**Flags this scan:** 19 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +264.8% | $633,502 |
| 🟢 | PF_NEARUSD | +216.0% | $3,420,913 |
| 🟢 | PF_LSKUSD | -168.8% | $769,987 |
| 🟢 | PF_LINKUSD | +118.3% | $807,719 |
| 🟢 | PF_ARCUSD | -110.3% | $777,921 |
| 🟢 | PF_RUNEUSD | -101.0% | $1,384,741 |
| 🟢 | PF_UNIUSD | +82.3% | $677,447 |
| 🟢 | PF_AVAXUSD | -72.0% | $804,032 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (kraken → coinbase) — coinbase: $84,943.42, kraken: $84,935.30, gemini: $84,939.50
- ⚪ **ETH** gap **0.016%** (gemini → coinbase) — coinbase: $2,711.71, kraken: $2,711.48, gemini: $2,711.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SOON (SOON) | #312 | $94.3M | 1.03x | +28.6% |
| Wormhole (W) | #305 | $97.1M | 0.85x | +15.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.26, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 12% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 19% vs 30d norm 46% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | +264.8% | 372.6% |
| PF_NEARUSD | 2 | +216.0% | 255.3% |
| PF_LINKUSD | 2 | +118.3% | 364.0% |
| PF_UNIUSD | 2 | +82.3% | 316.9% |
| PF_AVAXUSD | 2 | -72.0% | 91.6% |
| PF_ETHFIUSD | 2 | +42.9% | 137.8% |
| PF_WLDUSD | 2 | +38.4% | 93.0% |
| PF_2ZUSD | 2 | -36.6% | 92.0% |
| PF_LSKUSD | 1 | -168.8% | 168.8% |
| PF_ARCUSD | 1 | -110.3% | 110.3% |
| PF_RUNEUSD | 1 | -101.0% | 102.5% |
| PF_HFTUSD | 1 | -52.4% | 52.4% |
| PF_XRPUSD | 1 | +51.3% | 51.3% |
| PF_ONDOUSD | 1 | +50.3% | 50.3% |
| PF_DOTUSD | 1 | -46.8% | 46.8% |
| PF_VETUSD | 1 | +40.7% | 40.7% |
| PF_XPLUSD | 1 | +30.3% | 31.4% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 2d, worst 59%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
