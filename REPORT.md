# Pond Scanner Report
**Scan time:** 2026-08-29 20:56 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_STXUSD | -64.1% | $696,698 |
| 🟢 | PF_ACEUSD | -57.2% | $1,508,740 |
| 🟢 | PF_DEXEUSD | -45.2% | $938,168 |
| ⚪ | PF_WLDUSD | -26.8% | $636,526 |
| ⚪ | PF_FETUSD | +26.8% | $9,767,153 |
| ⚪ | PF_LDOUSD | +25.7% | $511,974 |
| ⚪ | PF_MELANIAUSD | +24.7% | $1,416,184 |
| ⚪ | PF_NEARUSD | +22.6% | $617,377 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → kraken) — coinbase: $78,138.13, kraken: $78,145.90, gemini: $78,138.58
- ⚪ **ETH** gap **0.002%** (gemini → kraken) — coinbase: $2,452.91, kraken: $2,452.93, gemini: $2,452.87

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Helium (HNT) | #327 | $74.8M | 1.09x | +84.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 56% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.52, realized vol 10d 61% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **USDe** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 38% (0.5x)
- ⚪ **ETH** 24h vol 19% vs 30d norm 51% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 8 | -57.2% | 241.7% |
| PF_STXUSD | 2 | -64.1% | 64.1% |
| PF_DEXEUSD | 1 | -45.2% | 214.7% |

**Resolved since last scan:** PF_SPXUSD (crowded 1d, worst 74%), PF_FETUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
