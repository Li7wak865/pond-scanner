# Pond Scanner Report
**Scan time:** 2026-09-14 21:50 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -649.0% | $5,295,597 |
| 🟢 | PF_UNIUSD | +170.3% | $1,010,030 |
| 🟢 | PF_STEEMUSD | -58.6% | $663,256 |
| 🟢 | PF_HFTUSD | +46.4% | $2,522,098 |
| ⚪ | PF_TRUMPUSD | -25.8% | $716,276 |
| ⚪ | PF_XTZUSD | -23.9% | $1,189,965 |
| ⚪ | PF_INITUSD | +23.1% | $551,897 |
| ⚪ | PF_DOTUSD | +20.9% | $1,782,416 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (gemini → kraken) — coinbase: $78,804.03, kraken: $78,814.80, gemini: $78,800.00
- ⚪ **ETH** gap **0.043%** (gemini → coinbase) — coinbase: $2,549.31, kraken: $2,549.16, gemini: $2,548.21

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #293 | $91.1M | 1.36x | -61.5% |
| Cap (CAP) | #284 | $96.8M | 1.26x | +31.2% |
| Teller (DEBIT) | #464 | $48.6M | 1.10x | -24.6% |
| VeThor (VTHO) | #377 | $65.9M | 0.64x | -21.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 24% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 32% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 42% (0.8x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 59% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_STEEMUSD | 2 | -58.6% | 187.8% |
| PF_LSKUSD | 1 | -649.0% | 649.0% |
| PF_UNIUSD | 1 | +170.3% | 170.3% |
| PF_HFTUSD | 1 | +46.4% | 65.1% |

**Resolved since last scan:** PF_ALCHUSD (crowded 1d, worst 141%), PF_POWRUSD (crowded 2d, worst 195%), PF_TRUMPUSD (crowded 1d, worst 56%), PF_FILUSD (crowded 2d, worst 81%), PF_VIRTUALUSD (crowded 1d, worst 72%), PF_NEARUSD (crowded 1d, worst 51%), PF_ACEUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
