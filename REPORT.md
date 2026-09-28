# Pond Scanner Report
**Scan time:** 2026-09-28 23:17 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -698.4% | $511,318 |
| 🟢 | PF_UNIUSD | +493.4% | $1,058,630 |
| 🟢 | PF_AVAXUSD | +125.6% | $738,871 |
| 🟢 | PF_NEARUSD | +114.7% | $4,740,880 |
| 🟢 | PF_ZROUSD | -79.1% | $1,051,941 |
| 🟢 | PF_FILUSD | -73.0% | $1,344,392 |
| 🟢 | PF_ETHFIUSD | +70.7% | $982,266 |
| 🟢 | PF_GRASSUSD | +48.5% | $823,251 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $83,466.07, kraken: $83,469.20, gemini: $83,476.37
- ⚪ **ETH** gap **0.010%** (coinbase → kraken) — coinbase: $2,687.11, kraken: $2,687.38, gemini: $2,687.17

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Numeraire (NMR) | #279 | $105.2M | 1.16x | +45.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 43% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 34% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 46% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +493.4% | 493.4% |
| PF_AVAXUSD | 3 | +125.6% | 167.3% |
| PF_NEARUSD | 3 | +114.7% | 285.8% |
| PF_ETHFIUSD | 3 | +70.7% | 137.8% |
| PF_LINKUSD | 3 | -46.1% | 600.3% |
| PF_SOLUSD | 1 | -698.4% | 698.4% |
| PF_ZROUSD | 1 | -79.1% | 141.3% |
| PF_FILUSD | 1 | -73.0% | 73.0% |
| PF_GRASSUSD | 1 | +48.5% | 101.2% |
| PF_TRUMPUSD | 1 | -38.9% | 40.2% |
| PF_SUIUSD | 1 | +35.9% | 35.9% |
| PF_TIAUSD | 1 | -35.3% | 35.3% |

**Resolved since last scan:** PF_RUNEUSD (crowded 1d, worst 71%), PF_VIRTUALUSD (crowded 1d, worst 54%), PF_XRPUSD (crowded 1d, worst 34%), PF_SAGAUSD (crowded 2d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
