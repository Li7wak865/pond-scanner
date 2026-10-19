# Pond Scanner Report
**Scan time:** 2026-10-19 04:42 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SANDUSD | -98.9% | $30,825,838 |
| 🟢 | PF_TIAUSD | +64.3% | $2,942,468 |
| 🟢 | PF_APTUSD | -44.0% | $520,731 |
| ⚪ | PF_NEARUSD | +22.3% | $5,095,167 |
| ⚪ | PF_XRPUSD | +22.1% | $9,445,946 |
| ⚪ | PF_DOTUSD | +20.7% | $1,587,545 |
| ⚪ | PF_PONSUSD | +17.3% | $1,513,597 |
| ⚪ | PF_CRVUSD | +15.6% | $3,704,902 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (gemini → coinbase) — coinbase: $82,616.14, kraken: $82,607.20, gemini: $82,605.50
- ⚪ **ETH** gap **0.105%** (gemini → kraken) — coinbase: $2,424.16, kraken: $2,424.33, gemini: $2,421.79

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.06, realized vol 10d 23% vs 60d 39%
- 🟡 **ETH: MIXED** — efficiency ratio 0.34, realized vol 10d 34% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9979 (-0.21% vs peg)
- ⚪ **USDT** $0.9994 (-0.06% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 42% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TIAUSD | 2 | +64.3% | 64.3% |
| PF_SANDUSD | 1 | -98.9% | 98.9% |
| PF_APTUSD | 1 | -44.0% | 44.0% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 103%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
