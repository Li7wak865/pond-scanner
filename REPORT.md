# Pond Scanner Report
**Scan time:** 2026-11-19 07:27 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +768.6% | $554,586 |
| 🟢 | PF_UNIUSD | -175.8% | $582,997 |
| 🟢 | PF_ZROUSD | +107.5% | $1,246,076 |
| 🟢 | PF_NEARUSD | -63.9% | $2,843,143 |
| ⚪ | PF_TRUMPUSD | -19.7% | $670,431 |
| ⚪ | PF_TRXUSD | +15.6% | $2,162,956 |
| ⚪ | PF_TIAUSD | +11.7% | $772,161 |
| ⚪ | PF_WLDUSD | -10.2% | $685,238 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (kraken → gemini) — coinbase: $63,523.95, kraken: $63,521.90, gemini: $63,535.23
- ⚪ **ETH** gap **0.087%** (kraken → gemini) — coinbase: $1,802.28, kraken: $1,802.07, gemini: $1,803.64

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #483 | $39.8M | 3.73x | -15.9% |
| Irys (IRYS) | #414 | $48.6M | 1.15x | +53.8% |
| Dolphin (POD) | #497 | $37.7M | 0.64x | +24.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.48, realized vol 10d 46% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.41, realized vol 10d 62% vs 60d 49%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9955 (-0.45% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 43% (1.1x)
- ⚪ **ETH** 24h vol 57% vs 30d norm 58% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 6 | -63.9% | 245.2% |
| PF_UNIUSD | 3 | -175.8% | 175.8% |
| PF_SOLUSD | 2 | +768.6% | 768.6% |
| PF_ZROUSD | 1 | +107.5% | 107.5% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
