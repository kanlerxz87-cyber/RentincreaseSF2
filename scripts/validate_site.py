#!/usr/bin/env python3
"""Validate static HTML pages, JSON data, and docs before deployment.

Checks:
1. Every required HTML page and style.css exists.
2. Every internal link resolves to an existing file in the repository root.
3. Every external URL is on the verified official-source allowlist.
4. Every table data row (<tr> containing <td>) has at least one official source link.
5. No tenant initials (encoded via hex escapes so no plaintext initials exist here)
   appear in any published HTML, Markdown, or JSON file.
6. Every page links to all sibling pages in navigation and includes the
   not-legal-advice disclaimer.
7. data/verified-data.json parses cleanly as JSON if present.
"""

from __future__ import annotations

import json
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
    "laws.html",
    "process.html",
    "tenant-protections.html",
    "practices.html",
    "flagged.html",
    "sources.html",
]

VERIFIED_URLS = {
    "https://calcivilrights.ca.gov/housing/",
    "https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-16540",
    "https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_admin/0-0-0-70881",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.52",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=51.",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955.",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1013.&lawCode=CCP",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.50.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?chapter=2.7.&division=3.&lawCode=CIV&part=4.&title=5.",
    "https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf",
    "https://media.api.sf.gov/documents/Rent_Board_Annual_Statistical_Report_FY2024-2025.pdf",
    "https://media.api.sf.gov/documents/minutes_040825.pdf",
    "https://oag.ca.gov/rentcaps",
    "https://oag.ca.gov/tenants",
    "https://portal.sfrb.org/",
    "https://sfplanninggis.org/pim/?pub=true",
    "https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap45.htm",
    "https://www.hud.gov/helping-americans/fair-housing-act-overview",
    "https://www.hud.gov/reporthousingdiscrimination",
    "https://www.justice.gov/archives/opa/pr/justice-department-sues-six-large-landlords-algorithmic-pricing-scheme-harms-millions",
    "https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and",
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
    "https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins",
    "https://www.sf.gov/information--sec-373-rent-limitations",
    "https://www.sf.gov/information--special-circumstances-petitions-based-rents-comparable-units",
    "https://www.sf.gov/information--tenant-summary-petitions",
    "https://www.sf.gov/information--utility-passthroughs-gas-electricity-and-steam-heat",
    "https://www.sf.gov/information--water-revenue-bond-passthroughs",
    "https://www.sf.gov/information/legal-resources-housing-discrimination",
    "https://www.sf.gov/information/topic-no-322-operating-and-maintenance-expense-petitions",
    "https://www.sf.gov/landlord-petitions-and-passthroughs",
    "https://www.sf.gov/learn-about-rent-increases-san-francisco",
    "https://www.sf.gov/learn-about-san-francisco-rental-laws",
    "https://www.sf.gov/news--annual-rent-increase-3126-22827-announced",
    "https://www.sf.gov/news--new-law-prohibits-algorithmic-devices-used-set-rents-san-francisco",
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

# Hex-encoded patterns for intake tenant initials so no raw initials exist in repo code.
PERSONAL_PATTERNS = [
    r"\b" + "\x4c" + r"\.?\s*" + "\x4f" + r"\.?\b",
    r"\b" + "\x56" + r"\.?\s*" + "\x4e" + r"\.?\b",
    r"\b" + "\x4a" + r"\.?\s*" + "\x50" + r"\.?\b",
    r"\b" + "\x4d" + r"\.?\s*" + "\x54" + r"\.?\b",
    r"\b" + "\x45" + r"\.?\s*" + "\x52" + r"\.?\b",
    r"\b" + "\x49" + r"\.?\s*" + "\x53" + r"\.?\b",
]


class SiteChecker(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.errors: list[str] = []
        self.links: list[tuple[str, int]] = []
        self.in_table = 0
        self.in_row = False
        self.row_has_td = False
        self.row_links: list[str] = []
        self.row_line = 0
        self.total_data_rows = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "table":
            self.in_table += 1
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.row_has_td = False
            self.row_links = []
            self.row_line = self.getpos()[0]
        elif tag == "td" and self.in_row:
            self.row_has_td = True
        elif tag == "a":
            href = next((value for key, value in attrs if key == "href" and value), "")
            if href:
                self.links.append((href, self.getpos()[0]))
                if self.in_row and (href.startswith("http://") or href.startswith("https://")):
                    self.row_links.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "table" and self.in_table:
            self.in_table -= 1
        elif tag == "tr" and self.in_row:
            if self.row_has_td:
                self.total_data_rows += 1
                if not self.row_links:
                    self.errors.append(
                        f"table row at line {self.row_line} has no official external source link"
                    )
            self.in_row = False


def check_pii_in_text(text: str, relpath: str) -> list[str]:
    errors: list[str] = []
    for idx, pattern in enumerate(PERSONAL_PATTERNS, start=1):
        match = re.search(pattern, text)
        if match:
            errors.append(f"{relpath}: personal identifier pattern #{idx} matched")
    return errors


def check_file(filename: str) -> tuple[int, list[str]]:
    path = os.path.join(ROOT, filename)
    with open(path, "r", encoding="utf-8") as handle:
        html = handle.read()

    checker = SiteChecker()
    checker.feed(html)
    checker.close()

    errors = list(checker.errors)

    for href, line in checker.links:
        if href.startswith("#") or href.startswith(("mailto:", "tel:")):
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

    errors.extend(check_pii_in_text(html, filename))

    link_targets = {href.split("#", 1)[0].split("?", 1)[0] for href, _ in checker.links}
    for page in PAGES:
        if page not in link_targets and page != filename:
            errors.append(f"missing navigation link to {page}")

    if "Not legal advice" not in html:
        errors.append("missing not-legal-advice footer")

    return checker.total_data_rows, errors


def check_repo_docs_and_json() -> list[str]:
    errors: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
        for fname in filenames:
            if not fname.endswith((".md", ".json")):
                continue
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, ROOT)
            with open(full, "r", encoding="utf-8") as handle:
                content = handle.read()
            errors.extend(check_pii_in_text(content, rel))
            if fname.endswith(".json"):
                try:
                    json.loads(content)
                except json.JSONDecodeError as exc:
                    errors.append(f"{rel}: invalid JSON: {exc}")
    return errors


def main() -> int:
    if not os.path.exists(os.path.join(ROOT, "style.css")):
        print("ERROR: style.css missing", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    total_rows = 0
    for page in PAGES:
        if not os.path.exists(os.path.join(ROOT, page)):
            all_errors.append(f"missing page: {page}")
            continue
        rows, errors = check_file(page)
        total_rows += rows
        all_errors.extend(f"{page}: {error}" for error in errors)

    all_errors.extend(check_repo_docs_and_json())

    if all_errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in all_errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    print(f" - {len(PAGES)} HTML pages checked ({total_rows} table data rows)")
    print(f" - {len(VERIFIED_URLS)} official source URLs on allowlist")
    print(" - 100% of table data rows have an official external source link")
    print(" - zero personal identifiers found across HTML, Markdown, and JSON files")
    print(" - all internal links and JSON data files valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
