# Pond Scanner Report
**Scan time:** 2026-08-29 07:05 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +547.5% | $680,376 |
| 🟢 | PF_TRUMPUSD | -232.2% | $4,440,395 |
| 🟢 | PF_NEARUSD | -113.4% | $688,585 |
| 🟢 | PF_STXUSD | -57.1% | $1,413,812 |
| 🟢 | PF_SPXUSD | -54.2% | $833,500 |
| 🟢 | PF_ACEUSD | -53.4% | $968,825 |
| 🟢 | PF_HFTUSD | -40.6% | $9,870,186 |
| 🟢 | PF_DEXEUSD | -36.0% | $1,006,190 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (kraken → gemini) — coinbase: $77,534.50, kraken: $77,528.30, gemini: $77,545.22
- ⚪ **ETH** gap **0.039%** (gemini → coinbase) — coinbase: $2,437.46, kraken: $2,437.30, gemini: $2,436.50

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DeXe (DEXE) | #296 | $85.9M | 1.96x | +27.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.49, realized vol 10d 56% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.51, realized vol 10d 62% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 36% vs 30d norm 38% (1.0x)
- ⚪ **ETH** 24h vol 47% vs 30d norm 51% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 8 | -53.4% | 241.7% |
| PF_SOLUSD | 2 | +547.5% | 547.5% |
| PF_STXUSD | 2 | -57.1% | 60.2% |
| PF_TRUMPUSD | 1 | -232.2% | 232.2% |
| PF_NEARUSD | 1 | -113.4% | 113.4% |
| PF_SPXUSD | 1 | -54.2% | 54.2% |
| PF_HFTUSD | 1 | -40.6% | 40.6% |
| PF_DEXEUSD | 1 | -36.0% | 36.0% |

**Resolved since last scan:** PF_RUNEUSD (crowded 2d, worst 102%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
