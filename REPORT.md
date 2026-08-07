# Pond Scanner Report
**Scan time:** 2026-08-07 07:42 UTC

**Flags this scan:** 6 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ACEUSD | -355.0% | $19,980,847 |
| 🟢 | PF_HFTUSD | -135.9% | $174,003,797 |
| 🟢 | PF_KAITOUSD | -105.0% | $525,649 |
| ⚪ | PF_UNIUSD | -25.1% | $1,265,796 |
| ⚪ | PF_BICOUSD | +22.9% | $39,723,316 |
| ⚪ | PF_LDOUSD | +13.8% | $940,840 |
| ⚪ | PF_SUIUSD | -12.4% | $3,457,294 |
| ⚪ | PF_CTSIUSD | -11.6% | $25,564,170 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.036%** (coinbase → gemini) — coinbase: $64,320.73, kraken: $64,336.90, gemini: $64,344.10
- ⚪ **ETH** gap **0.030%** (kraken → gemini) — coinbase: $1,901.94, kraken: $1,901.67, gemini: $1,902.25

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| SkyAI (SKYAI) | #261 | $97.5M | 0.65x | +28.8% |
| ETHGas (GWEI) | #428 | $48.8M | 0.56x | +40.8% |
| Allora (ALLO) | #296 | $77.4M | 0.51x | +21.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.04, realized vol 10d 22% vs 60d 30%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.07, realized vol 10d 27% vs 60d 43%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDe** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 18% vs 30d norm 29% (0.6x)
- ⚪ **ETH** 24h vol 24% vs 30d norm 41% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ACEUSD | 1 | -355.0% | 358.2% |
| PF_HFTUSD | 1 | -135.9% | 135.9% |
| PF_KAITOUSD | 1 | -105.0% | 124.5% |

**Resolved since last scan:** PF_SOLUSD (crowded 1d, worst 639%), PF_SYNUSD (crowded 2d, worst 54%), PF_SUIUSD (crowded 1d, worst 32%), PF_UNIUSD (crowded 2d, worst 144%), PF_MOODENGUSD (crowded 1d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
