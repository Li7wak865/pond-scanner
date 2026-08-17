# Pond Scanner Report
**Scan time:** 2026-08-17 07:16 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -219.5% | $12,640,327 |
| 🟢 | PF_ETHFIUSD | -98.7% | $922,590 |
| 🟢 | PF_NEARUSD | +42.1% | $1,791,212 |
| 🟢 | PF_MOODENGUSD | +31.7% | $1,013,403 |
| 🟢 | PF_KAITOUSD | -31.3% | $1,018,545 |
| ⚪ | PF_BICOUSD | -26.6% | $50,141,158 |
| ⚪ | PF_HFTUSD | -23.8% | $5,430,617 |
| ⚪ | PF_XRPUSD | +14.4% | $10,544,655 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (gemini → kraken) — coinbase: $63,495.86, kraken: $63,504.00, gemini: $63,490.30
- ⚪ **ETH** gap **0.059%** (coinbase → gemini) — coinbase: $1,901.88, kraken: $1,902.31, gemini: $1,903.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MarsCoin (MARSCOIN) | #467 | $42.0M | 0.70x | -15.0% |
| Cysic (CYS) | #257 | $94.6M | 0.65x | -16.8% |
| GoPlus Security (GPS) | #267 | $89.1M | 0.52x | +39.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 12% vs 60d 27%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 16% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 14% vs 30d norm 25% (0.5x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 34% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -219.5% | 732.3% |
| PF_ETHFIUSD | 1 | -98.7% | 98.7% |
| PF_NEARUSD | 1 | +42.1% | 42.1% |
| PF_MOODENGUSD | 1 | +31.7% | 69.2% |
| PF_KAITOUSD | 1 | -31.3% | 46.1% |

**Resolved since last scan:** PF_ZEREBROUSD (crowded 2d, worst 191%), PF_LINKUSD (crowded 4d, worst 228%), PF_ALICEUSD (crowded 4d, worst 196%), PF_BICOUSD (crowded 1d, worst 44%), PF_HFTUSD (crowded 2d, worst 117%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
