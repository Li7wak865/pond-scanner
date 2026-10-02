# Pond Scanner Report
**Scan time:** 2026-10-02 22:15 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +533.7% | $916,128 |
| 🟢 | PF_MOVRUSD | -197.6% | $1,495,886 |
| 🟢 | PF_NEARUSD | +126.4% | $3,241,442 |
| 🟢 | PF_LINKUSD | +115.4% | $779,809 |
| 🟢 | PF_SANDUSD | -78.8% | $23,517,302 |
| 🟢 | PF_ZROUSD | +65.3% | $643,406 |
| 🟢 | PF_JUPUSD | -43.1% | $4,325,223 |
| 🟢 | PF_ETHFIUSD | -36.2% | $909,554 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (kraken → gemini) — coinbase: $84,530.24, kraken: $84,525.80, gemini: $84,536.00
- ⚪ **ETH** gap **0.004%** (coinbase → kraken) — coinbase: $2,661.95, kraken: $2,662.05, gemini: $2,661.95

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟡 **BTC: MIXED** — efficiency ratio 0.34, realized vol 10d 17% vs 60d 42%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.17, realized vol 10d 18% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 43% vs 30d norm 35% (1.2x)
- ⚪ **ETH** 24h vol 42% vs 30d norm 46% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +533.7% | 543.2% |
| PF_MOVRUSD | 2 | -197.6% | 289.0% |
| PF_LINKUSD | 2 | +115.4% | 282.1% |
| PF_NEARUSD | 1 | +126.4% | 134.3% |
| PF_SANDUSD | 1 | -78.8% | 148.5% |
| PF_ZROUSD | 1 | +65.3% | 65.3% |
| PF_JUPUSD | 1 | -43.1% | 47.9% |
| PF_ETHFIUSD | 1 | -36.2% | 36.2% |
| PF_TRUMPUSD | 1 | -35.2% | 150.9% |
| PF_DOTUSD | 1 | -31.9% | 31.9% |

**Resolved since last scan:** PF_MANAUSD (crowded 1d, worst 86%), PF_TIAUSD (crowded 1d, worst 68%), PF_ASTERUSD (crowded 1d, worst 57%), PF_SYNUSD (crowded 1d, worst 47%), PF_XRPUSD (crowded 1d, worst 88%), PF_VIRTUALUSD (crowded 1d, worst 51%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
