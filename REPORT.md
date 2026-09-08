# Pond Scanner Report
**Scan time:** 2026-09-08 11:21 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | -139.1% | $653,936 |
| 🟢 | PF_INJUSD | +85.5% | $667,958 |
| 🟢 | PF_TRUMPUSD | +75.1% | $863,150 |
| 🟢 | PF_ASTERUSD | +61.8% | $962,957 |
| 🟢 | PF_ACEUSD | -58.4% | $2,969,050 |
| 🟢 | PF_DOTUSD | +54.6% | $5,097,545 |
| 🟢 | PF_NEARUSD | +34.1% | $1,179,918 |
| 🟢 | PF_KAITOUSD | +33.4% | $590,842 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → gemini) — coinbase: $78,399.60, kraken: $78,398.00, gemini: $78,406.90
- ⚪ **ETH** gap **0.009%** (coinbase → kraken) — coinbase: $2,475.12, kraken: $2,475.34, gemini: $2,475.28

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| A Meme Coin (AMC) | #284 | $96.2M | 0.50x | -18.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 37% vs 60d 39%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 40% (0.6x)
- ⚪ **ETH** 24h vol 37% vs 30d norm 54% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | +75.1% | 476.2% |
| PF_INJUSD | 2 | +85.5% | 604.5% |
| PF_ACEUSD | 2 | -58.4% | 289.3% |
| PF_UNIUSD | 1 | -139.1% | 139.1% |
| PF_ASTERUSD | 1 | +61.8% | 61.8% |
| PF_DOTUSD | 1 | +54.6% | 54.6% |
| PF_NEARUSD | 1 | +34.1% | 34.1% |
| PF_KAITOUSD | 1 | +33.4% | 33.4% |
| PF_HFTUSD | 1 | -32.0% | 32.0% |

**Resolved since last scan:** PF_ICPUSD (crowded 2d, worst 256%), PF_CFGUSD (crowded 2d, worst 114%), PF_LINKUSD (crowded 2d, worst 237%), PF_VIRTUALUSD (crowded 1d, worst 67%), PF_APTUSD (crowded 2d, worst 43%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
