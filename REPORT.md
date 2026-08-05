# Pond Scanner Report
**Scan time:** 2026-08-05 19:55 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZIGUSD | +191.5% | $1,197,090 |
| 🟢 | PF_KAITOUSD | +80.0% | $544,742 |
| 🟢 | PF_SYNUSD | -39.6% | $6,917,817 |
| 🟢 | PF_XRPUSD | +39.5% | $24,581,547 |
| 🟢 | PF_APTUSD | +33.1% | $598,597 |
| ⚪ | PF_NEARUSD | -17.5% | $1,255,862 |
| ⚪ | PF_UNIUSD | +15.7% | $1,786,027 |
| ⚪ | PF_ONDOUSD | +15.3% | $5,258,948 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.015%** (gemini → kraken) — coinbase: $64,871.57, kraken: $64,880.30, gemini: $64,870.58
- ⚪ **ETH** gap **0.027%** (coinbase → gemini) — coinbase: $1,919.07, kraken: $1,919.07, gemini: $1,919.58

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Bless (BLESS) | #442 | $47.4M | 0.89x | +144.2% |
| SkyAI (SKYAI) | #351 | $63.4M | 0.80x | +24.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.08, realized vol 10d 27% vs 60d 32%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.09, realized vol 10d 36% vs 60d 46%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9976 (-0.24% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 20% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 42% (0.8x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZIGUSD | 1 | +191.5% | 191.5% |
| PF_KAITOUSD | 1 | +80.0% | 80.6% |
| PF_SYNUSD | 1 | -39.6% | 61.5% |
| PF_XRPUSD | 1 | +39.5% | 39.5% |
| PF_APTUSD | 1 | +33.1% | 33.1% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 310%), PF_TRUMPUSD (crowded 1d, worst 79%), PF_FILUSD (crowded 1d, worst 38%), PF_ZEREBROUSD (crowded 1d, worst 66%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
