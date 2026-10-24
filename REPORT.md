# Pond Scanner Report
**Scan time:** 2026-10-24 04:38 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -48.2% | $1,067,051 |
| 🟢 | PF_TIAUSD | -45.7% | $2,490,234 |
| 🟢 | PF_ZROUSD | -45.5% | $652,516 |
| ⚪ | PF_XRPUSD | +22.7% | $13,460,744 |
| ⚪ | PF_NEARUSD | +21.6% | $4,995,883 |
| ⚪ | PF_SUIUSD | +18.9% | $6,222,987 |
| ⚪ | PF_SYNUSD | -13.5% | $949,074 |
| ⚪ | PF_ACEUSD | -13.1% | $3,345,120 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (kraken → gemini) — coinbase: $80,764.85, kraken: $80,762.30, gemini: $80,778.43
- ⚪ **ETH** gap **0.022%** (gemini → kraken) — coinbase: $2,379.49, kraken: $2,379.71, gemini: $2,379.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Moonbirds (BIRB) | #455 | $48.9M | 12.29x | +178.1% |
| Axis Robotics (AXIS) | #417 | $54.6M | 5.23x | +19.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.30, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 26% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 31% (0.8x)
- ⚪ **ETH** 24h vol 39% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | -45.5% | 45.5% |
| PF_TRUMPUSD | 1 | -48.2% | 48.2% |
| PF_TIAUSD | 1 | -45.7% | 45.7% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 39%), PF_XRPUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
