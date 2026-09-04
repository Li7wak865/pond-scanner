# Pond Scanner Report
**Scan time:** 2026-09-04 11:19 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +438.9% | $690,701 |
| 🟢 | PF_TRUMPUSD | +196.2% | $1,981,856 |
| 🟢 | PF_ZIGUSD | -180.3% | $517,095 |
| 🟢 | PF_COTIUSD | +179.1% | $774,725 |
| 🟢 | PF_BATUSD | +102.5% | $2,331,632 |
| 🟢 | PF_ACEUSD | -100.9% | $795,460 |
| 🟢 | PF_SPXUSD | -99.1% | $513,581 |
| 🟢 | PF_NEARUSD | +67.4% | $2,134,914 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (coinbase → gemini) — coinbase: $81,158.27, kraken: $81,159.90, gemini: $81,162.25
- ⚪ **ETH** gap **0.005%** (coinbase → kraken) — coinbase: $2,521.89, kraken: $2,522.01, gemini: $2,521.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Basecat (BASECAT) | #432 | $52.9M | 0.57x | +39.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 39% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.50, realized vol 10d 43% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 53% vs 30d norm 39% (1.4x)
- ⚪ **ETH** 24h vol 61% vs 30d norm 53% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -100.9% | 304.8% |
| PF_ZIGUSD | 2 | -180.3% | 180.3% |
| PF_UNIUSD | 2 | -37.8% | 246.7% |
| PF_SOLUSD | 1 | +438.9% | 438.9% |
| PF_TRUMPUSD | 1 | +196.2% | 196.2% |
| PF_COTIUSD | 1 | +179.1% | 179.1% |
| PF_BATUSD | 1 | +102.5% | 109.2% |
| PF_SPXUSD | 1 | -99.1% | 99.1% |
| PF_NEARUSD | 1 | +67.4% | 67.4% |

**Resolved since last scan:** PF_HFTUSD (crowded 3d, worst 113%), PF_SAGAUSD (crowded 1d, worst 65%), PF_JTOUSD (crowded 1d, worst 58%), PF_ZEREBROUSD (crowded 1d, worst 40%), PF_XRPUSD (crowded 1d, worst 35%), PF_FILUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
