# Pond Scanner Report
**Scan time:** 2026-11-15 06:34 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -569.1% | $740,562 |
| 🟢 | PF_ZROUSD | -191.3% | $1,195,082 |
| 🟢 | PF_AVAXUSD | -179.7% | $610,567 |
| 🟢 | PF_KAVAUSD | -168.5% | $37,801,258 |
| 🟢 | PF_TRUMPUSD | -112.0% | $1,203,934 |
| 🟢 | PF_NEARUSD | -69.6% | $3,456,163 |
| 🟢 | PF_APTUSD | -46.8% | $1,866,849 |
| 🟢 | PF_ASTERUSD | -44.0% | $2,956,189 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.079%** (kraken → gemini) — coinbase: $64,380.83, kraken: $64,379.00, gemini: $64,429.70
- ⚪ **ETH** gap **0.129%** (coinbase → gemini) — coinbase: $1,793.32, kraken: $1,793.45, gemini: $1,795.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Kava (KAVA) | #469 | $40.0M | 1.72x | -45.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 42% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.49, realized vol 10d 57% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9956 (-0.44% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 97% vs 30d norm 40% (2.4x)
- 🟢 **ETH** 24h vol 133% vs 30d norm 56% (2.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_INJUSD | 3 | -569.1% | 746.6% |
| PF_ZROUSD | 2 | -191.3% | 192.0% |
| PF_KAVAUSD | 2 | -168.5% | 169.0% |
| PF_TRUMPUSD | 2 | -112.0% | 112.0% |
| PF_NEARUSD | 2 | -69.6% | 210.0% |
| PF_APTUSD | 2 | -46.8% | 57.4% |
| PF_AVAXUSD | 1 | -179.7% | 179.7% |
| PF_ASTERUSD | 1 | -44.0% | 44.0% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 945%), PF_UNIUSD (crowded 4d, worst 274%), PF_SUIUSD (crowded 2d, worst 45%), PF_GRASSUSD (crowded 2d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
