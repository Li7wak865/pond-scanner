# Pond Scanner Report
**Scan time:** 2026-07-29 03:41 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -770.0% | $627,037 |
| 🟢 | PF_DEXEUSD | -560.5% | $1,042,123 |
| 🟢 | PF_UNIUSD | -148.4% | $882,253 |
| 🟢 | PF_KAITOUSD | -86.8% | $671,130 |
| 🟢 | PF_ATOMUSD | -77.0% | $624,644 |
| 🟢 | PF_SYNUSD | +73.2% | $2,607,324 |
| 🟢 | PF_TRUMPUSD | -70.7% | $640,117 |
| 🟢 | PF_RUNEUSD | +40.0% | $525,272 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (coinbase → kraken) — coinbase: $63,689.05, kraken: $63,703.20, gemini: $63,700.00
- ⚪ **ETH** gap **0.075%** (kraken → gemini) — coinbase: $1,896.61, kraken: $1,896.23, gemini: $1,897.65

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lorenzo Protocol (BANK) | #372 | $57.9M | 2.73x | -48.8% |
| Zilliqa (ZIL) | #405 | $52.1M | 0.98x | +15.9% |
| SOON (SOON) | #271 | $90.9M | 0.53x | +18.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 41% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 33% (0.9x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 46% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 4 | -86.8% | 510.3% |
| PF_SYNUSD | 3 | +73.2% | 73.2% |
| PF_DEXEUSD | 2 | -560.5% | 755.4% |
| PF_UNIUSD | 2 | -148.4% | 171.4% |
| PF_TRUMPUSD | 2 | -70.7% | 74.2% |
| PF_SOLUSD | 1 | -770.0% | 770.0% |
| PF_ATOMUSD | 1 | -77.0% | 77.0% |
| PF_RUNEUSD | 1 | +40.0% | 40.0% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 91%), PF_SOONUSD (crowded 2d, worst 69%), PF_SPXUSD (crowded 2d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
