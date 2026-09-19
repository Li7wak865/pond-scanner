# Pond Scanner Report
**Scan time:** 2026-09-19 04:39 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -534.0% | $864,510 |
| 🟢 | PF_INJUSD | +348.5% | $596,858 |
| 🟢 | PF_NEARUSD | +123.2% | $5,851,604 |
| 🟢 | PF_ETHFIUSD | +77.5% | $1,447,574 |
| 🟢 | PF_UNIUSD | +74.6% | $1,698,078 |
| 🟢 | PF_DEEPUSD | -74.0% | $582,337 |
| 🟢 | PF_DOTUSD | +69.5% | $2,284,314 |
| 🟢 | PF_XTZUSD | +69.0% | $1,103,366 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (coinbase → gemini) — coinbase: $80,922.94, kraken: $80,926.50, gemini: $80,935.23
- ⚪ **ETH** gap **0.023%** (coinbase → gemini) — coinbase: $2,613.61, kraken: $2,613.73, gemini: $2,614.20

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #412 | $63.3M | 8.22x | +78.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 45% vs 60d 41%
- 🟡 **ETH: MIXED** — efficiency ratio 0.21, realized vol 10d 56% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9995 (-0.05% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 58% vs 30d norm 41% (1.4x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 52% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | +123.2% | 176.8% |
| PF_UNIUSD | 3 | +74.6% | 583.0% |
| PF_LSKUSD | 2 | -534.0% | 673.9% |
| PF_INJUSD | 2 | +348.5% | 387.6% |
| PF_ETHFIUSD | 2 | +77.5% | 120.6% |
| PF_JTOUSD | 2 | +52.2% | 85.3% |
| PF_HFTUSD | 2 | -49.1% | 100.7% |
| PF_STGUSD | 2 | -38.4% | 76.9% |
| PF_DEEPUSD | 1 | -74.0% | 74.0% |
| PF_DOTUSD | 1 | +69.5% | 69.5% |
| PF_XTZUSD | 1 | +69.0% | 69.0% |
| PF_FILUSD | 1 | +65.3% | 65.3% |
| PF_CATIUSD | 1 | +50.1% | 50.1% |
| PF_APTUSD | 1 | +48.6% | 48.6% |
| PF_KAITOUSD | 1 | +42.4% | 42.4% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 444%), PF_BATUSD (crowded 2d, worst 130%), PF_TRUMPUSD (crowded 2d, worst 105%), PF_TUSD (crowded 2d, worst 83%), PF_ASTERUSD (crowded 2d, worst 73%), PF_GRIFFAINUSD (crowded 2d, worst 62%), PF_XRPUSD (crowded 2d, worst 73%), PF_RUNEUSD (crowded 2d, worst 41%), PF_CRVUSD (crowded 2d, worst 34%), PF_LDOUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
