# Pond Scanner Report
**Scan time:** 2026-09-09 16:40 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RAYUSD | +657.3% | $969,707 |
| 🟢 | PF_TRUMPUSD | -507.7% | $1,282,967 |
| 🟢 | PF_LINKUSD | -350.9% | $621,449 |
| 🟢 | PF_UNIUSD | +153.4% | $913,188 |
| 🟢 | PF_NEARUSD | +66.2% | $2,554,063 |
| 🟢 | PF_ICXUSD | -59.5% | $1,700,618 |
| 🟢 | PF_XRPUSD | -50.9% | $41,513,944 |
| 🟢 | PF_BATUSD | +44.5% | $1,199,148 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $78,757.00, kraken: $78,763.30, gemini: $78,770.23
- ⚪ **ETH** gap **0.024%** (gemini → coinbase) — coinbase: $2,496.90, kraken: $2,496.70, gemini: $2,496.31

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| IOST (IOST) | #398 | $64.6M | 2.67x | +102.8% |
| Siacoin (SC) | #453 | $51.4M | 0.73x | +38.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 37% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 38% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 40% (0.8x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 54% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +66.2% | 246.3% |
| PF_RAYUSD | 1 | +657.3% | 657.3% |
| PF_TRUMPUSD | 1 | -507.7% | 507.7% |
| PF_LINKUSD | 1 | -350.9% | 350.9% |
| PF_UNIUSD | 1 | +153.4% | 361.6% |
| PF_ICXUSD | 1 | -59.5% | 59.5% |
| PF_XRPUSD | 1 | -50.9% | 50.9% |
| PF_BATUSD | 1 | +44.5% | 44.5% |
| PF_ATOMUSD | 1 | -36.9% | 77.0% |
| PF_ACEUSD | 1 | -33.0% | 64.2% |
| PF_SWARMSUSD | 1 | -31.4% | 31.4% |

**Resolved since last scan:** PF_PROMPTUSD (crowded 1d, worst 101%), PF_CATIUSD (crowded 1d, worst 85%), PF_DOTUSD (crowded 1d, worst 54%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
