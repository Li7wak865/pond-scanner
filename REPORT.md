# Pond Scanner Report
**Scan time:** 2026-10-31 05:43 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +369.8% | $1,003,030 |
| 🟢 | PF_ATOMUSD | -150.8% | $2,573,932 |
| 🟢 | PF_LINKUSD | -54.6% | $716,586 |
| 🟢 | PF_TIAUSD | -31.4% | $1,686,218 |
| 🟢 | PF_VIRTUALUSD | +30.3% | $549,457 |
| ⚪ | PF_SUSHIUSD | -27.3% | $1,901,267 |
| ⚪ | PF_SYNUSD | +25.7% | $527,692 |
| ⚪ | PF_TRUMPUSD | -23.6% | $919,741 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.032%** (coinbase → gemini) — coinbase: $77,124.40, kraken: $77,130.00, gemini: $77,149.11
- ⚪ **ETH** gap **0.031%** (coinbase → gemini) — coinbase: $2,238.37, kraken: $2,238.63, gemini: $2,239.07

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Lisk (LSK) | #455 | $48.4M | 1.54x | +16.9% |
| Infinity Ground (AIN) | #459 | $48.2M | 0.95x | +75.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.35, realized vol 10d 30% vs 60d 36%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.45, realized vol 10d 32% vs 60d 41%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9975 (-0.25% vs peg)
- ⚪ **USDe** $0.9990 (-0.10% vs peg)
- ⚪ **USDT** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 32% vs 30d norm 33% (1.0x)
- ⚪ **ETH** 24h vol 38% vs 30d norm 45% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +369.8% | 486.9% |
| PF_ATOMUSD | 2 | -150.8% | 550.1% |
| PF_LINKUSD | 2 | -54.6% | 235.0% |
| PF_VIRTUALUSD | 2 | +30.3% | 72.5% |
| PF_TIAUSD | 1 | -31.4% | 31.4% |

**Resolved since last scan:** PF_ZROUSD (crowded 2d, worst 393%), PF_XTZUSD (crowded 2d, worst 43%), PF_NEARUSD (crowded 4d, worst 142%), PF_ASTERUSD (crowded 2d, worst 53%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
