# Pond Scanner Report
**Scan time:** 2026-09-03 16:26 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +147.4% | $1,181,323 |
| 🟢 | PF_HFTUSD | +111.3% | $1,656,029 |
| 🟢 | PF_ACEUSD | -69.9% | $1,104,036 |
| 🟢 | PF_SUIUSD | +50.7% | $8,790,092 |
| 🟢 | PF_FILUSD | -40.8% | $1,065,676 |
| 🟢 | PF_DOTUSD | +36.8% | $806,337 |
| 🟢 | PF_XRPUSD | +36.2% | $52,094,908 |
| ⚪ | PF_XPLUSD | +24.4% | $7,340,377 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.039%** (gemini → coinbase) — coinbase: $80,714.22, kraken: $80,700.00, gemini: $80,683.02
- ⚪ **ETH** gap **0.065%** (gemini → coinbase) — coinbase: $2,491.36, kraken: $2,491.11, gemini: $2,489.73

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| USD.AI (CHIP) | #253 | $110.1M | 0.80x | +34.9% |
| Cap (CAP) | #334 | $75.9M | 0.74x | -30.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 36% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 42% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 53% vs 30d norm 39% (1.4x)
- ⚪ **ETH** 24h vol 61% vs 30d norm 53% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -69.9% | 304.8% |
| PF_HFTUSD | 2 | +111.3% | 111.3% |
| PF_NEARUSD | 1 | +147.4% | 147.4% |
| PF_SUIUSD | 1 | +50.7% | 50.7% |
| PF_FILUSD | 1 | -40.8% | 40.8% |
| PF_DOTUSD | 1 | +36.8% | 36.8% |
| PF_XRPUSD | 1 | +36.2% | 36.2% |

**Resolved since last scan:** PF_DEEPUSD (crowded 1d, worst 66%), PF_UNIUSD (crowded 4d, worst 281%), PF_ASTERUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
