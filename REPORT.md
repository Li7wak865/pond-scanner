# Pond Scanner Report
**Scan time:** 2026-08-09 13:15 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_CATIUSD | +102.6% | $927,699 |
| 🟢 | PF_ACEUSD | -41.5% | $8,470,417 |
| 🟢 | PF_NEARUSD | +37.8% | $887,123 |
| 🟢 | PF_SYNUSD | +34.4% | $1,284,838 |
| ⚪ | PF_TIAUSD | +28.1% | $517,230 |
| ⚪ | PF_HFTUSD | +28.0% | $5,730,283 |
| ⚪ | PF_XRPUSD | +15.8% | $10,351,375 |
| ⚪ | PF_SUIUSD | +15.5% | $3,212,879 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.031%** (kraken → gemini) — coinbase: $64,981.38, kraken: $64,970.00, gemini: $64,990.21
- ⚪ **ETH** gap **0.005%** (kraken → coinbase) — coinbase: $1,918.87, kraken: $1,918.78, gemini: $1,918.82

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #587 | $46.7M | 5.06x | -20.6% |
| Catizen (CATI) | #750 | $50.5M | 0.52x | +24.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.03, realized vol 10d 27% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 8% vs 30d norm 28% (0.3x)
- ⚪ **ETH** 24h vol 11% vs 30d norm 40% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -41.5% | 501.6% |
| PF_CATIUSD | 1 | +102.6% | 102.6% |
| PF_NEARUSD | 1 | +37.8% | 37.8% |
| PF_SYNUSD | 1 | +34.4% | 34.4% |

**Resolved since last scan:** PF_HFTUSD (crowded 1d, worst 184%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
