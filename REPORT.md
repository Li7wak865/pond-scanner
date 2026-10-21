# Pond Scanner Report
**Scan time:** 2026-10-21 11:50 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -102.5% | $715,899 |
| 🟢 | PF_TRUMPUSD | +83.8% | $663,273 |
| 🟢 | PF_BATUSD | +75.2% | $5,627,740 |
| 🟢 | PF_NEARUSD | +60.9% | $5,812,164 |
| 🟢 | PF_ZROUSD | +53.1% | $676,896 |
| 🟢 | PF_ASTERUSD | +33.2% | $716,316 |
| ⚪ | PF_FILUSD | +29.9% | $2,770,087 |
| ⚪ | PF_SUIUSD | +15.4% | $3,887,190 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (gemini → coinbase) — coinbase: $83,401.15, kraken: $83,392.00, gemini: $83,386.52
- ⚪ **ETH** gap **0.009%** (coinbase → gemini) — coinbase: $2,465.07, kraken: $2,465.16, gemini: $2,465.30

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| IOST (IOST) | #439 | $53.6M | 4.69x | +83.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 24% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.32, realized vol 10d 34% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **PYUSD** $1.0010 (+0.10% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 36% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 60% vs 30d norm 42% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 3 | +53.1% | 165.8% |
| PF_TRUMPUSD | 2 | +83.8% | 93.4% |
| PF_ASTERUSD | 2 | +33.2% | 55.7% |
| PF_UNIUSD | 1 | -102.5% | 102.5% |
| PF_BATUSD | 1 | +75.2% | 75.2% |
| PF_NEARUSD | 1 | +60.9% | 60.9% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 279%), PF_ACEUSD (crowded 1d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
