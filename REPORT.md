# Pond Scanner Report
**Scan time:** 2026-10-14 21:42 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +601.7% | $514,641 |
| 🟢 | PF_LINKUSD | +384.0% | $523,238 |
| 🟢 | PF_NEARUSD | +203.9% | $5,377,715 |
| 🟢 | PF_ZROUSD | -76.7% | $788,174 |
| 🟢 | PF_GRASSUSD | +66.0% | $633,343 |
| 🟢 | PF_STXUSD | +37.8% | $726,039 |
| 🟢 | PF_SUIUSD | +32.3% | $6,282,295 |
| 🟢 | PF_FILUSD | +31.1% | $2,017,016 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → gemini) — coinbase: $81,738.22, kraken: $81,752.30, gemini: $81,756.73
- ⚪ **ETH** gap **0.019%** (kraken → gemini) — coinbase: $2,421.86, kraken: $2,421.71, gemini: $2,422.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #482 | $47.2M | 0.99x | +22.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 28% vs 60d 44%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 44% vs 60d 63%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 34% (0.9x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 42% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +601.7% | 601.7% |
| PF_LINKUSD | 1 | +384.0% | 384.0% |
| PF_NEARUSD | 1 | +203.9% | 203.9% |
| PF_ZROUSD | 1 | -76.7% | 100.8% |
| PF_GRASSUSD | 1 | +66.0% | 66.0% |
| PF_STXUSD | 1 | +37.8% | 37.8% |
| PF_SUIUSD | 1 | +32.3% | 32.3% |
| PF_FILUSD | 1 | +31.1% | 31.1% |
| PF_JTOUSD | 1 | -30.9% | 38.6% |

**Resolved since last scan:** PF_INJUSD (crowded 2d, worst 626%), PF_PONSUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
