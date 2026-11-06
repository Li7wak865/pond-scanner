# Pond Scanner Report
**Scan time:** 2026-11-06 19:25 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -237.4% | $509,383 |
| 🟢 | PF_TRUMPUSD | -72.3% | $3,735,600 |
| 🟢 | PF_FILUSD | -58.1% | $799,628 |
| 🟢 | PF_ZROUSD | -52.1% | $802,783 |
| ⚪ | PF_NEARUSD | -27.1% | $6,069,710 |
| ⚪ | PF_SUIUSD | -21.2% | $3,069,945 |
| ⚪ | PF_TIAUSD | -20.3% | $1,944,998 |
| ⚪ | PF_ACEUSD | +16.5% | $2,305,333 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → kraken) — coinbase: $75,644.88, kraken: $75,658.60, gemini: $75,655.51
- ⚪ **ETH** gap **0.055%** (coinbase → gemini) — coinbase: $2,224.61, kraken: $2,225.27, gemini: $2,225.84

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Magma Finance (MAGMA) | #434 | $50.8M | 3.91x | -23.7% |
| Akedo (AKE) | #295 | $84.3M | 1.30x | +49.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.24, realized vol 10d 50% vs 60d 37%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 68% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9966 (-0.34% vs peg)
- ⚪ **USDe** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 35% (0.8x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 49% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 3 | -237.4% | 987.6% |
| PF_TRUMPUSD | 3 | -72.3% | 178.3% |
| PF_ZROUSD | 2 | -52.1% | 123.9% |
| PF_FILUSD | 1 | -58.1% | 58.1% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 229%), PF_INJUSD (crowded 1d, worst 65%), PF_NEARUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
