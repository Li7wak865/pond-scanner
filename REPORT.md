# Pond Scanner Report
**Scan time:** 2026-11-22 19:42 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | +281.1% | $11,613,854 |
| 🟢 | PF_UNIUSD | -222.0% | $574,282 |
| 🟢 | PF_TRUMPUSD | -52.1% | $566,489 |
| 🟢 | PF_NEARUSD | +40.5% | $1,438,937 |
| ⚪ | PF_ETHFIUSD | -26.6% | $1,073,324 |
| ⚪ | PF_JUPUSD | -19.1% | $634,116 |
| ⚪ | PF_TIAUSD | -18.4% | $2,969,692 |
| ⚪ | PF_ONDOUSD | -12.3% | $1,857,745 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → gemini) — coinbase: $60,621.13, kraken: $60,624.80, gemini: $60,630.16
- ⚪ **ETH** gap **0.046%** (kraken → gemini) — coinbase: $1,711.24, kraken: $1,711.14, gemini: $1,711.93

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Akedo (AKE) | #331 | $63.4M | 0.82x | -48.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 53% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 78% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9949 (-0.51% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9990 (-0.10% vs peg)
- ⚪ **USDC** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 59% vs 30d norm 52% (1.1x)
- ⚪ **ETH** 24h vol 53% vs 30d norm 65% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 6 | -222.0% | 222.0% |
| PF_ACEUSD | 1 | +281.1% | 281.1% |
| PF_TRUMPUSD | 1 | -52.1% | 52.1% |
| PF_NEARUSD | 1 | +40.5% | 40.5% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
