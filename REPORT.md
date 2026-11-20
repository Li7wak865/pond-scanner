# Pond Scanner Report
**Scan time:** 2026-11-20 20:22 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -206.8% | $530,192 |
| 🟢 | PF_SOLUSD | +111.6% | $743,846 |
| 🟢 | PF_ZROUSD | +103.5% | $951,956 |
| 🟢 | PF_UNIUSD | -73.8% | $554,655 |
| 🟢 | PF_SPXUSD | -53.5% | $891,186 |
| 🟢 | PF_TRUMPUSD | -40.8% | $1,842,309 |
| 🟢 | PF_NEARUSD | +37.4% | $4,898,238 |
| 🟢 | PF_RUNEUSD | -31.4% | $593,464 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.083%** (coinbase → gemini) — coinbase: $58,450.00, kraken: $58,469.20, gemini: $58,498.63
- ⚪ **ETH** gap **0.101%** (coinbase → gemini) — coinbase: $1,608.85, kraken: $1,609.43, gemini: $1,610.47

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Kinetiq (KNTQ) | #337 | $61.1M | 6.26x | -16.6% |
| Semicon Bull 3X ETF (bStocks Tokenized ETF) (SOXLB) | #321 | $65.6M | 2.01x | -30.6% |
| Lombard (BARD) | #433 | $41.4M | 1.19x | +21.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 48% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.54, realized vol 10d 69% vs 60d 50%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9948 (-0.52% vs peg)
- ⚪ **USDT** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9987 (-0.13% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 88% vs 30d norm 46% (1.9x)
- ⚪ **ETH** 24h vol 111% vs 30d norm 61% (1.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | -73.8% | 220.1% |
| PF_SOLUSD | 3 | +111.6% | 768.6% |
| PF_TRUMPUSD | 2 | -40.8% | 40.8% |
| PF_INJUSD | 1 | -206.8% | 206.8% |
| PF_ZROUSD | 1 | +103.5% | 103.5% |
| PF_SPXUSD | 1 | -53.5% | 53.5% |
| PF_NEARUSD | 1 | +37.4% | 37.4% |
| PF_RUNEUSD | 1 | -31.4% | 31.4% |
| PF_TRXUSD | 1 | -30.6% | 30.6% |

**Resolved since last scan:** PF_JUPUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
