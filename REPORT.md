# Pond Scanner Report
**Scan time:** 2026-09-02 21:04 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -184.8% | $1,846,136 |
| 🟢 | PF_ACEUSD | -180.7% | $3,126,785 |
| 🟢 | PF_HFTUSD | +108.4% | $931,948 |
| 🟢 | PF_NEARUSD | +63.5% | $945,201 |
| 🟢 | PF_SYRUPUSD | -53.2% | $739,176 |
| 🟢 | PF_ICXUSD | +38.1% | $506,669 |
| 🟢 | PF_VIRTUALUSD | +38.0% | $941,433 |
| 🟢 | PF_ASTERUSD | -38.0% | $610,230 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → gemini) — coinbase: $77,314.40, kraken: $77,314.70, gemini: $77,322.75
- ⚪ **ETH** gap **0.018%** (coinbase → kraken) — coinbase: $2,391.80, kraken: $2,392.24, gemini: $2,392.21

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #395 | $58.5M | 2.51x | +45.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 26% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 33% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 38% (0.7x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -184.8% | 280.5% |
| PF_ACEUSD | 2 | -180.7% | 304.8% |
| PF_HFTUSD | 1 | +108.4% | 108.4% |
| PF_NEARUSD | 1 | +63.5% | 63.5% |
| PF_SYRUPUSD | 1 | -53.2% | 186.3% |
| PF_ICXUSD | 1 | +38.1% | 38.1% |
| PF_VIRTUALUSD | 1 | +38.0% | 38.0% |
| PF_ASTERUSD | 1 | -38.0% | 81.9% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 117%), PF_MUBARAKUSD (crowded 1d, worst 41%), PF_XRPUSD (crowded 1d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
