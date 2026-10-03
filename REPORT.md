# Pond Scanner Report
**Scan time:** 2026-10-03 16:18 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +152.4% | $1,023,185 |
| 🟢 | PF_LINKUSD | +113.0% | $513,348 |
| 🟢 | PF_MOVRUSD | -112.9% | $525,468 |
| 🟢 | PF_VIRTUALUSD | +77.9% | $651,301 |
| 🟢 | PF_SANDUSD | -58.4% | $38,595,728 |
| 🟢 | PF_UNIUSD | +54.3% | $916,961 |
| 🟢 | PF_ASTERUSD | +51.4% | $642,144 |
| 🟢 | PF_NEARUSD | -46.2% | $2,004,809 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (coinbase → gemini) — coinbase: $84,803.86, kraken: $84,804.20, gemini: $84,805.22
- ⚪ **ETH** gap **0.003%** (kraken → gemini) — coinbase: $2,678.14, kraken: $2,678.11, gemini: $2,678.19

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #417 | $62.7M | 1.91x | +36.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.38, realized vol 10d 13% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.27, realized vol 10d 11% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 34% (0.5x)
- ⚪ **ETH** 24h vol 18% vs 30d norm 45% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +113.0% | 329.1% |
| PF_MOVRUSD | 3 | -112.9% | 289.0% |
| PF_ZROUSD | 2 | +152.4% | 152.4% |
| PF_SANDUSD | 2 | -58.4% | 148.5% |
| PF_NEARUSD | 2 | -46.2% | 134.3% |
| PF_VIRTUALUSD | 1 | +77.9% | 77.9% |
| PF_UNIUSD | 1 | +54.3% | 54.3% |
| PF_ASTERUSD | 1 | +51.4% | 51.4% |
| PF_PONSUSD | 1 | +42.5% | 111.2% |
| PF_DOTUSD | 1 | +36.2% | 36.2% |
| PF_FILUSD | 1 | +31.2% | 31.2% |

**Resolved since last scan:** PF_BATUSD (crowded 1d, worst 216%), PF_TRUMPUSD (crowded 2d, worst 151%), PF_RUNEUSD (crowded 1d, worst 36%), PF_ALICEUSD (crowded 1d, worst 35%), PF_TIAUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
