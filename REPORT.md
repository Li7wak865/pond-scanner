# Pond Scanner Report
**Scan time:** 2026-09-30 05:34 UTC

**Flags this scan:** 21 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_2ZUSD | +282.6% | $1,362,619 |
| 🟢 | PF_UNIUSD | +268.9% | $552,018 |
| 🟢 | PF_ENJUSD | -128.6% | $663,176 |
| 🟢 | PF_NEARUSD | -105.1% | $4,302,877 |
| 🟢 | PF_AVAXUSD | -102.6% | $976,685 |
| 🟢 | PF_SOLUSD | -90.8% | $664,335 |
| 🟢 | PF_RAREUSD | +79.1% | $906,898 |
| 🟢 | PF_SPXUSD | -74.0% | $576,220 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.003%** (kraken → coinbase) — coinbase: $83,406.99, kraken: $83,404.30, gemini: $83,404.81
- ⚪ **ETH** gap **0.073%** (gemini → kraken) — coinbase: $2,676.19, kraken: $2,676.44, gemini: $2,674.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 0G (0G) | #366 | $74.1M | 2.18x | +16.3% |
| PHALA (PHA) | #412 | $63.2M | 1.25x | +18.9% |
| cat in a dogs world (MEW) | #479 | $50.3M | 0.81x | +21.4% |
| Numeraire (NMR) | #332 | $83.4M | 0.77x | -16.5% |
| Berachain (BERA) | #324 | $85.8M | 0.64x | +22.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.33, realized vol 10d 43% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.30, realized vol 10d 34% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9982 (-0.18% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 34% (0.9x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 45% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | +268.9% | 493.4% |
| PF_ETHFIUSD | 5 | -46.6% | 246.1% |
| PF_LINKUSD | 5 | +30.9% | 600.3% |
| PF_2ZUSD | 2 | +282.6% | 285.5% |
| PF_AVAXUSD | 2 | -102.6% | 289.8% |
| PF_SOLUSD | 2 | -90.8% | 804.0% |
| PF_RAREUSD | 2 | +79.1% | 79.1% |
| PF_SPXUSD | 2 | -74.0% | 109.2% |
| PF_RUNEUSD | 2 | +52.0% | 54.7% |
| PF_VETUSD | 2 | +38.8% | 38.8% |
| PF_SWARMSUSD | 2 | -35.3% | 35.4% |
| PF_ENJUSD | 1 | -128.6% | 128.6% |
| PF_NEARUSD | 1 | -105.1% | 105.1% |
| PF_APTUSD | 1 | +55.8% | 55.8% |
| PF_GRASSUSD | 1 | +45.3% | 45.3% |
| PF_GMTUSD | 1 | -37.3% | 37.3% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 3d, worst 136%), PF_SYRUPUSD (crowded 2d, worst 36%), PF_SOONUSD (crowded 2d, worst 33%), PF_VIRTUALUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
