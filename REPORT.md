# Pond Scanner Report
**Scan time:** 2026-08-02 13:56 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_KAITOUSD | +148.9% | $1,161,024 |
| 🟢 | PF_UNIUSD | +115.6% | $700,100 |
| 🟢 | PF_AGLDUSD | -32.8% | $1,207,541 |
| ⚪ | PF_SNXUSD | -28.4% | $877,664 |
| ⚪ | PF_SYNUSD | -27.6% | $2,908,813 |
| ⚪ | PF_SUIUSD | +24.1% | $3,227,394 |
| ⚪ | PF_COTIUSD | -19.5% | $17,348,552 |
| ⚪ | PF_NEARUSD | -17.0% | $1,330,512 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $63,044.88, kraken: $63,047.10, gemini: $63,052.73
- ⚪ **ETH** gap **0.029%** (coinbase → gemini) — coinbase: $1,853.81, kraken: $1,853.81, gemini: $1,854.35

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.05, realized vol 10d 28% vs 60d 33%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.12, realized vol 10d 39% vs 60d 53%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDe** $0.9995 (-0.05% vs peg)
- ⚪ **USDC** $0.9995 (-0.05% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 32% (0.7x)
- ⚪ **ETH** 24h vol 43% vs 30d norm 43% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_AGLDUSD | 2 | -32.8% | 526.7% |
| PF_KAITOUSD | 1 | +148.9% | 148.9% |
| PF_UNIUSD | 1 | +115.6% | 115.6% |

**Resolved since last scan:** PF_LPTUSD (crowded 1d, worst 209%), PF_SYNUSD (crowded 1d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
