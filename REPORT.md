# Pond Scanner Report
**Scan time:** 2026-08-18 18:56 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -147.0% | $18,293,750 |
| 🟢 | PF_ETHFIUSD | -87.0% | $737,779 |
| 🟢 | PF_NEARUSD | -64.6% | $1,402,017 |
| 🟢 | PF_RAREUSD | +44.7% | $1,863,921 |
| ⚪ | PF_SYNUSD | -25.8% | $659,826 |
| ⚪ | PF_XRPUSD | +21.1% | $7,892,926 |
| ⚪ | PF_ALICEUSD | -20.5% | $3,828,015 |
| ⚪ | PF_HFTUSD | -19.0% | $1,918,876 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (kraken → coinbase) — coinbase: $64,728.73, kraken: $64,722.40, gemini: $64,724.29
- ⚪ **ETH** gap **0.011%** (kraken → coinbase) — coinbase: $1,914.89, kraken: $1,914.67, gemini: $1,914.79

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cysic (CYS) | #274 | $84.8M | 0.67x | +21.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 19% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 18% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 26% (0.9x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 35% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -147.0% | 732.3% |
| PF_ETHFIUSD | 1 | -87.0% | 135.5% |
| PF_NEARUSD | 1 | -64.6% | 64.6% |
| PF_RAREUSD | 1 | +44.7% | 52.8% |

**Resolved since last scan:** PF_HFTUSD (crowded 1d, worst 46%), PF_KAITOUSD (crowded 1d, worst 75%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
