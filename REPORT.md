# Pond Scanner Report
**Scan time:** 2026-10-01 13:17 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +272.3% | $6,183,550 |
| 🟢 | PF_OPNUSD | +268.5% | $690,940 |
| 🟢 | PF_LINKUSD | +234.3% | $524,210 |
| 🟢 | PF_UNIUSD | +210.9% | $693,023 |
| 🟢 | PF_ZROUSD | -128.4% | $579,448 |
| 🟢 | PF_TRUMPUSD | -102.7% | $1,141,211 |
| 🟢 | PF_PONSUSD | +96.9% | $810,506 |
| 🟢 | PF_SOONUSD | -51.8% | $552,289 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.010%** (coinbase → gemini) — coinbase: $83,533.92, kraken: $83,541.90, gemini: $83,542.23
- ⚪ **ETH** gap **0.008%** (kraken → gemini) — coinbase: $2,687.30, kraken: $2,687.28, gemini: $2,687.50

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| 龙虾 (Lobster) (龙虾) | #316 | $87.7M | 0.92x | +55.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.32, realized vol 10d 14% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 15% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 35% (0.9x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 46% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +272.3% | 372.8% |
| PF_UNIUSD | 2 | +210.9% | 543.2% |
| PF_TRUMPUSD | 2 | -102.7% | 102.7% |
| PF_PONSUSD | 2 | +96.9% | 96.9% |
| PF_OPNUSD | 1 | +268.5% | 268.5% |
| PF_LINKUSD | 1 | +234.3% | 234.3% |
| PF_ZROUSD | 1 | -128.4% | 128.4% |
| PF_SOONUSD | 1 | -51.8% | 51.8% |
| PF_SUIUSD | 1 | +51.7% | 51.7% |
| PF_TRXUSD | 1 | -47.6% | 47.6% |
| PF_FILUSD | 1 | -44.9% | 44.9% |
| PF_VIRTUALUSD | 1 | -31.7% | 31.7% |

**Resolved since last scan:** PF_MOVRUSD (crowded 2d, worst 952%), PF_AVAXUSD (crowded 3d, worst 290%), PF_ETHFIUSD (crowded 1d, worst 38%), PF_WLDUSD (crowded 2d, worst 41%), PF_LSKUSD (crowded 2d, worst 73%), PF_DOTUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
