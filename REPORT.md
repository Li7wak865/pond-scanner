# Pond Scanner Report
**Scan time:** 2026-11-26 08:20 UTC

**Flags this scan:** 8 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -218.3% | $4,378,686 |
| 🟢 | PF_SOLUSD | +91.5% | $746,763 |
| 🟢 | PF_ATOMUSD | +48.0% | $566,896 |
| 🟢 | PF_RUNEUSD | -46.7% | $613,898 |
| 🟢 | PF_UNIUSD | +33.9% | $973,523 |
| 🟢 | PF_TRUMPUSD | +31.5% | $1,025,551 |
| ⚪ | PF_XRPUSD | +19.7% | $12,078,616 |
| ⚪ | PF_NEARUSD | -18.9% | $2,878,388 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.002%** (kraken → gemini) — coinbase: $60,598.59, kraken: $60,598.30, gemini: $60,599.36
- ⚪ **ETH** gap **0.021%** (gemini → kraken) — coinbase: $1,688.18, kraken: $1,688.29, gemini: $1,687.94

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SSV Network (SSV) | #485 | $36.3M | 1.00x | +50.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.59, realized vol 10d 42% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.58, realized vol 10d 57% vs 60d 51%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9950 (-0.50% vs peg)
- ⚪ **USDT** $0.9991 (-0.09% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 49% vs 30d norm 56% (0.9x)
- ⚪ **ETH** 24h vol 54% vs 30d norm 69% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 2 | -218.3% | 218.3% |
| PF_UNIUSD | 2 | +33.9% | 112.3% |
| PF_SOLUSD | 1 | +91.5% | 91.5% |
| PF_ATOMUSD | 1 | +48.0% | 48.0% |
| PF_RUNEUSD | 1 | -46.7% | 46.7% |
| PF_TRUMPUSD | 1 | +31.5% | 31.5% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 184%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
