# Pond Scanner Report
**Scan time:** 2026-09-21 12:50 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +457.9% | $9,308,023 |
| 🟢 | PF_HFTUSD | +104.6% | $1,195,638 |
| 🟢 | PF_ONDOUSD | +93.3% | $10,927,384 |
| 🟢 | PF_UNIUSD | +71.8% | $848,410 |
| 🟢 | PF_GRIFFAINUSD | +66.5% | $1,878,973 |
| 🟢 | PF_JTOUSD | -61.1% | $504,380 |
| 🟢 | PF_TRUMPUSD | +52.0% | $880,428 |
| 🟢 | PF_APTUSD | -49.0% | $793,319 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (gemini → coinbase) — coinbase: $85,271.89, kraken: $85,269.90, gemini: $85,255.42
- ⚪ **ETH** gap **0.018%** (kraken → gemini) — coinbase: $2,727.98, kraken: $2,727.77, gemini: $2,728.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Succinct (PROVE) | #472 | $50.8M | 3.88x | +17.9% |
| PHALA (PHA) | #473 | $50.9M | 2.28x | +70.1% |
| ZetaChain (ZETA) | #282 | $103.6M | 1.31x | +68.0% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.31, realized vol 10d 49% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.32, realized vol 10d 54% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 55% vs 30d norm 36% (1.5x)
- ⚪ **ETH** 24h vol 58% vs 30d norm 48% (1.2x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 5 | +71.8% | 624.1% |
| PF_NEARUSD | 2 | +457.9% | 457.9% |
| PF_SUIUSD | 2 | +39.5% | 50.4% |
| PF_HFTUSD | 1 | +104.6% | 104.6% |
| PF_ONDOUSD | 1 | +93.3% | 93.3% |
| PF_GRIFFAINUSD | 1 | +66.5% | 66.5% |
| PF_JTOUSD | 1 | -61.1% | 61.1% |
| PF_TRUMPUSD | 1 | +52.0% | 52.0% |
| PF_APTUSD | 1 | -49.0% | 49.0% |
| PF_ASTERUSD | 1 | -35.9% | 35.9% |
| PF_MINAUSD | 1 | +35.8% | 35.8% |
| PF_FILUSD | 1 | +35.3% | 35.3% |
| PF_AVAXUSD | 1 | +35.3% | 35.3% |
| PF_XRPUSD | 1 | +34.6% | 34.6% |

**Resolved since last scan:** PF_LINKUSD (crowded 2d, worst 223%), PF_RENDERUSD (crowded 1d, worst 127%), PF_LDOUSD (crowded 1d, worst 39%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
