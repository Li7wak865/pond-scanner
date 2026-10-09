# Pond Scanner Report
**Scan time:** 2026-10-09 22:39 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAIAUSD | -74.4% | $18,571,267 |
| 🟢 | PF_ASTERUSD | +69.7% | $582,300 |
| 🟢 | PF_ZROUSD | +58.3% | $1,167,769 |
| 🟢 | PF_ETHFIUSD | -51.6% | $517,342 |
| 🟢 | PF_SAGAUSD | -51.2% | $1,018,934 |
| 🟢 | PF_SUIUSD | +41.5% | $5,676,778 |
| 🟢 | PF_NEARUSD | -39.9% | $15,041,914 |
| 🟢 | PF_PONSUSD | +36.9% | $796,880 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → gemini) — coinbase: $82,550.00, kraken: $82,552.50, gemini: $82,557.70
- ⚪ **ETH** gap **0.016%** (gemini → coinbase) — coinbase: $2,487.85, kraken: $2,487.73, gemini: $2,487.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #309 | $91.6M | 2.20x | +22.2% |
| Talus (US) | #298 | $95.7M | 0.51x | +109.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 27% vs 60d 44%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 37% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 34% (0.8x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 46% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 4 | +58.3% | 176.3% |
| PF_NEARUSD | 4 | -39.9% | 417.9% |
| PF_KAIAUSD | 1 | -74.4% | 250.9% |
| PF_ASTERUSD | 1 | +69.7% | 69.7% |
| PF_ETHFIUSD | 1 | -51.6% | 51.6% |
| PF_SAGAUSD | 1 | -51.2% | 51.2% |
| PF_SUIUSD | 1 | +41.5% | 41.5% |
| PF_PONSUSD | 1 | +36.9% | 36.9% |
| PF_STXUSD | 1 | +36.1% | 36.1% |
| PF_XRPUSD | 1 | +33.1% | 33.1% |
| PF_TIAUSD | 1 | +30.8% | 30.8% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 475%), PF_AVAXUSD (crowded 2d, worst 157%), PF_RENDERUSD (crowded 2d, worst 203%), PF_OPNUSD (crowded 1d, worst 42%), PF_UNIUSD (crowded 1d, worst 124%), PF_CTSIUSD (crowded 2d, worst 41%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
