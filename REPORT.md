# Pond Scanner Report
**Scan time:** 2026-09-06 04:41 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BELUSD | +533.3% | $668,581 |
| 🟢 | PF_TRUMPUSD | +375.1% | $2,078,352 |
| 🟢 | PF_MINAUSD | +335.2% | $523,600 |
| 🟢 | PF_NEARUSD | -163.9% | $1,305,943 |
| 🟢 | PF_UNIUSD | -147.3% | $1,324,728 |
| 🟢 | PF_HFTUSD | +112.7% | $2,323,265 |
| 🟢 | PF_BLURUSD | +74.4% | $689,742 |
| 🟢 | PF_JUPUSD | +64.8% | $504,920 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (coinbase → gemini) — coinbase: $79,913.99, kraken: $79,914.20, gemini: $79,922.84
- ⚪ **ETH** gap **0.034%** (gemini → kraken) — coinbase: $2,502.57, kraken: $2,502.69, gemini: $2,501.85

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Sushi (SUSHI) | #372 | $67.4M | 1.56x | +22.6% |
| BOOK OF MEME (BOME) | #365 | $69.9M | 1.06x | +19.1% |
| STONK (STONK) | #273 | $101.1M | 0.79x | +301.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 40% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 43% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 12% vs 30d norm 40% (0.3x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 54% (0.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +375.1% | 375.1% |
| PF_HFTUSD | 3 | +112.7% | 113.8% |
| PF_NEARUSD | 2 | -163.9% | 163.9% |
| PF_UNIUSD | 2 | -147.3% | 387.6% |
| PF_BELUSD | 1 | +533.3% | 533.3% |
| PF_MINAUSD | 1 | +335.2% | 335.2% |
| PF_BLURUSD | 1 | +74.4% | 74.4% |
| PF_JUPUSD | 1 | +64.8% | 64.8% |
| PF_ICXUSD | 1 | -63.5% | 63.5% |
| PF_VIRTUALUSD | 1 | +51.8% | 51.8% |
| PF_IOTAUSD | 1 | -31.1% | 31.1% |

**Resolved since last scan:** PF_ACEUSD (crowded 6d, worst 305%), PF_ASTERUSD (crowded 2d, worst 84%), PF_SUSHIUSD (crowded 2d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
