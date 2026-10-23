# Pond Scanner Report
**Scan time:** 2026-10-23 11:40 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BATUSD | -48.9% | $3,110,850 |
| 🟢 | PF_XRPUSD | +47.7% | $15,133,384 |
| ⚪ | PF_TIAUSD | +25.6% | $2,418,436 |
| ⚪ | PF_WLDUSD | +22.8% | $8,277,666 |
| ⚪ | PF_TRUMPUSD | -21.5% | $869,021 |
| ⚪ | PF_ATOMUSD | -19.0% | $586,780 |
| ⚪ | PF_ACEUSD | +17.4% | $4,805,175 |
| ⚪ | PF_PONSUSD | +16.7% | $871,379 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $81,517.73, kraken: $81,519.40, gemini: $81,532.70
- ⚪ **ETH** gap **0.009%** (coinbase → kraken) — coinbase: $2,395.68, kraken: $2,395.89, gemini: $2,395.68

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #316 | $81.2M | 4.02x | +94.8% |
| DAPPOS (DOS) | #472 | $48.0M | 0.55x | +16.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 26% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.36, realized vol 10d 31% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 32% (0.8x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 43% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_BATUSD | 2 | -48.9% | 52.9% |
| PF_XRPUSD | 1 | +47.7% | 47.7% |

**Resolved since last scan:** PF_OPNUSD (crowded 1d, worst 225%), PF_NEARUSD (crowded 2d, worst 176%), PF_ATOMUSD (crowded 1d, worst 61%), PF_FILUSD (crowded 1d, worst 53%), PF_TRUMPUSD (crowded 2d, worst 47%), PF_PONSUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
