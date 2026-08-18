# Pond Scanner Report
**Scan time:** 2026-08-18 01:51 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -191.9% | $17,629,700 |
| 🟢 | PF_KAITOUSD | -75.4% | $1,326,328 |
| 🟢 | PF_ETHFIUSD | -73.9% | $632,070 |
| 🟢 | PF_HFTUSD | -58.2% | $6,182,338 |
| ⚪ | PF_BIOUSD | +29.0% | $742,506 |
| ⚪ | PF_NEARUSD | +21.9% | $2,250,510 |
| ⚪ | PF_XRPUSD | +20.8% | $31,682,206 |
| ⚪ | PF_APTUSD | +19.6% | $704,311 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → kraken) — coinbase: $64,162.01, kraken: $64,172.90, gemini: $64,166.74
- ⚪ **ETH** gap **0.028%** (coinbase → kraken) — coinbase: $1,901.16, kraken: $1,901.70, gemini: $1,901.55

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cysic (CYS) | #285 | $77.4M | 0.71x | -40.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 19% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 18% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 26% (0.9x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 35% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -191.9% | 732.3% |
| PF_ETHFIUSD | 2 | -73.9% | 95.3% |
| PF_HFTUSD | 2 | -58.2% | 58.2% |
| PF_KAITOUSD | 1 | -75.4% | 75.4% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 146%), PF_XRPUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
