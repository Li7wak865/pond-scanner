# Pond Scanner Report
**Scan time:** 2026-10-28 22:36 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SPXUSD | +73.7% | $509,500 |
| 🟢 | PF_NEARUSD | +60.2% | $3,142,543 |
| 🟢 | PF_TRUMPUSD | +49.4% | $642,747 |
| 🟢 | PF_WLDUSD | +37.7% | $12,218,267 |
| 🟢 | PF_XRPUSD | +31.5% | $7,880,094 |
| ⚪ | PF_PONSUSD | -27.2% | $6,412,840 |
| ⚪ | PF_BICOUSD | +22.1% | $1,040,229 |
| ⚪ | PF_TIAUSD | +21.5% | $811,967 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.009%** (coinbase → kraken) — coinbase: $81,259.33, kraken: $81,266.30, gemini: $81,263.15
- ⚪ **ETH** gap **0.046%** (coinbase → gemini) — coinbase: $2,359.45, kraken: $2,360.13, gemini: $2,360.53

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Cap (CAP) | #258 | $115.4M | 0.57x | -23.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.03, realized vol 10d 24% vs 60d 34%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.19, realized vol 10d 27% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDe** $0.9994 (-0.06% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 26% vs 30d norm 31% (0.8x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_SPXUSD | 1 | +73.7% | 73.7% |
| PF_NEARUSD | 1 | +60.2% | 141.8% |
| PF_TRUMPUSD | 1 | +49.4% | 49.4% |
| PF_WLDUSD | 1 | +37.7% | 37.7% |
| PF_XRPUSD | 1 | +31.5% | 31.5% |

**Resolved since last scan:** PF_GRASSUSD (crowded 1d, worst 78%), PF_APTUSD (crowded 1d, worst 53%), PF_ARCUSD (crowded 1d, worst 43%), PF_SUIUSD (crowded 1d, worst 34%), PF_SYNUSD (crowded 1d, worst 30%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
