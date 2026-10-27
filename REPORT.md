# Pond Scanner Report
**Scan time:** 2026-10-27 12:14 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +303.9% | $2,373,653 |
| 🟢 | PF_XRPUSD | +44.2% | $9,154,468 |
| 🟢 | PF_SYNUSD | +40.0% | $3,609,487 |
| 🟢 | PF_TIAUSD | +33.4% | $775,962 |
| 🟢 | PF_BBUSD | +32.2% | $684,905 |
| ⚪ | PF_FILUSD | +20.1% | $1,084,483 |
| ⚪ | PF_ACEUSD | +16.8% | $2,233,685 |
| ⚪ | PF_ZROUSD | -13.8% | $596,628 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (kraken → gemini) — coinbase: $79,756.04, kraken: $79,742.10, gemini: $79,761.99
- ⚪ **ETH** gap **0.029%** (kraken → gemini) — coinbase: $2,310.29, kraken: $2,310.20, gemini: $2,310.86

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Huma Finance (HUMA) | #466 | $47.6M | 1.94x | +43.7% |
| Dolphin (POD) | #416 | $53.0M | 0.83x | +49.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 24% vs 60d 34%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9968 (-0.32% vs peg)
- ⚪ **USDT** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 31% (0.9x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 43% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +303.9% | 303.9% |
| PF_SYNUSD | 2 | +40.0% | 52.1% |
| PF_XRPUSD | 1 | +44.2% | 44.2% |
| PF_TIAUSD | 1 | +33.4% | 39.5% |
| PF_BBUSD | 1 | +32.2% | 32.2% |

**Resolved since last scan:** PF_APTUSD (crowded 1d, worst 58%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
