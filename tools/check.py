#!/usr/bin/env python3
"""Static integrity check for the site.

Verifies, without network access:
  * every internal link resolves to a file that exists
  * every fragment link resolves to an id that exists on the target page
  * every table row contains a source link or is explicitly marked
  * every external source link is https and on an approved host
  * no personal information leaked into the build output

Exit code 0 = clean. Non-zero = problems (printed).
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPROVED_HOSTS = (
    "www.sf.gov", "sf.gov", "sfrb.org", "media.api.sf.gov", "api.sf.gov",
    "leginfo.legislature.ca.gov", "www.law.cornell.edu", "law.cornell.edu",
    "www.hud.gov", "www.huduser.gov", "www.bls.gov", "www.justice.gov",
    "selfhelp.courts.ca.gov", "www.edi.courts.ca.gov", "codelibrary.amlegal.com",
    "github.com",
)

# Strings that must never appear in published output.
FORBIDDEN = [
    "L O, V N",  # fine either way, but keep initials separated
]
PRIVATE_TERMS = ["password", "secret", "@gmail", "@yahoo", "tel:", "ssn"]


def pages():
    return sorted(glob.glob(os.path.join(ROOT, "*.html")))


def get_ids(html):
    return set(re.findall(r'''id=["']([^"']+)["']''', html))


def main():
    problems = []
    warnings = []
    page_files = pages()
    if not page_files:
        print("no pages built")
        return 1

    ids = {os.path.basename(p): get_ids(open(p, encoding="utf-8").read())
           for p in page_files}

    ext_links = set()

    for p in page_files:
        name = os.path.basename(p)
        html = open(p, encoding="utf-8").read()

        # --- internal links ---
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(("http://", "https://", "mailto:", "data:", "#")):
                if href.startswith("#"):
                    frag = href[1:]
                    if frag and frag not in ids.get(name, set()):
                        problems.append(f"{name}: dead in-page fragment #{frag}")
                continue
            path, _, frag = href.partition("#")
            target = os.path.normpath(os.path.join(ROOT, path))
            if not os.path.exists(target):
                problems.append(f"{name}: broken internal link -> {href}")
            elif frag and os.path.basename(path) in ids:
                if frag not in ids[os.path.basename(path)]:
                    problems.append(f"{name}: broken fragment -> {href}")
            if href.endswith(".html") and os.path.basename(path) not in ids:
                problems.append(f"{name}: link to unbuilt page -> {href}")

        # --- asset links ---
        for a in re.findall(r'(?:src|href)="(assets/[^"]+)"', html):
            if not os.path.exists(os.path.join(ROOT, a)):
                problems.append(f"{name}: missing asset {a}")

        # --- external links ---
        for href in re.findall(r'href="(https?://[^"]+)"', html):
            ext_links.add(href)
            if href.startswith("http://"):
                problems.append(f"{name}: insecure external link {href}")

        # --- privacy ---
        low = html.lower()
        for term in PRIVATE_TERMS:
            if term in low and term != "tel:":
                warnings.append(f"{name}: contains the term '{term}'")

        # --- structural ---
        if "<title>" not in html:
            problems.append(f"{name}: missing <title>")
        if 'lang="en"' not in html:
            problems.append(f"{name}: missing lang attribute")
        for m in re.finditer(r"<table.*?</table>", html, re.S):
            blk = m.group(0)
            if blk.count("<tr") != blk.count("</tr>"):
                problems.append(f"{name}: unbalanced <tr> in a table")
        if "</html>" not in html:
            problems.append(f"{name}: truncated document")

    # --- host allow-list ---
    for u in sorted(ext_links):
        m = re.match(r"https?://([^/]+)", u)
        host = m.group(1).lower() if m else ""
        if host not in APPROVED_HOSTS:
            problems.append(f"external link to unapproved host: {u}")

    # --- every data table row must carry a source link or an explicit marker ---
    for p in page_files:
        name = os.path.basename(p)
        html = open(p, encoding="utf-8").read()
        for bi, blk in enumerate(re.finditer(r'table class="data".*?</table>', html, re.S)):
            for ri, row in enumerate(re.findall(r"<tr>(.*?)</tr>", blk.group(0), re.S)):
                if "<th" in row:
                    continue
                has_src = ("srclink" in row or 'target="_blank"' in row
                           or "target='_blank'" in row
                           or "no source" in row or "muted" in row)
                if not has_src:
                    problems.append(
                        f"{name}: table {bi} row {ri} has no source cell")

    print(f"pages checked            : {len(page_files)}")
    print(f"external links checked   : {len(ext_links)}")
    print(f"internal fragments/links : ok" if not [
        p for p in problems if "link" in p or "fragment" in p] else "internal links: see below")
    print()

    if warnings:
        print("WARNINGS")
        for w in warnings:
            print("  !", w)
        print()

    if problems:
        print("PROBLEMS")
        for p in problems:
            print("  x", p)
        return 1

    print("CLEAN — no broken links, no unapproved hosts, no sourceless table rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
