# Pond Scanner Report
**Scan time:** 2026-08-21 13:11 UTC

**Flags this scan:** 31 

## 1. Funding skew (crowded positioning)
| | Perp | Annualized funding | 24h vol |
|---|---|---|---|
| 🟢 | PF_STXUSD | +718.1% | $949,988 |
| 🟢 | PF_LINKUSD | +676.6% | $807,436 |
| 🟢 | PF_AVAXUSD | +440.9% | $1,000,777 |
| 🟢 | PF_JTOUSD | +152.5% | $584,775 |
| 🟢 | PF_NEARUSD | +146.0% | $3,319,527 |
| 🟢 | PF_TRUMPUSD | +125.6% | $1,118,936 |
| 🟢 | PF_UNIUSD | +125.4% | $1,414,650 |
| 🟢 | PF_ACEUSD | -114.4% | $11,695,549 |

_🟢 = crowd paying >30%/yr to hold a side. Historically mean-reverting; also a froth gauge. Rate math is approximate._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.052%** (gemini → coinbase) — coinbase: $77,101.67, kraken: $77,097.60, gemini: $77,061.23
- ⚪ **ETH** gap **0.076%** (kraken → coinbase) — coinbase: $2,385.32, kraken: $2,383.50, gemini: $2,384.82

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| Ontology (ONT) | #457 | $48.5M | 1.74x | +19.7% |
| ConstitutionDAO (PEOPLE) | #395 | $58.0M | 1.74x | +35.2% |
| GALA (GALA) | #267 | $95.8M | 1.10x | +30.7% |
| Spark (SPK) | #411 | $55.0M | 0.84x | +19.8% |
| Berachain (BERA) | #381 | $62.1M | 0.60x | +22.7% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.74, realized vol 10d 54% vs 60d 37%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.76, realized vol 10d 98% vs 60d 58%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9983 (-0.17% vs peg)
- ⚪ **USDT** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **USDC** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (-0.00% vs peg)
- ⚪ **PYUSD** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 100% vs 30d norm 35% (2.8x)
- ⚪ **ETH** 24h vol 90% vs 30d norm 48% (1.9x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
| Perp | Days crowded | Funding now | Worst seen |
|---|---|---|---|
| PF_LINKUSD | 2 | +676.6% | 676.6% |
| PF_TRUMPUSD | 2 | +125.6% | 130.8% |
| PF_UNIUSD | 2 | +125.4% | 152.6% |
| PF_ACEUSD | 2 | -114.4% | 217.7% |
| PF_JUPUSD | 2 | +34.7% | 58.7% |
| PF_STXUSD | 1 | +718.1% | 718.1% |
| PF_AVAXUSD | 1 | +440.9% | 440.9% |
| PF_JTOUSD | 1 | +152.5% | 152.5% |
| PF_NEARUSD | 1 | +146.0% | 146.0% |
| PF_SUIUSD | 1 | +82.1% | 82.1% |
| PF_XRPUSD | 1 | +76.9% | 76.9% |
| PF_SYNUSD | 1 | +76.6% | 76.6% |
| PF_DOTUSD | 1 | +62.4% | 62.4% |
| PF_ALICEUSD | 1 | +60.0% | 60.0% |
| PF_FETUSD | 1 | +59.2% | 59.2% |
| PF_ASTERUSD | 1 | +57.2% | 57.2% |
| PF_FARTCOINUSD | 1 | +47.6% | 47.6% |
| PF_VIRTUALUSD | 1 | +47.2% | 50.9% |
| PF_LDOUSD | 1 | -45.4% | 49.1% |
| PF_APTUSD | 1 | +42.7% | 42.7% |
| PF_KAITOUSD | 1 | -37.4% | 137.5% |
| PF_TIAUSD | 1 | +37.0% | 43.0% |
| PF_MANAUSD | 1 | +36.0% | 36.0% |
| PF_ONTUSD | 1 | -33.1% | 103.2% |
| PF_ONDOUSD | 1 | +31.9% | 31.9% |

**Resolved since last scan:** PF_PYTHUSD (crowded 1d, worst 69%), PF_CATIUSD (crowded 2d, worst 215%), PF_ZKUSD (crowded 1d, worst 40%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
