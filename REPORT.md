# Pond Scanner Report
**Scan time:** 2026-08-09 07:16 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HFTUSD | -68.0% | $8,380,160 |
| 🟢 | PF_ACEUSD | -61.3% | $10,020,585 |
| ⚪ | PF_COTIUSD | -14.2% | $6,737,862 |
| ⚪ | PF_CRVUSD | +12.7% | $1,946,711 |
| ⚪ | PF_GRIFFAINUSD | +11.8% | $3,179,735 |
| ⚪ | PF_SUIUSD | +8.5% | $4,294,836 |
| ⚪ | PF_CSPRUSD | -8.4% | $6,150,278 |
| ⚪ | PF_MOODENGUSD | -8.0% | $1,258,528 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $64,797.05, kraken: $64,801.80, gemini: $64,802.02
- ⚪ **ETH** gap **0.046%** (coinbase → gemini) — coinbase: $1,916.48, kraken: $1,916.95, gemini: $1,917.37

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #385 | $82.4M | 3.25x | +16.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 27% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 7% vs 30d norm 28% (0.3x)
- ⚪ **ETH** 24h vol 9% vs 30d norm 40% (0.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -61.3% | 501.6% |
| PF_HFTUSD | 1 | -68.0% | 184.5% |

**Resolved since last scan:** PF_ZBTUSD (crowded 2d, worst 183%), PF_NEARUSD (crowded 2d, worst 57%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
