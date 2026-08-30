# Pond Scanner Report
**Scan time:** 2026-08-30 11:55 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +98.2% | $1,274,185 |
| 🟢 | PF_ACEUSD | -79.1% | $1,419,149 |
| ⚪ | PF_WLDUSD | -22.7% | $1,132,308 |
| ⚪ | PF_UNIUSD | -21.0% | $703,488 |
| ⚪ | PF_VELOUSD | -19.4% | $2,674,700 |
| ⚪ | PF_HFTUSD | +18.3% | $1,740,461 |
| ⚪ | PF_SYNUSD | -15.0% | $529,923 |
| ⚪ | PF_SUSHIUSD | -14.3% | $886,056 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $78,127.58, kraken: $78,132.80, gemini: $78,138.75
- ⚪ **ETH** gap **0.014%** (kraken → gemini) — coinbase: $2,457.95, kraken: $2,457.94, gemini: $2,458.28

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #373 | $63.9M | 1.13x | +16.7% |
| 牛来 (Niu Lai) (牛来) | #253 | $108.7M | 0.72x | +105.4% |
| Seeker (SKR) | #258 | $105.6M | 0.65x | +55.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 49% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.58, realized vol 10d 60% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 12% vs 30d norm 37% (0.3x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 51% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 9 | -79.1% | 241.7% |
| PF_TRUMPUSD | 1 | +98.2% | 98.2% |

**Resolved since last scan:** PF_UNIUSD (crowded 1d, worst 144%), PF_NEARUSD (crowded 1d, worst 52%), PF_SYNUSD (crowded 1d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
