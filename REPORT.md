# Pond Scanner Report
**Scan time:** 2026-10-11 12:52 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +66.2% | $1,973,816 |
| 🟢 | PF_XRPUSD | +32.0% | $5,872,821 |
| 🟢 | PF_DOTUSD | +30.8% | $810,890 |
| ⚪ | PF_SUIUSD | +23.1% | $3,918,791 |
| ⚪ | PF_TIAUSD | -16.7% | $3,787,398 |
| ⚪ | PF_FARTCOINUSD | +14.7% | $4,187,581 |
| ⚪ | PF_FILUSD | -11.4% | $1,441,897 |
| ⚪ | PF_KAIAUSD | -10.7% | $1,320,734 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → kraken) — coinbase: $83,038.58, kraken: $83,053.30, gemini: $83,051.40
- ⚪ **ETH** gap **0.016%** (coinbase → gemini) — coinbase: $2,502.44, kraken: $2,502.76, gemini: $2,502.84

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #308 | $95.2M | 1.01x | +16.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.25, realized vol 10d 25% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.51, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 34% (0.3x)
- ⚪ **ETH** 24h vol 17% vs 30d norm 44% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +66.2% | 66.2% |
| PF_DOTUSD | 2 | +30.8% | 53.0% |
| PF_XRPUSD | 1 | +32.0% | 32.0% |

**Resolved since last scan:** PF_FILUSD (crowded 2d, worst 65%), PF_SUIUSD (crowded 1d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
