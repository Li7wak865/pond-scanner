# Pond Scanner Report
**Scan time:** 2026-07-25 19:35 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | +82.3% | $2,673,482 |
| 🟢 | PF_EIGENUSD | -50.7% | $536,295 |
| 🟢 | PF_ACEUSD | -35.9% | $2,215,376 |
| 🟢 | PF_ONDOUSD | -31.6% | $4,851,353 |
| ⚪ | PF_SUIUSD | -17.4% | $4,559,453 |
| ⚪ | PF_NEARUSD | -13.3% | $744,850 |
| ⚪ | PF_LDOUSD | -10.7% | $727,463 |
| ⚪ | PF_WIFUSD | -9.6% | $2,519,320 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.014%** (coinbase → gemini) — coinbase: $64,348.47, kraken: $64,355.50, gemini: $64,357.40
- ⚪ **ETH** gap **0.044%** (kraken → gemini) — coinbase: $1,874.20, kraken: $1,873.48, gemini: $1,874.30

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Euler (EUL) | #505 | $45.5M | 1.96x | +60.6% |
| Allora (ALLO) | #283 | $88.1M | 1.14x | -30.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 22% vs 60d 38%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.15, realized vol 10d 30% vs 60d 55%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **USDe** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 11% vs 30d norm 36% (0.3x)
- ⚪ **ETH** 24h vol 13% vs 30d norm 47% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SYNUSD | 2 | +82.3% | 82.3% |
| PF_ACEUSD | 2 | -35.9% | 192.2% |
| PF_EIGENUSD | 1 | -50.7% | 50.7% |
| PF_ONDOUSD | 1 | -31.6% | 31.6% |

**Resolved since last scan:** PF_ALCHUSD (crowded 1d, worst 132%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
