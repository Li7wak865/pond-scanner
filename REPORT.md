# Pond Scanner Report
**Scan time:** 2026-07-25 14:02 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ALCHUSD | -132.3% | $1,177,010 |
| 🟢 | PF_SYNUSD | +67.3% | $1,620,220 |
| 🟢 | PF_ACEUSD | -50.7% | $3,103,642 |
| ⚪ | PF_SUIUSD | -28.9% | $6,164,307 |
| ⚪ | PF_GRASSUSD | +25.9% | $562,140 |
| ⚪ | PF_STXUSD | -20.6% | $876,214 |
| ⚪ | PF_UNIUSD | -19.8% | $511,691 |
| ⚪ | PF_SUSHIUSD | -14.8% | $511,403 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (kraken → gemini) — coinbase: $64,065.99, kraken: $64,060.60, gemini: $64,072.47
- ⚪ **ETH** gap **0.025%** (coinbase → gemini) — coinbase: $1,864.00, kraken: $1,864.40, gemini: $1,864.46

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #503 | $45.8M | 1.45x | +70.4% |
| Akedo (AKE) | #319 | $73.0M | 1.30x | +20.8% |
| Allora (ALLO) | #288 | $85.0M | 0.66x | -26.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 22% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 30% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9971 (-0.29% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 13% vs 30d norm 36% (0.4x)
- ⚪ **ETH** 24h vol 16% vs 30d norm 47% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 2 | +67.3% | 76.6% |
| PF_ACEUSD | 2 | -50.7% | 192.2% |
| PF_ALCHUSD | 1 | -132.3% | 132.3% |

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 145%), PF_MUBARAKUSD (crowded 1d, worst 46%), PF_SUIUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
