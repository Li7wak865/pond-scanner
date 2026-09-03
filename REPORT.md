# Pond Scanner Report
**Scan time:** 2026-09-03 21:03 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +400.4% | $691,657 |
| 🟢 | PF_TRUMPUSD | +287.6% | $1,524,132 |
| 🟢 | PF_UNIUSD | +246.7% | $956,965 |
| 🟢 | PF_ZIGUSD | +179.4% | $513,141 |
| 🟢 | PF_ACEUSD | -176.1% | $1,142,634 |
| 🟢 | PF_HFTUSD | +113.2% | $1,580,892 |
| 🟢 | PF_NEARUSD | +30.3% | $1,649,053 |
| ⚪ | PF_VIRTUALUSD | +27.6% | $508,615 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $81,394.78, kraken: $81,403.80, gemini: $81,404.25
- ⚪ **ETH** gap **0.019%** (gemini → coinbase) — coinbase: $2,503.21, kraken: $2,503.21, gemini: $2,502.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| USD.AI (CHIP) | #250 | $111.7M | 0.91x | +33.1% |
| Cap (CAP) | #326 | $77.0M | 0.80x | -29.1% |
| MarsCoin (MARSCOIN) | #266 | $105.1M | 0.61x | +59.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.60, realized vol 10d 40% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.49, realized vol 10d 43% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **FDUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 52% vs 30d norm 39% (1.3x)
- ⚪ **ETH** 24h vol 62% vs 30d norm 53% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -176.1% | 304.8% |
| PF_HFTUSD | 2 | +113.2% | 113.2% |
| PF_SOLUSD | 1 | +400.4% | 400.4% |
| PF_TRUMPUSD | 1 | +287.6% | 287.6% |
| PF_UNIUSD | 1 | +246.7% | 246.7% |
| PF_ZIGUSD | 1 | +179.4% | 179.4% |
| PF_NEARUSD | 1 | +30.3% | 147.4% |

**Resolved since last scan:** PF_SUIUSD (crowded 1d, worst 51%), PF_FILUSD (crowded 1d, worst 41%), PF_DOTUSD (crowded 1d, worst 37%), PF_XRPUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
