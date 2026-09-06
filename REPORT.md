# Pond Scanner Report
**Scan time:** 2026-09-06 10:58 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -133.5% | $555,102 |
| 🟢 | PF_NEARUSD | +124.4% | $1,616,892 |
| 🟢 | PF_UNIUSD | -121.9% | $1,448,638 |
| 🟢 | PF_TRUMPUSD | +101.4% | $2,062,332 |
| 🟢 | PF_DOTUSD | +90.7% | $2,566,197 |
| 🟢 | PF_JUPUSD | +49.5% | $1,424,361 |
| 🟢 | PF_JTOUSD | +47.7% | $919,391 |
| 🟢 | PF_ICXUSD | -42.5% | $2,318,765 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.008%** (coinbase → gemini) — coinbase: $80,021.66, kraken: $80,024.40, gemini: $80,028.23
- ⚪ **ETH** gap **0.006%** (kraken → gemini) — coinbase: $2,501.96, kraken: $2,501.91, gemini: $2,502.05

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Sushi (SUSHI) | #365 | $69.6M | 1.71x | +19.4% |
| COTI (COTI) | #421 | $56.1M | 1.03x | +26.7% |
| STONK (STONK) | #250 | $115.8M | 0.88x | +332.0% |
| 哈基米 (Hajimi) (哈基米) | #348 | $72.9M | 0.72x | +310.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.51, realized vol 10d 40% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 43% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 14% vs 30d norm 40% (0.4x)
- ⚪ **ETH** 24h vol 25% vs 30d norm 54% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 3 | +101.4% | 375.1% |
| PF_NEARUSD | 2 | +124.4% | 163.9% |
| PF_UNIUSD | 2 | -121.9% | 387.6% |
| PF_ACEUSD | 1 | -133.5% | 133.5% |
| PF_DOTUSD | 1 | +90.7% | 90.7% |
| PF_JUPUSD | 1 | +49.5% | 64.8% |
| PF_JTOUSD | 1 | +47.7% | 47.7% |
| PF_ICXUSD | 1 | -42.5% | 63.5% |
| PF_ASTERUSD | 1 | +31.4% | 31.4% |

**Resolved since last scan:** PF_BELUSD (crowded 1d, worst 533%), PF_MINAUSD (crowded 1d, worst 335%), PF_HFTUSD (crowded 3d, worst 114%), PF_BLURUSD (crowded 1d, worst 74%), PF_VIRTUALUSD (crowded 1d, worst 52%), PF_IOTAUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
