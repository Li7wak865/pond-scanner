# Pond Scanner Report
**Scan time:** 2026-11-14 18:03 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -321.6% | $579,372 |
| 🟢 | PF_UNIUSD | -249.7% | $632,801 |
| 🟢 | PF_NEARUSD | -163.7% | $2,299,966 |
| 🟢 | PF_KAVAUSD | -159.8% | $24,446,052 |
| 🟢 | PF_TRUMPUSD | -78.2% | $652,308 |
| 🟢 | PF_XRPUSD | -39.6% | $21,412,642 |
| 🟢 | PF_ZROUSD | -37.1% | $749,025 |
| 🟢 | PF_SUIUSD | -35.3% | $4,721,453 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.026%** (kraken → gemini) — coinbase: $65,846.12, kraken: $65,841.80, gemini: $65,859.11
- ⚪ **ETH** gap **0.021%** (coinbase → kraken) — coinbase: $1,839.12, kraken: $1,839.51, gemini: $1,839.44

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Kava (KAVA) | #451 | $42.2M | 1.22x | -42.8% |
| Lombard (BARD) | #403 | $50.1M | 0.53x | -15.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 39% vs 60d 40%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.49, realized vol 10d 51% vs 60d 48%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9955 (-0.45% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 37% (1.3x)
- ⚪ **ETH** 24h vol 66% vs 30d norm 51% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | -249.7% | 273.6% |
| PF_INJUSD | 2 | -321.6% | 321.6% |
| PF_NEARUSD | 1 | -163.7% | 163.7% |
| PF_KAVAUSD | 1 | -159.8% | 159.8% |
| PF_TRUMPUSD | 1 | -78.2% | 78.2% |
| PF_XRPUSD | 1 | -39.6% | 39.6% |
| PF_ZROUSD | 1 | -37.1% | 37.1% |
| PF_SUIUSD | 1 | -35.3% | 35.3% |
| PF_ASTERUSD | 1 | +34.6% | 34.6% |
| PF_TRXUSD | 1 | -30.4% | 30.4% |
| PF_DOTUSD | 1 | -30.1% | 30.1% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 822%), PF_AVAXUSD (crowded 2d, worst 176%), PF_STXUSD (crowded 1d, worst 40%), PF_FILUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
