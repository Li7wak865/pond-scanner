# Pond Scanner Report
**Scan time:** 2026-08-24 07:29 UTC

**Flags this scan:** 14 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_SYNUSD | +478.3% | $676,473 |
| 🟢 | PF_SOLUSD | -274.8% | $1,930,773 |
| 🟢 | PF_SUSD | +100.4% | $1,009,656 |
| 🟢 | PF_ETHFIUSD | -91.7% | $924,936 |
| 🟢 | PF_ZROUSD | +78.8% | $688,080 |
| 🟢 | PF_DEEPUSD | +58.3% | $749,603 |
| 🟢 | PF_TRUMPUSD | -56.3% | $3,997,947 |
| 🟢 | PF_ACEUSD | -55.2% | $1,919,820 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (kraken → gemini) — coinbase: $77,556.77, kraken: $77,543.90, gemini: $77,560.17
- ⚪ **ETH** gap **0.041%** (kraken → gemini) — coinbase: $2,460.61, kraken: $2,460.22, gemini: $2,461.22

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #368 | $64.5M | 2.47x | +20.8% |
| Spark (SPK) | #331 | $71.3M | 1.31x | +30.6% |
| Prom (PROM) | #352 | $68.0M | 1.03x | +34.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.63, realized vol 10d 60% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.65, realized vol 10d 109% vs 60d 59%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9984 (-0.16% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 38% vs 30d norm 36% (1.0x)
- ⚪ **ETH** 24h vol 56% vs 30d norm 52% (1.1x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_TRUMPUSD | 5 | -56.3% | 332.5% |
| PF_ACEUSD | 3 | -55.2% | 241.7% |
| PF_SOLUSD | 2 | -274.8% | 437.2% |
| PF_ZROUSD | 2 | +78.8% | 93.1% |
| PF_RENDERUSD | 2 | +40.6% | 152.2% |
| PF_SYNUSD | 1 | +478.3% | 478.3% |
| PF_SUSD | 1 | +100.4% | 100.4% |
| PF_ETHFIUSD | 1 | -91.7% | 91.7% |
| PF_DEEPUSD | 1 | +58.3% | 58.3% |
| PF_STORJUSD | 1 | -35.8% | 71.1% |
| PF_ASTERUSD | 1 | +32.5% | 32.5% |

**Resolved since last scan:** PI_XRPUSD (crowded 2d, worst 503%), PF_UNIUSD (crowded 5d, worst 414%), PF_GRASSUSD (crowded 1d, worst 64%), PF_HFTUSD (crowded 2d, worst 111%), PF_LDOUSD (crowded 1d, worst 54%), PF_CHILLGUYUSD (crowded 1d, worst 52%), PF_EIGENUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
