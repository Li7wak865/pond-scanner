# Pond Scanner Report
**Scan time:** 2026-10-02 12:37 UTC

**Flags this scan:** 15 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +362.4% | $948,256 |
| 🟢 | PF_LINKUSD | -282.2% | $1,051,139 |
| 🟢 | PF_MOVRUSD | +268.6% | $1,871,551 |
| 🟢 | PF_TRUMPUSD | +150.9% | $581,292 |
| 🟢 | PF_SANDUSD | -148.5% | $7,309,143 |
| 🟢 | PF_NEARUSD | +134.3% | $4,950,061 |
| 🟢 | PF_MANAUSD | -85.9% | $3,455,911 |
| 🟢 | PF_TIAUSD | +67.8% | $1,198,735 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.049%** (kraken → gemini) — coinbase: $86,941.88, kraken: $86,933.60, gemini: $86,975.94
- ⚪ **ETH** gap **0.082%** (gemini → coinbase) — coinbase: $2,757.65, kraken: $2,757.19, gemini: $2,755.38

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Enjin Coin (ENJ) | #371 | $74.8M | 0.80x | +28.3% |
| Cap (CAP) | #302 | $97.8M | 0.70x | -17.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.42, realized vol 10d 23% vs 60d 43%
- 🟡 **ETH: MIXED** — efficiency ratio 0.29, realized vol 10d 20% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 36% vs 30d norm 35% (1.0x)
- ⚪ **ETH** 24h vol 34% vs 30d norm 46% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +362.4% | 543.2% |
| PF_LINKUSD | 2 | -282.2% | 282.2% |
| PF_MOVRUSD | 2 | +268.6% | 289.0% |
| PF_TRUMPUSD | 1 | +150.9% | 150.9% |
| PF_SANDUSD | 1 | -148.5% | 148.5% |
| PF_NEARUSD | 1 | +134.3% | 134.3% |
| PF_MANAUSD | 1 | -85.9% | 85.9% |
| PF_TIAUSD | 1 | +67.8% | 67.8% |
| PF_ASTERUSD | 1 | +57.4% | 57.4% |
| PF_SYNUSD | 1 | +46.6% | 46.6% |
| PF_XRPUSD | 1 | +45.4% | 87.9% |
| PF_JUPUSD | 1 | +35.2% | 47.9% |
| PF_VIRTUALUSD | 1 | +34.6% | 50.7% |

**Resolved since last scan:** PF_OPNUSD (crowded 1d, worst 269%), PF_ZROUSD (crowded 1d, worst 67%), PF_DOTUSD (crowded 1d, worst 55%), PF_SUIUSD (crowded 1d, worst 45%), PF_WLDUSD (crowded 1d, worst 40%), PF_ALICEUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
