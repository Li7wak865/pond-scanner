# Pond Scanner Report
**Scan time:** 2026-09-18 20:55 UTC

**Flags this scan:** 19 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LINKUSD | +444.1% | $578,138 |
| 🟢 | PF_LSKUSD | -377.1% | $1,154,873 |
| 🟢 | PF_UNIUSD | +358.8% | $2,906,333 |
| 🟢 | PF_BATUSD | +127.8% | $1,632,428 |
| 🟢 | PF_ETHFIUSD | +120.6% | $1,449,790 |
| 🟢 | PF_NEARUSD | -111.1% | $6,298,568 |
| 🟢 | PF_TRUMPUSD | +104.8% | $690,208 |
| 🟢 | PF_JTOUSD | +85.3% | $568,482 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.013%** (gemini → coinbase) — coinbase: $81,086.58, kraken: $81,080.80, gemini: $81,075.89
- ⚪ **ETH** gap **0.037%** (coinbase → gemini) — coinbase: $2,631.86, kraken: $2,631.97, gemini: $2,632.84

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #435 | $55.7M | 7.08x | +56.4% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 46% vs 60d 41%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.17, realized vol 10d 60% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9996 (-0.04% vs peg)
- ⚪ **USDT** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **USDe** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 54% vs 30d norm 41% (1.3x)
- ⚪ **ETH** 24h vol 48% vs 30d norm 54% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -111.1% | 176.8% |
| PF_UNIUSD | 2 | +358.8% | 583.0% |
| PF_LINKUSD | 1 | +444.1% | 444.1% |
| PF_LSKUSD | 1 | -377.1% | 673.9% |
| PF_BATUSD | 1 | +127.8% | 130.5% |
| PF_ETHFIUSD | 1 | +120.6% | 120.6% |
| PF_TRUMPUSD | 1 | +104.8% | 104.8% |
| PF_JTOUSD | 1 | +85.3% | 85.3% |
| PF_TUSD | 1 | -83.5% | 83.5% |
| PF_ASTERUSD | 1 | -73.4% | 73.4% |
| PF_GRIFFAINUSD | 1 | -61.9% | 61.9% |
| PF_INJUSD | 1 | +44.8% | 387.6% |
| PF_STGUSD | 1 | -44.7% | 76.9% |
| PF_XRPUSD | 1 | +43.9% | 72.7% |
| PF_HFTUSD | 1 | -42.6% | 100.7% |
| PF_RUNEUSD | 1 | +41.4% | 41.4% |
| PF_CRVUSD | 1 | +34.3% | 34.3% |
| PF_LDOUSD | 1 | +31.0% | 31.0% |

**Resolved since last scan:** PF_INITUSD (crowded 1d, worst 54%), PF_APTUSD (crowded 1d, worst 33%), PF_RAREUSD (crowded 1d, worst 32%), PF_KAITOUSD (crowded 1d, worst 31%), PF_WLDUSD (crowded 1d, worst 36%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
