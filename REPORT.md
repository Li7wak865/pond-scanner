# Pond Scanner Report
**Scan time:** 2026-10-31 12:33 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +515.8% | $886,806 |
| 🟢 | PF_ATOMUSD | -139.2% | $1,320,466 |
| 🟢 | PF_LINKUSD | +107.2% | $571,634 |
| 🟢 | PF_NEARUSD | +52.3% | $3,085,848 |
| 🟢 | PF_TRXUSD | -47.0% | $15,279,468 |
| 🟢 | PF_TRUMPUSD | -38.7% | $756,758 |
| 🟢 | PF_STXUSD | +38.7% | $829,851 |
| 🟢 | PF_SUIUSD | -33.9% | $3,598,991 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → gemini) — coinbase: $77,445.51, kraken: $77,450.10, gemini: $77,461.93
- ⚪ **ETH** gap **0.024%** (coinbase → gemini) — coinbase: $2,246.13, kraken: $2,246.26, gemini: $2,246.67

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #375 | $62.9M | 2.02x | +38.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.33, realized vol 10d 31% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 33% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDe** $0.9984 (-0.16% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 45% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +515.8% | 515.8% |
| PF_ATOMUSD | 2 | -139.2% | 550.1% |
| PF_LINKUSD | 2 | +107.2% | 235.0% |
| PF_NEARUSD | 1 | +52.3% | 52.3% |
| PF_TRXUSD | 1 | -47.0% | 47.0% |
| PF_TRUMPUSD | 1 | -38.7% | 38.7% |
| PF_STXUSD | 1 | +38.7% | 38.7% |
| PF_SUIUSD | 1 | -33.9% | 33.9% |
| PF_TIAUSD | 1 | -33.1% | 33.1% |
| PF_SUSHIUSD | 1 | -30.1% | 30.1% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 2d, worst 73%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
