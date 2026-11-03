# Pond Scanner Report
**Scan time:** 2026-11-03 14:16 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +74.3% | $7,149,684 |
| 🟢 | PF_ACEUSD | +30.1% | $745,535 |
| ⚪ | PF_SYNUSD | +28.9% | $676,477 |
| ⚪ | PF_RUNEUSD | +21.6% | $808,558 |
| ⚪ | PF_TIAUSD | +19.7% | $1,162,129 |
| ⚪ | PF_SUSHIUSD | +15.4% | $547,697 |
| ⚪ | PF_DYDXUSD | +14.4% | $796,227 |
| ⚪ | PF_WIFUSD | +12.8% | $4,275,286 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → coinbase) — coinbase: $77,055.57, kraken: $77,045.30, gemini: $77,048.09
- ⚪ **ETH** gap **0.014%** (gemini → coinbase) — coinbase: $2,277.12, kraken: $2,276.98, gemini: $2,276.79

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MEET48 (IDOL) | #479 | $45.2M | 0.82x | +47.0% |
| Holo (HOT) | #284 | $94.2M | 0.66x | +32.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.27, realized vol 10d 30% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.27, realized vol 10d 31% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9963 (-0.37% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 32% (0.8x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 45% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +74.3% | 74.3% |
| PF_ACEUSD | 1 | +30.1% | 30.1% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 55%), PF_RUNEUSD (crowded 1d, worst 53%), PF_TRUMPUSD (crowded 1d, worst 49%), PF_STXUSD (crowded 1d, worst 41%), PF_XRPUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
