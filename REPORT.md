# Pond Scanner Report
**Scan time:** 2026-08-31 05:37 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -310.3% | $742,735 |
| 🟢 | PF_TRUMPUSD | -70.6% | $1,648,952 |
| 🟢 | PF_UNIUSD | +54.0% | $1,149,915 |
| 🟢 | PF_SYNUSD | +43.8% | $524,480 |
| 🟢 | PF_ACEUSD | -41.3% | $1,633,443 |
| ⚪ | PF_NEARUSD | +27.6% | $697,243 |
| ⚪ | PF_XRPUSD | +24.3% | $42,468,576 |
| ⚪ | PF_BICOUSD | -13.9% | $20,672,759 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $77,929.97, kraken: $77,938.00, gemini: $77,943.62
- ⚪ **ETH** gap **0.142%** (kraken → gemini) — coinbase: $2,432.69, kraken: $2,432.51, gemini: $2,435.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Zora (ZORA) | #445 | $49.6M | 2.47x | +76.6% |
| ZKsync (ZK) | #266 | $103.2M | 0.83x | +16.1% |
| Ontology Gas (ONG) | #475 | $46.1M | 0.67x | -18.4% |
| Prom (PROM) | #248 | $109.5M | 0.67x | -16.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 26% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.52, realized vol 10d 36% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 38% (0.9x)
- ⚪ **ETH** 24h vol 65% vs 30d norm 52% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 10 | -41.3% | 241.7% |
| PF_UNIUSD | 2 | +54.0% | 59.0% |
| PF_SOLUSD | 1 | -310.3% | 310.3% |
| PF_TRUMPUSD | 1 | -70.6% | 70.6% |
| PF_SYNUSD | 1 | +43.8% | 43.8% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 2d, worst 99%), PF_SAGAUSD (crowded 2d, worst 68%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
