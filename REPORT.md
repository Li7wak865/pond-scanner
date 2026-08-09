# Pond Scanner Report
**Scan time:** 2026-08-09 02:29 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_HFTUSD | -184.5% | $9,419,663 |
| 🟢 | PF_ZBTUSD | -182.7% | $534,824 |
| 🟢 | PF_ACEUSD | -115.3% | $9,490,249 |
| 🟢 | PF_NEARUSD | +57.1% | $1,058,822 |
| ⚪ | PF_SYNUSD | -29.4% | $2,025,153 |
| ⚪ | PF_SUSHIUSD | -22.1% | $633,363 |
| ⚪ | PF_SUIUSD | +18.0% | $4,742,248 |
| ⚪ | PF_DEEPUSD | +16.9% | $2,395,621 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (kraken → gemini) — coinbase: $64,786.58, kraken: $64,782.20, gemini: $64,795.47
- ⚪ **ETH** gap **0.026%** (kraken → gemini) — coinbase: $1,914.83, kraken: $1,914.58, gemini: $1,915.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #246 | $107.1M | 3.16x | +231.1% |
| Biconomy (BICO) | #423 | $69.7M | 3.07x | +29.5% |
| ETHGas (GWEI) | #420 | $51.3M | 0.66x | -21.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 27% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 7% vs 30d norm 28% (0.3x)
- ⚪ **ETH** 24h vol 9% vs 30d norm 40% (0.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 3 | -115.3% | 501.6% |
| PF_ZBTUSD | 2 | -182.7% | 182.7% |
| PF_NEARUSD | 2 | +57.1% | 57.1% |
| PF_HFTUSD | 1 | -184.5% | 184.5% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
