# Pond Scanner Report
**Scan time:** 2026-11-12 07:12 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_ZROUSD | -68.5% | $980,686 |
| 🟢 | PF_NEARUSD | -57.1% | $4,153,886 |
| 🟢 | PF_ZIGUSD | +47.8% | $526,162 |
| 🟢 | PF_UNIUSD | +47.6% | $546,458 |
| ⚪ | PF_STXUSD | -17.8% | $552,324 |
| ⚪ | PF_XRPUSD | +17.2% | $15,642,808 |
| ⚪ | PF_TRUMPUSD | -14.2% | $623,050 |
| ⚪ | PF_DOTUSD | -11.7% | $1,254,969 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.012%** (coinbase → gemini) — coinbase: $73,427.83, kraken: $73,433.60, gemini: $73,436.28
- ⚪ **ETH** gap **0.068%** (kraken → gemini) — coinbase: $2,044.63, kraken: $2,044.41, gemini: $2,045.79

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Janction (JCT) | #452 | $46.8M | 1.01x | -47.7% |
| MEET48 (IDOL) | #377 | $58.8M | 0.54x | -17.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.36, realized vol 10d 44% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.40, realized vol 10d 71% vs 60d 47%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- 🟢 **FDUSD** $0.9961 (-0.39% vs peg)
- ⚪ **USDT** $0.9990 (-0.10% vs peg)
- ⚪ **USDe** $0.9992 (-0.08% vs peg)
- ⚪ **USDC** $0.9994 (-0.06% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 27% vs 30d norm 36% (0.8x)
- ⚪ **ETH** 24h vol 35% vs 30d norm 50% (0.7x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_ZROUSD | 2 | -68.5% | 68.5% |
| PF_NEARUSD | 2 | -57.1% | 138.3% |
| PF_ZIGUSD | 1 | +47.8% | 47.8% |
| PF_UNIUSD | 1 | +47.6% | 47.6% |

**Resolved since last scan:** PF_SUIUSD (crowded 2d, worst 31%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
