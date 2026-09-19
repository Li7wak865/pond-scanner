# Pond Scanner Report
**Scan time:** 2026-09-19 11:00 UTC

**Flags this scan:** 16 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_LSKUSD | -761.5% | $803,045 |
| 🟢 | PF_SOLUSD | +600.5% | $922,139 |
| 🟢 | PF_INJUSD | +518.3% | $647,552 |
| 🟢 | PF_UNIUSD | +349.1% | $1,429,957 |
| 🟢 | PF_NEARUSD | +255.6% | $5,222,891 |
| 🟢 | PF_AVAXUSD | +157.8% | $808,777 |
| 🟢 | PF_HFTUSD | +107.0% | $1,456,160 |
| 🟢 | PF_APTUSD | +51.7% | $1,286,223 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → gemini) — coinbase: $81,193.97, kraken: $81,195.40, gemini: $81,210.82
- ⚪ **ETH** gap **0.007%** (kraken → coinbase) — coinbase: $2,637.45, kraken: $2,637.27, gemini: $2,637.29

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Synapse (SYN) | #440 | $55.2M | 1.87x | +42.8% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🔴 **BTC: CHOPPY** — efficiency ratio 0.15, realized vol 10d 45% vs 60d 41%
- 🟡 **ETH: MIXED** — efficiency ratio 0.23, realized vol 10d 56% vs 60d 61%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9991 (-0.09% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9999 (-0.01% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- ⚪ **BTC** 24h vol 57% vs 30d norm 40% (1.4x)
- ⚪ **ETH** 24h vol 53% vs 30d norm 52% (1.0x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_NEARUSD | 4 | +255.6% | 255.6% |
| PF_UNIUSD | 3 | +349.1% | 583.0% |
| PF_LSKUSD | 2 | -761.5% | 761.5% |
| PF_INJUSD | 2 | +518.3% | 518.3% |
| PF_HFTUSD | 2 | +107.0% | 107.0% |
| PF_ETHFIUSD | 2 | +40.8% | 120.6% |
| PF_SOLUSD | 1 | +600.5% | 600.5% |
| PF_AVAXUSD | 1 | +157.8% | 157.8% |
| PF_APTUSD | 1 | +51.7% | 51.7% |
| PF_XRPUSD | 1 | +47.1% | 47.1% |
| PF_SYNUSD | 1 | +45.9% | 45.9% |
| PF_XTZUSD | 1 | -41.4% | 69.0% |
| PF_KAITOUSD | 1 | +40.7% | 42.4% |
| PF_MINAUSD | 1 | -38.3% | 38.3% |
| PF_SUIUSD | 1 | +31.6% | 31.6% |

**Resolved since last scan:** PF_DEEPUSD (crowded 1d, worst 74%), PF_DOTUSD (crowded 1d, worst 69%), PF_FILUSD (crowded 1d, worst 65%), PF_JTOUSD (crowded 2d, worst 85%), PF_CATIUSD (crowded 1d, worst 50%), PF_STGUSD (crowded 2d, worst 77%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
