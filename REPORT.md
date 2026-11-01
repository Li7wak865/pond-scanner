# Pond Scanner Report
**Scan time:** 2026-11-01 13:26 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -73.2% | $2,152,375 |
| ⚪ | PF_STXUSD | -23.6% | $1,370,589 |
| ⚪ | PF_SUIUSD | +22.2% | $1,756,075 |
| ⚪ | PF_CRVUSD | +20.2% | $2,128,291 |
| ⚪ | PF_SYNUSD | +16.6% | $608,769 |
| ⚪ | PF_DOTUSD | +16.1% | $513,341 |
| ⚪ | PF_ONDOUSD | +13.7% | $2,002,727 |
| ⚪ | PF_ENAUSD | +10.8% | $10,564,777 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.049%** (coinbase → gemini) — coinbase: $77,810.37, kraken: $77,830.90, gemini: $77,848.29
- ⚪ **ETH** gap **0.061%** (kraken → gemini) — coinbase: $2,261.17, kraken: $2,260.87, gemini: $2,262.25

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #465 | $47.8M | 2.40x | -24.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 27% vs 60d 36%
- 🟡 **ETH: MIXED** — efficiency ratio 0.31, realized vol 10d 29% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 12% vs 30d norm 32% (0.4x)
- ⚪ **ETH** 24h vol 16% vs 30d norm 45% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -73.2% | 73.2% |

**Resolved since last scan:** PF_STXUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
