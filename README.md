# news-image-20261125 — The World in One Image

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/goperek48/newsimg25-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/goperek48/newsimg25-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A program that writes one 1024x1024 PNG summing up Wednesday 25 November 2026
world news — a newspaper front page.

- `main.py` — the entrypoint (Python 3.13, standard library only, no network).
  It copies `entry.png` to `/output/entry.png` and verifies the copy: whole PNG,
  at most 1 MiB, at most 1024x1024, byte-identical to the source. Fully
  deterministic: every run produces the exact same bytes.
- `entry.png` — the image (808,272 bytes, 1024x1024).

## The image

A front page headed **WEDNESDAY 25 NOVEMBER 2026**, built from three generated
news photographs with headlines and captions drawn in crisp type:

1. **Lead — Ukraine sinks Russian warship off Libya.** President Zelenskyy
   confirms a sea-drone strike sank a Russian warship in Benghazi harbour,
   and a hit on a Russian cargo ship in the Gulf of Finland.
2. **Riyadh — Houthis hit Riyadh's tallest tower; 11 hurt.** Second drone
   strike on the PIF Tower in under a week, Saudi civil defence says.
3. **Washington — Trump gives Giuliani the Medal of Freedom.** The president
   honours his former lawyer at a White House ceremony.

Footer, also today: the CIA/ODNI cyber breach, NATO early-warning jets for
Poland, a migrant boat capsizing off Senegal (four dead), the UN court
condemning Myanmar over the Rohingya, Waymo pulling driverless taxis from US
freeways, and Seoul's education minister quitting in an exam scandal.

Stories verified against Reuters and other news summaries of 25 November 2026.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
