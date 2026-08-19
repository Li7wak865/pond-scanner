# Pond Scanner Report
**Scan time:** 2026-08-19 18:53 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +258.3% | $1,329,472 |
| 🟢 | PF_ETHFIUSD | -113.4% | $1,063,475 |
| 🟢 | PF_LINKUSD | -111.8% | $1,084,744 |
| 🟢 | PF_ACEUSD | -92.7% | $17,501,545 |
| 🟢 | PF_VIRTUALUSD | -62.8% | $574,710 |
| 🟢 | PF_BBUSD | +49.8% | $1,499,704 |
| 🟢 | PF_GRASSUSD | +34.4% | $605,108 |
| ⚪ | PF_XRPUSD | +29.6% | $20,686,351 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.028%** (gemini → kraken) — coinbase: $68,354.15, kraken: $68,355.00, gemini: $68,335.97
- ⚪ **ETH** gap **0.064%** (gemini → coinbase) — coinbase: $2,088.91, kraken: $2,087.90, gemini: $2,087.58

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #399 | $54.0M | 1.21x | +20.7% |
| RE (RE) | #279 | $81.3M | 0.96x | +25.5% |
| GoPlus Security (GPS) | #319 | $70.6M | 0.69x | -31.2% |
| Audiera (BEAT) | #405 | $53.1M | 0.53x | -26.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.29, realized vol 10d 38% vs 60d 31%
- 🟡 **ETH: MIXED** — efficiency ratio 0.35, realized vol 10d 54% vs 60d 44%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 81% vs 30d norm 28% (2.8x)
- 🟢 **ETH** 24h vol 115% vs 30d norm 40% (2.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -92.7% | 732.3% |
| PF_UNIUSD | 1 | +258.3% | 258.3% |
| PF_ETHFIUSD | 1 | -113.4% | 154.5% |
| PF_LINKUSD | 1 | -111.8% | 111.8% |
| PF_VIRTUALUSD | 1 | -62.8% | 62.8% |
| PF_BBUSD | 1 | +49.8% | 49.8% |
| PF_GRASSUSD | 1 | +34.4% | 34.4% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 405%), PF_NEARUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
