# Pond Scanner Report
**Scan time:** 2026-07-27 10:10 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -203.2% | $829,928 |
| 🟢 | PF_UNIUSD | -51.0% | $615,449 |
| 🟢 | PF_LRCUSD | +49.8% | $596,539 |
| 🟢 | PF_ETHFIUSD | -35.1% | $566,544 |
| ⚪ | PF_NEARUSD | -24.9% | $808,649 |
| ⚪ | PF_WLDUSD | +20.6% | $4,792,085 |
| ⚪ | PF_XTZUSD | -17.6% | $750,511 |
| ⚪ | PF_STORJUSD | +17.2% | $592,587 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $65,195.99, kraken: $65,201.60, gemini: $65,207.59
- ⚪ **ETH** gap **0.083%** (gemini → kraken) — coinbase: $1,963.18, kraken: $1,964.00, gemini: $1,962.37

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Espresso (ESP) | #392 | $57.8M | 2.00x | +18.3% |
| Euler (EUL) | #462 | $50.3M | 1.88x | -23.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 23% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.31, realized vol 10d 33% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 33% (0.7x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 44% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -203.2% | 234.8% |
| PF_UNIUSD | 1 | -51.0% | 51.0% |
| PF_LRCUSD | 1 | +49.8% | 49.8% |
| PF_ETHFIUSD | 1 | -35.1% | 35.1% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
