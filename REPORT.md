# Pond Scanner Report
**Scan time:** 2026-09-08 04:38 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | +604.4% | $603,206 |
| 🟢 | PF_ICPUSD | +256.0% | $507,262 |
| 🟢 | PF_TRUMPUSD | -131.0% | $840,566 |
| 🟢 | PF_ACEUSD | -123.2% | $2,768,644 |
| 🟢 | PF_CFGUSD | -114.2% | $661,550 |
| 🟢 | PF_LINKUSD | -85.9% | $585,028 |
| 🟢 | PF_VIRTUALUSD | +67.3% | $1,052,494 |
| 🟢 | PF_APTUSD | +43.5% | $622,727 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (coinbase → kraken) — coinbase: $78,782.98, kraken: $78,786.10, gemini: $78,783.85
- ⚪ **ETH** gap **0.016%** (kraken → coinbase) — coinbase: $2,482.53, kraken: $2,482.13, gemini: $2,482.24

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| A Meme Coin (AMC) | #256 | $110.3M | 0.54x | +28.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.34, realized vol 10d 37% vs 60d 39%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 40% (0.6x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 54% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -131.0% | 476.2% |
| PF_INJUSD | 2 | +604.4% | 604.4% |
| PF_ICPUSD | 2 | +256.0% | 256.0% |
| PF_ACEUSD | 2 | -123.2% | 289.3% |
| PF_CFGUSD | 2 | -114.2% | 114.2% |
| PF_LINKUSD | 2 | -85.9% | 236.7% |
| PF_APTUSD | 2 | +43.5% | 43.5% |
| PF_VIRTUALUSD | 1 | +67.3% | 67.3% |
| PF_NEARUSD | 1 | -32.0% | 32.0% |
| PF_ASTERUSD | 1 | +30.6% | 30.6% |

**Resolved since last scan:** PF_UNIUSD (crowded 4d, worst 388%), PF_SUIUSD (crowded 2d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
