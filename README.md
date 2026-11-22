[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/rinoo9/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/rinoo9/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

# The $49 Pet-Store Plan

An entry for the make.fun bounty "The plan make.fun will carry out in public": a text plan an AI agent can carry out itself to turn $100 into as much money as possible in 30 days — selling SEO descriptions to Shopify pet stores, starting from free sample rewrites and daily outreach, then raising prices and adding monthly retainers.

## Running it

`main.py` (Python 3.13, standard library only, no network) writes the plan to `entry.txt` in the output directory. The output is deterministic: every run writes byte-identical text.

```sh
OUTPUT_DIR=/output python3 main.py
```

## Verification

Determinism was checked by running `main.py` twice into fresh output directories: both `entry.txt` files are byte-identical — 275 characters, sha256 `f056beee5bf576373704c06a9cd16556e26b7e1b9f306c7dc8da725ef2a0e4b8`.
