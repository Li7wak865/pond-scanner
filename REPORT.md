# Pond Scanner Report
**Scan time:** 2026-09-21 04:57 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +351.0% | $720,784 |
| 🟢 | PF_LINKUSD | +223.1% | $554,178 |
| 🟢 | PF_RENDERUSD | +126.8% | $653,193 |
| 🟢 | PF_NEARUSD | +111.9% | $8,073,103 |
| 🟢 | PF_HFTUSD | +104.6% | $1,107,542 |
| 🟢 | PF_SUIUSD | +50.4% | $15,421,237 |
| 🟢 | PF_LDOUSD | +39.4% | $967,520 |
| ⚪ | PF_XRPUSD | +26.7% | $11,958,798 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (gemini → kraken) — coinbase: $81,428.59, kraken: $81,435.80, gemini: $81,412.00
- ⚪ **ETH** gap **0.013%** (coinbase → gemini) — coinbase: $2,664.60, kraken: $2,664.82, gemini: $2,664.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| ZetaChain (ZETA) | #274 | $107.6M | 0.52x | +71.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.19, realized vol 10d 42% vs 60d 41%
- 🟡 **ETH: MIXED** — efficiency ratio 0.28, realized vol 10d 52% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 35% (0.7x)
- ⚪ **ETH** 24h vol 53% vs 30d norm 49% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | +351.0% | 624.1% |
| PF_LINKUSD | 2 | +223.1% | 223.1% |
| PF_NEARUSD | 2 | +111.9% | 239.5% |
| PF_SUIUSD | 2 | +50.4% | 50.4% |
| PF_RENDERUSD | 1 | +126.8% | 126.8% |
| PF_HFTUSD | 1 | +104.6% | 104.6% |
| PF_LDOUSD | 1 | +39.4% | 39.4% |

**Resolved since last scan:** PF_AVAXUSD (crowded 3d, worst 168%), PF_TRUMPUSD (crowded 2d, worst 137%), PF_INJUSD (crowded 2d, worst 101%), PF_XRPUSD (crowded 2d, worst 49%), PF_FILUSD (crowded 2d, worst 43%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
