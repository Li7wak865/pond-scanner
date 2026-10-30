# Pond Scanner Report
**Scan time:** 2026-10-30 05:51 UTC

**Flags this scan:** 18 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_INJUSD | -683.7% | $608,968 |
| 🟢 | PF_UNIUSD | +486.9% | $1,590,294 |
| 🟢 | PF_ZROUSD | +393.1% | $689,484 |
| 🟢 | PF_LINKUSD | +174.3% | $795,234 |
| 🟢 | PF_NEARUSD | -104.0% | $8,301,939 |
| 🟢 | PF_ICPUSD | -91.6% | $703,292 |
| 🟢 | PF_SYNUSD | +74.7% | $1,150,110 |
| 🟢 | PF_ETHFIUSD | +73.2% | $553,604 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.028%** (coinbase → kraken) — coinbase: $78,475.10, kraken: $78,497.10, gemini: $78,490.16
- ⚪ **ETH** gap **0.177%** (coinbase → gemini) — coinbase: $2,241.89, kraken: $2,242.46, gemini: $2,245.85

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.23, realized vol 10d 34% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.38, realized vol 10d 34% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9963 (-0.37% vs peg)
- ⚪ **USDe** $0.9975 (-0.25% vs peg)
- ⚪ **USDT** $0.9986 (-0.14% vs peg)
- ⚪ **PYUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDC** $0.9993 (-0.07% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 72% vs 30d norm 34% (2.1x)
- ⚪ **ETH** 24h vol 87% vs 30d norm 46% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -104.0% | 141.8% |
| PF_INJUSD | 2 | -683.7% | 683.7% |
| PF_UNIUSD | 2 | +486.9% | 486.9% |
| PF_ICPUSD | 2 | -91.6% | 322.3% |
| PF_SUSHIUSD | 2 | +50.6% | 144.2% |
| PF_TRXUSD | 2 | +50.3% | 225.3% |
| PF_JTOUSD | 2 | +38.2% | 123.0% |
| PF_ZROUSD | 1 | +393.1% | 393.1% |
| PF_LINKUSD | 1 | +174.3% | 174.3% |
| PF_SYNUSD | 1 | +74.7% | 74.7% |
| PF_ETHFIUSD | 1 | +73.2% | 73.2% |
| PF_EIGENUSD | 1 | -64.7% | 64.7% |
| PF_GRASSUSD | 1 | +64.2% | 64.2% |
| PF_ASTERUSD | 1 | -50.1% | 50.1% |
| PF_FILUSD | 1 | -36.2% | 36.2% |
| PF_PONSUSD | 1 | +33.7% | 33.7% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 531%), PF_RENDERUSD (crowded 2d, worst 84%), PF_ATOMUSD (crowded 2d, worst 137%), PF_BATUSD (crowded 2d, worst 44%), PF_TIAUSD (crowded 2d, worst 72%), PF_SUIUSD (crowded 2d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
