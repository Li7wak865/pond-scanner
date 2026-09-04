# Pond Scanner Report
**Scan time:** 2026-09-04 04:35 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZIGUSD | -179.1% | $588,365 |
| 🟢 | PF_BATUSD | +109.2% | $1,693,083 |
| 🟢 | PF_UNIUSD | +96.9% | $1,289,917 |
| 🟢 | PF_ACEUSD | -81.3% | $1,011,967 |
| 🟢 | PF_HFTUSD | +80.4% | $4,897,160 |
| 🟢 | PF_SAGAUSD | +65.1% | $2,438,304 |
| 🟢 | PF_JTOUSD | -57.6% | $552,320 |
| 🟢 | PF_ZEREBROUSD | -39.8% | $535,940 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → gemini) — coinbase: $81,177.77, kraken: $81,179.00, gemini: $81,186.27
- ⚪ **ETH** gap **0.065%** (coinbase → gemini) — coinbase: $2,520.42, kraken: $2,520.51, gemini: $2,522.07

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #335 | $75.0M | 1.06x | -22.6% |
| Basecat (BASECAT) | #419 | $55.8M | 0.59x | +74.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 39% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.50, realized vol 10d 43% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **FDUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 53% vs 30d norm 39% (1.4x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 53% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -81.3% | 304.8% |
| PF_HFTUSD | 3 | +80.4% | 113.2% |
| PF_ZIGUSD | 2 | -179.1% | 179.4% |
| PF_UNIUSD | 2 | +96.9% | 246.7% |
| PF_BATUSD | 1 | +109.2% | 109.2% |
| PF_SAGAUSD | 1 | +65.1% | 65.1% |
| PF_JTOUSD | 1 | -57.6% | 57.6% |
| PF_ZEREBROUSD | 1 | -39.8% | 39.8% |
| PF_XRPUSD | 1 | +35.4% | 35.4% |
| PF_FILUSD | 1 | +30.0% | 30.0% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 400%), PF_TRUMPUSD (crowded 2d, worst 288%), PF_NEARUSD (crowded 2d, worst 147%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
