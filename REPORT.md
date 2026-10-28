# Pond Scanner Report
**Scan time:** 2026-10-28 05:43 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +54.7% | $2,341,552 |
| 🟢 | PF_BBUSD | +33.0% | $781,479 |
| ⚪ | PF_XRPUSD | +27.4% | $7,631,526 |
| ⚪ | PF_ZROUSD | +26.6% | $664,970 |
| ⚪ | PF_DOTUSD | -23.2% | $1,048,896 |
| ⚪ | PF_BATUSD | -18.9% | $601,464 |
| ⚪ | PF_APTUSD | +12.7% | $537,932 |
| ⚪ | PF_WLDUSD | -11.6% | $6,181,583 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.047%** (coinbase → gemini) — coinbase: $80,827.69, kraken: $80,837.20, gemini: $80,865.73
- ⚪ **ETH** gap **0.017%** (coinbase → gemini) — coinbase: $2,349.52, kraken: $2,349.61, gemini: $2,349.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #440 | $50.2M | 1.55x | +27.9% |
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #395 | $60.3M | 1.24x | +16.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 24% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 27% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 29% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | +54.7% | 54.7% |
| PF_BBUSD | 1 | +33.0% | 33.0% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 93%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
