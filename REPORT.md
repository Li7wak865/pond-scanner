# Pond Scanner Report
**Scan time:** 2026-10-29 22:45 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -531.1% | $1,363,830 |
| 🟢 | PF_UNIUSD | -314.7% | $1,143,298 |
| 🟢 | PF_ICPUSD | -266.3% | $725,733 |
| 🟢 | PF_TRXUSD | -225.3% | $12,132,357 |
| 🟢 | PF_SUSHIUSD | +144.2% | $785,732 |
| 🟢 | PF_INJUSD | -84.3% | $635,765 |
| 🟢 | PF_RENDERUSD | -83.8% | $577,257 |
| 🟢 | PF_ATOMUSD | -53.5% | $819,619 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (gemini → coinbase) — coinbase: $78,763.61, kraken: $78,758.00, gemini: $78,750.36
- ⚪ **ETH** gap **0.117%** (coinbase → gemini) — coinbase: $2,268.45, kraken: $2,268.91, gemini: $2,271.10

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #498 | $43.4M | 1.31x | +18.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.21, realized vol 10d 30% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.32, realized vol 10d 34% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9964 (-0.36% vs peg)
- ⚪ **USDe** $0.9982 (-0.18% vs peg)
- ⚪ **PYUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9986 (-0.14% vs peg)
- ⚪ **USDC** $0.9992 (-0.08% vs peg)
- ⚪ **DAI** $0.9995 (-0.05% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 62% vs 30d norm 33% (1.9x)
- ⚪ **ETH** 24h vol 80% vs 30d norm 45% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +32.4% | 141.8% |
| PF_SOLUSD | 1 | -531.1% | 531.1% |
| PF_UNIUSD | 1 | -314.7% | 314.7% |
| PF_ICPUSD | 1 | -266.3% | 322.3% |
| PF_TRXUSD | 1 | -225.3% | 225.3% |
| PF_SUSHIUSD | 1 | +144.2% | 144.2% |
| PF_INJUSD | 1 | -84.3% | 84.3% |
| PF_RENDERUSD | 1 | -83.8% | 83.8% |
| PF_ATOMUSD | 1 | -53.5% | 136.7% |
| PF_BATUSD | 1 | +43.6% | 43.6% |
| PF_TIAUSD | 1 | +42.0% | 72.2% |
| PF_JTOUSD | 1 | -36.1% | 123.0% |
| PF_SUIUSD | 1 | -31.7% | 31.7% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 68%), PF_SYNUSD (crowded 1d, worst 38%), PF_ONDOUSD (crowded 1d, worst 33%), PF_ASTERUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
