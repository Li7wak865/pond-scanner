# Pond Scanner Report
**Scan time:** 2026-10-06 06:22 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -375.2% | $619,378 |
| 🟢 | PF_UNIUSD | -254.4% | $1,076,134 |
| 🟢 | PF_LINKUSD | +186.0% | $803,362 |
| 🟢 | PF_NEARUSD | -178.3% | $3,335,307 |
| 🟢 | PF_ZROUSD | +80.1% | $1,170,234 |
| 🟢 | PF_SPXUSD | +76.2% | $519,382 |
| 🟢 | PF_RUNEUSD | -65.5% | $686,433 |
| 🟢 | PF_DOTUSD | +61.0% | $1,571,998 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (kraken → gemini) — coinbase: $85,211.20, kraken: $85,210.50, gemini: $85,226.77
- ⚪ **ETH** gap **0.025%** (coinbase → gemini) — coinbase: $2,692.08, kraken: $2,692.31, gemini: $2,692.74

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| iExec RLC (RLC) | #350 | $77.8M | 3.42x | +135.3% |
| Api3 (API3) | #488 | $50.6M | 1.05x | +17.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.46, realized vol 10d 19% vs 60d 43%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.43, realized vol 10d 15% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9986 (-0.14% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 33% (0.8x)
- ⚪ **ETH** 24h vol 23% vs 30d norm 43% (0.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_PONSUSD | 4 | +46.6% | 111.2% |
| PF_MOVRUSD | 2 | -375.2% | 541.5% |
| PF_UNIUSD | 2 | -254.4% | 254.4% |
| PF_RUNEUSD | 2 | -65.5% | 98.6% |
| PF_LINKUSD | 1 | +186.0% | 244.2% |
| PF_NEARUSD | 1 | -178.3% | 178.3% |
| PF_ZROUSD | 1 | +80.1% | 80.1% |
| PF_SPXUSD | 1 | +76.2% | 76.2% |
| PF_DOTUSD | 1 | +61.0% | 61.0% |
| PF_FILUSD | 1 | -59.5% | 59.5% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 1d, worst 140%), PF_GRASSUSD (crowded 2d, worst 84%), PF_ATOMUSD (crowded 1d, worst 45%), PF_TIAUSD (crowded 1d, worst 39%), PF_APTUSD (crowded 1d, worst 39%), PF_FETUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
