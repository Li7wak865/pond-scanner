# Pond Scanner Report
**Scan time:** 2026-09-02 11:19 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +638.4% | $558,868 |
| 🟢 | PF_UNIUSD | +280.5% | $1,715,502 |
| 🟢 | PF_ACEUSD | -262.6% | $4,900,060 |
| 🟢 | PF_TRUMPUSD | +88.1% | $1,030,254 |
| 🟢 | PF_RENDERUSD | -65.1% | $780,743 |
| 🟢 | PF_SAGAUSD | +63.8% | $2,449,716 |
| ⚪ | PF_TIAUSD | +23.7% | $626,229 |
| ⚪ | PF_TUSD | -22.8% | $28,117,956 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $76,506.32, kraken: $76,508.90, gemini: $76,517.02
- ⚪ **ETH** gap **0.003%** (kraken → coinbase) — coinbase: $2,371.46, kraken: $2,371.40, gemini: $2,371.40

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #357 | $65.8M | 1.52x | +63.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.47, realized vol 10d 27% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.41, realized vol 10d 34% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 38% (0.7x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 52% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +280.5% | 280.5% |
| PF_SOLUSD | 2 | +638.4% | 638.4% |
| PF_ACEUSD | 2 | -262.6% | 304.8% |
| PF_RENDERUSD | 2 | -65.1% | 175.0% |
| PF_TRUMPUSD | 1 | +88.1% | 88.1% |
| PF_SAGAUSD | 1 | +63.8% | 63.8% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 57%), PF_DOTUSD (crowded 1d, worst 39%), PF_LDOUSD (crowded 1d, worst 36%), PF_POPCATUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
