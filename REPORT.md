# Pond Scanner Report
**Scan time:** 2026-09-18 04:45 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +159.8% | $5,998,381 |
| 🟢 | PF_UNIUSD | -101.5% | $2,892,237 |
| 🟢 | PF_ETHFIUSD | +60.2% | $736,533 |
| 🟢 | PF_DOTUSD | +40.0% | $1,911,986 |
| 🟢 | PF_XRPUSD | +37.0% | $35,994,920 |
| 🟢 | PF_HFTUSD | +33.9% | $1,668,466 |
| 🟢 | PF_SUIUSD | +31.5% | $8,424,081 |
| ⚪ | PF_ASTERUSD | -23.3% | $559,815 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (gemini → coinbase) — coinbase: $77,381.46, kraken: $77,379.70, gemini: $77,369.84
- ⚪ **ETH** gap **0.131%** (gemini → kraken) — coinbase: $2,475.27, kraken: $2,475.29, gemini: $2,472.04

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #367 | $69.8M | 1.85x | +31.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 29% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 41% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 42% (0.4x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 60% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +159.8% | 159.8% |
| PF_UNIUSD | 2 | -101.5% | 311.9% |
| PF_ETHFIUSD | 1 | +60.2% | 60.2% |
| PF_DOTUSD | 1 | +40.0% | 40.0% |
| PF_XRPUSD | 1 | +37.0% | 37.0% |
| PF_HFTUSD | 1 | +33.9% | 33.9% |
| PF_SUIUSD | 1 | +31.5% | 31.5% |

**Resolved since last scan:** PF_LSKUSD (crowded 2d, worst 961%), PF_NATGASUSD (crowded 2d, worst 125%), PF_MUBARAKUSD (crowded 2d, worst 108%), PF_FILUSD (crowded 2d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
