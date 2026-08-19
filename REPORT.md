# Pond Scanner Report
**Scan time:** 2026-08-19 07:05 UTC

**Flags this scan:** 4 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -166.4% | $17,992,950 |
| ⚪ | PF_FILUSD | -28.3% | $521,019 |
| ⚪ | PF_NEARUSD | -26.9% | $1,763,631 |
| ⚪ | PF_ALICEUSD | -25.2% | $3,629,234 |
| ⚪ | PF_KAITOUSD | -23.0% | $851,579 |
| ⚪ | PF_VIRTUALUSD | +22.9% | $791,904 |
| ⚪ | PF_CATIUSD | -20.6% | $587,731 |
| ⚪ | PF_ETHFIUSD | -20.5% | $770,804 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (kraken → coinbase) — coinbase: $64,242.79, kraken: $64,235.10, gemini: $64,236.25
- ⚪ **ETH** gap **0.043%** (kraken → gemini) — coinbase: $1,914.73, kraken: $1,914.44, gemini: $1,915.26

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| DAPPOS (DOS) | #397 | $52.6M | 0.91x | +17.9% |
| GoPlus Security (GPS) | #304 | $72.1M | 0.85x | -27.7% |
| RedStone (RED) | #455 | $42.8M | 0.55x | -16.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 20% vs 60d 28%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.01, realized vol 10d 18% vs 60d 39%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 21% vs 30d norm 25% (0.8x)
- ⚪ **ETH** 24h vol 22% vs 30d norm 34% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -166.4% | 732.3% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 73%), PF_RAREUSD (crowded 2d, worst 53%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
