# Pond Scanner Report
**Scan time:** 2026-11-14 06:25 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -246.0% | $671,184 |
| 🟢 | PF_SOLUSD | -110.1% | $1,105,502 |
| 🟢 | PF_AVAXUSD | -101.4% | $548,204 |
| 🟢 | PF_STXUSD | -40.0% | $606,901 |
| 🟢 | PF_INJUSD | -38.1% | $700,050 |
| 🟢 | PF_TRUMPUSD | -35.5% | $714,466 |
| 🟢 | PF_FILUSD | -31.3% | $588,760 |
| ⚪ | PF_ONDOUSD | -25.6% | $3,171,538 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (coinbase → gemini) — coinbase: $67,289.29, kraken: $67,300.00, gemini: $67,305.78
- ⚪ **ETH** gap **0.116%** (coinbase → gemini) — coinbase: $1,906.31, kraken: $1,906.68, gemini: $1,908.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Berachain (BERA) | #455 | $45.1M | 1.13x | +23.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.48, realized vol 10d 38% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 51% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9956 (-0.44% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 45% vs 30d norm 37% (1.2x)
- ⚪ **ETH** 24h vol 53% vs 30d norm 51% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -246.0% | 273.6% |
| PF_SOLUSD | 2 | -110.1% | 822.3% |
| PF_AVAXUSD | 2 | -101.4% | 175.5% |
| PF_INJUSD | 2 | -38.1% | 154.5% |
| PF_STXUSD | 1 | -40.0% | 40.0% |
| PF_TRUMPUSD | 1 | -35.5% | 35.5% |
| PF_FILUSD | 1 | -31.3% | 31.3% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 714%), PF_ZROUSD (crowded 2d, worst 187%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
