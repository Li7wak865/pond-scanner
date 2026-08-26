# Pond Scanner Report
**Scan time:** 2026-08-26 20:03 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SPXUSD | -136.2% | $696,626 |
| 🟢 | PF_ACEUSD | -80.6% | $970,129 |
| 🟢 | PF_STXUSD | -71.8% | $2,122,401 |
| 🟢 | PF_HFTUSD | -58.8% | $2,567,412 |
| 🟢 | PF_NEARUSD | +51.5% | $1,244,808 |
| 🟢 | PF_TRUMPUSD | -50.0% | $1,474,978 |
| 🟢 | PF_SUSD | -41.0% | $1,181,879 |
| 🟢 | PF_ONTUSD | -39.2% | $1,124,009 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (gemini → coinbase) — coinbase: $78,462.74, kraken: $78,460.00, gemini: $78,450.54
- ⚪ **ETH** gap **0.045%** (gemini → coinbase) — coinbase: $2,471.27, kraken: $2,470.46, gemini: $2,470.17

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #306 | $78.1M | 1.71x | +71.7% |
| Ontology (ONT) | #376 | $62.1M | 0.89x | +16.9% |
| 牛来 (Niu Lai) (牛来) | #483 | $46.0M | 0.55x | +28.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.60, realized vol 10d 108% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 52% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -80.6% | 241.7% |
| PF_TRUMPUSD | 2 | -50.0% | 417.1% |
| PF_SPXUSD | 1 | -136.2% | 136.2% |
| PF_STXUSD | 1 | -71.8% | 74.2% |
| PF_HFTUSD | 1 | -58.8% | 106.1% |
| PF_NEARUSD | 1 | +51.5% | 51.5% |
| PF_SUSD | 1 | -41.0% | 41.0% |
| PF_ONTUSD | 1 | -39.2% | 39.2% |

**Resolved since last scan:** PF_ALCHUSD (crowded 1d, worst 126%), PF_LINKUSD (crowded 3d, worst 478%), PF_ZROUSD (crowded 1d, worst 48%), PF_RENDERUSD (crowded 1d, worst 42%), PF_FETUSD (crowded 1d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
