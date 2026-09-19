# Pond Scanner Report
**Scan time:** 2026-09-19 15:53 UTC

**Flags this scan:** 17 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_NEARUSD | +365.6% | $4,191,991 |
| 🟢 | PF_INJUSD | +348.8% | $749,261 |
| 🟢 | PF_XTZUSD | -219.1% | $2,145,271 |
| 🟢 | PF_AVAXUSD | +168.4% | $1,262,700 |
| 🟢 | PF_SOLUSD | -163.8% | $670,013 |
| 🟢 | PF_UNIUSD | +153.7% | $1,211,888 |
| 🟢 | PF_SYNUSD | +127.9% | $5,766,641 |
| 🟢 | PF_HFTUSD | -106.3% | $929,843 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.007%** (gemini → coinbase) — coinbase: $81,721.76, kraken: $81,716.00, gemini: $81,715.66
- ⚪ **ETH** gap **0.025%** (gemini → kraken) — coinbase: $2,646.79, kraken: $2,646.96, gemini: $2,646.30

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #379 | $69.9M | 4.03x | +17.0% |
| Synapse (SYN) | #461 | $51.8M | 1.58x | +27.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.17, realized vol 10d 45% vs 60d 41%
- 🟡 **ETH: MIXED** — efficiency ratio 0.24, realized vol 10d 56% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9992 (-0.08% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9998 (-0.02% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 25% vs 30d norm 40% (0.6x)
- ⚪ **ETH** 24h vol 32% vs 30d norm 52% (0.6x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | +365.6% | 365.6% |
| PF_UNIUSD | 3 | +153.7% | 583.0% |
| PF_INJUSD | 2 | +348.8% | 518.3% |
| PF_HFTUSD | 2 | -106.3% | 107.0% |
| PF_XTZUSD | 1 | -219.1% | 219.1% |
| PF_AVAXUSD | 1 | +168.4% | 168.4% |
| PF_SOLUSD | 1 | -163.8% | 600.5% |
| PF_SYNUSD | 1 | +127.9% | 127.9% |
| PF_TRUMPUSD | 1 | -60.0% | 60.0% |
| PF_CATIUSD | 1 | -56.1% | 56.1% |
| PF_MINAUSD | 1 | -54.7% | 54.7% |
| PF_KAITOUSD | 1 | +49.9% | 49.9% |
| PF_ACEUSD | 1 | -43.5% | 43.5% |
| PF_ONDOUSD | 1 | +43.2% | 43.2% |
| PF_ASTERUSD | 1 | -41.4% | 41.4% |

**Resolved since last scan:** PF_LSKUSD (crowded 2d, worst 761%), PF_APTUSD (crowded 1d, worst 52%), PF_XRPUSD (crowded 1d, worst 47%), PF_ETHFIUSD (crowded 2d, worst 121%), PF_SUIUSD (crowded 1d, worst 32%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
