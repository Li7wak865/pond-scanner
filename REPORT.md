# Pond Scanner Report
**Scan time:** 2026-09-14 04:58 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +200.4% | $648,820 |
| 🟢 | PF_STEEMUSD | -187.8% | $3,774,860 |
| 🟢 | PF_POWRUSD | -162.8% | $6,506,690 |
| 🟢 | PF_VIRTUALUSD | -72.4% | $1,008,968 |
| 🟢 | PF_FILUSD | -51.6% | $3,645,903 |
| 🟢 | PF_HFTUSD | +35.7% | $2,718,228 |
| ⚪ | PF_DOTUSD | -29.6% | $1,753,380 |
| ⚪ | PF_XRPUSD | +23.0% | $9,540,919 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (gemini → coinbase) — coinbase: $77,608.61, kraken: $77,595.20, gemini: $77,593.27
- ⚪ **ETH** gap **0.039%** (kraken → coinbase) — coinbase: $2,513.01, kraken: $2,512.03, gemini: $2,512.83

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Teller (DEBIT) | #423 | $55.2M | 1.65x | +54.3% |
| VeThor (VTHO) | #323 | $78.4M | 1.15x | -22.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 19% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 28% vs 60d 57%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 41% (0.6x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 59% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | +200.4% | 247.8% |
| PF_STEEMUSD | 2 | -187.8% | 187.8% |
| PF_POWRUSD | 2 | -162.8% | 195.0% |
| PF_FILUSD | 2 | -51.6% | 80.8% |
| PF_VIRTUALUSD | 1 | -72.4% | 72.4% |
| PF_HFTUSD | 1 | +35.7% | 35.7% |

**Resolved since last scan:** PF_CATIUSD (crowded 2d, worst 86%), PF_ACEUSD (crowded 2d, worst 60%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
