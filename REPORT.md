# Pond Scanner Report
**Scan time:** 2026-10-22 11:54 UTC

**Flags this scan:** 5 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | +85.7% | $797,907 |
| 🟢 | PF_IMXUSD | -41.3% | $727,180 |
| 🟢 | PF_DOTUSD | -30.6% | $1,444,468 |
| ⚪ | PF_APTUSD | +26.8% | $980,506 |
| ⚪ | PF_SUIUSD | -19.1% | $4,339,638 |
| ⚪ | PF_NEARUSD | +18.5% | $4,178,515 |
| ⚪ | PF_ATOMUSD | +14.0% | $592,433 |
| ⚪ | PF_LDOUSD | -13.3% | $1,782,425 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- 🟢 **BTC** gap **0.903%** (coinbase → gemini) — coinbase: $81,690.08, kraken: $81,690.90, gemini: $82,427.78
- 🟢 **ETH** gap **0.316%** (coinbase → gemini) — coinbase: $2,397.42, kraken: $2,397.65, gemini: $2,405.00

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 26% vs 60d 35%
- 🟡 **ETH: MIXED** — efficiency ratio 0.34, realized vol 10d 33% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 35% vs 30d norm 32% (1.1x)
- ⚪ **ETH** 24h vol 40% vs 30d norm 42% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | +85.7% | 85.7% |
| PF_IMXUSD | 1 | -41.3% | 53.1% |
| PF_DOTUSD | 1 | -30.6% | 30.6% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 3d, worst 95%), PF_NEARUSD (crowded 2d, worst 117%), PF_FILUSD (crowded 1d, worst 78%), PF_UNIUSD (crowded 1d, worst 65%), PF_TIAUSD (crowded 1d, worst 59%), PF_BATUSD (crowded 2d, worst 49%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
