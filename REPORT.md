# Pond Scanner Report
**Scan time:** 2026-11-01 22:02 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | -70.9% | $511,316 |
| 🟢 | PF_SYNUSD | +43.9% | $1,027,676 |
| 🟢 | PF_STXUSD | +39.6% | $674,649 |
| ⚪ | PF_TRUMPUSD | -26.3% | $1,645,344 |
| ⚪ | PF_CRVUSD | +21.3% | $2,390,479 |
| ⚪ | PF_ACEUSD | +17.3% | $750,243 |
| ⚪ | PF_NEARUSD | +16.1% | $1,891,906 |
| ⚪ | PF_TIAUSD | +13.5% | $524,227 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (coinbase → gemini) — coinbase: $77,795.80, kraken: $77,798.00, gemini: $77,799.78
- ⚪ **ETH** gap **0.023%** (kraken → coinbase) — coinbase: $2,261.66, kraken: $2,261.13, gemini: $2,261.63

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #480 | $45.6M | 1.35x | -15.8% |
| MEET48 (IDOL) | #423 | $52.9M | 0.58x | +42.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 27% vs 60d 36%
- 🟡 **ETH: MIXED** — efficiency ratio 0.31, realized vol 10d 29% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDe** $0.9986 (-0.14% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 13% vs 30d norm 32% (0.4x)
- ⚪ **ETH** 24h vol 18% vs 30d norm 44% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 1 | -70.9% | 70.9% |
| PF_SYNUSD | 1 | +43.9% | 43.9% |
| PF_STXUSD | 1 | +39.6% | 39.6% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 73%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
