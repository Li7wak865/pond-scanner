# Pond Scanner Report
**Scan time:** 2026-10-22 21:36 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +134.0% | $590,845 |
| 🟢 | PF_BATUSD | -52.9% | $3,695,995 |
| 🟢 | PF_TRUMPUSD | +40.7% | $1,014,819 |
| 🟢 | PF_TIAUSD | -35.3% | $4,820,592 |
| 🟢 | PF_APTUSD | -33.8% | $560,963 |
| 🟢 | PF_NEARUSD | +32.0% | $3,475,455 |
| ⚪ | PF_ATOMUSD | -26.6% | $595,035 |
| ⚪ | PF_PONSUSD | +26.3% | $703,531 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (coinbase → gemini) — coinbase: $81,350.46, kraken: $81,355.50, gemini: $81,366.89
- ⚪ **ETH** gap **0.021%** (gemini → kraken) — coinbase: $2,388.87, kraken: $2,389.12, gemini: $2,388.63

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| AltLayer (ALT) | #389 | $60.8M | 1.75x | -38.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 28% vs 60d 36%
- 🟡 **ETH: MIXED** — efficiency ratio 0.34, realized vol 10d 34% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 32% (0.9x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +134.0% | 148.2% |
| PF_BATUSD | 1 | -52.9% | 52.9% |
| PF_TRUMPUSD | 1 | +40.7% | 40.7% |
| PF_TIAUSD | 1 | -35.3% | 44.5% |
| PF_APTUSD | 1 | -33.8% | 33.8% |
| PF_NEARUSD | 1 | +32.0% | 175.8% |

**Resolved since last scan:** PF_FILUSD (crowded 1d, worst 63%), PF_IMXUSD (crowded 1d, worst 53%), PF_WLDUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
