# Pond Scanner Report
**Scan time:** 2026-10-18 11:07 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +99.7% | $3,651,751 |
| 🟢 | PF_ZROUSD | -88.1% | $612,612 |
| 🟢 | PF_TIAUSD | +41.4% | $3,748,332 |
| ⚪ | PF_SPXUSD | +22.9% | $715,814 |
| ⚪ | PF_XRPUSD | +18.9% | $10,270,487 |
| ⚪ | PF_PONSUSD | -15.5% | $723,753 |
| ⚪ | PF_BATUSD | -15.5% | $1,521,033 |
| ⚪ | PF_SANDUSD | -10.7% | $48,225,476 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → gemini) — coinbase: $81,991.01, kraken: $81,997.40, gemini: $82,010.00
- ⚪ **ETH** gap **0.017%** (coinbase → gemini) — coinbase: $2,415.62, kraken: $2,415.89, gemini: $2,416.02

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Impossible Cloud Network Token (ICNT) | #410 | $55.4M | 1.09x | +17.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 24% vs 60d 41%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.36, realized vol 10d 34% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 34% (0.6x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 43% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +99.7% | 99.7% |
| PF_ZROUSD | 1 | -88.1% | 88.1% |
| PF_TIAUSD | 1 | +41.4% | 49.6% |

**Resolved since last scan:** PF_SANDUSD (crowded 1d, worst 114%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
