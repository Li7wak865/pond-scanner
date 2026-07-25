# Pond Scanner Report
**Scan time:** 2026-07-25 08:24 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -100.9% | $695,105 |
| 🟢 | PF_ACEUSD | -64.2% | $2,905,682 |
| 🟢 | PF_MUBARAKUSD | +45.5% | $908,338 |
| 🟢 | PF_SYNUSD | +35.1% | $2,417,331 |
| 🟢 | PF_SUIUSD | -30.6% | $9,129,115 |
| ⚪ | PF_KAITOUSD | -26.6% | $612,850 |
| ⚪ | PF_STXUSD | -26.6% | $1,261,472 |
| ⚪ | PF_NEARUSD | -23.0% | $1,420,826 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $63,912.73, kraken: $63,913.70, gemini: $63,918.09
- ⚪ **ETH** gap **0.033%** (kraken → gemini) — coinbase: $1,853.69, kraken: $1,853.52, gemini: $1,854.13

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #319 | $73.0M | 1.61x | +32.4% |
| ETHGas (GWEI) | #364 | $62.3M | 0.91x | +44.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 22% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 30% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 41% (0.6x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 52% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -100.9% | 144.5% |
| PF_ACEUSD | 2 | -64.2% | 192.2% |
| PF_SYNUSD | 2 | +35.1% | 76.6% |
| PF_MUBARAKUSD | 1 | +45.5% | 45.5% |
| PF_SUIUSD | 1 | -30.6% | 30.6% |

**Resolved since last scan:** PF_DEXEUSD (crowded 1d, worst 824%), PF_KAITOUSD (crowded 2d, worst 179%), PF_STXUSD (crowded 1d, worst 41%), PF_GRASSUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
