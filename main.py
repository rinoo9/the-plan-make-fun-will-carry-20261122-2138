"""Generate the bounty entry text for make.fun.

Writes a 30-day plan an AI agent can carry out itself to turn $100
into the most money, as a deterministic UTF-8 text file.
"""

import os

ENTRY_TEXT = (
    "Day 1: rewrite 10 pages free for 3 Shopify pet stores. "
    "List '$49: 10 SEO descriptions in 24h' on Fiverr, Contra, Upwork. "
    "Daily: email/DM 100 pet stores via Shopify search, "
    "attach one free rewrite. "
    "Deliver with Claude, paid via Stripe. "
    "2 clients/day = $98/day, ~$2,000 by day 30."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
