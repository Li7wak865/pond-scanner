# Pond Scanner Report
**Scan time:** 2026-10-25 16:22 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -101.5% | $3,035,569 |
| 🟢 | PF_TIAUSD | -39.2% | $1,182,830 |
| ⚪ | PF_JUPUSD | -14.8% | $518,797 |
| ⚪ | PF_XRPUSD | +11.3% | $8,760,023 |
| ⚪ | PF_ENAUSD | -10.1% | $14,960,762 |
| ⚪ | PF_OPNUSD | -8.5% | $792,407 |
| ⚪ | PF_BICOUSD | +7.4% | $1,172,947 |
| ⚪ | PF_WLDUSD | -6.9% | $5,562,146 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.039%** (coinbase → gemini) — coinbase: $80,467.18, kraken: $80,471.30, gemini: $80,498.42
- ⚪ **ETH** gap **0.023%** (kraken → gemini) — coinbase: $2,341.71, kraken: $2,341.48, gemini: $2,342.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #322 | $77.6M | 3.98x | -19.2% |
| Threshold Network (T) | #378 | $62.9M | 3.33x | +24.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.28, realized vol 10d 23% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 25% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 31% (0.6x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -101.5% | 101.5% |
| PF_TIAUSD | 1 | -39.2% | 39.2% |

**Resolved since last scan:** PF_DOTUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
