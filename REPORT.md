# Pond Scanner Report
**Scan time:** 2026-11-16 22:04 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAVAUSD | -150.2% | $14,453,494 |
| 🟢 | PF_SPXUSD | -76.7% | $725,372 |
| 🟢 | PF_ZROUSD | -55.4% | $697,678 |
| 🟢 | PF_NEARUSD | -30.9% | $1,808,570 |
| ⚪ | PF_ZIGUSD | -22.2% | $670,664 |
| ⚪ | PF_SUIUSD | -16.6% | $2,439,663 |
| ⚪ | PF_DOTUSD | -14.0% | $945,809 |
| ⚪ | PF_ASTERUSD | -12.2% | $3,403,313 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (coinbase → gemini) — coinbase: $65,421.99, kraken: $65,427.20, gemini: $65,432.56
- ⚪ **ETH** gap **0.019%** (kraken → gemini) — coinbase: $1,832.14, kraken: $1,831.96, gemini: $1,832.30

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Aria.AI (ARIA) | #480 | $38.5M | 1.02x | -16.9% |
| Cash Cat (CASHCAT) | #389 | $52.5M | 0.98x | +32.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 46% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 63% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9963 (-0.37% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 53% vs 30d norm 42% (1.3x)
- ⚪ **ETH** 24h vol 70% vs 30d norm 57% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAVAUSD | 3 | -150.2% | 169.0% |
| PF_ZROUSD | 3 | -55.4% | 192.0% |
| PF_NEARUSD | 3 | -30.9% | 245.2% |
| PF_SPXUSD | 1 | -76.7% | 76.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 837%), PF_TRUMPUSD (crowded 3d, worst 112%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
