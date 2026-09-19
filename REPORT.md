# Pond Scanner Report
**Scan time:** 2026-09-19 20:41 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -984.9% | $557,613 |
| 🟢 | PF_UNIUSD | +427.7% | $1,007,633 |
| 🟢 | PF_HFTUSD | -105.1% | $857,321 |
| 🟢 | PF_AVAXUSD | +80.9% | $1,594,752 |
| 🟢 | PF_MINAUSD | -73.3% | $1,117,444 |
| 🟢 | PF_SYNUSD | +69.2% | $6,442,074 |
| 🟢 | PF_ASTERUSD | -65.1% | $521,295 |
| 🟢 | PF_STXUSD | +57.8% | $547,352 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (kraken → gemini) — coinbase: $81,248.55, kraken: $81,243.60, gemini: $81,257.35
- ⚪ **ETH** gap **0.056%** (gemini → coinbase) — coinbase: $2,639.26, kraken: $2,639.18, gemini: $2,637.79

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #385 | $69.0M | 4.36x | +27.1% |
| Harmony (ONE) | #415 | $63.8M | 3.07x | +149.4% |
| Synapse (SYN) | #450 | $53.6M | 2.00x | +38.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 45% vs 60d 41%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 56% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 40% (0.6x)
- ⚪ **ETH** 24h vol 26% vs 30d norm 51% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +427.7% | 583.0% |
| PF_HFTUSD | 2 | -105.1% | 107.0% |
| PF_SOLUSD | 1 | -984.9% | 984.9% |
| PF_AVAXUSD | 1 | +80.9% | 168.4% |
| PF_MINAUSD | 1 | -73.3% | 73.3% |
| PF_SYNUSD | 1 | +69.2% | 127.9% |
| PF_ASTERUSD | 1 | -65.1% | 65.1% |
| PF_STXUSD | 1 | +57.8% | 57.8% |
| PF_ACEUSD | 1 | -56.7% | 56.7% |
| PF_DOTUSD | 1 | +47.4% | 47.4% |
| PF_XRPUSD | 1 | +45.3% | 45.3% |
| PF_XTZUSD | 1 | -42.3% | 219.1% |
| PF_APTUSD | 1 | +32.7% | 32.7% |
| PF_KAITOUSD | 1 | +32.5% | 49.9% |

**Resolved since last scan:** PF_NEARUSD (crowded 4d, worst 366%), PF_INJUSD (crowded 2d, worst 518%), PF_TRUMPUSD (crowded 1d, worst 60%), PF_CATIUSD (crowded 1d, worst 56%), PF_ONDOUSD (crowded 1d, worst 43%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
