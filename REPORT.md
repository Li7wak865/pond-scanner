# Pond Scanner Report
**Scan time:** 2026-08-20 07:07 UTC

**Flags this scan:** 7 

## 1. Funding skew (crowded positioning)
_Data source unavailable this run._

## 2. Cross-exchange basis (US venues)
- ⚪ **BTC** gap **0.159%** (kraken → gemini) — coinbase: $69,828.93, kraken: $69,778.80, gemini: $69,889.63
- ⚪ **ETH** gap **0.072%** (kraken → gemini) — coinbase: $2,260.21, kraken: $2,259.49, gemini: $2,261.12

_Gaps under ~0.3% are normal noise/fees. Persistent large gaps usually mean withdrawal friction somewhere — information either way._

## 3. Small-coin radar (ranks ~250-500, whale-free zone)
| Coin | Rank | Mcap | 24h vol/mcap | 24h move |
|---|---|---|---|---|
| RE (RE) | #279 | $84.8M | 1.88x | +33.3% |
| BOOK OF MEME (BOME) | #323 | $70.5M | 0.89x | +33.0% |
| Bio Protocol (BIO) | #350 | $64.6M | 0.69x | +19.5% |
| Audiera (BEAT) | #470 | $44.3M | 0.62x | -31.1% |
| RedStone (RED) | #387 | $57.3M | 0.54x | +34.9% |

_⚠️ WATCHLIST ONLY. Volume spikes in small coins are often pumps, listings, or news. Research before touching; never a buy signal by itself._

## 4. Volatility regime (feeds your momentum bot)
- 🟢 **BTC: TRENDING** — efficiency ratio 0.57, realized vol 10d 43% vs 60d 33%
- 🟢 **ETH: TRENDING** — efficiency ratio 0.66, realized vol 10d 99% vs 60d 57%

_TRENDING = momentum strategies feed well. CHOPPY = expect your momentum bot to sit in cash a lot (correct behavior)._

## 5. Stablecoin pegs (mechanical stress gauge)
- ⚪ **FDUSD** $0.9981 (-0.19% vs peg)
- ⚪ **USDT** $0.9993 (-0.07% vs peg)
- ⚪ **USDC** $0.9996 (-0.04% vs peg)
- ⚪ **USDe** $0.9997 (-0.03% vs peg)
- ⚪ **PYUSD** $0.9997 (-0.03% vs peg)
- ⚪ **DAI** $1.0000 (+0.00% vs peg)

_Flags at ±0.3%. Small persistent discounts = redemption friction; large = panic. Tail risk on depegs is total loss - observation, not a trade._

## 6. Volatility spike (dislocation weather siren)
- 🟢 **BTC** 24h vol 85% vs 30d norm 29% (2.9x)
- 🟢 **ETH** 24h vol 161% vs 30d norm 46% (3.5x)

_>2x = markets dislocating; spreads widen and forced flows appear. Expect the momentum bot and basis gaps to behave unusually._

## 7. Funding persistence (days each perp has stayed crowded)
No perps currently crowded. ⚪

**Resolved since last scan:** PF_UNIUSD (crowded 2d, worst 323%), PF_NEARUSD (crowded 1d, worst 152%), PF_GRASSUSD (crowded 2d, worst 78%), PF_ETHFIUSD (crowded 2d, worst 155%), PF_AVAXUSD (crowded 1d, worst 55%), PF_ACEUSD (crowded 6d, worst 732%), PF_RAREUSD (crowded 1d, worst 55%), PF_ASTERUSD (crowded 1d, worst 49%), PF_DYMUSD (crowded 1d, worst 38%), PF_TRUMPUSD (crowded 1d, worst 35%)

_Persistence separates blips from durable structural payments - the raw evidence file for the funding-harvest hypothesis._

## Data issues this run
- funding: HTTPError: 503 Server Error: Service Unavailable for url: https://futures.kraken.com/derivatives/api/v3/tickers

---
_All data from free public endpoints (Kraken, Coinbase, Gemini, CoinGecko). Nothing here is financial advice; flags are conditions to research, not trades to take._
