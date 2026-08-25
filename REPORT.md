# Pond Scanner Report
**Scan time:** 2026-08-25 01:52 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | -657.8% | $623,038 |
| 🟢 | PF_LINKUSD | +198.0% | $719,827 |
| 🟢 | PF_ACEUSD | -167.2% | $1,471,286 |
| 🟢 | PF_HFTUSD | +107.3% | $3,543,530 |
| 🟢 | PF_STORJUSD | -87.6% | $2,067,917 |
| 🟢 | PF_TRUMPUSD | -57.8% | $2,037,158 |
| 🟢 | PF_XRPUSD | +48.2% | $42,244,302 |
| 🟢 | PF_NEARUSD | -46.9% | $4,935,072 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.032%** (coinbase → kraken) — coinbase: $79,547.00, kraken: $79,572.50, gemini: $79,572.23
- ⚪ **ETH** gap **0.006%** (gemini → coinbase) — coinbase: $2,490.52, kraken: $2,490.48, gemini: $2,490.36

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Prom (PROM) | #346 | $69.3M | 1.77x | +32.3% |
| Velvet (VELVET) | #351 | $69.7M | 0.77x | -77.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.67, realized vol 10d 57% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.65, realized vol 10d 107% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 50% vs 30d norm 37% (1.3x)
- ⚪ **ETH** 24h vol 48% vs 30d norm 52% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -167.2% | 241.7% |
| PF_LINKUSD | 2 | +198.0% | 223.0% |
| PF_HFTUSD | 2 | +107.3% | 110.1% |
| PF_STORJUSD | 2 | -87.6% | 214.3% |
| PF_XRPUSD | 2 | +48.2% | 51.4% |
| PF_NEARUSD | 2 | -46.9% | 166.1% |
| PF_HYPEUSD | 1 | -657.8% | 657.8% |
| PF_TRUMPUSD | 1 | -57.8% | 57.8% |
| PF_SUPERUSD | 1 | -39.0% | 39.0% |
| PF_STXUSD | 1 | -37.3% | 37.3% |
| PF_POPCATUSD | 1 | +35.6% | 35.6% |
| PF_ETHFIUSD | 1 | -33.5% | 33.5% |

**Resolved since last scan:** PF_RIVERUSD (crowded 2d, worst 276%), PF_UNIUSD (crowded 2d, worst 161%), PF_RENDERUSD (crowded 2d, worst 72%), PF_SYNUSD (crowded 2d, worst 478%), PF_PNUTUSD (crowded 2d, worst 63%), PF_KAITOUSD (crowded 2d, worst 46%), PF_APTUSD (crowded 2d, worst 45%), PF_GRASSUSD (crowded 2d, worst 65%), PF_LDOUSD (crowded 2d, worst 36%), PF_XTZUSD (crowded 2d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
