# Pond Scanner Report
**Scan time:** 2026-08-07 03:19 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SOLUSD | +638.8% | $531,712 |
| 🟢 | PF_ACEUSD | -322.0% | $16,425,281 |
| 🟢 | PF_KAITOUSD | -68.2% | $633,902 |
| 🟢 | PF_SYNUSD | -49.3% | $2,398,124 |
| 🟢 | PF_SUIUSD | -31.7% | $3,567,915 |
| 🟢 | PF_UNIUSD | -31.4% | $1,424,586 |
| 🟢 | PF_MOODENGUSD | +31.1% | $1,122,914 |
| ⚪ | PF_HFTUSD | -14.7% | $156,110,831 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.004%** (gemini → kraken) — coinbase: $64,263.49, kraken: $64,264.10, gemini: $64,261.69
- ⚪ **ETH** gap **0.039%** (kraken → gemini) — coinbase: $1,899.06, kraken: $1,898.88, gemini: $1,899.63

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SkyAI (SKYAI) | #258 | $97.7M | 0.69x | +39.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 27% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9996 (-0.04% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 19% vs 30d norm 29% (0.7x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 41% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 2 | -49.3% | 53.5% |
| PF_UNIUSD | 2 | -31.4% | 144.4% |
| PF_SOLUSD | 1 | +638.8% | 638.8% |
| PF_ACEUSD | 1 | -322.0% | 358.2% |
| PF_KAITOUSD | 1 | -68.2% | 124.5% |
| PF_SUIUSD | 1 | -31.7% | 31.7% |
| PF_MOODENGUSD | 1 | +31.1% | 31.1% |

**Resolved since last scan:** PF_BICOUSD (crowded 1d, worst 51%), PF_GRIFFAINUSD (crowded 1d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
