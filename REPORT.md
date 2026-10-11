# Pond Scanner Report
**Scan time:** 2026-10-11 21:59 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -142.6% | $2,830,811 |
| 🟢 | PF_GRASSUSD | +68.1% | $893,935 |
| 🟢 | PF_APTUSD | -66.3% | $723,416 |
| 🟢 | PF_ATOMUSD | +57.6% | $580,448 |
| 🟢 | PF_XRPUSD | -33.2% | $15,499,022 |
| ⚪ | PF_WLDUSD | +21.0% | $2,309,090 |
| ⚪ | PF_FARTCOINUSD | +17.3% | $5,821,876 |
| ⚪ | PF_SYNUSD | -16.7% | $576,447 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (kraken → coinbase) — coinbase: $83,432.65, kraken: $83,421.80, gemini: $83,431.86
- ⚪ **ETH** gap **0.026%** (gemini → coinbase) — coinbase: $2,526.65, kraken: $2,526.62, gemini: $2,525.99

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Nervos Network (CKB) | #295 | $102.0M | 0.97x | +42.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.22, realized vol 10d 25% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 38% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 33% (0.6x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 40% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | -142.6% | 142.6% |
| PF_GRASSUSD | 1 | +68.1% | 68.1% |
| PF_APTUSD | 1 | -66.3% | 66.3% |
| PF_ATOMUSD | 1 | +57.6% | 57.6% |
| PF_XRPUSD | 1 | -33.2% | 33.2% |

**Resolved since last scan:** PF_DOTUSD (crowded 2d, worst 53%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
