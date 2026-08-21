# Pond Scanner Report
**Scan time:** 2026-08-21 18:56 UTC

**Flags this scan:** 25 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_AVAXUSD | +277.0% | $598,764 |
| 🟢 | PF_PNUTUSD | +236.1% | $4,923,182 |
| 🟢 | PF_TRUMPUSD | +140.2% | $1,686,017 |
| 🟢 | PF_LINKUSD | -115.7% | $811,056 |
| 🟢 | PF_UNIUSD | +95.6% | $1,096,100 |
| 🟢 | PF_JTOUSD | -77.5% | $549,959 |
| 🟢 | PF_NEARUSD | +68.6% | $3,292,503 |
| 🟢 | PF_SYNUSD | +68.0% | $1,187,611 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.042%** (gemini → coinbase) — coinbase: $76,934.00, kraken: $76,932.60, gemini: $76,902.00
- ⚪ **ETH** gap **0.055%** (gemini → coinbase) — coinbase: $2,414.02, kraken: $2,413.33, gemini: $2,412.70

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Audiera (BEAT) | #394 | $58.2M | 1.01x | +45.7% |
| Spark (SPK) | #423 | $53.7M | 0.89x | +19.7% |
| Berachain (BERA) | #379 | $62.6M | 0.64x | +21.3% |
| Prom (PROM) | #460 | $49.0M | 0.56x | +28.0% |
| Tellor Tributes (TRB) | #470 | $48.0M | 0.54x | +18.1% |
| RedStone (RED) | #384 | $61.4M | 0.50x | +20.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.74, realized vol 10d 53% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.77, realized vol 10d 99% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9982 (-0.18% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 100% vs 30d norm 35% (2.8x)
- ⚪ **ETH** 24h vol 80% vs 30d norm 48% (1.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 2 | +140.2% | 140.2% |
| PF_LINKUSD | 2 | -115.7% | 676.6% |
| PF_UNIUSD | 2 | +95.6% | 152.6% |
| PF_ACEUSD | 2 | -62.5% | 217.7% |
| PF_AVAXUSD | 1 | +277.0% | 440.9% |
| PF_PNUTUSD | 1 | +236.1% | 236.1% |
| PF_JTOUSD | 1 | -77.5% | 152.5% |
| PF_NEARUSD | 1 | +68.6% | 146.0% |
| PF_SYNUSD | 1 | +68.0% | 76.6% |
| PF_KAITOUSD | 1 | -65.2% | 137.5% |
| PF_FETUSD | 1 | +61.5% | 61.5% |
| PF_GRASSUSD | 1 | +51.2% | 51.2% |
| PF_APTUSD | 1 | +40.3% | 42.7% |
| PF_STXUSD | 1 | +37.4% | 718.1% |
| PF_XRPUSD | 1 | +35.6% | 76.9% |
| PF_ONTUSD | 1 | -35.3% | 103.2% |
| PF_ZIGUSD | 1 | +34.0% | 34.0% |
| PF_LDOUSD | 1 | -32.5% | 49.1% |

**Resolved since last scan:** PF_SUIUSD (crowded 1d, worst 82%), PF_DOTUSD (crowded 1d, worst 62%), PF_ALICEUSD (crowded 1d, worst 60%), PF_ASTERUSD (crowded 1d, worst 57%), PF_FARTCOINUSD (crowded 1d, worst 48%), PF_VIRTUALUSD (crowded 1d, worst 51%), PF_TIAUSD (crowded 1d, worst 43%), PF_MANAUSD (crowded 1d, worst 36%), PF_JUPUSD (crowded 2d, worst 59%), PF_ONDOUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
