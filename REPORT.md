# Pond Scanner Report
**Scan time:** 2026-08-07 19:16 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +929.8% | $638,213 |
| 🟢 | PF_ACEUSD | -162.5% | $20,585,156 |
| 🟢 | PF_KAITOUSD | -113.5% | $760,207 |
| 🟢 | PF_HFTUSD | -77.9% | $153,902,371 |
| 🟢 | PF_GRASSUSD | +48.4% | $585,343 |
| 🟢 | PF_FILUSD | -46.4% | $1,522,611 |
| 🟢 | PF_MOODENGUSD | +41.7% | $519,789 |
| 🟢 | PF_NEARUSD | -36.0% | $1,961,574 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.034%** (kraken → gemini) — coinbase: $64,808.86, kraken: $64,800.10, gemini: $64,821.82
- ⚪ **ETH** gap **0.019%** (gemini → kraken) — coinbase: $1,912.97, kraken: $1,913.27, gemini: $1,912.91

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #512 | $53.9M | 4.77x | +43.3% |
| Allora (ALLO) | #281 | $87.0M | 0.85x | +32.3% |
| ETHGas (GWEI) | #344 | $65.0M | 0.68x | +70.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.00, realized vol 10d 23% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 28% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 29% (0.6x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 41% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +929.8% | 929.8% |
| PF_ACEUSD | 1 | -162.5% | 501.6% |
| PF_KAITOUSD | 1 | -113.5% | 124.5% |
| PF_HFTUSD | 1 | -77.9% | 148.9% |
| PF_GRASSUSD | 1 | +48.4% | 48.4% |
| PF_FILUSD | 1 | -46.4% | 46.4% |
| PF_MOODENGUSD | 1 | +41.7% | 41.7% |
| PF_NEARUSD | 1 | -36.0% | 54.7% |
| PF_SNXUSD | 1 | -33.1% | 33.1% |

**Resolved since last scan:** PF_AIXBTUSD (crowded 1d, worst 77%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
