# Pond Scanner Report
**Scan time:** 2026-08-22 06:59 UTC

**Flags this scan:** 46 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SPXUSD | -947.3% | $583,321 |
| 🟢 | PF_SYNUSD | +505.9% | $1,672,358 |
| 🟢 | PF_TRUMPUSD | -332.5% | $4,956,491 |
| 🟢 | PF_LINKUSD | +283.3% | $1,450,420 |
| 🟢 | PF_CATIUSD | +221.2% | $520,678 |
| 🟢 | PF_ACEUSD | -197.4% | $8,688,844 |
| 🟢 | PF_UNIUSD | +187.4% | $1,549,463 |
| 🟢 | PF_ZIGUSD | +187.0% | $1,159,615 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (gemini → coinbase) — coinbase: $77,489.23, kraken: $77,484.50, gemini: $77,473.22
- ⚪ **ETH** gap **0.037%** (gemini → kraken) — coinbase: $2,438.80, kraken: $2,438.99, gemini: $2,438.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| GALA (GALA) | #268 | $97.5M | 1.75x | +21.8% |
| Audiera (BEAT) | #423 | $54.3M | 1.15x | +32.5% |
| Tellor Tributes (TRB) | #436 | $52.6M | 1.01x | +25.2% |
| Prom (PROM) | #447 | $51.0M | 0.73x | +24.1% |
| 牛来 (Niu Lai) (牛来) | #393 | $58.9M | 0.55x | -15.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.68, realized vol 10d 60% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.63, realized vol 10d 108% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 99% vs 30d norm 36% (2.7x)
- 🟢 **ETH** 24h vol 114% vs 30d norm 51% (2.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | -332.5% | 332.5% |
| PF_LINKUSD | 3 | +283.3% | 819.3% |
| PF_ACEUSD | 3 | -197.4% | 217.7% |
| PF_UNIUSD | 3 | +187.4% | 187.4% |
| PF_SYNUSD | 2 | +505.9% | 505.9% |
| PF_ZIGUSD | 2 | +187.0% | 187.0% |
| PF_AVAXUSD | 2 | -131.5% | 440.9% |
| PF_LDOUSD | 2 | -118.1% | 118.1% |
| PF_GRASSUSD | 2 | +63.8% | 63.8% |
| PF_JTOUSD | 2 | -63.8% | 191.2% |
| PF_KAITOUSD | 2 | -59.3% | 137.5% |
| PF_XRPUSD | 2 | -39.3% | 76.9% |
| PF_SPXUSD | 1 | -947.3% | 947.3% |
| PF_CATIUSD | 1 | +221.2% | 221.2% |
| PF_ICPUSD | 1 | +182.3% | 182.3% |
| PF_JUPUSD | 1 | +169.9% | 169.9% |
| PF_IOTAUSD | 1 | +164.8% | 164.8% |
| PF_NEARUSD | 1 | -142.8% | 142.8% |
| PF_COTIUSD | 1 | -141.0% | 141.0% |
| PF_MELANIAUSD | 1 | -110.9% | 110.9% |
| PF_ETHFIUSD | 1 | +92.6% | 92.6% |
| PF_IMXUSD | 1 | +90.3% | 90.3% |
| PF_RENDERUSD | 1 | +87.5% | 87.5% |
| PF_OGNUSD | 1 | +81.7% | 81.7% |
| PF_MIRAUSD | 1 | +81.4% | 81.4% |
| PF_BLURUSD | 1 | +71.6% | 73.0% |
| PF_ASTERUSD | 1 | -68.0% | 68.0% |
| PF_DEEPUSD | 1 | +66.8% | 66.8% |
| PF_MOODENGUSD | 1 | -63.3% | 63.3% |
| PF_WLDUSD | 1 | -62.2% | 62.2% |
| PF_DOTUSD | 1 | +51.9% | 51.9% |
| PF_FETUSD | 1 | +51.9% | 51.9% |
| PF_PNUTUSD | 1 | -47.4% | 47.4% |
| PF_ARCUSD | 1 | +44.1% | 44.1% |
| PF_STXUSD | 1 | -38.9% | 38.9% |
| PF_FILUSD | 1 | -37.1% | 41.8% |
| PF_SWARMSUSD | 1 | +36.3% | 36.3% |
| PF_MANAUSD | 1 | +33.9% | 33.9% |
| PF_YGGUSD | 1 | +32.8% | 32.8% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 306%), PF_SUSD (crowded 1d, worst 130%), PF_ONTUSD (crowded 2d, worst 103%), PF_ONDOUSD (crowded 1d, worst 58%), PF_CRVUSD (crowded 1d, worst 55%), PF_FARTCOINUSD (crowded 1d, worst 48%), PF_TIAUSD (crowded 1d, worst 48%), PF_EIGENUSD (crowded 1d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
