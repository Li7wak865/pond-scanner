# Pond Scanner Report
**Scan time:** 2026-08-23 02:00 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +491.5% | $867,560 |
| 🟢 | PF_UNIUSD | +190.3% | $1,178,383 |
| 🟢 | PF_AVAXUSD | -133.3% | $739,707 |
| 🟢 | PF_RIVERUSD | +119.4% | $533,084 |
| 🟢 | PF_KAITOUSD | -96.7% | $638,494 |
| 🟢 | PF_JUPUSD | +96.4% | $717,755 |
| 🟢 | PF_NEARUSD | +91.6% | $4,991,634 |
| 🟢 | PF_ACEUSD | -70.2% | $4,418,350 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → gemini) — coinbase: $77,181.42, kraken: $77,186.90, gemini: $77,188.52
- ⚪ **ETH** gap **0.017%** (gemini → kraken) — coinbase: $2,422.88, kraken: $2,423.00, gemini: $2,422.60

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #451 | $48.5M | 2.58x | +47.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 61% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.64, realized vol 10d 110% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9982 (-0.18% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 33% vs 30d norm 36% (0.9x)
- ⚪ **ETH** 24h vol 64% vs 30d norm 51% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 4 | +491.5% | 819.3% |
| PF_UNIUSD | 4 | +190.3% | 371.9% |
| PF_TRUMPUSD | 4 | +46.8% | 332.5% |
| PF_SYNUSD | 3 | +50.8% | 505.9% |
| PF_JUPUSD | 2 | +96.4% | 97.3% |
| PF_NEARUSD | 2 | +91.6% | 142.8% |
| PF_ACEUSD | 2 | -70.2% | 70.2% |
| PF_ICPUSD | 2 | -54.1% | 54.1% |
| PF_FETUSD | 2 | +45.8% | 146.4% |
| PF_ETHFIUSD | 2 | +43.2% | 92.6% |
| PF_AVAXUSD | 1 | -133.3% | 133.3% |
| PF_RIVERUSD | 1 | +119.4% | 119.4% |
| PF_KAITOUSD | 1 | -96.7% | 96.7% |
| PF_POPCATUSD | 1 | -41.3% | 41.3% |
| PF_LDOUSD | 1 | -40.5% | 40.5% |
| PF_CRVUSD | 1 | +34.7% | 34.7% |

**Resolved since last scan:** PF_PNUTUSD (crowded 2d, worst 50%), PF_WUSD (crowded 2d, worst 42%), PF_XRPUSD (crowded 3d, worst 77%), PF_FARTCOINUSD (crowded 2d, worst 34%), PF_GOATUSD (crowded 2d, worst 33%), PF_MELANIAUSD (crowded 2d, worst 31%), PF_APTUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
