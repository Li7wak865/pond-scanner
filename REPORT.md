# Pond Scanner Report
**Scan time:** 2026-10-01 22:42 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -413.8% | $767,365 |
| 🟢 | PF_MOVRUSD | +182.6% | $1,357,473 |
| 🟢 | PF_LINKUSD | +128.4% | $980,428 |
| 🟢 | PF_TRUMPUSD | -105.3% | $1,006,964 |
| 🟢 | PF_ACEUSD | +44.0% | $1,954,541 |
| ⚪ | PF_ZROUSD | +25.8% | $624,306 |
| ⚪ | PF_WLDUSD | +25.4% | $6,911,502 |
| ⚪ | PF_JUPUSD | +24.7% | $2,527,971 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (kraken → coinbase) — coinbase: $84,719.35, kraken: $84,715.50, gemini: $84,718.52
- ⚪ **ETH** gap **0.012%** (kraken → gemini) — coinbase: $2,701.42, kraken: $2,701.17, gemini: $2,701.49

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MegaETH (MEGA) | #435 | $58.6M | 1.27x | +23.8% |
| 龙虾 (Lobster) (龙虾) | #276 | $106.5M | 0.88x | +204.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.36, realized vol 10d 17% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 16% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 35% (0.8x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 46% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | -413.8% | 543.2% |
| PF_TRUMPUSD | 2 | -105.3% | 105.3% |
| PF_MOVRUSD | 1 | +182.6% | 182.6% |
| PF_LINKUSD | 1 | +128.4% | 234.3% |
| PF_ACEUSD | 1 | +44.0% | 44.0% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 373%), PF_OPNUSD (crowded 1d, worst 268%), PF_ZROUSD (crowded 1d, worst 128%), PF_PONSUSD (crowded 2d, worst 97%), PF_SOONUSD (crowded 1d, worst 52%), PF_SUIUSD (crowded 1d, worst 52%), PF_TRXUSD (crowded 1d, worst 48%), PF_FILUSD (crowded 1d, worst 45%), PF_VIRTUALUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
