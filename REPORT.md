# Pond Scanner Report
**Scan time:** 2026-09-27 21:21 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +600.3% | $582,458 |
| 🟢 | PF_UNIUSD | +479.0% | $837,435 |
| 🟢 | PF_NEARUSD | +285.8% | $4,037,817 |
| 🟢 | PF_AVAXUSD | +167.3% | $601,453 |
| 🟢 | PF_ETHFIUSD | +69.7% | $1,489,667 |
| 🟢 | PF_XRPUSD | +57.8% | $47,622,553 |
| 🟢 | PF_GRASSUSD | +46.2% | $539,367 |
| 🟢 | PF_ONDOUSD | +43.8% | $7,842,699 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → gemini) — coinbase: $84,657.83, kraken: $84,651.80, gemini: $84,661.52
- ⚪ **ETH** gap **0.028%** (kraken → gemini) — coinbase: $2,689.02, kraken: $2,688.90, gemini: $2,689.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SOON (SOON) | #274 | $109.9M | 1.53x | +41.2% |
| Wormhole (W) | #292 | $100.8M | 1.26x | +20.6% |
| Amp (AMP) | #442 | $58.7M | 0.75x | -18.5% |
| PHALA (PHA) | #444 | $58.2M | 0.70x | -17.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.25, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 34% (0.5x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 46% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | +600.3% | 600.3% |
| PF_UNIUSD | 2 | +479.0% | 479.0% |
| PF_NEARUSD | 2 | +285.8% | 285.8% |
| PF_AVAXUSD | 2 | +167.3% | 167.3% |
| PF_ETHFIUSD | 2 | +69.7% | 137.8% |
| PF_XRPUSD | 1 | +57.8% | 57.8% |
| PF_GRASSUSD | 1 | +46.2% | 46.2% |
| PF_ONDOUSD | 1 | +43.8% | 43.8% |
| PF_RUNEUSD | 1 | +40.5% | 102.5% |
| PF_SAGAUSD | 1 | -36.7% | 36.7% |
| PF_XPLUSD | 1 | +35.1% | 35.1% |
| PF_HFTUSD | 1 | -32.4% | 32.4% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 5d, worst 373%), PF_LSKUSD (crowded 1d, worst 169%), PF_FILUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
