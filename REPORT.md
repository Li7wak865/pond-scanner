# Pond Scanner Report
**Scan time:** 2026-09-13 16:18 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALCHUSD | -153.7% | $4,269,262 |
| 🟢 | PF_POWRUSD | -125.2% | $8,343,330 |
| 🟢 | PF_STEEMUSD | -87.8% | $3,031,278 |
| 🟢 | PF_FILUSD | -80.8% | $937,563 |
| 🟢 | PF_DYMUSD | +65.0% | $600,912 |
| 🟢 | PF_ACEUSD | -59.5% | $879,463 |
| 🟢 | PF_DOTUSD | -49.9% | $2,010,258 |
| 🟢 | PF_RIVERUSD | +47.2% | $593,401 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (kraken → gemini) — coinbase: $77,187.95, kraken: $77,182.40, gemini: $77,191.33
- ⚪ **ETH** gap **0.037%** (kraken → coinbase) — coinbase: $2,499.45, kraken: $2,498.53, gemini: $2,498.59

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Teller (DEBIT) | #446 | $50.5M | 2.40x | +50.1% |
| VeThor (VTHO) | #312 | $83.1M | 1.25x | +21.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.10, realized vol 10d 20% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.02, realized vol 10d 28% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 15% vs 30d norm 41% (0.4x)
- ⚪ **ETH** 24h vol 28% vs 30d norm 58% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ALCHUSD | 1 | -153.7% | 153.7% |
| PF_POWRUSD | 1 | -125.2% | 195.0% |
| PF_STEEMUSD | 1 | -87.8% | 93.4% |
| PF_FILUSD | 1 | -80.8% | 80.8% |
| PF_DYMUSD | 1 | +65.0% | 65.0% |
| PF_ACEUSD | 1 | -59.5% | 59.5% |
| PF_DOTUSD | 1 | -49.9% | 49.9% |
| PF_RIVERUSD | 1 | +47.2% | 102.8% |
| PF_UNIUSD | 1 | -44.3% | 247.8% |
| PF_ICXUSD | 1 | -36.4% | 36.4% |
| PF_VIRTUALUSD | 1 | +30.3% | 52.8% |

**Resolved since last scan:** PF_HFTUSD (crowded 2d, worst 106%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
