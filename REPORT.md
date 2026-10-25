# Pond Scanner Report
**Scan time:** 2026-10-25 04:43 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +100.0% | $6,012,365 |
| 🟢 | PF_ASTERUSD | +41.8% | $590,232 |
| 🟢 | PF_PONSUSD | +38.6% | $1,149,986 |
| 🟢 | PF_TIAUSD | -31.9% | $1,697,969 |
| ⚪ | PF_XRPUSD | +20.0% | $9,642,024 |
| ⚪ | PF_KAITOUSD | -18.0% | $655,727 |
| ⚪ | PF_TRXUSD | -15.8% | $1,303,666 |
| ⚪ | PF_OPNUSD | -14.1% | $1,003,241 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → gemini) — coinbase: $80,827.88, kraken: $80,825.50, gemini: $80,835.70
- ⚪ **ETH** gap **0.020%** (coinbase → gemini) — coinbase: $2,365.54, kraken: $2,365.74, gemini: $2,366.01

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #293 | $90.9M | 2.08x | -51.8% |
| Threshold Network (T) | #353 | $69.9M | 1.55x | +33.8% |
| Janction (JCT) | #354 | $69.5M | 1.22x | +130.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.27, realized vol 10d 23% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 43% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TIAUSD | 2 | -31.9% | 37.5% |
| PF_NEARUSD | 1 | +100.0% | 100.0% |
| PF_ASTERUSD | 1 | +41.8% | 41.8% |
| PF_PONSUSD | 1 | +38.6% | 38.6% |

**Resolved since last scan:** PF_FILUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
