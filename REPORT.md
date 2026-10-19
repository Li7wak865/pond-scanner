# Pond Scanner Report
**Scan time:** 2026-10-19 13:19 UTC

**Flags this scan:** 2 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -119.1% | $5,558,266 |
| ⚪ | PF_SANDUSD | -23.1% | $20,277,845 |
| ⚪ | PF_BATUSD | -19.4% | $1,232,119 |
| ⚪ | PF_ACEUSD | -18.7% | $2,857,327 |
| ⚪ | PF_TIAUSD | +18.3% | $2,800,044 |
| ⚪ | PF_SYNUSD | -18.2% | $549,818 |
| ⚪ | PF_SPXUSD | +17.7% | $760,265 |
| ⚪ | PF_CRVUSD | +14.9% | $3,535,544 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.025%** (coinbase → gemini) — coinbase: $82,475.41, kraken: $82,485.40, gemini: $82,495.82
- ⚪ **ETH** gap **0.041%** (coinbase → gemini) — coinbase: $2,420.29, kraken: $2,420.33, gemini: $2,421.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Amp (AMP) | #322 | $79.0M | 0.73x | +18.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 23% vs 60d 39%
- 🟡 **ETH: MIXED** — efficiency ratio 0.35, realized vol 10d 33% vs 60d 45%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9978 (-0.22% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 45% vs 30d norm 42% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 1 | -119.1% | 119.1% |

**Resolved since last scan:** PF_SANDUSD (crowded 1d, worst 99%), PF_TIAUSD (crowded 2d, worst 64%), PF_APTUSD (crowded 1d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
