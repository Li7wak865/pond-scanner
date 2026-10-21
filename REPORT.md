# Pond Scanner Report
**Scan time:** 2026-10-21 04:50 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +278.8% | $694,830 |
| 🟢 | PF_ZROUSD | -115.4% | $727,235 |
| 🟢 | PF_TRUMPUSD | +93.4% | $623,072 |
| 🟢 | PF_UNIUSD | +78.6% | $597,582 |
| 🟢 | PF_ASTERUSD | +44.5% | $617,692 |
| 🟢 | PF_ACEUSD | +44.3% | $3,456,097 |
| ⚪ | PF_BATUSD | -29.6% | $4,749,732 |
| ⚪ | PF_NEARUSD | -23.2% | $4,630,430 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $82,698.52, kraken: $82,701.10, gemini: $82,705.12
- ⚪ **ETH** gap **0.014%** (gemini → kraken) — coinbase: $2,441.14, kraken: $2,441.16, gemini: $2,440.81

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Janction (JCT) | #471 | $49.0M | 0.97x | +98.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 23% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.35, realized vol 10d 33% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9980 (-0.20% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 37% vs 30d norm 33% (1.1x)
- ⚪ **ETH** 24h vol 61% vs 30d norm 43% (1.4x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 3 | -115.4% | 165.8% |
| PF_LINKUSD | 2 | +278.8% | 278.8% |
| PF_TRUMPUSD | 2 | +93.4% | 93.4% |
| PF_ASTERUSD | 2 | +44.5% | 55.7% |
| PF_UNIUSD | 1 | +78.6% | 78.6% |
| PF_ACEUSD | 1 | +44.3% | 44.3% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 241%), PF_FILUSD (crowded 2d, worst 50%), PF_APTUSD (crowded 2d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
