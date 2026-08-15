# Pond Scanner Report
**Scan time:** 2026-08-15 06:58 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -732.3% | $49,049,943 |
| 🟢 | PF_ALICEUSD | -164.1% | $3,851,562 |
| 🟢 | PF_UNIUSD | -142.4% | $2,358,845 |
| 🟢 | PF_KAITOUSD | -91.8% | $652,678 |
| 🟢 | PF_MONUSD | +91.3% | $2,178,238 |
| 🟢 | PF_TRUMPUSD | -78.5% | $535,869 |
| 🟢 | PF_LINKUSD | +51.0% | $943,891 |
| 🟢 | PF_ETHFIUSD | -36.1% | $503,746 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → kraken) — coinbase: $63,045.54, kraken: $63,056.00, gemini: $63,052.69
- ⚪ **ETH** gap **0.061%** (kraken → gemini) — coinbase: $1,880.37, kraken: $1,880.34, gemini: $1,881.49

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Fabric Protocol (ROBO) | #485 | $41.3M | 1.32x | +42.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 12% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 13% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 16% vs 30d norm 26% (0.6x)
- ⚪ **ETH** 24h vol 21% vs 30d norm 36% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALICEUSD | 2 | -164.1% | 195.8% |
| PF_UNIUSD | 2 | -142.4% | 142.4% |
| PF_KAITOUSD | 2 | -91.8% | 124.2% |
| PF_LINKUSD | 2 | +51.0% | 102.8% |
| PF_ETHFIUSD | 2 | -36.1% | 120.5% |
| PF_ACEUSD | 1 | -732.3% | 732.3% |
| PF_MONUSD | 1 | +91.3% | 91.3% |
| PF_TRUMPUSD | 1 | -78.5% | 78.5% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 36%), PF_ATOMUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
