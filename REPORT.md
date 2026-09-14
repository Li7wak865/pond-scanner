# Pond Scanner Report
**Scan time:** 2026-09-14 12:49 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALCHUSD | +140.7% | $1,327,858 |
| 🟢 | PF_POWRUSD | -69.4% | $3,352,265 |
| 🟢 | PF_HFTUSD | -65.1% | $3,092,090 |
| 🟢 | PF_TRUMPUSD | +55.8% | $573,035 |
| 🟢 | PF_FILUSD | -54.5% | $5,295,677 |
| 🟢 | PF_VIRTUALUSD | -53.7% | $719,961 |
| 🟢 | PF_NEARUSD | -51.4% | $983,737 |
| 🟢 | PF_STEEMUSD | -46.2% | $2,240,406 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $77,757.87, kraken: $77,758.60, gemini: $77,767.01
- ⚪ **ETH** gap **0.003%** (kraken → gemini) — coinbase: $2,508.00, kraken: $2,507.96, gemini: $2,508.04

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Teller (DEBIT) | #419 | $56.1M | 1.65x | +49.9% |
| Threshold Network (T) | #417 | $57.1M | 1.16x | +16.5% |
| VeThor (VTHO) | #356 | $70.6M | 0.90x | -18.7% |
| Cap (CAP) | #271 | $102.1M | 0.62x | +40.4% |
| Polymesh (POLYX) | #437 | $52.5M | 0.53x | -17.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 20% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 28% vs 60d 57%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 41% (0.7x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 59% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_POWRUSD | 2 | -69.4% | 195.0% |
| PF_FILUSD | 2 | -54.5% | 80.8% |
| PF_STEEMUSD | 2 | -46.2% | 187.8% |
| PF_ALCHUSD | 1 | +140.7% | 140.7% |
| PF_HFTUSD | 1 | -65.1% | 65.1% |
| PF_TRUMPUSD | 1 | +55.8% | 55.8% |
| PF_VIRTUALUSD | 1 | -53.7% | 72.4% |
| PF_NEARUSD | 1 | -51.4% | 51.4% |
| PF_ACEUSD | 1 | -32.5% | 32.5% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 248%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
