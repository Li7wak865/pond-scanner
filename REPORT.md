# Pond Scanner Report
**Scan time:** 2026-08-31 13:53 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -233.6% | $1,420,154 |
| 🟢 | PF_SOLUSD | -199.5% | $747,206 |
| 🟢 | PF_VIRTUALUSD | +38.5% | $906,003 |
| ⚪ | PF_VELOUSD | -20.2% | $7,797,570 |
| ⚪ | PF_JTOUSD | -20.0% | $600,830 |
| ⚪ | PF_RAREUSD | +18.9% | $1,600,925 |
| ⚪ | PF_SANDUSD | -18.6% | $1,738,885 |
| ⚪ | PF_MIRAUSD | -18.1% | $1,987,152 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.060%** (kraken → coinbase) — coinbase: $77,778.80, kraken: $77,732.50, gemini: $77,766.53
- ⚪ **ETH** gap **0.097%** (kraken → gemini) — coinbase: $2,438.42, kraken: $2,438.30, gemini: $2,440.66

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology Gas (ONG) | #487 | $44.9M | 0.71x | -17.9% |
| Prom (PROM) | #253 | $109.7M | 0.69x | -16.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 26% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.52, realized vol 10d 37% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 38% (0.9x)
- ⚪ **ETH** 24h vol 67% vs 30d norm 52% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 1 | -233.6% | 233.6% |
| PF_SOLUSD | 1 | -199.5% | 310.3% |
| PF_VIRTUALUSD | 1 | +38.5% | 38.5% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 59%), PF_SYNUSD (crowded 1d, worst 44%), PF_ACEUSD (crowded 10d, worst 242%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
