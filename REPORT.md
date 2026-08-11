# Pond Scanner Report
**Scan time:** 2026-08-11 13:43 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -983.6% | $556,149 |
| 🟢 | PF_ENJUSD | +108.3% | $598,229 |
| 🟢 | PF_UNIUSD | -77.1% | $1,061,141 |
| 🟢 | PF_RAREUSD | +52.9% | $502,152 |
| ⚪ | PF_SUSHIUSD | +19.8% | $2,100,137 |
| ⚪ | PF_TUSD | +15.4% | $586,919 |
| ⚪ | PF_ACEUSD | -15.2% | $5,237,506 |
| ⚪ | PF_CRVUSD | -14.4% | $6,225,501 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → gemini) — coinbase: $64,125.28, kraken: $64,121.30, gemini: $64,129.34
- ⚪ **ETH** gap **0.055%** (coinbase → gemini) — coinbase: $1,888.71, kraken: $1,889.09, gemini: $1,889.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #269 | $94.1M | 0.56x | +73.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 15% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 24% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 28% (0.7x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 40% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | -983.6% | 983.6% |
| PF_ENJUSD | 1 | +108.3% | 108.3% |
| PF_UNIUSD | 1 | -77.1% | 84.5% |
| PF_RAREUSD | 1 | +52.9% | 52.9% |

**Resolved since last scan:** PF_ACEUSD (crowded 1d, worst 47%), PF_EIGENUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
