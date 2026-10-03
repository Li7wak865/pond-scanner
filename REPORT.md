# Pond Scanner Report
**Scan time:** 2026-10-03 11:41 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +178.7% | $634,937 |
| 🟢 | PF_MOVRUSD | -118.3% | $655,915 |
| 🟢 | PF_NEARUSD | +113.9% | $2,706,510 |
| 🟢 | PF_PONSUSD | +111.3% | $541,758 |
| 🟢 | PF_BATUSD | +105.8% | $630,180 |
| 🟢 | PF_TRUMPUSD | -86.0% | $781,679 |
| 🟢 | PF_SANDUSD | -67.9% | $43,475,170 |
| 🟢 | PF_RUNEUSD | -36.4% | $638,679 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (gemini → coinbase) — coinbase: $84,649.98, kraken: $84,643.40, gemini: $84,640.00
- ⚪ **ETH** gap **0.020%** (coinbase → kraken) — coinbase: $2,685.18, kraken: $2,685.72, gemini: $2,685.51

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
Nothing unusual. ⚪

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.37, realized vol 10d 12% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.28, realized vol 10d 11% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $1.0000 (-0.00% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 28% vs 30d norm 35% (0.8x)
- ⚪ **ETH** 24h vol 33% vs 30d norm 46% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +178.7% | 329.1% |
| PF_MOVRUSD | 3 | -118.3% | 289.0% |
| PF_NEARUSD | 2 | +113.9% | 134.3% |
| PF_TRUMPUSD | 2 | -86.0% | 150.9% |
| PF_SANDUSD | 2 | -67.9% | 148.5% |
| PF_ZROUSD | 2 | +34.1% | 65.3% |
| PF_PONSUSD | 1 | +111.3% | 111.3% |
| PF_BATUSD | 1 | +105.8% | 215.7% |
| PF_RUNEUSD | 1 | -36.4% | 36.4% |
| PF_ALICEUSD | 1 | +35.3% | 35.3% |
| PF_TIAUSD | 1 | +31.1% | 31.1% |

**Resolved since last scan:** PF_UNIUSD (crowded 4d, worst 543%), PF_ASTERUSD (crowded 1d, worst 73%), PF_MANAUSD (crowded 1d, worst 73%), PF_ETHFIUSD (crowded 2d, worst 45%), PF_SYNUSD (crowded 1d, worst 43%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
