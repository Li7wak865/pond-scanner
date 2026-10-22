# Pond Scanner Report
**Scan time:** 2026-10-22 17:11 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +175.7% | $3,492,730 |
| 🟢 | PF_ZROUSD | +148.2% | $713,327 |
| 🟢 | PF_FILUSD | -63.0% | $4,425,630 |
| 🟢 | PF_BATUSD | +51.6% | $2,935,518 |
| 🟢 | PF_TIAUSD | -44.5% | $4,967,825 |
| 🟢 | PF_IMXUSD | -32.1% | $788,492 |
| 🟢 | PF_WLDUSD | +30.5% | $5,482,878 |
| ⚪ | PF_TRUMPUSD | -23.2% | $1,127,633 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.033%** (coinbase → gemini) — coinbase: $81,079.94, kraken: $81,080.50, gemini: $81,106.86
- ⚪ **ETH** gap **0.005%** (coinbase → kraken) — coinbase: $2,374.15, kraken: $2,374.28, gemini: $2,374.23

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| AltLayer (ALT) | #384 | $62.1M | 2.02x | -43.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 29% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.36, realized vol 10d 36% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 32% (0.9x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +148.2% | 148.2% |
| PF_NEARUSD | 1 | +175.7% | 175.7% |
| PF_FILUSD | 1 | -63.0% | 63.0% |
| PF_BATUSD | 1 | +51.6% | 51.6% |
| PF_TIAUSD | 1 | -44.5% | 44.5% |
| PF_IMXUSD | 1 | -32.1% | 53.1% |
| PF_WLDUSD | 1 | +30.5% | 30.5% |

**Resolved since last scan:** PF_DOTUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
