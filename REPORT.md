# Pond Scanner Report
**Scan time:** 2026-09-06 15:28 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +561.5% | $537,678 |
| 🟢 | PF_SOLUSD | +328.1% | $541,913 |
| 🟢 | PF_IOTAUSD | -117.5% | $571,687 |
| 🟢 | PF_ACEUSD | -100.7% | $550,577 |
| 🟢 | PF_NEARUSD | +79.4% | $1,921,645 |
| 🟢 | PF_TRUMPUSD | +70.2% | $1,820,302 |
| 🟢 | PF_DOTUSD | +62.9% | $3,722,885 |
| 🟢 | PF_UNIUSD | -62.7% | $1,550,807 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $79,620.00, kraken: $79,620.50, gemini: $79,630.73
- ⚪ **ETH** gap **0.017%** (kraken → gemini) — coinbase: $2,478.40, kraken: $2,478.14, gemini: $2,478.57

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Sushi (SUSHI) | #352 | $72.3M | 1.86x | +20.9% |
| COTI (COTI) | #434 | $53.2M | 1.35x | +18.3% |
| 哈基米 (Hajimi) (哈基米) | #394 | $62.4M | 0.83x | +250.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.49, realized vol 10d 40% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 42% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 16% vs 30d norm 40% (0.4x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 54% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +70.2% | 375.1% |
| PF_NEARUSD | 2 | +79.4% | 163.9% |
| PF_UNIUSD | 2 | -62.7% | 387.6% |
| PF_LINKUSD | 1 | +561.5% | 561.5% |
| PF_SOLUSD | 1 | +328.1% | 328.1% |
| PF_IOTAUSD | 1 | -117.5% | 117.5% |
| PF_ACEUSD | 1 | -100.7% | 133.5% |
| PF_DOTUSD | 1 | +62.9% | 90.7% |
| PF_HFTUSD | 1 | +34.4% | 34.4% |

**Resolved since last scan:** PF_JUPUSD (crowded 1d, worst 65%), PF_JTOUSD (crowded 1d, worst 48%), PF_ICXUSD (crowded 1d, worst 63%), PF_ASTERUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
