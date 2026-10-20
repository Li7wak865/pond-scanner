# Pond Scanner Report
**Scan time:** 2026-10-20 04:52 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +72.3% | $590,278 |
| ⚪ | PF_XRPUSD | +25.7% | $6,344,866 |
| ⚪ | PF_PONSUSD | +22.4% | $1,105,024 |
| ⚪ | PF_DOTUSD | +20.2% | $1,492,073 |
| ⚪ | PF_WLDUSD | +14.3% | $6,028,611 |
| ⚪ | PF_BATUSD | -13.8% | $2,399,449 |
| ⚪ | PF_EIGENUSD | -13.1% | $653,888 |
| ⚪ | PF_NEARUSD | -12.8% | $2,619,819 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (gemini → coinbase) — coinbase: $81,952.87, kraken: $81,952.40, gemini: $81,949.28
- ⚪ **ETH** gap **0.110%** (coinbase → gemini) — coinbase: $2,407.91, kraken: $2,407.99, gemini: $2,410.55

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #431 | $52.6M | 1.95x | +26.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 23% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 33% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 33% (0.6x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +72.3% | 72.3% |

**Resolved since last scan:** PF_ACEUSD (crowded 2d, worst 72%), PF_NEARUSD (crowded 2d, worst 119%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
