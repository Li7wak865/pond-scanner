# Pond Scanner Report
**Scan time:** 2026-07-29 09:09 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_DEXEUSD | -364.2% | $1,051,779 |
| 🟢 | PF_SYNUSD | +79.9% | $2,133,350 |
| 🟢 | PF_NEARUSD | +55.7% | $1,758,127 |
| 🟢 | PF_SAGAUSD | +53.7% | $711,660 |
| 🟢 | PF_RUNEUSD | +45.4% | $515,875 |
| 🟢 | PF_COTIUSD | -36.4% | $140,626,450 |
| 🟢 | PF_FILUSD | -34.7% | $583,601 |
| ⚪ | PF_KAITOUSD | +27.1% | $672,492 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (kraken → gemini) — coinbase: $64,348.29, kraken: $64,336.90, gemini: $64,349.68
- ⚪ **ETH** gap **0.019%** (kraken → coinbase) — coinbase: $1,915.90, kraken: $1,915.54, gemini: $1,915.84

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #321 | $71.0M | 3.47x | -42.3% |
| Euler (EUL) | #455 | $42.8M | 2.19x | +18.1% |
| pipedog (PIPEDOG) | #479 | $41.1M | 1.57x | +294.4% |
| Zilliqa (ZIL) | #398 | $53.3M | 1.12x | +17.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 40% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 33% (1.0x)
- ⚪ **ETH** 24h vol 61% vs 30d norm 46% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 3 | +79.9% | 79.9% |
| PF_DEXEUSD | 2 | -364.2% | 755.4% |
| PF_NEARUSD | 1 | +55.7% | 55.7% |
| PF_SAGAUSD | 1 | +53.7% | 53.7% |
| PF_RUNEUSD | 1 | +45.4% | 45.4% |
| PF_COTIUSD | 1 | -36.4% | 36.4% |
| PF_FILUSD | 1 | -34.7% | 34.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 770%), PF_UNIUSD (crowded 2d, worst 171%), PF_KAITOUSD (crowded 4d, worst 510%), PF_ATOMUSD (crowded 1d, worst 77%), PF_TRUMPUSD (crowded 2d, worst 74%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
