# Pond Scanner Report
**Scan time:** 2026-08-22 13:01 UTC

**Flags this scan:** 22 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +621.7% | $1,280,088 |
| 🟢 | PF_UNIUSD | +307.1% | $1,348,674 |
| 🟢 | PF_TRUMPUSD | -280.7% | $6,325,205 |
| 🟢 | PF_POPCATUSD | +246.1% | $3,116,020 |
| 🟢 | PF_ZIGUSD | +179.1% | $1,653,586 |
| 🟢 | PF_FETUSD | +120.0% | $19,193,834 |
| 🟢 | PF_AVAXUSD | +108.6% | $813,043 |
| 🟢 | PF_RIVERUSD | +81.9% | $508,054 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.006%** (gemini → kraken) — coinbase: $77,294.34, kraken: $77,298.10, gemini: $77,293.35
- ⚪ **ETH** gap **0.012%** (gemini → kraken) — coinbase: $2,428.47, kraken: $2,428.61, gemini: $2,428.33

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Audiera (BEAT) | #444 | $50.9M | 1.21x | +25.7% |
| 牛来 (Niu Lai) (牛来) | #405 | $55.5M | 0.51x | -19.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.66, realized vol 10d 60% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.61, realized vol 10d 109% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **USDe** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 45% vs 30d norm 36% (1.2x)
- ⚪ **ETH** 24h vol 89% vs 30d norm 50% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +621.7% | 819.3% |
| PF_UNIUSD | 3 | +307.1% | 307.1% |
| PF_TRUMPUSD | 3 | -280.7% | 332.5% |
| PF_ZIGUSD | 2 | +179.1% | 187.0% |
| PF_AVAXUSD | 2 | +108.6% | 440.9% |
| PF_SYNUSD | 2 | +80.8% | 505.9% |
| PF_LDOUSD | 2 | +52.6% | 118.1% |
| PF_XRPUSD | 2 | -34.3% | 76.9% |
| PF_POPCATUSD | 1 | +246.1% | 246.1% |
| PF_FETUSD | 1 | +120.0% | 120.0% |
| PF_RIVERUSD | 1 | +81.9% | 81.9% |
| PF_NEARUSD | 1 | +72.2% | 142.8% |
| PF_GRIFFAINUSD | 1 | +57.3% | 57.3% |
| PF_RAREUSD | 1 | -55.6% | 55.6% |
| PF_ETHFIUSD | 1 | +52.2% | 92.6% |
| PF_ARCUSD | 1 | -46.5% | 46.5% |
| PF_MOODENGUSD | 1 | +41.0% | 63.3% |
| PF_EIGENUSD | 1 | -36.6% | 36.6% |
| PF_ONDOUSD | 1 | -34.0% | 34.0% |
| PF_COTIUSD | 1 | -33.0% | 141.0% |

**Resolved since last scan:** PF_SPXUSD (crowded 1d, worst 947%), PF_CATIUSD (crowded 1d, worst 221%), PF_ACEUSD (crowded 3d, worst 218%), PF_ICPUSD (crowded 1d, worst 182%), PF_JUPUSD (crowded 1d, worst 170%), PF_IOTAUSD (crowded 1d, worst 165%), PF_MELANIAUSD (crowded 1d, worst 111%), PF_IMXUSD (crowded 1d, worst 90%), PF_RENDERUSD (crowded 1d, worst 87%), PF_OGNUSD (crowded 1d, worst 82%), PF_MIRAUSD (crowded 1d, worst 81%), PF_BLURUSD (crowded 1d, worst 73%), PF_ASTERUSD (crowded 1d, worst 68%), PF_DEEPUSD (crowded 1d, worst 67%), PF_GRASSUSD (crowded 2d, worst 64%), PF_JTOUSD (crowded 2d, worst 191%), PF_WLDUSD (crowded 1d, worst 62%), PF_KAITOUSD (crowded 2d, worst 137%), PF_DOTUSD (crowded 1d, worst 52%), PF_PNUTUSD (crowded 1d, worst 47%), PF_STXUSD (crowded 1d, worst 39%), PF_FILUSD (crowded 1d, worst 42%), PF_SWARMSUSD (crowded 1d, worst 36%), PF_MANAUSD (crowded 1d, worst 34%), PF_YGGUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
