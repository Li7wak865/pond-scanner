# Pond Scanner Report
**Scan time:** 2026-08-01 03:51 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AGLDUSD | +309.6% | $536,904 |
| 🟢 | PF_KAITOUSD | -163.9% | $511,806 |
| 🟢 | PF_UNIUSD | +80.1% | $1,794,040 |
| 🟢 | PF_SYNUSD | +79.9% | $2,169,239 |
| 🟢 | PF_DEXEUSD | +36.4% | $967,984 |
| 🟢 | PF_VIRTUALUSD | -32.8% | $505,075 |
| 🟢 | PF_SWARMSUSD | +30.2% | $714,758 |
| ⚪ | PF_MIRAUSD | -26.8% | $987,757 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → gemini) — coinbase: $62,951.97, kraken: $62,956.30, gemini: $62,958.06
- ⚪ **ETH** gap **0.026%** (kraken → coinbase) — coinbase: $1,867.48, kraken: $1,867.00, gemini: $1,867.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Giggle Fund (GIGGLE) | #448 | $44.8M | 3.09x | +50.8% |
| COTI (COTI) | #429 | $49.5M | 1.87x | +24.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 28% vs 60d 35%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 42% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 32% (0.9x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 44% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 4 | -163.9% | 326.1% |
| PF_UNIUSD | 3 | +80.1% | 237.0% |
| PF_AGLDUSD | 2 | +309.6% | 644.9% |
| PF_SYNUSD | 2 | +79.9% | 79.9% |
| PF_DEXEUSD | 2 | +36.4% | 732.1% |
| PF_VIRTUALUSD | 2 | -32.8% | 32.8% |
| PF_SWARMSUSD | 1 | +30.2% | 30.2% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 605%), PF_APTUSD (crowded 2d, worst 57%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
