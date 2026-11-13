#!/usr/bin/env python3
"""Validate the static RentincreaseSF2 site.

Checks:
- every internal link resolves to a file in the repo;
- every external link is on the verified official-source allowlist;
- every data row in a table contains at least one official source link;
- public text files contain no privately supplied identifier patterns or merge markers;
- every page has the shared navigation and the not-legal-advice footer.
"""

from __future__ import annotations

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = [
    "index.html",
    "executive-summary.html",
    "units.html",
    "analysis.html",
    "occupancy.html",
    "laws.html",
    "process.html",
    "tenant-protections.html",
    "practices.html",
    "checklist.html",
    "answers.html",
    "suggestions.html",
    "flagged.html",
    "sources.html",
    "banking-rule.html",
]

VERIFIED_URLS = {
    "https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770",
    "https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E",
    "https://sfgov.legistar.com/View.ashx?M=F&ID=15865647&GUID=CC09B796-4675-4A7D-9960-85FE239F7FBB",
    "https://sfrb.org/section-1314-licensing-%E2%80%93-notice-rent-increase",
    "https://www.sf.gov/documents/64370/538_2026-2027_Bond_Measure_Worksheet_10.26.pdf",
    "https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins",
    "https://www.sf.gov/information--charging-additional-occupants-prohibited",
    "https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV",
    "https://calcivilrights.ca.gov/housing/",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.50.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.52.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV",
    "https://portal.sfrb.org/",
    "https://sfplanninggis.org/pim/?pub=true",
    "https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm",
    "https://www.hud.gov/reporthousingdiscrimination",
    "https://www.sf.gov/departments--rent-board",
    "https://www.sf.gov/departments--rent-board--about",
    "https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf",
    "https://www.sf.gov/evictions-san-francisco",
    "https://www.sf.gov/information--annual-rent-increase-multiple-years",
    "https://www.sf.gov/information--banked-rent-increases",
    "https://www.sf.gov/information--capital-improvement-petitions",
    "https://www.sf.gov/information--general-obligation-bond-passthrough-worksheets",
    "https://www.sf.gov/information--get-help-discrimination-housing",
    "https://www.sf.gov/information--increasing-rents-during-irregular-periods",
    "https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins",
    "https://www.sf.gov/information--partial-exemption-newly-constructed-rental-units",
    "https://www.sf.gov/information--sec-3710b-tenant-harassment",
    "https://www.sf.gov/information--sec-3711a-civil-actions",
    "https://www.sf.gov/information--sec-373-rent-limitations",
    "https://www.sf.gov/information--sec-3715-reporting-obligations-licensing",
    "https://www.sf.gov/information--special-circumstances-petitions-based-rents-comparable-units",
    "https://www.sf.gov/information--tenant-summary-petitions",
    "https://www.sf.gov/information--utility-passthroughs-gas-electricity-and-steam-heat",
    "https://www.sf.gov/information--water-revenue-bond-passthroughs",
    "https://www.sf.gov/information/legal-resources-housing-discrimination",
    "https://www.sf.gov/information--operating-and-maintenance-expense-petitions",
    "https://www.sf.gov/landlord-petitions-and-passthroughs",
    "https://www.sf.gov/learn-about-rent-increases-san-francisco",
    "https://www.sf.gov/learn-about-san-francisco-rental-laws",
    "https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory",
    "https://www.sf.gov/rent-board-fee",
    "https://www.sf.gov/rent-board-forms-forms-center",
    "https://www.sf.gov/rent-board-housing-inventory",
    "https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482",
    "https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit",
    "https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring",
    "https://www.sf.gov/reports--rent-ordinance",
    "https://www.sf.gov/speak-rent-board-counselor",
    "https://www.sf.gov/tenant-and-landlord-resources",
    "https://www.sf.gov/tenant-petitions",
    "https://www.sfassessor.org/property-information/homeowners/property-search-tool",
}

