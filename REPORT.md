# Pond Scanner Report
**Scan time:** 2026-10-22 04:49 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | +94.9% | $1,274,624 |
| 🟢 | PF_NEARUSD | +81.5% | $5,161,281 |
| 🟢 | PF_FILUSD | -77.8% | $3,889,247 |
| 🟢 | PF_UNIUSD | +65.1% | $502,431 |
| 🟢 | PF_TIAUSD | -58.6% | $3,272,059 |
| 🟢 | PF_IMXUSD | -53.1% | $687,177 |
| 🟢 | PF_BATUSD | +49.5% | $3,450,554 |
| 🟢 | PF_ZROUSD | -46.8% | $650,896 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $82,735.61, kraken: $82,736.40, gemini: $82,745.25
- ⚪ **ETH** gap **0.097%** (coinbase → gemini) — coinbase: $2,439.39, kraken: $2,439.60, gemini: $2,441.75

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| AltLayer (ALT) | #306 | $89.4M | 1.35x | +20.8% |
| PHALA (PHA) | #408 | $56.1M | 0.97x | +15.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.09, realized vol 10d 22% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.30, realized vol 10d 28% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **DAI** $1.0010 (+0.10% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 42% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +94.9% | 94.9% |
| PF_NEARUSD | 2 | +81.5% | 116.8% |
| PF_BATUSD | 2 | +49.5% | 49.5% |
| PF_ZROUSD | 2 | -46.8% | 46.8% |
| PF_FILUSD | 1 | -77.8% | 77.8% |
| PF_UNIUSD | 1 | +65.1% | 65.1% |
| PF_TIAUSD | 1 | -58.6% | 58.6% |
| PF_IMXUSD | 1 | -53.1% | 53.1% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
