# Pond Scanner Report
**Scan time:** 2026-10-25 11:32 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -76.6% | $5,007,202 |
| 🟢 | PF_DOTUSD | -30.2% | $931,884 |
| ⚪ | PF_ASTERUSD | +29.6% | $616,429 |
| ⚪ | PF_PONSUSD | +20.6% | $1,051,910 |
| ⚪ | PF_TIAUSD | -16.0% | $1,406,807 |
| ⚪ | PF_FETUSD | -15.8% | $9,770,529 |
| ⚪ | PF_WLDUSD | -15.6% | $5,282,674 |
| ⚪ | PF_XRPUSD | +15.5% | $10,878,079 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.022%** (coinbase → gemini) — coinbase: $80,287.92, kraken: $80,301.90, gemini: $80,305.92
- ⚪ **ETH** gap **0.041%** (coinbase → kraken) — coinbase: $2,327.52, kraken: $2,328.47, gemini: $2,328.22

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Irys (IRYS) | #341 | $71.6M | 3.94x | -45.5% |
| Threshold Network (T) | #347 | $70.9M | 2.75x | +36.2% |
| Janction (JCT) | #308 | $83.6M | 1.19x | +49.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.29, realized vol 10d 24% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 26% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 31% (0.8x)
- ⚪ **ETH** 24h vol 47% vs 30d norm 43% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -76.6% | 100.0% |
| PF_DOTUSD | 1 | -30.2% | 30.2% |

**Resolved since last scan:** PF_ASTERUSD (crowded 1d, worst 42%), PF_PONSUSD (crowded 1d, worst 39%), PF_TIAUSD (crowded 2d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
