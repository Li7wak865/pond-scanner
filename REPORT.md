# Pond Scanner Report
**Scan time:** 2026-09-16 21:19 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HFTUSD | +95.4% | $3,304,218 |
| 🟢 | PF_TRUMPUSD | -95.4% | $778,859 |
| 🟢 | PF_LSKUSD | -90.8% | $3,789,687 |
| 🟢 | PF_DOTUSD | -58.1% | $970,818 |
| 🟢 | PF_SYNUSD | -57.4% | $11,005,320 |
| 🟢 | PF_ICXUSD | +47.5% | $5,083,780 |
| 🟢 | PF_NEARUSD | +47.3% | $2,069,764 |
| 🟢 | PF_ACEUSD | -33.0% | $1,649,686 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (coinbase → gemini) — coinbase: $76,038.49, kraken: $76,038.80, gemini: $76,041.90
- ⚪ **ETH** gap **0.028%** (kraken → gemini) — coinbase: $2,406.49, kraken: $2,406.14, gemini: $2,406.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Teller (DEBIT) | #469 | $46.6M | 0.66x | +18.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.20, realized vol 10d 28% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9979 (-0.21% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 42% (0.6x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 60% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 3 | -90.8% | 896.9% |
| PF_HFTUSD | 1 | +95.4% | 95.4% |
| PF_TRUMPUSD | 1 | -95.4% | 95.4% |
| PF_DOTUSD | 1 | -58.1% | 58.1% |
| PF_SYNUSD | 1 | -57.4% | 61.9% |
| PF_ICXUSD | 1 | +47.5% | 47.5% |
| PF_NEARUSD | 1 | +47.3% | 47.3% |
| PF_ACEUSD | 1 | -33.0% | 33.0% |
| PF_ETHFIUSD | 1 | -30.6% | 30.6% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 492%), PF_IDUSD (crowded 1d, worst 70%), PF_STEEMUSD (crowded 1d, worst 205%), PF_FILUSD (crowded 1d, worst 56%), PF_APTUSD (crowded 1d, worst 38%), PF_UNIUSD (crowded 1d, worst 213%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
