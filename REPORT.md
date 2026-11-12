# Pond Scanner Report
**Scan time:** 2026-11-12 19:55 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +744.2% | $816,791 |
| 🟢 | PF_SOLUSD | -638.1% | $779,594 |
| 🟢 | PF_UNIUSD | -159.2% | $525,839 |
| 🟢 | PF_ZIGUSD | +102.4% | $706,772 |
| 🟢 | PF_TRUMPUSD | -57.2% | $809,343 |
| 🟢 | PF_NEARUSD | +42.4% | $4,509,949 |
| 🟢 | PF_ETHFIUSD | -35.1% | $688,995 |
| ⚪ | PF_DOTUSD | -28.8% | $898,218 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.027%** (coinbase → gemini) — coinbase: $71,595.71, kraken: $71,609.80, gemini: $71,615.31
- ⚪ **ETH** gap **0.017%** (kraken → coinbase) — coinbase: $2,014.71, kraken: $2,014.36, gemini: $2,014.36

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lombard (BARD) | #418 | $51.6M | 1.04x | +55.1% |
| Magma Finance (MAGMA) | #360 | $64.9M | 0.64x | +26.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.41, realized vol 10d 47% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.42, realized vol 10d 71% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9960 (-0.40% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 36% (0.9x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 50% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +42.4% | 138.3% |
| PF_HYPEUSD | 1 | +744.2% | 744.2% |
| PF_SOLUSD | 1 | -638.1% | 638.1% |
| PF_UNIUSD | 1 | -159.2% | 159.2% |
| PF_ZIGUSD | 1 | +102.4% | 102.4% |
| PF_TRUMPUSD | 1 | -57.2% | 57.2% |
| PF_ETHFIUSD | 1 | -35.1% | 35.1% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 68%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
