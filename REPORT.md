# Pond Scanner Report
**Scan time:** 2026-10-24 15:58 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -47.6% | $6,523,083 |
| 🟢 | PF_TRUMPUSD | -38.0% | $902,347 |
| ⚪ | PF_PONSUSD | +26.0% | $1,202,819 |
| ⚪ | PF_KAITOUSD | -25.4% | $883,526 |
| ⚪ | PF_ATOMUSD | -22.3% | $528,013 |
| ⚪ | PF_APEUSD | -19.3% | $4,040,970 |
| ⚪ | PF_OPNUSD | +18.3% | $576,125 |
| ⚪ | PF_XRPUSD | +17.8% | $8,019,530 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $79,652.60, kraken: $79,655.60, gemini: $79,663.65
- ⚪ **ETH** gap **0.010%** (kraken → coinbase) — coinbase: $2,301.52, kraken: $2,301.30, gemini: $2,301.50

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #282 | $96.8M | 2.69x | -24.5% |
| Janction (JCT) | #320 | $77.9M | 1.47x | +30.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.34, realized vol 10d 26% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.51, realized vol 10d 32% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 31% (0.9x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 43% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -47.6% | 47.6% |
| PF_TRUMPUSD | 1 | -38.0% | 38.0% |

**Resolved since last scan:** PF_ATOMUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
