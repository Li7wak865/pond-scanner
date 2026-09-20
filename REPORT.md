# Pond Scanner Report
**Scan time:** 2026-09-20 20:50 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -184.9% | $6,230,436 |
| 🟢 | PF_AVAXUSD | +162.6% | $2,516,162 |
| 🟢 | PF_TRUMPUSD | +136.7% | $647,096 |
| 🟢 | PF_UNIUSD | +129.2% | $837,640 |
| 🟢 | PF_INJUSD | -100.8% | $633,230 |
| 🟢 | PF_LINKUSD | +82.3% | $545,332 |
| 🟢 | PF_XRPUSD | +48.9% | $13,760,656 |
| 🟢 | PF_SUIUSD | +47.8% | $12,439,577 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → gemini) — coinbase: $81,128.57, kraken: $81,124.80, gemini: $81,133.50
- ⚪ **ETH** gap **0.055%** (coinbase → gemini) — coinbase: $2,636.74, kraken: $2,637.19, gemini: $2,638.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #478 | $49.4M | 6.01x | -30.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 42% vs 60d 41%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 55% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 35% (0.7x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 50% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +129.2% | 624.1% |
| PF_AVAXUSD | 2 | +162.6% | 168.4% |
| PF_NEARUSD | 1 | -184.9% | 239.5% |
| PF_TRUMPUSD | 1 | +136.7% | 136.7% |
| PF_INJUSD | 1 | -100.8% | 100.8% |
| PF_LINKUSD | 1 | +82.3% | 82.3% |
| PF_XRPUSD | 1 | +48.9% | 48.9% |
| PF_SUIUSD | 1 | +47.8% | 47.8% |
| PF_FILUSD | 1 | -30.9% | 43.5% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 275%), PF_HFTUSD (crowded 3d, worst 107%), PF_CATIUSD (crowded 1d, worst 73%), PF_JTOUSD (crowded 1d, worst 58%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
