# Pond Scanner Report
**Scan time:** 2026-07-30 09:03 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -326.1% | $748,133 |
| 🟢 | PF_CTSIUSD | +71.4% | $1,629,001 |
| 🟢 | PF_SPXUSD | +66.7% | $523,254 |
| 🟢 | PF_UNIUSD | +61.1% | $976,102 |
| 🟢 | PF_COTIUSD | -59.3% | $131,432,276 |
| 🟢 | PF_SAGAUSD | +53.7% | $810,607 |
| 🟢 | PF_SOONUSD | +47.2% | $1,188,290 |
| 🟢 | PF_SYNUSD | +43.0% | $1,191,056 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (kraken → gemini) — coinbase: $64,214.03, kraken: $64,209.80, gemini: $64,223.02
- ⚪ **ETH** gap **0.050%** (kraken → gemini) — coinbase: $1,912.70, kraken: $1,912.26, gemini: $1,913.21

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #426 | $48.4M | 3.69x | +25.2% |
| Lorenzo Protocol (BANK) | #423 | $49.1M | 2.53x | -36.1% |
| Espresso (ESP) | #438 | $49.5M | 0.84x | +17.7% |
| RE (RE) | #304 | $75.8M | 0.74x | +15.1% |
| Cash Cat (CASHCAT) | #441 | $46.7M | 0.62x | +18.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 26% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.18, realized vol 10d 39% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9968 (-0.32% vs peg)
- ⚪ **USDT** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 45% vs 30d norm 34% (1.3x)
- ⚪ **ETH** 24h vol 55% vs 30d norm 46% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 4 | +43.0% | 79.8% |
| PF_KAITOUSD | 2 | -326.1% | 326.1% |
| PF_CTSIUSD | 1 | +71.4% | 71.4% |
| PF_SPXUSD | 1 | +66.7% | 66.7% |
| PF_UNIUSD | 1 | +61.1% | 61.1% |
| PF_COTIUSD | 1 | -59.3% | 59.3% |
| PF_SAGAUSD | 1 | +53.7% | 53.7% |
| PF_SOONUSD | 1 | +47.2% | 47.2% |

**Resolved since last scan:** PF_XRPUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
