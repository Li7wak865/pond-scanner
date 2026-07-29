# Pond Scanner Report
**Scan time:** 2026-07-29 14:32 UTC

**Flags this scan:** 9 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +877.7% | $595,436 |
| 🟢 | PF_DEXEUSD | -601.9% | $935,846 |
| 🟢 | PF_KAITOUSD | -306.5% | $672,421 |
| 🟢 | PF_UNIUSD | -150.7% | $708,619 |
| 🟢 | PF_SYNUSD | +61.3% | $1,269,210 |
| ⚪ | PF_FILUSD | -27.6% | $569,612 |
| ⚪ | PF_NEARUSD | +24.6% | $1,605,097 |
| ⚪ | PF_SPXUSD | +21.6% | $619,422 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.024%** (kraken → coinbase) — coinbase: $64,161.80, kraken: $64,146.60, gemini: $64,155.65
- ⚪ **ETH** gap **0.064%** (gemini → coinbase) — coinbase: $1,898.11, kraken: $1,897.21, gemini: $1,896.90

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| COTI (COTI) | #439 | $46.2M | 2.93x | +32.8% |
| Lorenzo Protocol (BANK) | #322 | $70.8M | 2.67x | -52.0% |
| Orochi Network (ON) | #455 | $44.0M | 1.36x | +27.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 26% vs 60d 38%
- 🟡 **ETH: MIXED** — efficiency ratio 0.22, realized vol 10d 41% vs 60d 56%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9967 (-0.33% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 34% (1.0x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 46% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 3 | +61.3% | 79.8% |
| PF_DEXEUSD | 2 | -601.9% | 755.4% |
| PF_SOLUSD | 1 | +877.7% | 877.7% |
| PF_KAITOUSD | 1 | -306.5% | 306.5% |
| PF_UNIUSD | 1 | -150.7% | 150.7% |

**Resolved since last scan:** PF_NEARUSD (crowded 1d, worst 56%), PF_SAGAUSD (crowded 1d, worst 54%), PF_RUNEUSD (crowded 1d, worst 45%), PF_COTIUSD (crowded 1d, worst 36%), PF_FILUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
