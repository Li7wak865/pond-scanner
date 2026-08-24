# Pond Scanner Report
**Scan time:** 2026-08-24 13:13 UTC

**Flags this scan:** 11 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_TRUMPUSD | -161.2% | $3,674,041 |
| 🟢 | PF_HFTUSD | +110.1% | $1,492,210 |
| 🟢 | PF_ACEUSD | -90.9% | $1,591,597 |
| 🟢 | PF_ETHFIUSD | -78.8% | $638,653 |
| 🟢 | PF_UNIUSD | +76.2% | $936,517 |
| 🟢 | PF_GRASSUSD | +65.2% | $1,438,686 |
| 🟢 | PF_SYNUSD | -58.5% | $682,538 |
| 🟢 | PF_XRPUSD | +51.4% | $47,046,224 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → coinbase) — coinbase: $79,211.16, kraken: $79,202.40, gemini: $79,208.00
- ⚪ **ETH** gap **0.075%** (gemini → kraken) — coinbase: $2,513.87, kraken: $2,514.26, gemini: $2,512.38

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Prom (PROM) | #361 | $66.1M | 1.42x | +27.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.67, realized vol 10d 58% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.67, realized vol 10d 107% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9987 (-0.13% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 44% vs 30d norm 37% (1.2x)
- ⚪ **ETH** 24h vol 52% vs 30d norm 52% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -161.2% | 332.5% |
| PF_ACEUSD | 3 | -90.9% | 241.7% |
| PF_HFTUSD | 1 | +110.1% | 110.1% |
| PF_ETHFIUSD | 1 | -78.8% | 91.6% |
| PF_UNIUSD | 1 | +76.2% | 76.2% |
| PF_GRASSUSD | 1 | +65.2% | 65.2% |
| PF_SYNUSD | 1 | -58.5% | 478.3% |
| PF_XRPUSD | 1 | +51.4% | 51.4% |
| PF_STORJUSD | 1 | -50.7% | 71.1% |
| PF_LDOUSD | 1 | +35.9% | 35.9% |

**Resolved since last scan:** PF_SOLUSD (crowded 2d, worst 437%), PF_SUSD (crowded 1d, worst 100%), PF_ZROUSD (crowded 2d, worst 93%), PF_DEEPUSD (crowded 1d, worst 58%), PF_RENDERUSD (crowded 2d, worst 152%), PF_ASTERUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
