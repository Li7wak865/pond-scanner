# Pond Scanner Report
**Scan time:** 2026-08-23 13:02 UTC

**Flags this scan:** 12 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +413.9% | $685,557 |
| 🟢 | PF_LINKUSD | +290.4% | $589,225 |
| 🟢 | PI_XRPUSD | -272.3% | $1,584,225 |
| 🟢 | PF_NEARUSD | +161.1% | $3,651,492 |
| 🟢 | PF_ACEUSD | -139.7% | $1,766,086 |
| 🟢 | PF_FETUSD | +95.8% | $9,449,809 |
| 🟢 | PF_ETHFIUSD | -69.2% | $896,553 |
| 🟢 | PF_TRUMPUSD | -51.1% | $6,580,011 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.033%** (gemini → kraken) — coinbase: $77,212.07, kraken: $77,223.50, gemini: $77,198.40
- ⚪ **ETH** gap **0.083%** (gemini → kraken) — coinbase: $2,428.22, kraken: $2,428.37, gemini: $2,426.35

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #416 | $54.2M | 3.05x | +50.3% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.65, realized vol 10d 61% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.65, realized vol 10d 110% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 31% vs 30d norm 36% (0.9x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 51% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 4 | +413.9% | 413.9% |
| PF_LINKUSD | 4 | +290.4% | 819.3% |
| PF_TRUMPUSD | 4 | -51.1% | 332.5% |
| PF_SYNUSD | 3 | -33.5% | 505.9% |
| PF_ACEUSD | 2 | -139.7% | 139.7% |
| PF_ETHFIUSD | 2 | -69.2% | 92.6% |
| PI_XRPUSD | 1 | -272.3% | 377.2% |
| PF_NEARUSD | 1 | +161.1% | 161.1% |
| PF_FETUSD | 1 | +95.8% | 95.8% |
| PF_XTZUSD | 1 | +48.7% | 48.7% |
| PF_XRPUSD | 1 | +41.9% | 55.5% |

**Resolved since last scan:** PF_GRIFFAINUSD (crowded 1d, worst 54%), PF_STXUSD (crowded 1d, worst 39%), PF_HFTUSD (crowded 1d, worst 38%), PF_SUIUSD (crowded 1d, worst 37%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
