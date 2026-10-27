# Pond Scanner Report
**Scan time:** 2026-10-27 22:15 UTC

**Flags this scan:** 3 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | -93.0% | $649,401 |
| ⚪ | PF_SUIUSD | +27.9% | $2,776,327 |
| ⚪ | PF_XRPUSD | +27.3% | $8,511,027 |
| ⚪ | PF_LDOUSD | +14.9% | $778,929 |
| ⚪ | PF_APTUSD | +13.8% | $744,938 |
| ⚪ | PF_BATUSD | -10.8% | $595,053 |
| ⚪ | PF_WIFUSD | +10.5% | $3,619,810 |
| ⚪ | PF_FILUSD | +10.2% | $754,202 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.019%** (kraken → gemini) — coinbase: $80,796.83, kraken: $80,791.70, gemini: $80,806.73
- ⚪ **ETH** gap **0.040%** (coinbase → gemini) — coinbase: $2,346.65, kraken: $2,346.79, gemini: $2,347.58

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Dolphin (POD) | #443 | $50.5M | 1.35x | +33.3% |
| Renzo (REZ) | #447 | $49.7M | 0.65x | +15.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.14, realized vol 10d 25% vs 60d 34%
- 🟡 **ETH: MIXED** — efficiency ratio 0.33, realized vol 10d 27% vs 60d 40%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9973 (-0.27% vs peg)
- ⚪ **USDT** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9993 (-0.07% vs peg)
- ⚪ **DAI** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9998 (-0.02% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 22% vs 30d norm 31% (0.7x)
- ⚪ **ETH** 24h vol 30% vs 30d norm 43% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 1 | -93.0% | 93.0% |

**Resolved since last scan:** PF_NEARUSD (crowded 2d, worst 304%), PF_ARCUSD (crowded 1d, worst 34%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
