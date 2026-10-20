# Pond Scanner Report
**Scan time:** 2026-10-20 21:38 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +240.8% | $4,596,075 |
| 🟢 | PF_TRUMPUSD | +64.1% | $611,107 |
| 🟢 | PF_ZROUSD | +57.9% | $756,692 |
| 🟢 | PF_ASTERUSD | +55.7% | $561,545 |
| 🟢 | PF_FILUSD | -49.6% | $1,879,679 |
| 🟢 | PF_APTUSD | -37.1% | $852,150 |
| 🟢 | PF_LINKUSD | -33.0% | $686,693 |
| ⚪ | PF_SPXUSD | +29.4% | $661,941 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.110%** (kraken → gemini) — coinbase: $82,759.00, kraken: $82,757.80, gemini: $82,849.02
- ⚪ **ETH** gap **0.016%** (kraken → gemini) — coinbase: $2,447.52, kraken: $2,447.43, gemini: $2,447.83

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Janction (JCT) | #428 | $53.0M | 0.82x | +133.7% |
| Dolphin (POD) | #419 | $53.9M | 0.73x | +21.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 24% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.31, realized vol 10d 35% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 62% vs 30d norm 43% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +57.9% | 165.8% |
| PF_NEARUSD | 1 | +240.8% | 240.8% |
| PF_TRUMPUSD | 1 | +64.1% | 64.1% |
| PF_ASTERUSD | 1 | +55.7% | 55.7% |
| PF_FILUSD | 1 | -49.6% | 49.6% |
| PF_APTUSD | 1 | -37.1% | 37.1% |
| PF_LINKUSD | 1 | -33.0% | 249.4% |

**Resolved since last scan:** PF_TIAUSD (crowded 1d, worst 36%), PF_ATOMUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
