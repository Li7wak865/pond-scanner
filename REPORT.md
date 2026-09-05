# Pond Scanner Report
**Scan time:** 2026-09-05 15:15 UTC

**Flags this scan:** 10 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_BELUSD | +527.4% | $637,647 |
| 🟢 | PF_TRUMPUSD | +256.4% | $1,170,664 |
| 🟢 | PF_UNIUSD | +241.0% | $575,555 |
| 🟢 | PF_COTIUSD | +122.1% | $2,338,607 |
| 🟢 | PF_HFTUSD | +113.8% | $10,049,020 |
| 🟢 | PF_ACEUSD | -97.2% | $762,349 |
| 🟢 | PF_ASTERUSD | +55.1% | $1,460,011 |
| 🟢 | PF_ICXUSD | -53.8% | $2,767,304 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.017%** (coinbase → gemini) — coinbase: $79,718.83, kraken: $79,730.10, gemini: $79,732.37
- ⚪ **ETH** gap **0.025%** (gemini → coinbase) — coinbase: $2,459.35, kraken: $2,459.33, gemini: $2,458.73

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.53, realized vol 10d 41% vs 60d 39%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.44, realized vol 10d 42% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $1.0000 (-0.00% vs peg)
- ⚪ **USDT** $1.0000 (+0.00% vs peg)
- ⚪ **USDC** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 13% vs 30d norm 40% (0.3x)
- ⚪ **ETH** 24h vol 17% vs 30d norm 53% (0.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 5 | -97.2% | 304.8% |
| PF_TRUMPUSD | 2 | +256.4% | 256.4% |
| PF_HFTUSD | 2 | +113.8% | 113.8% |
| PF_BELUSD | 1 | +527.4% | 528.8% |
| PF_UNIUSD | 1 | +241.0% | 269.5% |
| PF_COTIUSD | 1 | +122.1% | 122.1% |
| PF_ASTERUSD | 1 | +55.1% | 55.1% |
| PF_ICXUSD | 1 | -53.8% | 53.8% |
| PF_VIRTUALUSD | 1 | +43.9% | 43.9% |
| PF_NEARUSD | 1 | -38.0% | 38.0% |

**Resolved since last scan:** PF_SPXUSD (crowded 2d, worst 210%), PF_LDOUSD (crowded 1d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
