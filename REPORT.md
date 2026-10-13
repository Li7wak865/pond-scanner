# Pond Scanner Report
**Scan time:** 2026-10-13 00:41 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +314.3% | $6,164,083 |
| 🟢 | PF_GRASSUSD | +71.5% | $1,385,748 |
| 🟢 | PF_APTUSD | +53.1% | $1,146,246 |
| 🟢 | PF_VIRTUALUSD | -36.4% | $613,541 |
| 🟢 | PF_TIAUSD | +30.5% | $3,168,455 |
| 🟢 | PF_BATUSD | -30.3% | $5,038,210 |
| ⚪ | PF_TRUMPUSD | -23.7% | $1,123,817 |
| ⚪ | PF_ZROUSD | -20.8% | $1,026,818 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → kraken) — coinbase: $81,313.07, kraken: $81,325.20, gemini: $81,317.98
- ⚪ **ETH** gap **0.109%** (kraken → gemini) — coinbase: $2,423.83, kraken: $2,423.32, gemini: $2,425.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| BOOK OF MEME (BOME) | #450 | $52.8M | 1.01x | -30.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 28% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 40% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 33% (1.0x)
- ⚪ **ETH** 24h vol 45% vs 30d norm 41% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | +314.3% | 314.3% |
| PF_GRASSUSD | 2 | +71.5% | 71.5% |
| PF_TIAUSD | 2 | +30.5% | 35.1% |
| PF_BATUSD | 2 | -30.3% | 43.4% |
| PF_APTUSD | 1 | +53.1% | 53.1% |
| PF_VIRTUALUSD | 1 | -36.4% | 36.4% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 184%), PF_TRUMPUSD (crowded 2d, worst 49%), PF_DOTUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
