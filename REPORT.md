# Pond Scanner Report
**Scan time:** 2026-08-24 18:59 UTC

**Flags this scan:** 20 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_RIVERUSD | -275.7% | $639,684 |
| 🟢 | PF_LINKUSD | +223.0% | $732,965 |
| 🟢 | PF_STORJUSD | -214.3% | $1,608,207 |
| 🟢 | PF_NEARUSD | -166.1% | $5,602,031 |
| 🟢 | PF_UNIUSD | -160.6% | $658,471 |
| 🟢 | PF_ACEUSD | -115.2% | $1,341,182 |
| 🟢 | PF_RENDERUSD | -72.1% | $592,766 |
| 🟢 | PF_SYNUSD | +64.8% | $636,806 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (kraken → coinbase) — coinbase: $78,926.48, kraken: $78,918.70, gemini: $78,924.85
- ⚪ **ETH** gap **0.053%** (kraken → gemini) — coinbase: $2,473.91, kraken: $2,473.70, gemini: $2,475.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Prom (PROM) | #353 | $67.5M | 1.46x | +28.9% |
| Spark (SPK) | #389 | $59.8M | 1.24x | -16.1% |
| Velvet (VELVET) | #305 | $80.9M | 0.69x | -73.9% |
| Amp (AMP) | #491 | $44.5M | 0.55x | +18.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.67, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.66, realized vol 10d 108% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 51% vs 30d norm 37% (1.4x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 52% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -115.2% | 241.7% |
| PF_RIVERUSD | 1 | -275.7% | 275.7% |
| PF_LINKUSD | 1 | +223.0% | 223.0% |
| PF_STORJUSD | 1 | -214.3% | 214.3% |
| PF_NEARUSD | 1 | -166.1% | 166.1% |
| PF_UNIUSD | 1 | -160.6% | 160.6% |
| PF_RENDERUSD | 1 | -72.1% | 72.1% |
| PF_SYNUSD | 1 | +64.8% | 478.3% |
| PF_PNUTUSD | 1 | -63.0% | 63.0% |
| PF_HFTUSD | 1 | -62.7% | 110.1% |
| PF_KAITOUSD | 1 | -45.7% | 45.7% |
| PF_APTUSD | 1 | -44.9% | 44.9% |
| PF_GRASSUSD | 1 | +40.0% | 65.2% |
| PF_XRPUSD | 1 | -39.3% | 51.4% |
| PF_LDOUSD | 1 | -35.1% | 35.9% |
| PF_XTZUSD | 1 | -32.5% | 32.5% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 5d, worst 333%), PF_ETHFIUSD (crowded 1d, worst 92%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
