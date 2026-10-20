# Pond Scanner Report
**Scan time:** 2026-10-20 11:39 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | -93.0% | $573,896 |
| 🟢 | PF_TIAUSD | -34.8% | $2,525,436 |
| 🟢 | PF_ATOMUSD | -31.3% | $577,667 |
| ⚪ | PF_FILUSD | -19.2% | $1,456,746 |
| ⚪ | PF_LDOUSD | -17.4% | $1,029,693 |
| ⚪ | PF_ARCUSD | +13.7% | $3,227,532 |
| ⚪ | PF_PONSUSD | +13.0% | $1,122,749 |
| ⚪ | PF_SANDUSD | -12.3% | $8,858,056 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (coinbase → gemini) — coinbase: $81,445.24, kraken: $81,450.90, gemini: $81,464.39
- ⚪ **ETH** gap **0.033%** (coinbase → gemini) — coinbase: $2,384.40, kraken: $2,384.84, gemini: $2,385.18

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| PHALA (PHA) | #437 | $50.6M | 2.34x | +17.4% |
| AltLayer (ALT) | #328 | $76.2M | 0.59x | +22.4% |
| Dolphin (POD) | #406 | $55.0M | 0.55x | +24.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 23% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.40, realized vol 10d 32% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9972 (-0.28% vs peg)
- ⚪ **PYUSD** $1.0010 (+0.10% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 33% (0.6x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | -93.0% | 93.0% |
| PF_TIAUSD | 1 | -34.8% | 34.8% |
| PF_ATOMUSD | 1 | -31.3% | 31.3% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
