# Pond Scanner Report
**Scan time:** 2026-10-15 11:31 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +383.1% | $683,260 |
| 🟢 | PF_NEARUSD | -89.5% | $6,051,637 |
| 🟢 | PF_TRUMPUSD | -68.6% | $909,119 |
| 🟢 | PF_LINKUSD | -43.7% | $812,398 |
| 🟢 | PF_STXUSD | -34.3% | $923,465 |
| 🟢 | PF_FILUSD | -34.1% | $2,813,909 |
| 🟢 | PF_XTZUSD | -32.9% | $503,022 |
| 🟢 | PF_ACEUSD | -31.9% | $3,019,863 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.049%** (coinbase → gemini) — coinbase: $80,902.65, kraken: $80,914.90, gemini: $80,942.34
- ⚪ **ETH** gap **0.051%** (coinbase → gemini) — coinbase: $2,360.29, kraken: $2,360.93, gemini: $2,361.50

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Zerebro (ZEREBRO) | #470 | $47.2M | 0.95x | +49.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.18, realized vol 10d 28% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 44% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 43% vs 30d norm 34% (1.3x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 42% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | -43.7% | 403.5% |
| PF_FILUSD | 2 | -34.1% | 49.8% |
| PF_SOLUSD | 1 | +383.1% | 383.1% |
| PF_NEARUSD | 1 | -89.5% | 89.5% |
| PF_TRUMPUSD | 1 | -68.6% | 68.6% |
| PF_STXUSD | 1 | -34.3% | 34.3% |
| PF_XTZUSD | 1 | -32.9% | 32.9% |
| PF_ACEUSD | 1 | -31.9% | 31.9% |

**Resolved since last scan:** PF_ATOMUSD (crowded 1d, worst 153%), PF_ZROUSD (crowded 2d, worst 101%), PF_GRASSUSD (crowded 2d, worst 66%), PF_VIRTUALUSD (crowded 1d, worst 50%), PF_PONSUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
