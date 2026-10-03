# Pond Scanner Report
**Scan time:** 2026-10-03 21:17 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +221.9% | $1,258,652 |
| 🟢 | PF_MOVRUSD | -198.4% | $613,981 |
| 🟢 | PF_PONSUSD | +69.1% | $815,615 |
| 🟢 | PF_NEARUSD | +60.5% | $1,259,990 |
| 🟢 | PF_SANDUSD | -44.1% | $37,447,347 |
| 🟢 | PF_UNIUSD | +34.1% | $697,533 |
| 🟢 | PF_SYNUSD | -33.4% | $756,781 |
| ⚪ | PF_SUIUSD | +29.7% | $6,455,483 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → gemini) — coinbase: $84,699.23, kraken: $84,700.00, gemini: $84,708.21
- ⚪ **ETH** gap **0.005%** (kraken → coinbase) — coinbase: $2,687.61, kraken: $2,687.48, gemini: $2,687.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #415 | $63.0M | 1.87x | +29.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.38, realized vol 10d 12% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.28, realized vol 10d 11% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 11% vs 30d norm 45% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_MOVRUSD | 3 | -198.4% | 289.0% |
| PF_ZROUSD | 2 | +221.9% | 221.9% |
| PF_NEARUSD | 2 | +60.5% | 134.3% |
| PF_SANDUSD | 2 | -44.1% | 148.5% |
| PF_PONSUSD | 1 | +69.1% | 111.2% |
| PF_UNIUSD | 1 | +34.1% | 54.3% |
| PF_SYNUSD | 1 | -33.4% | 33.4% |

**Resolved since last scan:** PF_LINKUSD (crowded 3d, worst 329%), PF_VIRTUALUSD (crowded 1d, worst 78%), PF_ASTERUSD (crowded 1d, worst 51%), PF_DOTUSD (crowded 1d, worst 36%), PF_FILUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
