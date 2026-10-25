# Pond Scanner Report
**Scan time:** 2026-10-25 20:52 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| ⚪ | PF_ARCUSD | -21.4% | $3,655,498 |
| ⚪ | PF_NEARUSD | +17.5% | $3,693,968 |
| ⚪ | PF_XRPUSD | +15.7% | $7,525,080 |
| ⚪ | PF_WLDUSD | +13.8% | $5,943,430 |
| ⚪ | PF_TIAUSD | -10.6% | $872,190 |
| ⚪ | PF_ACEUSD | +9.9% | $4,554,347 |
| ⚪ | PF_GRASSUSD | +9.3% | $949,285 |
| ⚪ | PF_SUIUSD | +8.3% | $4,572,812 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (gemini → coinbase) — coinbase: $80,356.56, kraken: $80,355.40, gemini: $80,348.07
- ⚪ **ETH** gap **0.018%** (gemini → coinbase) — coinbase: $2,343.39, kraken: $2,343.06, gemini: $2,342.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #383 | $61.3M | 3.40x | +20.2% |
| Irys (IRYS) | #342 | $71.7M | 1.74x | -19.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.29, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.47, realized vol 10d 25% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 31% (0.6x)
- ⚪ **ETH** 24h vol 31% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
No perps currently crowded. ⚪

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 102%), PF_TIAUSD (crowded 1d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
