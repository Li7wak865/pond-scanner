# Pond Scanner Report
**Scan time:** 2026-08-06 14:35 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | -457.5% | $818,440 |
| 🟢 | PF_UNIUSD | +144.4% | $2,285,019 |
| 🟢 | PF_ZIGUSD | -84.2% | $659,035 |
| 🟢 | PF_SUSD | +68.3% | $1,192,054 |
| 🟢 | PF_SYNUSD | -53.5% | $4,019,278 |
| 🟢 | PF_MOODENGUSD | +53.2% | $1,111,215 |
| 🟢 | PF_AXSUSD | +43.5% | $559,647 |
| 🟢 | PF_HFTUSD | -38.1% | $122,705,154 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.048%** (kraken → gemini) — coinbase: $64,528.32, kraken: $64,503.90, gemini: $64,534.96
- ⚪ **ETH** gap **0.063%** (kraken → gemini) — coinbase: $1,909.86, kraken: $1,909.32, gemini: $1,910.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| ZEROBASE (ZBT) | #410 | $51.1M | 2.27x | +40.4% |
| Bless (BLESS) | #448 | $45.6M | 0.83x | +24.7% |
| SkyAI (SKYAI) | #290 | $81.6M | 0.72x | +47.8% |
| Orochi Network (ON) | #425 | $49.2M | 0.53x | +26.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 29% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 17% vs 30d norm 30% (0.6x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 42% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SOLUSD | 1 | -457.5% | 457.5% |
| PF_UNIUSD | 1 | +144.4% | 144.4% |
| PF_ZIGUSD | 1 | -84.2% | 84.2% |
| PF_SUSD | 1 | +68.3% | 68.3% |
| PF_SYNUSD | 1 | -53.5% | 53.5% |
| PF_MOODENGUSD | 1 | +53.2% | 53.2% |
| PF_AXSUSD | 1 | +43.5% | 43.5% |
| PF_HFTUSD | 1 | -38.1% | 38.1% |
| PF_NEARUSD | 1 | +37.9% | 37.9% |

**Resolved since last scan:** PF_ETHFIUSD (crowded 1d, worst 68%), PF_GRIFFAINUSD (crowded 1d, worst 41%), PF_FILUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
