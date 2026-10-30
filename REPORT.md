# Pond Scanner Report
**Scan time:** 2026-10-30 12:57 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HYPEUSD | +949.3% | $1,179,303 |
| 🟢 | PF_ATOMUSD | -550.1% | $1,756,022 |
| 🟢 | PF_INJUSD | -518.1% | $603,197 |
| 🟢 | PF_ZROUSD | +185.1% | $809,733 |
| 🟢 | PF_NEARUSD | +75.9% | $8,333,969 |
| 🟢 | PF_VIRTUALUSD | +72.5% | $999,756 |
| 🟢 | PF_LINKUSD | -69.1% | $1,004,100 |
| 🟢 | PF_ETHFIUSD | +66.0% | $569,838 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.016%** (gemini → coinbase) — coinbase: $77,280.92, kraken: $77,277.80, gemini: $77,268.18
- ⚪ **ETH** gap **0.099%** (gemini → kraken) — coinbase: $2,229.12, kraken: $2,229.26, gemini: $2,227.06

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #476 | $45.4M | 1.89x | +20.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.29, realized vol 10d 32% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.39, realized vol 10d 34% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDe** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 73% vs 30d norm 33% (2.2x)
- ⚪ **ETH** 24h vol 91% vs 30d norm 46% (2.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | +75.9% | 141.8% |
| PF_INJUSD | 2 | -518.1% | 683.7% |
| PF_SUSHIUSD | 2 | +57.4% | 144.2% |
| PF_JTOUSD | 2 | +47.1% | 123.0% |
| PF_UNIUSD | 2 | -38.0% | 486.9% |
| PF_HYPEUSD | 1 | +949.3% | 949.3% |
| PF_ATOMUSD | 1 | -550.1% | 550.1% |
| PF_ZROUSD | 1 | +185.1% | 393.1% |
| PF_VIRTUALUSD | 1 | +72.5% | 72.5% |
| PF_LINKUSD | 1 | -69.1% | 174.3% |
| PF_ETHFIUSD | 1 | +66.0% | 73.2% |
| PF_ASTERUSD | 1 | -52.7% | 52.7% |
| PF_FLOWUSD | 1 | +47.2% | 47.2% |
| PF_XTZUSD | 1 | -42.5% | 42.5% |
| PF_GRASSUSD | 1 | +37.1% | 64.2% |

**Resolved since last scan:** PF_ICPUSD (crowded 2d, worst 322%), PF_SYNUSD (crowded 1d, worst 75%), PF_EIGENUSD (crowded 1d, worst 65%), PF_TRXUSD (crowded 2d, worst 225%), PF_FILUSD (crowded 1d, worst 36%), PF_PONSUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
