# Pond Scanner Report
**Scan time:** 2026-08-22 01:50 UTC

**Flags this scan:** 32 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +819.2% | $1,257,640 |
| 🟢 | PF_HYPEUSD | -305.7% | $730,007 |
| 🟢 | PF_JTOUSD | +191.2% | $554,542 |
| 🟢 | PF_ZIGUSD | +176.5% | $1,142,034 |
| 🟢 | PF_TRUMPUSD | +138.2% | $1,892,192 |
| 🟢 | PF_SUSD | -129.8% | $1,181,947 |
| 🟢 | PF_JUPUSD | +94.7% | $651,467 |
| 🟢 | PF_BLURUSD | +73.0% | $825,602 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.011%** (kraken → coinbase) — coinbase: $77,843.64, kraken: $77,834.90, gemini: $77,836.44
- ⚪ **ETH** gap **0.030%** (kraken → coinbase) — coinbase: $2,515.00, kraken: $2,514.24, gemini: $2,514.27

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| GALA (GALA) | #253 | $104.6M | 1.54x | +35.9% |
| Audiera (BEAT) | #408 | $56.5M | 1.04x | +34.0% |
| KAITO (KAITO) | #274 | $96.9M | 0.76x | +16.7% |
| Tellor Tributes (TRB) | #443 | $52.3M | 0.63x | +22.9% |
| Prom (PROM) | #470 | $49.3M | 0.59x | +21.5% |
| Berachain (BERA) | #379 | $63.1M | 0.56x | +17.6% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.70, realized vol 10d 59% vs 60d 38%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.78, realized vol 10d 103% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9993 (-0.07% vs peg)
- ⚪ **USDT** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **USDC** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 96% vs 30d norm 36% (2.7x)
- ⚪ **ETH** 24h vol 97% vs 30d norm 50% (2.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 3 | +819.2% | 819.2% |
| PF_TRUMPUSD | 3 | +138.2% | 140.2% |
| PF_UNIUSD | 3 | +71.2% | 152.6% |
| PF_ACEUSD | 3 | -55.1% | 217.7% |
| PF_JTOUSD | 2 | +191.2% | 191.2% |
| PF_ZIGUSD | 2 | +176.5% | 176.5% |
| PF_KAITOUSD | 2 | +72.3% | 137.5% |
| PF_ONTUSD | 2 | -61.0% | 103.2% |
| PF_LDOUSD | 2 | +60.1% | 60.1% |
| PF_SYNUSD | 2 | +56.7% | 76.6% |
| PF_GRASSUSD | 2 | +51.2% | 51.2% |
| PF_XRPUSD | 2 | +41.5% | 76.9% |
| PF_AVAXUSD | 2 | -33.8% | 440.9% |
| PF_HYPEUSD | 1 | -305.7% | 305.7% |
| PF_SUSD | 1 | -129.8% | 129.8% |
| PF_JUPUSD | 1 | +94.7% | 94.7% |
| PF_BLURUSD | 1 | +73.0% | 73.0% |
| PF_ETHFIUSD | 1 | -60.9% | 60.9% |
| PF_ONDOUSD | 1 | +58.2% | 58.2% |
| PF_CRVUSD | 1 | +55.2% | 55.2% |
| PF_FARTCOINUSD | 1 | +47.6% | 47.6% |
| PF_TIAUSD | 1 | +47.6% | 47.6% |
| PF_DOTUSD | 1 | +46.6% | 46.6% |
| PF_FILUSD | 1 | +41.8% | 41.8% |
| PF_EIGENUSD | 1 | -39.0% | 39.0% |

**Resolved since last scan:** PF_PNUTUSD (crowded 2d, worst 236%), PF_NEARUSD (crowded 2d, worst 146%), PF_FETUSD (crowded 2d, worst 62%), PF_APTUSD (crowded 2d, worst 43%), PF_STXUSD (crowded 2d, worst 718%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
