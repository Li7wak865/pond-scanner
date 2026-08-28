# Pond Scanner Report
**Scan time:** 2026-08-28 11:24 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -325.6% | $540,063 |
| 🟢 | PF_TRUMPUSD | -200.9% | $3,912,932 |
| 🟢 | PF_UNIUSD | -93.8% | $558,868 |
| 🟢 | PF_SPXUSD | +90.5% | $578,042 |
| 🟢 | PF_NEARUSD | -57.1% | $623,413 |
| 🟢 | PF_ACEUSD | -47.3% | $801,816 |
| ⚪ | PF_MELANIAUSD | -27.5% | $901,480 |
| ⚪ | PF_JTOUSD | -27.0% | $771,119 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.037%** (kraken → coinbase) — coinbase: $79,768.50, kraken: $79,739.10, gemini: $79,757.12
- ⚪ **ETH** gap **0.020%** (gemini → coinbase) — coinbase: $2,509.11, kraken: $2,508.74, gemini: $2,508.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| USD.AI (CHIP) | #295 | $86.3M | 0.53x | +15.1% |
| Beam (BEAM) | #300 | $86.0M | 0.52x | -17.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.63, realized vol 10d 59% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.60, realized vol 10d 109% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 51% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 7 | -47.3% | 241.7% |
| PF_TRUMPUSD | 4 | -200.9% | 417.1% |
| PF_SPXUSD | 3 | +90.5% | 201.0% |
| PF_NEARUSD | 3 | -57.1% | 75.4% |
| PF_MOVRUSD | 2 | -325.6% | 328.0% |
| PF_UNIUSD | 1 | -93.8% | 93.8% |

**Resolved since last scan:** PF_RUNEUSD (crowded 2d, worst 170%), PF_HFTUSD (crowded 3d, worst 106%), PF_STXUSD (crowded 2d, worst 55%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
