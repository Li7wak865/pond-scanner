# Pond Scanner Report
**Scan time:** 2026-08-08 02:22 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +657.2% | $613,890 |
| 🟢 | PF_MONUSD | +91.5% | $1,397,195 |
| 🟢 | PF_KAITOUSD | -75.2% | $711,419 |
| 🟢 | PF_ACEUSD | -69.6% | $13,366,824 |
| 🟢 | PF_GRASSUSD | +67.4% | $536,003 |
| 🟢 | PF_GRIFFAINUSD | -46.9% | $1,414,844 |
| 🟢 | PF_MIRAUSD | -38.2% | $563,948 |
| 🟢 | PF_SNXUSD | -31.3% | $878,842 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (kraken → gemini) — coinbase: $64,870.12, kraken: $64,869.80, gemini: $64,880.04
- ⚪ **ETH** gap **0.013%** (gemini → kraken) — coinbase: $1,912.47, kraken: $1,912.53, gemini: $1,912.28

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Biconomy (BICO) | #494 | $56.2M | 5.20x | +42.0% |
| SpaceX (bStocks Tokenized Stock) (SPCXB) | #281 | $87.0M | 2.10x | +16.6% |
| ETHGas (GWEI) | #329 | $69.3M | 1.34x | +41.8% |
| Cap (CAP) | #384 | $57.6M | 0.85x | +16.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 23% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.08, realized vol 10d 27% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 29% (0.7x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 41% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +657.2% | 929.8% |
| PF_KAITOUSD | 2 | -75.2% | 124.5% |
| PF_ACEUSD | 2 | -69.6% | 501.6% |
| PF_GRASSUSD | 2 | +67.4% | 67.4% |
| PF_SNXUSD | 2 | -31.3% | 33.1% |
| PF_MONUSD | 1 | +91.5% | 91.5% |
| PF_GRIFFAINUSD | 1 | -46.9% | 46.9% |
| PF_MIRAUSD | 1 | -38.2% | 38.2% |
| PF_XTZUSD | 1 | +31.0% | 31.0% |

**Resolved since last scan:** PF_HFTUSD (crowded 2d, worst 149%), PF_FILUSD (crowded 2d, worst 46%), PF_MOODENGUSD (crowded 2d, worst 42%), PF_NEARUSD (crowded 2d, worst 55%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
