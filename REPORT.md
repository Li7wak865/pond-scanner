# Pond Scanner Report
**Scan time:** 2026-08-25 07:08 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_STORJUSD | -160.3% | $2,070,779 |
| 🟢 | PF_SUPERUSD | -149.0% | $1,912,909 |
| 🟢 | PF_SUSD | +129.0% | $754,188 |
| 🟢 | PF_ACEUSD | -127.9% | $1,533,618 |
| 🟢 | PF_LINKUSD | +112.4% | $748,892 |
| 🟢 | PF_HFTUSD | +92.0% | $3,453,166 |
| 🟢 | PF_BBUSD | +44.4% | $1,476,433 |
| 🟢 | PF_XRPUSD | +42.9% | $43,345,656 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.031%** (gemini → kraken) — coinbase: $80,695.85, kraken: $80,710.30, gemini: $80,685.39
- ⚪ **ETH** gap **0.100%** (coinbase → gemini) — coinbase: $2,506.68, kraken: $2,507.30, gemini: $2,509.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Prom (PROM) | #314 | $78.3M | 2.06x | +18.3% |
| Amp (AMP) | #478 | $46.8M | 1.20x | +23.3% |
| Ontology Gas (ONG) | #485 | $45.2M | 1.03x | +32.1% |
| Velvet (VELVET) | #354 | $68.0M | 0.84x | -78.4% |
| Spark (SPK) | #391 | $60.2M | 0.79x | -15.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.68, realized vol 10d 56% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.66, realized vol 10d 107% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 38% (1.3x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 52% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 4 | -127.9% | 241.7% |
| PF_STORJUSD | 2 | -160.3% | 214.3% |
| PF_LINKUSD | 2 | +112.4% | 223.0% |
| PF_HFTUSD | 2 | +92.0% | 110.1% |
| PF_XRPUSD | 2 | +42.9% | 51.4% |
| PF_SUPERUSD | 1 | -149.0% | 149.0% |
| PF_SUSD | 1 | +129.0% | 129.0% |
| PF_BBUSD | 1 | +44.4% | 44.4% |
| PF_ETHFIUSD | 1 | +39.8% | 39.8% |
| PF_GRASSUSD | 1 | +38.1% | 38.1% |
| PF_APTUSD | 1 | -37.3% | 37.3% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 658%), PF_TRUMPUSD (crowded 1d, worst 58%), PF_NEARUSD (crowded 2d, worst 166%), PF_STXUSD (crowded 1d, worst 37%), PF_POPCATUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
