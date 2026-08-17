# Pond Scanner Report
**Scan time:** 2026-08-17 01:55 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZEREBROUSD | -190.9% | $587,359 |
| 🟢 | PF_ACEUSD | -188.4% | $9,195,125 |
| 🟢 | PF_LINKUSD | +131.8% | $513,146 |
| 🟢 | PF_MOODENGUSD | +69.2% | $876,671 |
| 🟢 | PF_ALICEUSD | -46.8% | $2,280,337 |
| 🟢 | PF_KAITOUSD | -46.1% | $1,233,075 |
| 🟢 | PF_BICOUSD | -43.6% | $53,173,367 |
| 🟢 | PF_HFTUSD | +41.4% | $5,219,946 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (kraken → gemini) — coinbase: $63,052.28, kraken: $63,050.00, gemini: $63,058.70
- ⚪ **ETH** gap **0.051%** (kraken → gemini) — coinbase: $1,890.18, kraken: $1,890.01, gemini: $1,890.97

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #441 | $46.3M | 1.87x | -16.6% |
| Capricorn (APR) | #408 | $52.6M | 0.62x | +20.9% |
| CoW Protocol (COW) | #352 | $64.2M | 0.53x | -19.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 9% vs 60d 27%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 14% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 10% vs 30d norm 25% (0.4x)
- ⚪ **ETH** 24h vol 18% vs 30d norm 34% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 4 | +131.8% | 227.6% |
| PF_ALICEUSD | 4 | -46.8% | 195.8% |
| PF_ACEUSD | 3 | -188.4% | 732.3% |
| PF_ZEREBROUSD | 2 | -190.9% | 190.9% |
| PF_HFTUSD | 2 | +41.4% | 117.4% |
| PF_MOODENGUSD | 1 | +69.2% | 69.2% |
| PF_KAITOUSD | 1 | -46.1% | 46.1% |
| PF_BICOUSD | 1 | -43.6% | 43.6% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 2d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