# Optional privacy patterns may be supplied privately by a reviewer, one regex per
# line. No tenant-specific identifier is embedded in this public repository.
PRIVATE_PATTERNS = [
    pattern for pattern in os.environ.get("PRIVATE_IDENTIFIER_PATTERNS", "").splitlines()
    if pattern.strip()
]
PUBLIC_TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".json", ".md", ".py", ".txt", ".yaml", ".yml",
}
MERGE_MARKERS = ("<<<<<<< ", "=======", ">>>>>>> ")



VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


class SiteChecker(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.errors: list[str] = []
        self.links: list[tuple[str, int]] = []
        self.ids: set[str] = set()
        self.in_table = 0
        self.in_row = False
        self.row_has_td = False
        self.row_links: list[str] = []
        self.row_line = 0
        self.header_cols = 0
        self.expected_cols: list[int] = []
        self.row_cells = 0
        self.tag_stack: list[tuple[str, int]] = []
        self.in_head = False
        self.head_text_allowed = 0
        self.has_meta_description = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        element_id = next((value for key, value in attrs if key == "id" and value), "")
        if element_id:
            if element_id in self.ids:
                self.errors.append(f"line {self.getpos()[0]}: duplicate id: {element_id}")
            self.ids.add(element_id)
        if tag not in VOID_TAGS:
            self.tag_stack.append((tag, self.getpos()[0]))
        if tag == "head":
            self.in_head = True
        elif self.in_head and tag in ("title", "style", "script"):
            self.head_text_allowed += 1
        elif tag == "meta":
            attr_map = {k.lower(): (v or "") for k, v in attrs}
            if attr_map.get("name", "").lower() == "description":
                if not attr_map.get("content", "").strip():
                    self.errors.append(
                        f"line {self.getpos()[0]}: <meta name=\"description\"> missing non-empty content attribute"
                    )
                else:
                    self.has_meta_description = True
        if tag == "table":
            self.in_table += 1
            self.header_cols = 0
            self.expected_cols.append(0)
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.row_has_td = False
            self.row_links = []
            self.row_cells = 0
            self.row_line = self.getpos()[0]
        elif tag == "th" and self.in_row:
            self.header_cols += 1
        elif tag == "td" and self.in_row:
            self.row_has_td = True
            span = next((v for k, v in attrs if k == "colspan" and v), "1")
            self.row_cells += int(span) if span.isdigit() else 1
        elif tag == "a":
            href = next((value for key, value in attrs if key == "href" and value), "")
            if href:
                self.links.append((href, self.getpos()[0]))
                if self.in_row:
                    self.row_links.append(href)

    def handle_data(self, data: str) -> None:
        if self.in_head and not self.head_text_allowed and data.strip():
            self.errors.append(
                f"line {self.getpos()[0]}: unexpected text inside <head>: {data.strip()[:60]!r}"
            )

    def handle_endtag(self, tag: str) -> None:
        if tag not in VOID_TAGS:
            if not self.tag_stack:
                self.errors.append(f"line {self.getpos()[0]}: unexpected closing </{tag}>")
            elif self.tag_stack[-1][0] != tag:
                open_tag, open_line = self.tag_stack[-1]
                self.errors.append(
                    f"line {self.getpos()[0]}: closing </{tag}> mismatches <{open_tag}> from line {open_line}"
                )
            else:
                self.tag_stack.pop()
        if tag == "head":
            self.in_head = False
        elif self.in_head and tag in ("title", "style", "script") and self.head_text_allowed:
            self.head_text_allowed -= 1
        if tag == "table" and self.in_table:
            self.in_table -= 1
            self.expected_cols.pop()
            self.header_cols = self.expected_cols[-1] if self.expected_cols else 0
        elif tag == "tr" and self.in_row:
            if self.row_has_td and not any(
                href.startswith(("https://", "http://")) for href in self.row_links
            ):
                self.errors.append(
                    f"table row at line {self.row_line} has no external official source link"
                )
            if self.row_has_td and self.header_cols and self.row_cells != self.header_cols:
                self.errors.append(
                    f"table row at line {self.row_line} has {self.row_cells} cells, "
                    f"header declares {self.header_cols}"
                )
            if not self.row_has_td and self.header_cols:
                self.expected_cols[-1] = self.header_cols
            self.in_row = False

    def close(self) -> None:
        super().close()
        for tag, line in self.tag_stack:
            self.errors.append(f"line {line}: unclosed <{tag}>")
        if not self.has_meta_description:
            self.errors.append("missing valid <meta name=\"description\" content=\"...\">")


def check_file(filename: str) -> tuple[list[tuple[str, int]], list[str], set[str]]:
    path = os.path.join(ROOT, filename)
    with open(path, "r", encoding="utf-8") as handle:
        html = handle.read()

    checker = SiteChecker()
    checker.feed(html)
    checker.close()

    errors = list(checker.errors)

    for href, line in checker.links:
        if href.startswith("#"):
            continue
        if href.startswith(("mailto:", "tel:")):
            continue
        if href.startswith("http://") or href.startswith("https://"):
            if href not in VERIFIED_URLS:
                errors.append(f"line {line}: external URL not on verified allowlist: {href}")
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if not target:
            target = "index.html"
        if not os.path.exists(os.path.join(ROOT, target)):
            errors.append(f"line {line}: broken internal link: {href}")

    for pattern in PRIVATE_PATTERNS:
        if re.search(pattern, html):
            errors.append("privately supplied identifier pattern found in HTML")

    link_targets = {href.split("#", 1)[0].split("?", 1)[0] for href, _ in checker.links}
    for page in PAGES:
        if page not in link_targets and page != filename:
            # The current page does not need to link to itself.
            errors.append(f"missing navigation link to {page}")

    if "Not legal advice" not in html:
        errors.append("missing not-legal-advice footer")

    return checker.links, errors, checker.ids


def main() -> int:
    if not os.path.exists(os.path.join(ROOT, "style.css")):
        print("ERROR: style.css missing", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    sources_external_links: set[str] = set()
    page_links: dict[str, list[tuple[str, int]]] = {}
    page_ids: dict[str, set[str]] = {}
    for page in PAGES:
        if not os.path.exists(os.path.join(ROOT, page)):
            all_errors.append(f"missing page: {page}")
            continue
        links, errors, ids = check_file(page)
        page_links[page] = links
        page_ids[page] = ids
        if page == "sources.html":
            sources_external_links = {
                href for href, _ in links
                if href.startswith("http://") or href.startswith("https://")
            }
        all_errors.extend(f"{page}: {error}" for error in errors)

    for source, links in page_links.items():
        for href, line in links:
            if "#" not in href or href.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            target, fragment = href.split("#", 1)
            target = target.split("?", 1)[0] or source
            if target in page_ids and fragment not in page_ids[target]:
                all_errors.append(
                    f"{source}: line {line}: unresolved fragment {fragment!r} in {target}"
                )

    for url in sorted(VERIFIED_URLS - sources_external_links):
        all_errors.append(f"sources.html: missing allowlisted official URL: {url}")

    # GitHub Pages serves the repository root. Check every public text file, not
    # only HTML/Markdown: a script or audit example can leak identifiers too.
    public_paths = set()
    for directory, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in {".git", "__pycache__"}]
        for filename in filenames:
            path = os.path.join(directory, filename)
            if os.path.splitext(filename)[1] in PUBLIC_TEXT_SUFFIXES:
                public_paths.add(path)
    for path in sorted(public_paths):
        doc = os.path.relpath(path, ROOT)
        with open(path, "r", encoding="utf-8") as handle:
            body = handle.read()
        for marker in MERGE_MARKERS:
            if any(line.startswith(marker) for line in body.splitlines()):
                all_errors.append(f"{doc}: unresolved merge conflict marker: {marker}")
        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, body):
                all_errors.append(
                    f"{doc}: privately supplied identifier pattern found in a public file"
                )

    if all_errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in all_errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    print(f" - {len(PAGES)} pages checked (HTML tag balance & <head>/<meta> valid)")
    print(f" - {len(VERIFIED_URLS)} official source URLs on allowlist (all listed on sources.html)")
    print(" - every table data row has an external official source link")
    print(f" - {len(PRIVATE_PATTERNS)} optional private patterns configured; all public text files scanned")
    print(" - no unresolved merge-conflict markers in public text files")
    print(" - all internal links and fragments resolve; element IDs are unique")
    print(" - every table row matches its header column count")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
