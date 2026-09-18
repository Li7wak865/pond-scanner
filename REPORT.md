# Pond Scanner Report
**Scan time:** 2026-09-18 11:17 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +583.1% | $3,264,329 |
| 🟢 | PF_HFTUSD | +100.7% | $1,946,111 |
| 🟢 | PF_STGUSD | -76.9% | $565,417 |
| 🟢 | PF_ASTERUSD | -75.0% | $633,139 |
| 🟢 | PF_DOTUSD | +58.6% | $2,160,836 |
| 🟢 | PF_INITUSD | -53.6% | $643,060 |
| 🟢 | PF_EIGENUSD | +48.9% | $775,897 |
| 🟢 | PF_TIAUSD | +40.7% | $928,890 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (kraken → coinbase) — coinbase: $78,097.49, kraken: $78,089.80, gemini: $78,090.69
- ⚪ **ETH** gap **0.173%** (gemini → coinbase) — coinbase: $2,502.60, kraken: $2,502.39, gemini: $2,498.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #412 | $58.9M | 4.29x | +94.1% |
| Canopy (CNPY) | #416 | $58.3M | 1.18x | +39.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.01, realized vol 10d 31% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.05, realized vol 10d 42% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 43% (0.5x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 60% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +30.8% | 159.8% |
| PF_UNIUSD | 2 | +583.1% | 583.1% |
| PF_HFTUSD | 1 | +100.7% | 100.7% |
| PF_STGUSD | 1 | -76.9% | 76.9% |
| PF_ASTERUSD | 1 | -75.0% | 75.0% |
| PF_DOTUSD | 1 | +58.6% | 58.6% |
| PF_INITUSD | 1 | -53.6% | 53.6% |
| PF_EIGENUSD | 1 | +48.9% | 48.9% |
| PF_TIAUSD | 1 | +40.7% | 40.7% |
| PF_TRUMPUSD | 1 | +37.0% | 37.0% |
| PF_WLDUSD | 1 | +35.5% | 35.5% |
| PF_SUIUSD | 1 | +33.1% | 33.1% |
| PF_XRPUSD | 1 | +31.1% | 37.0% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 1d, worst 60%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
