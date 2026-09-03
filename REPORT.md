# Pond Scanner Report
**Scan time:** 2026-09-03 11:16 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -226.0% | $1,541,144 |
| 🟢 | PF_HFTUSD | +109.2% | $1,518,569 |
| 🟢 | PF_DEEPUSD | +66.3% | $1,503,893 |
| 🟢 | PF_UNIUSD | -51.8% | $1,031,411 |
| 🟢 | PF_NEARUSD | +35.4% | $708,952 |
| 🟢 | PF_ASTERUSD | -32.1% | $744,144 |
| ⚪ | PF_XPLUSD | +27.5% | $6,412,365 |
| ⚪ | PF_JUPUSD | +26.0% | $625,622 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.034%** (gemini → coinbase) — coinbase: $77,829.20, kraken: $77,825.80, gemini: $77,802.67
- ⚪ **ETH** gap **0.022%** (kraken → gemini) — coinbase: $2,400.59, kraken: $2,400.21, gemini: $2,400.73

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #438 | $49.7M | 1.07x | -21.9% |
| Cap (CAP) | #322 | $76.2M | 0.60x | -29.8% |
| Cysic (CYS) | #464 | $46.7M | 0.53x | -15.4% |
| Spark (SPK) | #339 | $72.3M | 0.52x | +15.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.55, realized vol 10d 25% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 32% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 38% (0.7x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | -51.8% | 280.5% |
| PF_ACEUSD | 3 | -226.0% | 304.8% |
| PF_HFTUSD | 2 | +109.2% | 109.2% |
| PF_DEEPUSD | 1 | +66.3% | 66.3% |
| PF_NEARUSD | 1 | +35.4% | 35.4% |
| PF_ASTERUSD | 1 | -32.1% | 32.1% |

**Resolved since last scan:** PF_XRPUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
