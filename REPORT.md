# Pond Scanner Report
**Scan time:** 2026-09-17 21:23 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -960.6% | $2,078,162 |
| 🟢 | PF_NATGASUSD | +124.6% | $581,259 |
| 🟢 | PF_MUBARAKUSD | -108.3% | $10,562,020 |
| 🟢 | PF_NEARUSD | +102.9% | $5,639,774 |
| 🟢 | PF_UNIUSD | +94.2% | $1,891,574 |
| 🟢 | PF_FILUSD | -34.4% | $1,045,701 |
| ⚪ | PF_ASTERUSD | -28.3% | $665,195 |
| ⚪ | PF_SUIUSD | +27.9% | $6,869,864 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $76,463.93, kraken: $76,467.00, gemini: $76,477.73
- ⚪ **ETH** gap **0.035%** (gemini → kraken) — coinbase: $2,449.58, kraken: $2,449.62, gemini: $2,448.77

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #364 | $69.8M | 1.35x | +34.8% |
| Canopy (CNPY) | #411 | $59.1M | 1.09x | +35.6% |
| Lisk (LSK) | #274 | $101.9M | 0.94x | -40.3% |
| MarsCoin (MARSCOIN) | #252 | $115.6M | 0.67x | +29.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.07, realized vol 10d 28% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 40% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **PYUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 42% (0.5x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 60% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 2 | +102.9% | 137.4% |
| PF_LSKUSD | 1 | -960.6% | 960.6% |
| PF_NATGASUSD | 1 | +124.6% | 124.6% |
| PF_MUBARAKUSD | 1 | -108.3% | 108.3% |
| PF_UNIUSD | 1 | +94.2% | 311.9% |
| PF_FILUSD | 1 | -34.4% | 34.4% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 1d, worst 109%), PF_SYNUSD (crowded 2d, worst 86%), PF_SUIUSD (crowded 1d, worst 49%), PF_DOTUSD (crowded 1d, worst 39%), PF_ASTERUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
