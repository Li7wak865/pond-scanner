# Pond Scanner Report
**Scan time:** 2026-10-24 11:03 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +38.0% | $5,879,077 |
| 🟢 | PF_ATOMUSD | -35.5% | $535,002 |
| ⚪ | PF_PONSUSD | +28.8% | $618,414 |
| ⚪ | PF_XRPUSD | +27.0% | $7,510,817 |
| ⚪ | PF_FILUSD | -21.8% | $612,157 |
| ⚪ | PF_WLDUSD | -20.2% | $9,634,839 |
| ⚪ | PF_TIAUSD | -14.5% | $2,565,569 |
| ⚪ | PF_LDOUSD | -13.2% | $722,184 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.038%** (coinbase → gemini) — coinbase: $80,567.72, kraken: $80,572.30, gemini: $80,598.11
- ⚪ **ETH** gap **0.019%** (gemini → kraken) — coinbase: $2,367.53, kraken: $2,367.69, gemini: $2,367.25

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| ZIG Finance (ZIG) | #407 | $56.2M | 1.45x | -17.8% |
| Janction (JCT) | #413 | $55.1M | 1.05x | +17.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.31, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.46, realized vol 10d 26% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 31% (0.8x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 42% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +38.0% | 38.0% |
| PF_ATOMUSD | 1 | -35.5% | 35.5% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 48%), PF_TIAUSD (crowded 1d, worst 46%), PF_ZROUSD (crowded 2d, worst 45%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
