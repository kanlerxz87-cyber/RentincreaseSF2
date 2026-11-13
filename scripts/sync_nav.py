#!/usr/bin/env python3
"""Render one canonical sidebar navigation into every page of the site.

The validator requires every page to link to every other page. Keeping the nav in
one place removes the chance of a broken or drifting link when a page is added.

Run:  python3 scripts/sync_nav.py
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LAST_VERIFIED = "2026-11-13"

# (group label, [(file, link text), ...])
NAV = [
    ("Overview", [
        ("index.html", "Dashboard"),
        ("executive-summary.html", "Executive Summary"),
    ]),
    ("Units &amp; Analysis", [
        ("units.html", "Units (Anonymized)"),
        ("analysis.html", "Increase Analysis"),
        ("occupancy.html", "Occupancy &amp; Roommates"),
    ]),
    ("Legal &amp; Process", [
        ("laws.html", "Laws &amp; Regulations"),
        ("process.html", "Notice &amp; Process"),
        ("tenant-protections.html", "Tenant Protections"),
        ("practices.html", "Owner Practices"),
    ]),
    ("Action", [
        ("checklist.html", "Action Checklist"),
        ("answers.html", "Your Questions"),
    ]),
    ("Review", [
        ("flagged.html", "Flagged for Review"),
        ("sources.html", "Sources"),
    ]),
    ("Verification", [
        ("banking-rule.html", "Banking Interval (F-16)"),
    ]),
]

PAGES = [f for _, items in NAV for f, _ in items]


def render_nav(active: str) -> str:
    out = [
        "<nav>",
        "  <h1>Rental Increase Review</h1>",
        f'  <div class="sub">San Francisco &middot; Outer Sunset 94122<br>Last verified: {LAST_VERIFIED}</div>',
    ]
    for group, items in NAV:
        out.append(f'  <div class="nav-group">{group}</div>')
        for filename, text in items:
            cls = ' class="active"' if filename == active else ""
            out.append(f'  <a href="{filename}"{cls}>{text}</a>')
    out.append("</nav>")
    return "\n".join(out)


def main() -> int:
    changed = []
    for page in PAGES:
        path = os.path.join(ROOT, page)
        if not os.path.exists(path):
            print(f"ERROR: missing page {page}", file=sys.stderr)
            return 1
        with open(path, "r", encoding="utf-8") as handle:
            html = handle.read()
        new_html, count = re.subn(r"<nav>.*?</nav>", lambda m: render_nav(page), html, flags=re.S)
        if count != 1:
            print(f"ERROR: {page} has {count} <nav> blocks, expected 1", file=sys.stderr)
            return 1
        # Keep the footer stamp in step with the nav stamp.
        new_html = re.sub(r"Last verified: \d{4}-\d{2}-\d{2}", f"Last verified: {LAST_VERIFIED}", new_html)
        if new_html != html:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(new_html)
            changed.append(page)
    print(f"NAV OK - {len(PAGES)} pages, {len(changed)} updated")
    for page in changed:
        print(f"  updated {page}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
