# Pond Scanner Report
**Scan time:** 2026-09-22 16:58 UTC

**Flags this scan:** 20 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | -322.8% | $9,481,986 |
| 🟢 | PF_LSKUSD | -290.1% | $1,343,040 |
| 🟢 | PF_TRUMPUSD | +207.1% | $1,543,940 |
| 🟢 | PF_RENDERUSD | +139.0% | $695,398 |
| 🟢 | PF_HFTUSD | -108.7% | $560,388 |
| 🟢 | PF_MINAUSD | -99.3% | $504,188 |
| 🟢 | PF_BLURUSD | +87.3% | $578,780 |
| 🟢 | PF_AVAXUSD | +74.7% | $884,789 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.051%** (coinbase → gemini) — coinbase: $86,464.87, kraken: $86,502.60, gemini: $86,509.27
- ⚪ **ETH** gap **0.043%** (coinbase → kraken) — coinbase: $2,746.19, kraken: $2,747.36, gemini: $2,746.48

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Mubarak (MUBARAK) | #338 | $81.6M | 2.57x | +82.6% |
| Aurora (AURORA) | #389 | $68.6M | 0.65x | +107.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.35, realized vol 10d 55% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.35, realized vol 10d 59% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 34% vs 30d norm 36% (0.9x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 48% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 6 | +64.8% | 624.1% |
| PF_NEARUSD | 3 | -322.8% | 457.9% |
| PF_TRUMPUSD | 2 | +207.1% | 207.1% |
| PF_RENDERUSD | 2 | +139.0% | 209.9% |
| PF_LINKUSD | 2 | -60.2% | 725.7% |
| PF_LSKUSD | 1 | -290.1% | 290.1% |
| PF_HFTUSD | 1 | -108.7% | 109.4% |
| PF_MINAUSD | 1 | -99.3% | 99.3% |
| PF_BLURUSD | 1 | +87.3% | 87.3% |
| PF_AVAXUSD | 1 | +74.7% | 135.6% |
| PF_SPXUSD | 1 | +54.5% | 68.9% |
| PF_XRPUSD | 1 | +50.1% | 50.1% |
| PF_APTUSD | 1 | -48.9% | 48.9% |
| PF_VIRTUALUSD | 1 | -45.3% | 45.3% |
| PF_JTOUSD | 1 | -44.8% | 65.0% |
| PF_RUNEUSD | 1 | +43.6% | 43.6% |
| PF_FILUSD | 1 | -37.5% | 37.5% |
| PF_ETHFIUSD | 1 | +36.6% | 36.6% |

**Resolved since last scan:** PF_DOTUSD (crowded 1d, worst 47%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
