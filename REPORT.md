# Pond Scanner Report
**Scan time:** 2026-09-02 16:35 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYRUPUSD | +186.3% | $607,773 |
| 🟢 | PF_UNIUSD | +146.1% | $1,895,764 |
| 🟢 | PF_TRUMPUSD | -117.5% | $1,205,650 |
| 🟢 | PF_ASTERUSD | -81.9% | $512,098 |
| 🟢 | PF_ACEUSD | -63.3% | $3,784,174 |
| 🟢 | PF_MUBARAKUSD | -41.2% | $6,166,715 |
| 🟢 | PF_XRPUSD | +36.9% | $39,450,906 |
| ⚪ | PF_NEARUSD | -24.7% | $1,143,328 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (gemini → coinbase) — coinbase: $77,415.22, kraken: $77,411.70, gemini: $77,410.09
- ⚪ **ETH** gap **0.024%** (gemini → coinbase) — coinbase: $2,397.72, kraken: $2,397.36, gemini: $2,397.14

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Threshold Network (T) | #397 | $58.1M | 2.48x | +43.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.52, realized vol 10d 26% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 33% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9985 (-0.15% vs peg)
- ⚪ **USDe** $0.9993 (-0.07% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 29% vs 30d norm 38% (0.8x)
- ⚪ **ETH** 24h vol 39% vs 30d norm 52% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +146.1% | 280.5% |
| PF_ACEUSD | 2 | -63.3% | 304.8% |
| PF_SYRUPUSD | 1 | +186.3% | 186.3% |
| PF_TRUMPUSD | 1 | -117.5% | 117.5% |
| PF_ASTERUSD | 1 | -81.9% | 81.9% |
| PF_MUBARAKUSD | 1 | -41.2% | 41.2% |
| PF_XRPUSD | 1 | +36.9% | 36.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 638%), PF_RENDERUSD (crowded 2d, worst 175%), PF_SAGAUSD (crowded 1d, worst 64%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
