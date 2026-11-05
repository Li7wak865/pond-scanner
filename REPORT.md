# Pond Scanner Report
**Scan time:** 2026-11-05 19:57 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +987.6% | $779,328 |
| 🟢 | PF_ZROUSD | +123.9% | $559,771 |
| 🟢 | PF_XTZUSD | -73.9% | $2,627,296 |
| 🟢 | PF_TRUMPUSD | -54.4% | $8,243,658 |
| 🟢 | PF_UNIUSD | -45.3% | $1,152,315 |
| 🟢 | PF_STXUSD | -30.3% | $674,126 |
| ⚪ | PF_INJUSD | +29.9% | $587,928 |
| ⚪ | PF_KAITOUSD | -27.5% | $985,897 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.020%** (gemini → kraken) — coinbase: $76,266.54, kraken: $76,275.10, gemini: $76,259.61
- ⚪ **ETH** gap **0.045%** (gemini → kraken) — coinbase: $2,258.61, kraken: $2,259.02, gemini: $2,258.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #447 | $48.4M | 1.94x | -27.7% |
| SanDisk (bStocks Tokenized Stock) (SNDKB) | #271 | $98.4M | 1.10x | -17.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 50% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.20, realized vol 10d 65% vs 60d 45%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDe** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 70% vs 30d norm 35% (2.0x)
- ⚪ **ETH** 24h vol 89% vs 30d norm 49% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 2 | +987.6% | 987.6% |
| PF_TRUMPUSD | 2 | -54.4% | 178.3% |
| PF_ZROUSD | 1 | +123.9% | 123.9% |
| PF_XTZUSD | 1 | -73.9% | 73.9% |
| PF_UNIUSD | 1 | -45.3% | 229.5% |
| PF_STXUSD | 1 | -30.3% | 30.3% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 617%), PF_NEARUSD (crowded 3d, worst 158%), PF_SYNUSD (crowded 1d, worst 34%), PF_BBUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
