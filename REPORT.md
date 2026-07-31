# Pond Scanner Report
**Scan time:** 2026-07-31 09:17 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AGLDUSD | +353.8% | $574,953 |
| 🟢 | PF_UNIUSD | -146.2% | $2,355,889 |
| 🟢 | PF_KAITOUSD | +62.0% | $981,215 |
| 🟢 | PF_MUBARAKUSD | -57.8% | $954,727 |
| 🟢 | PF_RAREUSD | +52.1% | $999,384 |
| 🟢 | PF_SNXUSD | +32.8% | $956,813 |
| ⚪ | PF_FILUSD | +24.3% | $1,410,570 |
| ⚪ | PF_NEARUSD | -21.3% | $1,533,406 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (gemini → coinbase) — coinbase: $63,706.28, kraken: $63,702.70, gemini: $63,690.00
- ⚪ **ETH** gap **0.079%** (kraken → gemini) — coinbase: $1,887.43, kraken: $1,886.83, gemini: $1,888.32

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #284 | $85.1M | 2.89x | +34.1% |
| Momentum (MMT) | #365 | $61.1M | 2.15x | +54.2% |
| Micron Technology (bStocks Tokenized Stock) (MUB) | #314 | $73.7M | 1.09x | +25.6% |
| Cap (CAP) | #392 | $54.5M | 0.68x | +21.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.00, realized vol 10d 24% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.15, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 34% (0.6x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 45% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 3 | +62.0% | 326.1% |
| PF_UNIUSD | 2 | -146.2% | 237.0% |
| PF_AGLDUSD | 1 | +353.8% | 353.8% |
| PF_MUBARAKUSD | 1 | -57.8% | 57.8% |
| PF_RAREUSD | 1 | +52.1% | 52.1% |
| PF_SNXUSD | 1 | +32.8% | 32.8% |

**Resolved since last scan:** PF_MIRAUSD (crowded 1d, worst 68%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
