# Pond Scanner Report
**Scan time:** 2026-08-05 14:34 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +310.1% | $918,510 |
| 🟢 | PF_KAITOUSD | +80.6% | $639,064 |
| 🟢 | PF_TRUMPUSD | -78.6% | $1,053,405 |
| 🟢 | PF_SYNUSD | -61.5% | $7,320,357 |
| 🟢 | PF_FILUSD | -37.5% | $677,568 |
| 🟢 | PF_ZEREBROUSD | -30.7% | $1,950,638 |
| ⚪ | PF_UNIUSD | -26.5% | $1,389,339 |
| ⚪ | PF_ZIGUSD | +18.5% | $592,328 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.023%** (coinbase → gemini) — coinbase: $64,392.60, kraken: $64,402.80, gemini: $64,407.47
- ⚪ **ETH** gap **0.025%** (coinbase → kraken) — coinbase: $1,872.54, kraken: $1,873.01, gemini: $1,872.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cysic (CYS) | #243 | $109.0M | 1.44x | +53.6% |
| SkyAI (SKYAI) | #386 | $57.1M | 0.76x | +19.3% |
| Seeker (SKR) | #376 | $57.6M | 0.57x | +17.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 26% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 32% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 32% (0.7x)
- ⚪ **ETH** 24h vol 21% vs 30d norm 43% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +310.1% | 310.1% |
| PF_KAITOUSD | 1 | +80.6% | 80.6% |
| PF_TRUMPUSD | 1 | -78.6% | 78.6% |
| PF_SYNUSD | 1 | -61.5% | 61.5% |
| PF_FILUSD | 1 | -37.5% | 37.5% |
| PF_ZEREBROUSD | 1 | -30.7% | 66.4% |

**Resolved since last scan:** PF_LDOUSD (crowded 1d, worst 50%), PF_UNIUSD (crowded 2d, worst 94%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
