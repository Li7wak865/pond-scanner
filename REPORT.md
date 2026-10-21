# Pond Scanner Report
**Scan time:** 2026-10-21 17:13 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -141.4% | $659,725 |
| 🟢 | PF_NEARUSD | -116.8% | $4,584,084 |
| 🟢 | PF_SUSHIUSD | +41.7% | $519,251 |
| 🟢 | PF_POLUSD | -39.7% | $16,386,908 |
| 🟢 | PF_TRUMPUSD | +32.2% | $943,853 |
| ⚪ | PF_ETHFIUSD | -26.0% | $704,653 |
| ⚪ | PF_BATUSD | +20.2% | $3,812,255 |
| ⚪ | PF_LDOUSD | +15.4% | $1,620,379 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → gemini) — coinbase: $84,353.29, kraken: $84,344.30, gemini: $84,355.61
- ⚪ **ETH** gap **0.004%** (coinbase → kraken) — coinbase: $2,503.87, kraken: $2,503.96, gemini: $2,503.88

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| IOST (IOST) | #401 | $63.1M | 4.46x | +93.8% |
| AltLayer (ALT) | #271 | $110.9M | 0.79x | +48.3% |
| Wormhole (W) | #287 | $102.8M | 0.71x | +17.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 25% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 37% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 32% (0.7x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 2 | +32.2% | 93.4% |
| PF_UNIUSD | 1 | -141.4% | 141.4% |
| PF_NEARUSD | 1 | -116.8% | 116.8% |
| PF_SUSHIUSD | 1 | +41.7% | 41.7% |
| PF_POLUSD | 1 | -39.7% | 39.7% |

**Resolved since last scan:** PF_BATUSD (crowded 1d, worst 75%), PF_ZROUSD (crowded 3d, worst 166%), PF_ASTERUSD (crowded 2d, worst 56%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
