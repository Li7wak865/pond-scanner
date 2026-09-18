# Pond Scanner Report
**Scan time:** 2026-09-18 16:24 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -673.9% | $1,488,307 |
| 🟢 | PF_INJUSD | -387.6% | $527,677 |
| 🟢 | PF_NEARUSD | -176.8% | $6,873,722 |
| 🟢 | PF_BATUSD | +130.5% | $1,530,059 |
| 🟢 | PF_JTOUSD | +80.8% | $570,436 |
| 🟢 | PF_XRPUSD | +72.7% | $83,551,729 |
| 🟢 | PF_UNIUSD | -70.8% | $3,078,937 |
| 🟢 | PF_ETHFIUSD | +57.6% | $1,137,918 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.029%** (kraken → gemini) — coinbase: $80,962.83, kraken: $80,946.90, gemini: $80,970.31
- ⚪ **ETH** gap **0.016%** (coinbase → gemini) — coinbase: $2,596.20, kraken: $2,596.23, gemini: $2,596.62

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Gravity (by Galxe) (G) | #411 | $60.5M | 4.64x | +85.2% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.12, realized vol 10d 45% vs 60d 41%
- 🔴 **ETH: CHOPPY** — efficiency ratio 0.14, realized vol 10d 54% vs 60d 60%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9989 (-0.11% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 54% vs 30d norm 41% (1.3x)
- ⚪ **ETH** 24h vol 49% vs 30d norm 57% (0.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 3 | -176.8% | 176.8% |
| PF_UNIUSD | 2 | -70.8% | 583.0% |
| PF_LSKUSD | 1 | -673.9% | 673.9% |
| PF_INJUSD | 1 | -387.6% | 387.6% |
| PF_BATUSD | 1 | +130.5% | 130.5% |
| PF_JTOUSD | 1 | +80.8% | 80.8% |
| PF_XRPUSD | 1 | +72.7% | 72.7% |
| PF_ETHFIUSD | 1 | +57.6% | 57.6% |
| PF_INITUSD | 1 | -51.7% | 53.6% |
| PF_STGUSD | 1 | -42.4% | 76.9% |
| PF_HFTUSD | 1 | -41.3% | 100.7% |
| PF_APTUSD | 1 | -33.1% | 33.1% |
| PF_RAREUSD | 1 | +31.8% | 31.8% |
| PF_KAITOUSD | 1 | +31.4% | 31.4% |
| PF_WLDUSD | 1 | +30.1% | 35.5% |

**Resolved since last scan:** PF_ASTERUSD (crowded 1d, worst 75%), PF_DOTUSD (crowded 1d, worst 59%), PF_EIGENUSD (crowded 1d, worst 49%), PF_TIAUSD (crowded 1d, worst 41%), PF_TRUMPUSD (crowded 1d, worst 37%), PF_SUIUSD (crowded 1d, worst 33%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
