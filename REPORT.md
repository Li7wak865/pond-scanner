# Pond Scanner Report
**Scan time:** 2026-08-23 07:01 UTC

**Flags this scan:** 13 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +747.7% | $651,207 |
| 🟢 | PI_XRPUSD | +377.2% | $1,588,364 |
| 🟢 | PF_UNIUSD | +358.6% | $716,097 |
| 🟢 | PF_ACEUSD | -93.7% | $3,627,982 |
| 🟢 | PF_SYNUSD | +71.2% | $556,002 |
| 🟢 | PF_TRUMPUSD | -59.1% | $7,412,966 |
| 🟢 | PF_XRPUSD | +55.5% | $80,918,272 |
| 🟢 | PF_GRIFFAINUSD | +53.9% | $915,075 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.040%** (kraken → gemini) — coinbase: $76,025.65, kraken: $76,023.50, gemini: $76,053.90
- ⚪ **ETH** gap **0.045%** (coinbase → gemini) — coinbase: $2,387.44, kraken: $2,387.92, gemini: $2,388.52

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Tutorial (TUT) | #411 | $52.7M | 2.78x | +69.5% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 63% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.58, realized vol 10d 111% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9977 (-0.23% vs peg)
- ⚪ **USDT** $0.9998 (-0.02% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 24% vs 30d norm 36% (0.7x)
- ⚪ **ETH** 24h vol 44% vs 30d norm 51% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 4 | +747.7% | 819.3% |
| PF_UNIUSD | 4 | +358.6% | 371.9% |
| PF_TRUMPUSD | 4 | -59.1% | 332.5% |
| PF_SYNUSD | 3 | +71.2% | 505.9% |
| PF_ACEUSD | 2 | -93.7% | 93.7% |
| PF_ETHFIUSD | 2 | +39.6% | 92.6% |
| PI_XRPUSD | 1 | +377.2% | 377.2% |
| PF_XRPUSD | 1 | +55.5% | 55.5% |
| PF_GRIFFAINUSD | 1 | +53.9% | 53.9% |
| PF_STXUSD | 1 | +38.6% | 38.6% |
| PF_HFTUSD | 1 | -37.6% | 37.6% |
| PF_SUIUSD | 1 | +37.3% | 37.3% |

**Resolved since last scan:** PF_AVAXUSD (crowded 1d, worst 133%), PF_RIVERUSD (crowded 1d, worst 119%), PF_KAITOUSD (crowded 1d, worst 97%), PF_JUPUSD (crowded 2d, worst 97%), PF_NEARUSD (crowded 2d, worst 143%), PF_ICPUSD (crowded 2d, worst 54%), PF_FETUSD (crowded 2d, worst 146%), PF_POPCATUSD (crowded 1d, worst 41%), PF_LDOUSD (crowded 1d, worst 40%), PF_CRVUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
