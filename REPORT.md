# Pond Scanner Report
**Scan time:** 2026-09-27 16:58 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +445.2% | $818,381 |
| 🟢 | PF_LINKUSD | +219.8% | $665,033 |
| 🟢 | PF_NEARUSD | +166.8% | $3,898,556 |
| 🟢 | PF_TRUMPUSD | +165.7% | $546,618 |
| 🟢 | PF_AVAXUSD | +106.3% | $668,009 |
| 🟢 | PF_LSKUSD | -98.9% | $564,050 |
| 🟢 | PF_ETHFIUSD | +75.2% | $2,113,624 |
| 🟢 | PF_RUNEUSD | -55.1% | $1,224,303 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → gemini) — coinbase: $84,410.42, kraken: $84,412.00, gemini: $84,419.83
- ⚪ **ETH** gap **0.016%** (coinbase → gemini) — coinbase: $2,686.60, kraken: $2,686.76, gemini: $2,687.02

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SOON (SOON) | #265 | $114.4M | 1.43x | +55.8% |
| Amp (AMP) | #454 | $56.8M | 1.27x | -15.3% |
| Wormhole (W) | #289 | $101.7M | 1.09x | +20.2% |
| Arcium (ARX) | #423 | $61.3M | 0.82x | +27.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 50% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 34% (0.5x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 46% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | +165.7% | 372.6% |
| PF_UNIUSD | 2 | +445.2% | 445.2% |
| PF_LINKUSD | 2 | +219.8% | 364.0% |
| PF_NEARUSD | 2 | +166.8% | 255.3% |
| PF_AVAXUSD | 2 | +106.3% | 106.3% |
| PF_ETHFIUSD | 2 | +75.2% | 137.8% |
| PF_LSKUSD | 1 | -98.9% | 168.8% |
| PF_RUNEUSD | 1 | -55.1% | 102.5% |
| PF_FILUSD | 1 | +38.2% | 38.2% |

**Resolved since last scan:** PF_ARCUSD (crowded 1d, worst 110%), PF_HFTUSD (crowded 1d, worst 52%), PF_XRPUSD (crowded 1d, worst 51%), PF_ONDOUSD (crowded 1d, worst 50%), PF_DOTUSD (crowded 1d, worst 47%), PF_VETUSD (crowded 1d, worst 41%), PF_WLDUSD (crowded 2d, worst 93%), PF_2ZUSD (crowded 2d, worst 92%), PF_XPLUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
