# Pond Scanner Report
**Scan time:** 2026-08-21 01:57 UTC

**Flags this scan:** 21 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_UNIUSD | +130.2% | $1,047,412 |
| 🟢 | PF_AVAXUSD | +95.3% | $1,052,369 |
| 🟢 | PF_ONTUSD | -88.1% | $1,011,058 |
| 🟢 | PF_ETHFIUSD | -84.1% | $629,443 |
| 🟢 | PF_SUSHIUSD | +81.5% | $913,553 |
| 🟢 | PF_LINKUSD | +67.5% | $537,035 |
| 🟢 | PF_KAITOUSD | -66.4% | $1,144,598 |
| 🟢 | PF_ACEUSD | -61.7% | $14,311,547 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.021%** (coinbase → kraken) — coinbase: $75,111.18, kraken: $75,127.30, gemini: $75,114.81
- ⚪ **ETH** gap **0.062%** (kraken → gemini) — coinbase: $2,359.70, kraken: $2,359.65, gemini: $2,361.12

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| BOOK OF MEME (BOME) | #301 | $79.3M | 2.80x | +34.0% |
| Ontology (ONT) | #426 | $51.9M | 1.23x | +25.7% |
| ConstitutionDAO (PEOPLE) | #417 | $53.1M | 0.90x | +28.7% |
| Ontology Gas (ONG) | #343 | $68.4M | 0.84x | +126.1% |
| 牛来 (Niu Lai) (牛来) | #371 | $63.6M | 0.62x | +42.1% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.71, realized vol 10d 49% vs 60d 35%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.75, realized vol 10d 99% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9988 (-0.12% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDC** $0.9998 (-0.02% vs peg)
- ⚪ **USDe** $0.9998 (-0.02% vs peg)
- ⚪ **DAI** $0.9999 (-0.01% vs peg)
- ⚪ **PYUSD** $1.0000 (-0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 65% vs 30d norm 31% (2.1x)
- ⚪ **ETH** 24h vol 63% vs 30d norm 47% (1.3x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_UNIUSD | 2 | +130.2% | 130.2% |
| PF_AVAXUSD | 2 | +95.3% | 151.8% |
| PF_ETHFIUSD | 2 | -84.1% | 154.6% |
| PF_LINKUSD | 2 | +67.5% | 67.6% |
| PF_ACEUSD | 2 | -61.7% | 217.7% |
| PF_JUPUSD | 2 | +51.4% | 54.3% |
| PF_CATIUSD | 2 | -47.0% | 215.5% |
| PF_TRUMPUSD | 2 | +46.3% | 130.8% |
| PF_HFTUSD | 2 | -37.8% | 37.8% |
| PF_NEARUSD | 2 | +35.4% | 71.2% |
| PF_ONTUSD | 1 | -88.1% | 88.1% |
| PF_SUSHIUSD | 1 | +81.5% | 81.5% |
| PF_KAITOUSD | 1 | -66.4% | 66.4% |
| PF_RAREUSD | 1 | -54.9% | 54.9% |
| PF_LDOUSD | 1 | +44.3% | 44.3% |

**Resolved since last scan:** PF_HYPEUSD (crowded 2d, worst 819%), PF_IOTAUSD (crowded 2d, worst 131%), PF_GOATUSD (crowded 2d, worst 67%), PF_CHILLGUYUSD (crowded 2d, worst 52%), PF_GRASSUSD (crowded 2d, worst 53%), PF_XRPUSD (crowded 2d, worst 38%), PF_SUIUSD (crowded 2d, worst 38%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
