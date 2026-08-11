# Pond Scanner Report
**Scan time:** 2026-08-11 19:23 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -704.4% | $559,448 |
| 🟢 | PF_UNIUSD | -116.0% | $1,274,717 |
| 🟢 | PF_RUNEUSD | +90.3% | $504,457 |
| 🟢 | PF_JUPUSD | -51.9% | $1,660,176 |
| ⚪ | PF_FILUSD | +24.1% | $684,127 |
| ⚪ | PF_ACEUSD | -23.8% | $4,142,067 |
| ⚪ | PF_MONUSD | +19.0% | $3,884,741 |
| ⚪ | PF_FETUSD | -18.0% | $4,664,426 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (kraken → gemini) — coinbase: $63,276.19, kraken: $63,268.70, gemini: $63,287.24
- ⚪ **ETH** gap **0.061%** (kraken → gemini) — coinbase: $1,865.88, kraken: $1,865.22, gemini: $1,866.35

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #276 | $88.3M | 1.25x | +21.1% |
| Tutorial (TUT) | #296 | $77.2M | 1.00x | -29.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 16% vs 60d 29%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.13, realized vol 10d 23% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9970 (-0.30% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 28% (0.7x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 40% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 1 | -704.4% | 704.4% |
| PF_UNIUSD | 1 | -116.0% | 116.0% |
| PF_RUNEUSD | 1 | +90.3% | 90.3% |
| PF_JUPUSD | 1 | -51.9% | 51.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 984%), PF_ENJUSD (crowded 1d, worst 108%), PF_RAREUSD (crowded 1d, worst 53%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
