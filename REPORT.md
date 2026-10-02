# Pond Scanner Report
**Scan time:** 2026-10-02 05:39 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_MOVRUSD | -289.0% | $1,635,201 |
| 🟢 | PF_OPNUSD | +268.9% | $945,006 |
| 🟢 | PF_UNIUSD | +191.5% | $870,358 |
| 🟢 | PF_XRPUSD | +87.9% | $19,693,889 |
| 🟢 | PF_ZROUSD | -67.0% | $660,272 |
| 🟢 | PF_LINKUSD | -64.4% | $997,449 |
| 🟢 | PF_DOTUSD | +55.1% | $1,338,704 |
| 🟢 | PF_VIRTUALUSD | +50.7% | $584,922 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.005%** (coinbase → gemini) — coinbase: $85,949.17, kraken: $85,950.90, gemini: $85,953.59
- ⚪ **ETH** gap **0.016%** (kraken → gemini) — coinbase: $2,717.33, kraken: $2,717.03, gemini: $2,717.47

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| MegaETH (MEGA) | #427 | $60.3M | 1.75x | +18.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.39, realized vol 10d 19% vs 60d 42%
- 🟡 **ETH: MIXED** — efficiency ratio 0.26, realized vol 10d 16% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 40% vs 30d norm 35% (1.1x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 46% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 3 | +191.5% | 543.2% |
| PF_MOVRUSD | 2 | -289.0% | 289.0% |
| PF_LINKUSD | 2 | -64.4% | 234.3% |
| PF_OPNUSD | 1 | +268.9% | 268.9% |
| PF_XRPUSD | 1 | +87.9% | 87.9% |
| PF_ZROUSD | 1 | -67.0% | 67.0% |
| PF_DOTUSD | 1 | +55.1% | 55.1% |
| PF_VIRTUALUSD | 1 | +50.7% | 50.7% |
| PF_JUPUSD | 1 | +47.9% | 47.9% |
| PF_SUIUSD | 1 | +44.8% | 44.8% |
| PF_WLDUSD | 1 | +40.2% | 40.2% |
| PF_ALICEUSD | 1 | -30.3% | 30.3% |

**Resolved since last scan:** PF_TRUMPUSD (crowded 3d, worst 105%), PF_ACEUSD (crowded 2d, worst 44%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
