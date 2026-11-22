[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/rinoo9/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/rinoo9/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

# The $49 Pet-Store Plan

An AI agent turns $100 into as much money as possible in 30 days by selling
SEO product-description writing to pet stores on Shopify.

The plan: days 1-3, rewrite 10 SEO descriptions free for 3 pet stores as
samples and list a "$49: 10 SEO descriptions in 24h" offer on
Fiverr/Contra/Upwork. Days 4-30, email/DM 100 pet stores a day, close
2 clients a day at $49 paid via Stripe, and draft the descriptions with
Claude — about $98 a day, roughly $2,000 by day 30. If nobody replies,
follow up once, then offer a cheaper $19 5-description trial.

## How it works

`main.py` (Python 3.13, standard library only, no network) holds the plan as
`ENTRY_TEXT`, validates it (1-280 Unicode characters, not blank, valid
UTF-8, single line), and writes it to `entry.txt` inside `$OUTPUT_DIR`
(default `/output`). Every run produces byte-identical output.

## Run

```sh
OUTPUT_DIR=/output python3 main.py
```

## Verification

Measured by running `main.py` twice into two fresh output directories and
comparing the results:

- Entry length: 278 characters (limit 280)
- `entry.txt` sha256: `e2bb7ccb1620693171c9cfbd0935e9f4486b453cf211d1fa361ee7f19bff9ac1`
- Both runs byte-identical: yes
