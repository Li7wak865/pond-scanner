# Pond Scanner Report
**Scan time:** 2026-08-17 13:06 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -246.7% | $14,426,178 |
| ⚪ | PF_ETHFIUSD | -24.8% | $959,346 |
| ⚪ | PF_ZEREBROUSD | +18.1% | $713,382 |
| ⚪ | PF_HFTUSD | -17.5% | $6,640,197 |
| ⚪ | PF_SUIUSD | -16.5% | $3,018,534 |
| ⚪ | PF_ALICEUSD | -16.0% | $3,665,130 |
| ⚪ | PF_VELOUSD | +13.6% | $746,030 |
| ⚪ | PF_APTUSD | -13.5% | $568,563 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.047%** (gemini → kraken) — coinbase: $63,478.23, kraken: $63,478.30, gemini: $63,448.67
- ⚪ **ETH** gap **0.049%** (kraken → coinbase) — coinbase: $1,897.93, kraken: $1,897.00, gemini: $1,897.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 牛来 (Niu Lai) (牛来) | #462 | $42.2M | 1.54x | +198.1% |
| Cysic (CYS) | #280 | $82.0M | 0.98x | -24.9% |
| GoPlus Security (GPS) | #263 | $90.2M | 0.86x | +46.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 12% vs 60d 27%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 15% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 25% (0.7x)
- ⚪ **ETH** 24h vol 27% vs 30d norm 35% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -246.7% | 732.3% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 1d, worst 99%), PF_NEARUSD (crowded 1d, worst 42%), PF_MOODENGUSD (crowded 1d, worst 69%), PF_KAITOUSD (crowded 1d, worst 46%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
