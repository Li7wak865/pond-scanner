# Pond Scanner Report
**Scan time:** 2026-09-24 21:31 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +204.4% | $638,263 |
| 🟢 | PF_NEARUSD | -138.0% | $5,476,909 |
| 🟢 | PF_HFTUSD | -110.0% | $2,793,383 |
| 🟢 | PF_TRUMPUSD | +89.0% | $1,638,444 |
| 🟢 | PF_SPXUSD | +83.1% | $704,865 |
| 🟢 | PF_ZROUSD | +55.9% | $624,752 |
| 🟢 | PF_XPLUSD | +53.7% | $7,323,010 |
| 🟢 | PF_VIRTUALUSD | +47.8% | $751,248 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (kraken → coinbase) — coinbase: $84,438.54, kraken: $84,433.00, gemini: $84,435.99
- ⚪ **ETH** gap **0.002%** (gemini → coinbase) — coinbase: $2,689.73, kraken: $2,689.69, gemini: $2,689.68

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nillion (NIL) | #438 | $57.8M | 2.70x | +19.3% |
| Lisk (LSK) | #282 | $104.9M | 1.54x | +30.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 57% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 60% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 41% vs 30d norm 35% (1.2x)
- ⚪ **ETH** 24h vol 45% vs 30d norm 47% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -138.0% | 343.9% |
| PF_HFTUSD | 2 | -110.0% | 112.1% |
| PF_TRUMPUSD | 2 | +89.0% | 372.6% |
| PF_SPXUSD | 2 | +83.1% | 83.1% |
| PF_LINKUSD | 1 | +204.4% | 482.7% |
| PF_ZROUSD | 1 | +55.9% | 69.9% |
| PF_XPLUSD | 1 | +53.7% | 53.7% |
| PF_VIRTUALUSD | 1 | +47.8% | 57.1% |

**Resolved since last scan:** PF_MINAUSD (crowded 1d, worst 660%), PF_UNIUSD (crowded 2d, worst 546%), PF_LSKUSD (crowded 1d, worst 172%), PF_JTOUSD (crowded 1d, worst 74%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
