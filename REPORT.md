# Pond Scanner Report
**Scan time:** 2026-10-07 06:02 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -141.5% | $1,126,808 |
| 🟢 | PF_BATUSD | +141.4% | $554,098 |
| 🟢 | PF_RENDERUSD | +137.6% | $1,247,692 |
| 🟢 | PF_AVAXUSD | +117.2% | $823,615 |
| 🟢 | PF_NEARUSD | +95.0% | $2,827,845 |
| 🟢 | PF_DOTUSD | -60.1% | $1,845,146 |
| 🟢 | PF_ZROUSD | +55.2% | $1,606,443 |
| 🟢 | PF_UNIUSD | +50.6% | $804,395 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.037%** (coinbase → gemini) — coinbase: $84,266.24, kraken: $84,266.90, gemini: $84,297.44
- ⚪ **ETH** gap **0.072%** (coinbase → gemini) — coinbase: $2,618.11, kraken: $2,618.26, gemini: $2,619.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #405 | $64.5M | 2.35x | -15.3% |
| Numeraire (NMR) | #260 | $122.2M | 1.66x | +42.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.39, realized vol 10d 20% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 23% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 39% vs 30d norm 34% (1.1x)
- ⚪ **ETH** 24h vol 47% vs 30d norm 44% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 5 | +37.1% | 111.2% |
| PF_UNIUSD | 3 | +50.6% | 299.0% |
| PF_AVAXUSD | 2 | +117.2% | 117.2% |
| PF_NEARUSD | 2 | +95.0% | 178.3% |
| PF_DOTUSD | 2 | -60.1% | 61.0% |
| PF_ZROUSD | 2 | +55.2% | 80.1% |
| PF_ASTERUSD | 2 | -36.9% | 36.9% |
| PF_SUIUSD | 2 | +33.8% | 44.5% |
| PF_FILUSD | 2 | -32.4% | 59.5% |
| PF_TRUMPUSD | 1 | -141.5% | 141.5% |
| PF_BATUSD | 1 | +141.4% | 141.4% |
| PF_RENDERUSD | 1 | +137.6% | 137.6% |

**Resolved since last scan:** PF_SPXUSD (crowded 2d, worst 76%), PF_ETHFIUSD (crowded 2d, worst 45%), PF_XRPUSD (crowded 2d, worst 36%), PF_GRASSUSD (crowded 2d, worst 36%), PF_CROUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
