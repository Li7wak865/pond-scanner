# Pond Scanner Report
**Scan time:** 2026-07-27 15:14 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -248.3% | $544,013 |
| 🟢 | PF_TRUMPUSD | +66.7% | $531,034 |
| 🟢 | PF_SYNUSD | -40.9% | $3,097,000 |
| 🟢 | PF_NEARUSD | -30.9% | $782,671 |
| ⚪ | PF_ETHFIUSD | -22.2% | $602,444 |
| ⚪ | PF_XRPUSD | -21.4% | $13,546,554 |
| ⚪ | PF_LDOUSD | +18.0% | $1,562,745 |
| ⚪ | PF_JUPUSD | -17.9% | $623,562 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (coinbase → gemini) — coinbase: $64,653.81, kraken: $64,661.40, gemini: $64,662.23
- ⚪ **ETH** gap **0.146%** (gemini → coinbase) — coinbase: $1,931.89, kraken: $1,931.53, gemini: $1,929.08

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #465 | $48.8M | 1.57x | -27.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 24% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.25, realized vol 10d 35% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **PYUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 33% (0.9x)
- ⚪ **ETH** 24h vol 46% vs 30d norm 45% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -248.3% | 248.3% |
| PF_TRUMPUSD | 1 | +66.7% | 66.7% |
| PF_SYNUSD | 1 | -40.9% | 40.9% |
| PF_NEARUSD | 1 | -30.9% | 30.9% |

**Resolved since last scan:** PF_UNIUSD (crowded 1d, worst 51%), PF_LRCUSD (crowded 1d, worst 50%), PF_ETHFIUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
