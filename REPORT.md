# Pond Scanner Report
**Scan time:** 2026-10-03 05:20 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +364.1% | $876,123 |
| 🟢 | PF_LINKUSD | +329.1% | $796,559 |
| 🟢 | PF_MOVRUSD | -249.9% | $1,113,734 |
| 🟢 | PF_BATUSD | +215.7% | $648,542 |
| 🟢 | PF_SANDUSD | -78.5% | $32,178,118 |
| 🟢 | PF_NEARUSD | +73.4% | $2,987,726 |
| 🟢 | PF_ASTERUSD | +73.0% | $802,055 |
| 🟢 | PF_MANAUSD | -72.9% | $8,163,339 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → gemini) — coinbase: $84,585.12, kraken: $84,578.40, gemini: $84,587.99
- ⚪ **ETH** gap **0.009%** (coinbase → kraken) — coinbase: $2,676.57, kraken: $2,676.80, gemini: $2,676.59

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Enjin Coin (ENJ) | #367 | $73.6M | 1.85x | +19.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.37, realized vol 10d 12% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.27, realized vol 10d 11% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 35% (0.8x)
- ⚪ **ETH** 24h vol 36% vs 30d norm 46% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +364.1% | 543.2% |
| PF_LINKUSD | 3 | +329.1% | 329.1% |
| PF_MOVRUSD | 3 | -249.9% | 289.0% |
| PF_SANDUSD | 2 | -78.5% | 148.5% |
| PF_NEARUSD | 2 | +73.4% | 134.3% |
| PF_ZROUSD | 2 | -52.0% | 65.3% |
| PF_ETHFIUSD | 2 | +45.5% | 45.5% |
| PF_TRUMPUSD | 2 | +31.0% | 150.9% |
| PF_BATUSD | 1 | +215.7% | 215.7% |
| PF_ASTERUSD | 1 | +73.0% | 73.0% |
| PF_MANAUSD | 1 | -72.9% | 72.9% |
| PF_SYNUSD | 1 | -42.9% | 42.9% |

**Resolved since last scan:** PF_JUPUSD (crowded 2d, worst 48%), PF_DOTUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
