# Pond Scanner Report
**Scan time:** 2026-10-19 22:22 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | +72.1% | $1,663,246 |
| 🟢 | PF_NEARUSD | -69.2% | $3,122,616 |
| 🟢 | PF_ZROUSD | +39.0% | $662,049 |
| ⚪ | PF_XRPUSD | +26.2% | $8,336,172 |
| ⚪ | PF_CRVUSD | +17.8% | $6,067,692 |
| ⚪ | PF_FILUSD | +14.8% | $1,990,421 |
| ⚪ | PF_BATUSD | -11.9% | $2,129,346 |
| ⚪ | PF_FETUSD | -11.1% | $3,540,019 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → gemini) — coinbase: $82,115.32, kraken: $82,115.70, gemini: $82,127.52
- ⚪ **ETH** gap **0.019%** (gemini → kraken) — coinbase: $2,411.22, kraken: $2,411.26, gemini: $2,410.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #408 | $56.3M | 1.36x | +36.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 23% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.36, realized vol 10d 33% vs 60d 45%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 23% vs 30d norm 33% (0.7x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 1 | +72.1% | 72.1% |
| PF_NEARUSD | 1 | -69.2% | 119.1% |
| PF_ZROUSD | 1 | +39.0% | 39.0% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
