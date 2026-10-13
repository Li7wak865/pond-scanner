# Pond Scanner Report
**Scan time:** 2026-10-13 22:46 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -333.6% | $706,094 |
| 🟢 | PF_ATOMUSD | -161.4% | $648,771 |
| 🟢 | PF_BATUSD | -132.6% | $5,931,847 |
| 🟢 | PF_UNIUSD | -98.7% | $557,913 |
| 🟢 | PF_NEARUSD | +74.9% | $6,934,428 |
| 🟢 | PF_APTUSD | -54.2% | $1,264,212 |
| 🟢 | PF_RENDERUSD | -45.7% | $764,314 |
| 🟢 | PF_STXUSD | +41.7% | $1,619,284 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (gemini → coinbase) — coinbase: $83,429.29, kraken: $83,423.00, gemini: $83,421.20
- ⚪ **ETH** gap **0.051%** (coinbase → gemini) — coinbase: $2,508.69, kraken: $2,508.90, gemini: $2,509.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Amp (AMP) | #375 | $68.5M | 0.85x | +16.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 32% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.28, realized vol 10d 46% vs 60d 62%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 33% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 55% vs 30d norm 41% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | +74.9% | 314.3% |
| PF_INJUSD | 1 | -333.6% | 333.6% |
| PF_ATOMUSD | 1 | -161.4% | 161.4% |
| PF_BATUSD | 1 | -132.6% | 132.6% |
| PF_UNIUSD | 1 | -98.7% | 153.1% |
| PF_APTUSD | 1 | -54.2% | 62.2% |
| PF_RENDERUSD | 1 | -45.7% | 99.9% |
| PF_STXUSD | 1 | +41.7% | 41.7% |
| PF_ZROUSD | 1 | +36.1% | 132.8% |
| PF_XTZUSD | 1 | +32.6% | 32.6% |

**Resolved since last scan:** PF_OPNUSD (crowded 1d, worst 274%), PF_ICPUSD (crowded 1d, worst 72%), PF_TRUMPUSD (crowded 1d, worst 42%), PF_ONDOUSD (crowded 1d, worst 40%), PF_TIAUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
