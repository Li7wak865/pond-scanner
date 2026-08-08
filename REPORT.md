# Pond Scanner Report
**Scan time:** 2026-08-08 13:12 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | -607.9% | $917,131 |
| 🟢 | PF_ACEUSD | -91.4% | $8,276,514 |
| 🟢 | PF_DEEPUSD | +75.3% | $993,681 |
| 🟢 | PF_UNIUSD | +65.5% | $560,786 |
| 🟢 | PF_NEARUSD | +55.1% | $1,625,471 |
| 🟢 | PF_HFTUSD | -50.1% | $13,372,698 |
| 🟢 | PF_SYNUSD | -40.1% | $2,384,761 |
| 🟢 | PF_ZBTUSD | -39.4% | $1,027,640 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → gemini) — coinbase: $64,962.14, kraken: $64,967.10, gemini: $64,975.99
- ⚪ **ETH** gap **0.013%** (kraken → gemini) — coinbase: $1,918.77, kraken: $1,918.65, gemini: $1,918.90

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Momentum (MMT) | #443 | $46.1M | 5.71x | +38.8% |
| Biconomy (BICO) | #492 | $57.6M | 3.62x | +19.8% |
| SpaceX (bStocks Tokenized Stock) (SPCXB) | #278 | $87.6M | 1.65x | +15.7% |
| Tutorial (TUT) | #399 | $54.4M | 1.65x | +81.4% |
| RE (RE) | #306 | $75.6M | 0.52x | +24.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.02, realized vol 10d 23% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 28% vs 60d 42%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 10% vs 30d norm 29% (0.3x)
- ⚪ **ETH** 24h vol 18% vs 30d norm 41% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_KAITOUSD | 2 | -607.9% | 607.9% |
| PF_ACEUSD | 2 | -91.4% | 501.6% |
| PF_DEEPUSD | 1 | +75.3% | 75.3% |
| PF_UNIUSD | 1 | +65.5% | 65.5% |
| PF_NEARUSD | 1 | +55.1% | 55.1% |
| PF_HFTUSD | 1 | -50.1% | 210.3% |
| PF_SYNUSD | 1 | -40.1% | 40.1% |
| PF_ZBTUSD | 1 | -39.4% | 39.4% |
| PF_SNXUSD | 1 | -38.3% | 38.3% |
| PF_XRPUSD | 1 | +33.5% | 33.5% |
| PF_FILUSD | 1 | +31.7% | 32.6% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 930%), PF_GRASSUSD (crowded 2d, worst 67%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
