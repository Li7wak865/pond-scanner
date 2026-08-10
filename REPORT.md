# Pond Scanner Report
**Scan time:** 2026-08-10 08:04 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +949.1% | $533,482 |
| 🟢 | PF_UNIUSD | +50.1% | $534,075 |
| 🟢 | PF_HFTUSD | -39.7% | $3,207,889 |
| ⚪ | PF_SYNUSD | -26.5% | $546,858 |
| ⚪ | PF_DOTUSD | +22.1% | $716,638 |
| ⚪ | PF_XRPUSD | +18.4% | $8,602,968 |
| ⚪ | PF_SUIUSD | +13.4% | $3,110,308 |
| ⚪ | PF_WLDUSD | +13.0% | $2,678,487 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (coinbase → gemini) — coinbase: $65,243.60, kraken: $65,246.70, gemini: $65,248.02
- ⚪ **ETH** gap **0.077%** (gemini → kraken) — coinbase: $1,926.12, kraken: $1,926.42, gemini: $1,924.94

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| BOOK OF MEME (BOME) | #394 | $55.4M | 1.77x | +25.3% |
| Cap (CAP) | #298 | $78.4M | 0.96x | +31.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.11, realized vol 10d 11% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.00, realized vol 10d 21% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9974 (-0.26% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 28% (0.6x)
- ⚪ **ETH** 24h vol 23% vs 30d norm 40% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | +949.1% | 949.1% |
| PF_UNIUSD | 1 | +50.1% | 50.1% |
| PF_HFTUSD | 1 | -39.7% | 170.5% |

**Resolved since last scan:** PF_KAITOUSD (crowded 1d, worst 742%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
