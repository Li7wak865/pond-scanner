# Pond Scanner Report
**Scan time:** 2026-10-24 20:51 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TIAUSD | -37.5% | $2,882,581 |
| 🟢 | PF_FILUSD | -31.9% | $649,050 |
| ⚪ | PF_TRUMPUSD | +29.9% | $867,118 |
| ⚪ | PF_PONSUSD | +28.8% | $1,275,351 |
| ⚪ | PF_XRPUSD | +28.3% | $9,822,398 |
| ⚪ | PF_KAITOUSD | -23.6% | $905,581 |
| ⚪ | PF_NEARUSD | -21.7% | $6,544,918 |
| ⚪ | PF_ARCUSD | -17.6% | $2,609,201 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (kraken → gemini) — coinbase: $80,435.99, kraken: $80,432.30, gemini: $80,452.09
- ⚪ **ETH** gap **0.030%** (kraken → gemini) — coinbase: $2,344.71, kraken: $2,344.46, gemini: $2,345.16

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #298 | $88.4M | 1.59x | -45.8% |
| Janction (JCT) | #320 | $81.4M | 1.14x | +171.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.31, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 27% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 31% (0.9x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 42% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TIAUSD | 1 | -37.5% | 37.5% |
| PF_FILUSD | 1 | -31.9% | 31.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 48%), PF_TRUMPUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
