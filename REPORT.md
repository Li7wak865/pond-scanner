# Pond Scanner Report
**Scan time:** 2026-07-26 08:39 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | -113.0% | $3,567,456 |
| 🟢 | PF_AVAXUSD | +40.9% | $733,230 |
| 🟢 | PF_NEARUSD | -32.6% | $554,662 |
| ⚪ | PF_ACEUSD | -29.7% | $1,429,780 |
| ⚪ | PF_SUIUSD | -26.7% | $3,479,258 |
| ⚪ | PF_SUSHIUSD | -24.3% | $527,073 |
| ⚪ | PF_MOODENGUSD | +20.4% | $2,800,048 |
| ⚪ | PF_STXUSD | -20.1% | $657,939 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (kraken → gemini) — coinbase: $64,338.83, kraken: $64,338.10, gemini: $64,340.82
- ⚪ **ETH** gap **0.028%** (kraken → gemini) — coinbase: $1,879.11, kraken: $1,878.98, gemini: $1,879.51

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #371 | $58.5M | 3.91x | +76.6% |
| ETHGas (GWEI) | #453 | $45.9M | 0.70x | -24.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 21% vs 60d 37%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 25% vs 60d 54%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 9% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 14% vs 30d norm 45% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 3 | -113.0% | 113.0% |
| PF_AVAXUSD | 1 | +40.9% | 96.5% |
| PF_NEARUSD | 1 | -32.6% | 32.6% |

**Resolved since last scan:** PF_LUNA2USD (crowded 1d, worst 103%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
