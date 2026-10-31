# Pond Scanner Report
**Scan time:** 2026-10-31 21:36 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BATUSD | +137.5% | $610,095 |
| 🟢 | PF_TRXUSD | -54.7% | $32,701,401 |
| ⚪ | PF_ACEUSD | -20.0% | $813,742 |
| ⚪ | PF_SYNUSD | +19.8% | $844,773 |
| ⚪ | PF_SUIUSD | -17.1% | $1,293,724 |
| ⚪ | PF_TIAUSD | -16.1% | $1,067,477 |
| ⚪ | PF_FARTCOINUSD | +15.0% | $1,867,171 |
| ⚪ | PF_XRPUSD | +13.6% | $3,854,795 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (coinbase → gemini) — coinbase: $77,368.07, kraken: $77,370.10, gemini: $77,382.43
- ⚪ **ETH** gap **0.019%** (kraken → gemini) — coinbase: $2,249.79, kraken: $2,249.73, gemini: $2,250.16

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #419 | $53.9M | 3.07x | +18.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.34, realized vol 10d 30% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 33% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9978 (-0.22% vs peg)
- ⚪ **DAI** $1.0010 (+0.10% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDT** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 33% (0.5x)
- ⚪ **ETH** 24h vol 15% vs 30d norm 45% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_BATUSD | 1 | +137.5% | 137.5% |
| PF_TRXUSD | 1 | -54.7% | 54.7% |

**Resolved since last scan:** PF_UNIUSD (crowded 3d, worst 516%), PF_ATOMUSD (crowded 2d, worst 550%), PF_LINKUSD (crowded 2d, worst 235%), PF_NEARUSD (crowded 1d, worst 52%), PF_TRUMPUSD (crowded 1d, worst 39%), PF_STXUSD (crowded 1d, worst 39%), PF_SUIUSD (crowded 1d, worst 34%), PF_TIAUSD (crowded 1d, worst 33%), PF_SUSHIUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
