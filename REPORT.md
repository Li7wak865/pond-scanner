# Pond Scanner Report
**Scan time:** 2026-10-29 05:50 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ATOMUSD | -136.6% | $654,216 |
| 🟢 | PF_JTOUSD | -123.1% | $649,369 |
| 🟢 | PF_NEARUSD | +72.7% | $3,755,116 |
| 🟢 | PF_SYNUSD | +37.6% | $912,424 |
| 🟢 | PF_CRVUSD | +36.9% | $6,600,352 |
| ⚪ | PF_LDOUSD | -27.6% | $6,697,355 |
| ⚪ | PF_APTUSD | +23.0% | $997,128 |
| ⚪ | PF_ONDOUSD | -22.3% | $9,235,805 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.035%** (coinbase → gemini) — coinbase: $80,244.37, kraken: $80,255.90, gemini: $80,272.37
- ⚪ **ETH** gap **0.046%** (coinbase → gemini) — coinbase: $2,325.95, kraken: $2,326.02, gemini: $2,327.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Initia (INIT) | #495 | $45.8M | 2.02x | +23.0% |
| Cap (CAP) | #259 | $113.5M | 0.65x | -22.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 25% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 28% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 31% (1.2x)
- ⚪ **ETH** 24h vol 47% vs 30d norm 43% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +72.7% | 141.8% |
| PF_ATOMUSD | 1 | -136.6% | 136.6% |
| PF_JTOUSD | 1 | -123.1% | 123.1% |
| PF_SYNUSD | 1 | +37.6% | 37.6% |
| PF_CRVUSD | 1 | +36.9% | 36.9% |

**Resolved since last scan:** PF_SPXUSD (crowded 2d, worst 74%), PF_TRUMPUSD (crowded 2d, worst 49%), PF_WLDUSD (crowded 2d, worst 38%), PF_XRPUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
