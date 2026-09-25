# Pond Scanner Report
**Scan time:** 2026-09-25 17:12 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +229.1% | $1,075,766 |
| 🟢 | PF_LSKUSD | -156.6% | $1,776,974 |
| 🟢 | PF_TRUMPUSD | +144.2% | $590,231 |
| 🟢 | PF_RUNEUSD | +116.3% | $504,011 |
| 🟢 | PF_LINKUSD | -88.9% | $1,024,491 |
| 🟢 | PF_RAREUSD | -72.0% | $1,014,881 |
| 🟢 | PF_ASTERUSD | +63.1% | $864,883 |
| 🟢 | PF_MINAUSD | -61.8% | $579,703 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $83,898.09, kraken: $83,901.00, gemini: $83,908.70
- ⚪ **ETH** gap **0.019%** (kraken → gemini) — coinbase: $2,688.86, kraken: $2,688.68, gemini: $2,689.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #398 | $66.9M | 2.40x | +55.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 52% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 49% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 35% (0.6x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 47% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +144.2% | 372.6% |
| PF_NEARUSD | 3 | +58.9% | 404.8% |
| PF_LINKUSD | 2 | -88.9% | 482.7% |
| PF_UNIUSD | 1 | +229.1% | 229.1% |
| PF_LSKUSD | 1 | -156.6% | 156.6% |
| PF_RUNEUSD | 1 | +116.3% | 116.3% |
| PF_RAREUSD | 1 | -72.0% | 72.0% |
| PF_ASTERUSD | 1 | +63.1% | 63.1% |
| PF_MINAUSD | 1 | -61.8% | 61.8% |
| PF_XRPUSD | 1 | +50.4% | 50.4% |
| PF_SPXUSD | 1 | -44.3% | 44.3% |
| PF_SUIUSD | 1 | +38.4% | 38.4% |
| PF_BLURUSD | 1 | +36.3% | 36.3% |
| PF_ZROUSD | 1 | +35.1% | 230.0% |

**Resolved since last scan:** PF_SYNUSD (crowded 1d, worst 43%), PF_TRXUSD (crowded 1d, worst 38%), PF_KAITOUSD (crowded 1d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
