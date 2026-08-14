# Pond Scanner Report
**Scan time:** 2026-08-14 13:44 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -147.6% | $28,964,722 |
| 🟢 | PF_ETHFIUSD | +111.5% | $1,130,796 |
| 🟢 | PF_KAITOUSD | -98.9% | $1,538,638 |
| 🟢 | PF_ATOMUSD | +65.7% | $651,708 |
| 🟢 | PF_UNIUSD | -53.5% | $2,193,527 |
| 🟢 | PF_2ZUSD | -53.2% | $634,414 |
| 🟢 | PF_GRASSUSD | -48.2% | $609,305 |
| 🟢 | PF_GPSUSD | +44.3% | $9,260,492 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (gemini → coinbase) — coinbase: $62,623.50, kraken: $62,614.10, gemini: $62,608.03
- ⚪ **ETH** gap **0.011%** (gemini → coinbase) — coinbase: $1,868.13, kraken: $1,867.95, gemini: $1,867.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #434 | $49.5M | 2.68x | +21.0% |
| LAB (LAB) | #617 | $72.4M | 0.55x | -23.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.16, realized vol 10d 14% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 19% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9969 (-0.31% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 26% (0.8x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 36% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 1 | -147.6% | 147.6% |
| PF_ETHFIUSD | 1 | +111.5% | 111.5% |
| PF_KAITOUSD | 1 | -98.9% | 98.9% |
| PF_ATOMUSD | 1 | +65.7% | 65.7% |
| PF_UNIUSD | 1 | -53.5% | 129.8% |
| PF_2ZUSD | 1 | -53.2% | 53.2% |
| PF_GRASSUSD | 1 | -48.2% | 48.2% |
| PF_GPSUSD | 1 | +44.3% | 44.3% |
| PF_VIRTUALUSD | 1 | -36.7% | 42.6% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 237%), PF_SAGAUSD (crowded 1d, worst 56%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
