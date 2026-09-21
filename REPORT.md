# Pond Scanner Report
**Scan time:** 2026-09-21 21:59 UTC

**Flags this scan:** 19 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +725.7% | $615,346 |
| 🟢 | PF_AVAXUSD | +314.4% | $1,203,270 |
| 🟢 | PF_UNIUSD | +260.5% | $809,664 |
| 🟢 | PF_RENDERUSD | +152.3% | $605,212 |
| 🟢 | PF_NEARUSD | +67.9% | $8,920,575 |
| 🟢 | PF_FILUSD | -67.1% | $2,322,796 |
| 🟢 | PF_NIGHTUSD | +60.2% | $2,552,131 |
| 🟢 | PF_ONDOUSD | -55.7% | $18,105,391 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $86,598.03, kraken: $86,599.90, gemini: $86,612.39
- ⚪ **ETH** gap **0.037%** (kraken → coinbase) — coinbase: $2,770.79, kraken: $2,769.77, gemini: $2,769.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| ZetaChain (ZETA) | #301 | $95.5M | 1.67x | +52.0% |
| Harmony (ONE) | #399 | $66.2M | 1.64x | +21.0% |
| Synapse (SYN) | #435 | $57.7M | 0.76x | +20.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.35, realized vol 10d 54% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.35, realized vol 10d 57% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 55% vs 30d norm 36% (1.5x)
- ⚪ **ETH** 24h vol 57% vs 30d norm 48% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | +260.5% | 624.1% |
| PF_NEARUSD | 2 | +67.9% | 457.9% |
| PF_LINKUSD | 1 | +725.7% | 725.7% |
| PF_AVAXUSD | 1 | +314.4% | 314.4% |
| PF_RENDERUSD | 1 | +152.3% | 152.3% |
| PF_FILUSD | 1 | -67.1% | 67.1% |
| PF_NIGHTUSD | 1 | +60.2% | 60.2% |
| PF_ONDOUSD | 1 | -55.7% | 93.3% |
| PF_WLDUSD | 1 | +54.6% | 54.6% |
| PF_MOODENGUSD | 1 | +52.2% | 52.2% |
| PF_HFTUSD | 1 | +42.8% | 104.6% |
| PF_VIRTUALUSD | 1 | +41.2% | 41.2% |
| PF_XPLUSD | 1 | +37.4% | 37.4% |
| PF_JTOUSD | 1 | +34.4% | 61.1% |
| PF_TRUMPUSD | 1 | -31.2% | 52.0% |
| PF_APTUSD | 1 | -31.0% | 49.0% |

**Resolved since last scan:** PF_GRIFFAINUSD (crowded 1d, worst 67%), PF_SUIUSD (crowded 2d, worst 50%), PF_ASTERUSD (crowded 1d, worst 36%), PF_MINAUSD (crowded 1d, worst 36%), PF_XRPUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
