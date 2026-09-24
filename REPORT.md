# Pond Scanner Report
**Scan time:** 2026-09-24 11:47 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +545.8% | $1,156,355 |
| 🟢 | PF_NEARUSD | +343.9% | $7,102,568 |
| 🟢 | PF_RAYUSD | -119.3% | $669,578 |
| 🟢 | PF_HFTUSD | -85.4% | $3,033,444 |
| 🟢 | PF_LSKUSD | -79.4% | $2,168,335 |
| 🟢 | PF_AVAXUSD | +78.0% | $545,407 |
| 🟢 | PF_TRUMPUSD | +48.4% | $2,153,210 |
| 🟢 | PF_APTUSD | -39.6% | $575,618 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.006%** (coinbase → kraken) — coinbase: $83,444.55, kraken: $83,449.60, gemini: $83,446.20
- ⚪ **ETH** gap **0.006%** (gemini → kraken) — coinbase: $2,645.99, kraken: $2,646.15, gemini: $2,645.98

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #399 | $64.9M | 2.56x | +33.1% |
| Lisk (LSK) | #302 | $91.9M | 1.21x | +23.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 58% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 61% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 43% vs 30d norm 35% (1.2x)
- ⚪ **ETH** 24h vol 45% vs 30d norm 47% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AVAXUSD | 3 | +78.0% | 218.8% |
| PF_UNIUSD | 2 | +545.8% | 545.8% |
| PF_NEARUSD | 2 | +343.9% | 343.9% |
| PF_HFTUSD | 2 | -85.4% | 112.1% |
| PF_TRUMPUSD | 2 | +48.4% | 372.6% |
| PF_SPXUSD | 2 | -33.0% | 58.4% |
| PF_RAYUSD | 1 | -119.3% | 119.3% |
| PF_LSKUSD | 1 | -79.4% | 79.4% |
| PF_APTUSD | 1 | -39.6% | 39.6% |
| PF_SUIUSD | 1 | +34.1% | 34.1% |
| PF_DOTUSD | 1 | -32.5% | 32.5% |

**Resolved since last scan:** PF_MINAUSD (crowded 2d, worst 628%), PF_LINKUSD (crowded 2d, worst 406%), PF_JTOUSD (crowded 2d, worst 94%), PF_KAITOUSD (crowded 2d, worst 167%), PF_SWARMSUSD (crowded 2d, worst 35%), PF_FETUSD (crowded 2d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
