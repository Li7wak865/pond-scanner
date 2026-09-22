# Pond Scanner Report
**Scan time:** 2026-09-22 21:20 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +416.6% | $1,234,728 |
| 🟢 | PF_NEARUSD | -380.6% | $8,102,865 |
| 🟢 | PF_ETHFIUSD | +115.2% | $795,774 |
| 🟢 | PF_SOLUSD | -91.7% | $718,355 |
| 🟢 | PF_TRUMPUSD | +83.2% | $1,722,169 |
| 🟢 | PF_LINKUSD | +74.8% | $590,718 |
| 🟢 | PF_FILUSD | -70.9% | $1,467,907 |
| 🟢 | PF_SPXUSD | +66.4% | $525,360 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → gemini) — coinbase: $86,255.53, kraken: $86,260.20, gemini: $86,268.60
- ⚪ **ETH** gap **0.014%** (kraken → coinbase) — coinbase: $2,749.66, kraken: $2,749.27, gemini: $2,749.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #352 | $77.6M | 3.41x | +77.8% |
| Aurora (AURORA) | #392 | $68.7M | 0.63x | +55.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.34, realized vol 10d 55% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.36, realized vol 10d 59% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 30% vs 30d norm 36% (0.8x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 48% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 6 | +416.6% | 624.1% |
| PF_NEARUSD | 3 | -380.6% | 457.9% |
| PF_TRUMPUSD | 2 | +83.2% | 207.1% |
| PF_LINKUSD | 2 | +74.8% | 725.7% |
| PF_RENDERUSD | 2 | +41.8% | 209.9% |
| PF_ETHFIUSD | 1 | +115.2% | 115.2% |
| PF_SOLUSD | 1 | -91.7% | 91.7% |
| PF_FILUSD | 1 | -70.9% | 70.9% |
| PF_SPXUSD | 1 | +66.4% | 68.9% |
| PF_LSKUSD | 1 | -54.0% | 290.1% |
| PF_BIGTIMEUSD | 1 | +36.9% | 36.9% |
| PF_ASTERUSD | 1 | +33.8% | 33.8% |
| PF_AVAXUSD | 1 | +33.0% | 135.6% |
| PF_DOTUSD | 1 | +32.2% | 32.2% |
| PF_RUNEUSD | 1 | +30.5% | 43.6% |

**Resolved since last scan:** PF_HFTUSD (crowded 1d, worst 109%), PF_MINAUSD (crowded 1d, worst 99%), PF_BLURUSD (crowded 1d, worst 87%), PF_XRPUSD (crowded 1d, worst 50%), PF_APTUSD (crowded 1d, worst 49%), PF_VIRTUALUSD (crowded 1d, worst 45%), PF_JTOUSD (crowded 1d, worst 65%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
