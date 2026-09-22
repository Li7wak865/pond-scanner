# Pond Scanner Report
**Scan time:** 2026-09-22 11:40 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +304.4% | $566,017 |
| 🟢 | PF_LSKUSD | -210.2% | $1,050,533 |
| 🟢 | PF_NEARUSD | -186.8% | $8,726,255 |
| 🟢 | PF_AVAXUSD | -135.6% | $936,318 |
| 🟢 | PF_UNIUSD | +114.5% | $828,149 |
| 🟢 | PF_HFTUSD | -109.4% | $584,097 |
| 🟢 | PF_RENDERUSD | +88.7% | $678,583 |
| 🟢 | PF_TRUMPUSD | +76.7% | $962,268 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (gemini → coinbase) — coinbase: $86,050.74, kraken: $86,045.00, gemini: $86,044.70
- ⚪ **ETH** gap **0.017%** (coinbase → kraken) — coinbase: $2,743.85, kraken: $2,744.32, gemini: $2,744.26

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #412 | $62.8M | 2.07x | +41.5% |
| ZetaChain (ZETA) | #319 | $87.2M | 1.33x | -16.8% |
| Harmony (ONE) | #463 | $52.7M | 1.29x | -27.5% |
| Four (FORM) | #257 | $122.1M | 0.58x | +19.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.33, realized vol 10d 55% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.35, realized vol 10d 59% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 36% (1.0x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 48% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 6 | +114.5% | 624.1% |
| PF_NEARUSD | 3 | -186.8% | 457.9% |
| PF_LINKUSD | 2 | +304.4% | 725.7% |
| PF_RENDERUSD | 2 | +88.7% | 209.9% |
| PF_TRUMPUSD | 2 | +76.7% | 76.7% |
| PF_LSKUSD | 1 | -210.2% | 210.2% |
| PF_AVAXUSD | 1 | -135.6% | 135.6% |
| PF_HFTUSD | 1 | -109.4% | 109.4% |
| PF_JTOUSD | 1 | -65.0% | 65.0% |
| PF_SPXUSD | 1 | +56.3% | 68.9% |
| PF_DOTUSD | 1 | +47.1% | 47.1% |

**Resolved since last scan:** PF_RUNEUSD (crowded 1d, worst 66%), PF_SYNUSD (crowded 1d, worst 42%), PF_VIRTUALUSD (crowded 2d, worst 41%), PF_XPLUSD (crowded 2d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
