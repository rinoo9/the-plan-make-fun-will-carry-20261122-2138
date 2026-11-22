#!/usr/bin/env python3
"""Generate entry.txt: a 30-day plan for an AI agent to turn $100 into as
much money as possible by selling SEO product-description writing to pet
stores on Shopify.

Standard library only. No network access. Deterministic: every run writes
byte-identical output.
"""

import hashlib
import os
import sys

ENTRY_TEXT = (
    "Day 1-3: rewrite 10 SEO descriptions free for 3 pet Shopify stores; "
    "list '$49: 10 SEO descriptions in 24h' on Fiverr/Contra/Upwork. "
    "Days 4-30: DM 100 pet stores daily, close 2/day at $49 via Stripe, "
    "draft with Claude. ~$2,000 by day 30. "
    "No replies? Follow up, offer a $19 trial."
)

MAX_CHARS = 280


def validate_entry(text: str) -> None:
    """ENTRY_TEXT must be 1-280 Unicode characters, not blank, valid UTF-8."""
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line, no newlines")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    validate_entry(ENTRY_TEXT)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = ENTRY_TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path}: {len(ENTRY_TEXT)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
