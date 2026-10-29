# Pond Scanner Report
**Scan time:** 2026-10-29 13:03 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ICPUSD | -322.3% | $518,127 |
| 🟢 | PF_NEARUSD | +124.5% | $4,825,001 |
| 🟢 | PF_UNIUSD | -72.3% | $530,322 |
| 🟢 | PF_TIAUSD | +72.2% | $3,158,966 |
| 🟢 | PF_ATOMUSD | -71.4% | $663,493 |
| 🟢 | PF_TRUMPUSD | +67.9% | $800,180 |
| 🟢 | PF_JTOUSD | -44.2% | $717,094 |
| 🟢 | PF_SYNUSD | +34.5% | $655,375 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → gemini) — coinbase: $80,033.10, kraken: $80,034.80, gemini: $80,044.90
- ⚪ **ETH** gap **0.017%** (coinbase → gemini) — coinbase: $2,323.97, kraken: $2,324.05, gemini: $2,324.37

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #255 | $115.3M | 0.67x | -17.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 26% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 28% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 31% (1.1x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 43% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +124.5% | 141.8% |
| PF_ICPUSD | 1 | -322.3% | 322.3% |
| PF_UNIUSD | 1 | -72.3% | 72.3% |
| PF_TIAUSD | 1 | +72.2% | 72.2% |
| PF_ATOMUSD | 1 | -71.4% | 136.7% |
| PF_TRUMPUSD | 1 | +67.9% | 67.9% |
| PF_JTOUSD | 1 | -44.2% | 123.0% |
| PF_SYNUSD | 1 | +34.5% | 37.6% |
| PF_ONDOUSD | 1 | -32.7% | 32.7% |
| PF_ASTERUSD | 1 | -31.8% | 31.8% |

**Resolved since last scan:** PF_CRVUSD (crowded 1d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
