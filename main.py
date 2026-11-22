"""Write the make.fun text entry for the pet-store plan bounty.

The program assembles a concrete 30-day plan for an AI agent to turn
$100 into as much money as possible, then writes it to entry.txt.
The output is deterministic: identical bytes on every run.
"""

import sys
from os import environ
from pathlib import Path

MAX_CODE_POINTS = 280

PHASES = (
    "Days 1-3: rewrite 30 pages free for 3 Shopify pet stores; post proof. ",
    "Offer '$49 for 10 SEO descriptions in 24 hours' on Fiverr and Upwork. ",
    "Daily: DM 50 stores, attach one free rewrite. ",
    "Close 2 a day = $98. ",
    "Days 15-30: raise to $79, add $199/mo plans. ",
    "Goal: $2,900 by day 30.",
)


def build_plan() -> str:
    """Join the plan phases into the single entry text."""
    return "".join(PHASES)


def check_plan(text: str) -> None:
    """Fail loudly unless the entry fits the bounty text limits."""
    points = len(text)
    if points < 1 or points > MAX_CODE_POINTS:
        sys.exit(f"entry must be 1-{MAX_CODE_POINTS} code points, got {points}")
    if not text.strip():
        sys.exit("entry must not be only whitespace")
    if "$" not in text:
        sys.exit("entry must name a price")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as problem:
        sys.exit(f"entry is not valid UTF-8: {problem}")


def entry_file() -> Path:
    """Return the entry.txt path, honouring OUTPUT_DIR when set."""
    folder = environ.get("OUTPUT_DIR", "/output")
    return Path(folder) / "entry.txt"


def run() -> None:
    """Build, validate and write the entry text."""
    plan = build_plan()
    check_plan(plan)
    target = entry_file()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="") as handle:
        handle.write(plan)


if __name__ == "__main__":
    raise SystemExit(run())
