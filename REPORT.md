# Pond Scanner Report
**Scan time:** 2026-09-16 11:36 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -349.1% | $2,717,750 |
| 🟢 | PF_UNIUSD | +209.3% | $1,271,670 |
| 🟢 | PF_NEARUSD | -78.6% | $1,960,931 |
| 🟢 | PF_TRUMPUSD | -73.1% | $1,250,586 |
| 🟢 | PF_STEEMUSD | -64.5% | $543,582 |
| 🟢 | PF_ACEUSD | -56.0% | $2,442,855 |
| 🟢 | PF_SYNUSD | -51.2% | $6,159,520 |
| 🟢 | PF_ICXUSD | +45.7% | $4,919,620 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.018%** (coinbase → gemini) — coinbase: $75,976.76, kraken: $75,987.50, gemini: $75,990.21
- ⚪ **ETH** gap **0.028%** (coinbase → kraken) — coinbase: $2,410.72, kraken: $2,411.40, gemini: $2,411.37

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.20, realized vol 10d 28% vs 60d 39%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 39% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDe** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **PYUSD** $0.9995 (-0.05% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 43% vs 30d norm 42% (1.0x)
- ⚪ **ETH** 24h vol 59% vs 30d norm 60% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LSKUSD | 3 | -349.1% | 896.9% |
| PF_ACEUSD | 2 | -56.0% | 175.3% |
| PF_UNIUSD | 1 | +209.3% | 212.9% |
| PF_NEARUSD | 1 | -78.6% | 78.6% |
| PF_TRUMPUSD | 1 | -73.1% | 73.1% |
| PF_STEEMUSD | 1 | -64.5% | 205.3% |
| PF_SYNUSD | 1 | -51.2% | 51.2% |
| PF_ICXUSD | 1 | +45.7% | 45.7% |
| PF_RAREUSD | 1 | -37.9% | 37.9% |
| PF_APTUSD | 1 | -34.5% | 34.5% |

**Resolved since last scan:** PF_VIRTUALUSD (crowded 1d, worst 42%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
