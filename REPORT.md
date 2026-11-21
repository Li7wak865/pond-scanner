# Pond Scanner Report
**Scan time:** 2026-11-21 19:17 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +365.0% | $901,962 |
| 🟢 | PF_UNIUSD | -120.3% | $602,438 |
| 🟢 | PF_NEARUSD | +67.3% | $4,581,545 |
| ⚪ | PF_ETHFIUSD | +18.0% | $2,064,929 |
| ⚪ | PF_SUIUSD | -14.6% | $8,286,256 |
| ⚪ | PF_JUPUSD | -12.1% | $618,773 |
| ⚪ | PF_ONDOUSD | -10.5% | $3,191,678 |
| ⚪ | PF_FETUSD | -10.0% | $7,254,118 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → kraken) — coinbase: $60,179.92, kraken: $60,185.20, gemini: $60,184.74
- ⚪ **ETH** gap **0.076%** (coinbase → gemini) — coinbase: $1,681.12, kraken: $1,681.19, gemini: $1,682.40

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DODO (DODO) | #461 | $39.1M | 1.30x | +16.9% |
| Momentum (MMT) | #426 | $43.5M | 0.78x | -15.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.56, realized vol 10d 52% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.48, realized vol 10d 75% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9944 (-0.56% vs peg)
- ⚪ **USDT** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9987 (-0.13% vs peg)
- ⚪ **USDC** $0.9992 (-0.08% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 122% vs 30d norm 51% (2.4x)
- ⚪ **ETH** 24h vol 125% vs 30d norm 65% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | -120.3% | 220.1% |
| PF_SOLUSD | 1 | +365.0% | 365.0% |
| PF_NEARUSD | 1 | +67.3% | 67.3% |

**Resolved since last scan:** PF_HYPEUSD (crowded 1d, worst 527%), PF_INJUSD (crowded 2d, worst 446%), PF_ZROUSD (crowded 2d, worst 107%), PF_RUNEUSD (crowded 2d, worst 49%), PF_SPXUSD (crowded 2d, worst 54%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
