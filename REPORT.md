# Pond Scanner Report
**Scan time:** 2026-08-08 07:16 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +693.5% | $642,060 |
| 🟢 | PF_HFTUSD | +210.3% | $72,997,817 |
| 🟢 | PF_ACEUSD | -89.6% | $9,814,128 |
| 🟢 | PF_KAITOUSD | -74.3% | $781,182 |
| 🟢 | PF_GRASSUSD | +42.4% | $552,757 |
| 🟢 | PF_FILUSD | +32.6% | $1,342,753 |
| 🟢 | PF_NEARUSD | +32.5% | $1,819,503 |
| ⚪ | PF_ZBTUSD | -25.0% | $1,537,944 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (coinbase → gemini) — coinbase: $64,954.37, kraken: $64,958.00, gemini: $64,973.36
- ⚪ **ETH** gap **0.006%** (kraken → gemini) — coinbase: $1,915.05, kraken: $1,914.97, gemini: $1,915.09

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #493 | $57.0M | 4.54x | +41.8% |
| Momentum (MMT) | #434 | $48.3M | 2.88x | +41.3% |
| SpaceX (bStocks Tokenized Stock) (SPCXB) | #281 | $87.0M | 2.16x | +16.4% |
| Cap (CAP) | #391 | $54.7M | 0.92x | +17.0% |
| SkyAI (SKYAI) | #244 | $108.8M | 0.52x | +16.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 23% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 27% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 29% (0.6x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 41% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +693.5% | 929.8% |
| PF_ACEUSD | 2 | -89.6% | 501.6% |
| PF_KAITOUSD | 2 | -74.3% | 124.5% |
| PF_GRASSUSD | 2 | +42.4% | 67.4% |
| PF_HFTUSD | 1 | +210.3% | 210.3% |
| PF_FILUSD | 1 | +32.6% | 32.6% |
| PF_NEARUSD | 1 | +32.5% | 32.5% |

**Resolved since last scan:** PF_MONUSD (crowded 1d, worst 92%), PF_GRIFFAINUSD (crowded 1d, worst 47%), PF_MIRAUSD (crowded 1d, worst 38%), PF_SNXUSD (crowded 2d, worst 33%), PF_XTZUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
