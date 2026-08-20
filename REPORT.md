# Pond Scanner Report
**Scan time:** 2026-08-20 13:11 UTC

**Flags this scan:** 26 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZEREBROUSD | +192.2% | $704,813 |
| 🟢 | PF_ETHFIUSD | -154.6% | $1,377,780 |
| 🟢 | PF_AVAXUSD | +113.3% | $886,578 |
| 🟢 | PF_MOODENGUSD | +79.1% | $1,800,443 |
| 🟢 | PF_ACEUSD | -66.6% | $14,906,823 |
| 🟢 | PF_TRUMPUSD | +65.3% | $2,622,720 |
| 🟢 | PF_IOTAUSD | +63.5% | $1,523,723 |
| 🟢 | PF_VIRTUALUSD | -55.4% | $1,871,360 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (gemini → coinbase) — coinbase: $71,928.94, kraken: $71,916.00, gemini: $71,908.41
- ⚪ **ETH** gap **0.024%** (kraken → coinbase) — coinbase: $2,288.67, kraken: $2,288.11, gemini: $2,288.38

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RE (RE) | #282 | $84.7M | 2.02x | +24.9% |
| BOOK OF MEME (BOME) | #281 | $85.2M | 1.97x | +65.3% |
| Bio Protocol (BIO) | #349 | $65.5M | 1.08x | +19.4% |
| Perle (PRL) | #433 | $49.7M | 0.82x | -25.2% |
| 牛来 (Niu Lai) (牛来) | #368 | $61.8M | 0.71x | +57.5% |
| Audiera (BEAT) | #473 | $44.5M | 0.69x | -32.0% |
| RedStone (RED) | #411 | $52.4M | 0.67x | +23.6% |
| Peanut the Squirrel (PNUT) | #416 | $51.3M | 0.59x | +26.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.64, realized vol 10d 46% vs 60d 34%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.67, realized vol 10d 99% vs 60d 57%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 94% vs 30d norm 30% (3.1x)
- 🟢 **ETH** 24h vol 162% vs 30d norm 46% (3.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZEREBROUSD | 1 | +192.2% | 192.2% |
| PF_ETHFIUSD | 1 | -154.6% | 154.6% |
| PF_AVAXUSD | 1 | +113.3% | 113.3% |
| PF_MOODENGUSD | 1 | +79.1% | 79.1% |
| PF_ACEUSD | 1 | -66.6% | 66.6% |
| PF_TRUMPUSD | 1 | +65.3% | 65.3% |
| PF_IOTAUSD | 1 | +63.5% | 63.5% |
| PF_VIRTUALUSD | 1 | -55.4% | 55.4% |
| PF_JUPUSD | 1 | +54.3% | 54.3% |
| PF_RAREUSD | 1 | +53.4% | 53.4% |
| PF_GRASSUSD | 1 | +52.8% | 52.8% |
| PF_UNIUSD | 1 | -40.5% | 40.5% |
| PF_DOTUSD | 1 | -39.5% | 39.5% |
| PF_SUIUSD | 1 | +37.6% | 37.6% |
| PF_WLDUSD | 1 | +32.4% | 32.4% |
| PF_HFTUSD | 1 | -32.1% | 32.1% |

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
