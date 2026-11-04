# Pond Scanner Report
**Scan time:** 2026-11-04 06:25 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +61.5% | $6,731,078 |
| 🟢 | PF_TRUMPUSD | -43.6% | $1,002,412 |
| 🟢 | PF_RUNEUSD | -42.2% | $1,030,865 |
| ⚪ | PF_SYNUSD | +25.7% | $565,246 |
| ⚪ | PF_DOTUSD | -22.7% | $759,232 |
| ⚪ | PF_PONSUSD | +17.5% | $3,362,267 |
| ⚪ | PF_XRPUSD | +17.0% | $9,303,731 |
| ⚪ | PF_ACEUSD | +12.2% | $601,309 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (gemini → coinbase) — coinbase: $77,674.53, kraken: $77,674.00, gemini: $77,667.58
- ⚪ **ETH** gap **0.066%** (coinbase → gemini) — coinbase: $2,288.24, kraken: $2,288.30, gemini: $2,289.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Holo (HOT) | #293 | $88.2M | 0.54x | +16.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.27, realized vol 10d 31% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.29, realized vol 10d 31% vs 60d 38%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9965 (-0.35% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 41% vs 30d norm 33% (1.2x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 45% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +61.5% | 74.3% |
| PF_RUNEUSD | 2 | -42.2% | 51.8% |
| PF_TRUMPUSD | 1 | -43.6% | 43.6% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
