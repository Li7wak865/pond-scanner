# Pond Scanner Report
**Scan time:** 2026-11-07 13:03 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -102.6% | $2,720,593 |
| 🟢 | PF_XTZUSD | -30.7% | $742,365 |
| ⚪ | PF_WLDUSD | -21.6% | $2,675,146 |
| ⚪ | PF_SUIUSD | -19.4% | $1,840,357 |
| ⚪ | PF_CRVUSD | +18.4% | $2,739,328 |
| ⚪ | PF_NEARUSD | +16.2% | $2,985,402 |
| ⚪ | PF_XRPUSD | +15.3% | $11,382,387 |
| ⚪ | PF_FETUSD | -10.4% | $5,112,934 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.030%** (coinbase → gemini) — coinbase: $75,806.25, kraken: $75,807.00, gemini: $75,829.03
- ⚪ **ETH** gap **0.036%** (coinbase → gemini) — coinbase: $2,239.19, kraken: $2,239.54, gemini: $2,240.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Magma Finance (MAGMA) | #417 | $53.3M | 0.85x | -17.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.27, realized vol 10d 50% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 68% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 35% (0.5x)
- ⚪ **ETH** 24h vol 20% vs 30d norm 49% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 4 | -102.6% | 178.3% |
| PF_XTZUSD | 1 | -30.7% | 30.7% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 163%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
