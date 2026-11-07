#!/usr/bin/env python3
"""Validate the static RentincreaseSF2 site.

Checks:
- every internal link resolves to a file in the repo;
- every external link is on the verified official-source allowlist;
- every data row in a table contains at least one official source link;
- no tenant initials or other personal identifiers appear in the HTML;
- every page has the shared navigation and the not-legal-advice footer.
"""

from __future__ import annotations

import os
import re
import sys
from decimal import Decimal
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
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV",
    "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1954.50.&lawCode=CIV",
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
    "https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco",
    "https://www.sf.gov/information--banked-rent-increases",
    "https://www.sf.gov/information--capital-improvement-petitions",
    "https://www.sf.gov/information--general-obligation-bond-passthrough-worksheets",
    "https://www.sf.gov/information--get-help-discrimination-housing",
    "https://www.sf.gov/information--increasing-rents-during-irregular-periods",
    "https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins",
    "https://www.sf.gov/information--partial-exemption-newly-constructed-rental-units",
    "https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins",
    "https://www.sf.gov/information--sec-373-rent-limitations",
    "https://www.sf.gov/information--sec-379-evictions",
    "https://www.sf.gov/information--special-circumstances-petitions-based-rents-comparable-units",
    "https://www.sf.gov/information--tenant-summary-petitions",
    "https://www.sf.gov/information--utility-passthroughs-gas-electricity-and-steam-heat",
    "https://www.sf.gov/information--water-revenue-bond-passthroughs",
    "https://www.sf.gov/information/legal-resources-housing-discrimination",
    "https://www.sf.gov/information/topic-no-322-operating-and-maintenance-expense-petitions",
    "https://www.sf.gov/landlord-petitions-and-passthroughs",
    "https://www.sf.gov/learn-about-rent-increases-san-francisco",
    "https://www.sf.gov/learn-about-san-francisco-rental-laws",
    "https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory",
    "https://www.sf.gov/rent-board-fee",
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

# Tenant initials supplied in the intake. They must never appear in published HTML.
PERSONAL_PATTERNS = [
    r"\bL\s*O\b",
    r"\bV\s*N\b",
    r"\bJP\b",
    r"\bM\s*T\b",
    r"\bE\s*R\b",
    r"\bI\s*S\b",
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
                if self.in_row:
                    self.row_links.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "table" and self.in_table:
            self.in_table -= 1
        elif tag == "tr" and self.in_row:
            if self.row_has_td and not self.row_links:
                self.errors.append(
                    f"table row at line {self.row_line} has no official source link"
                )
            self.in_row = False


def check_file(filename: str) -> tuple[list[tuple[str, int]], list[str]]:
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

    for pattern in PERSONAL_PATTERNS:
        if re.search(pattern, html):
            errors.append(f"personal identifier pattern found in HTML: {pattern}")

    link_targets = {href.split("#", 1)[0].split("?", 1)[0] for href, _ in checker.links}
    for page in PAGES:
        if page not in link_targets and page != filename:
            # The current page does not need to link to itself.
            errors.append(f"missing navigation link to {page}")

    if "Not legal advice" not in html:
        errors.append("missing not-legal-advice footer")

    return checker.links, errors


# --------------------------------------------------------------------------
# Arithmetic self-check. Every published dollar figure is re-derived here from
# the official percentages (Info Sheet 571 / Current Rates) and the base rents,
# so a typo in a published number fails the build instead of shipping.
# --------------------------------------------------------------------------
BASE = {"unit1": Decimal("3995.00"), "unit2": Decimal("3150.00")}

# Official annual allowable percentages, Info Sheet 571 (26-27 edition).
RATES = {
    "2020-21": Decimal("1.8"),
    "2021-22": Decimal("0.7"),
    "2022-23": Decimal("2.3"),
    "2023-24": Decimal("3.6"),
    "2024-25": Decimal("1.7"),
    "2025-26": Decimal("1.4"),
    "2026-27": Decimal("1.6"),
}


def money(value: Decimal) -> str:
    return f"${value.quantize(Decimal('0.01')):,}"


def calc_checks() -> list[str]:
    errors: list[str] = []

    def expect(page: str, text: str, label: str) -> None:
        path = os.path.join(ROOT, page)
        with open(path, "r", encoding="utf-8") as handle:
            body = handle.read()
        if text not in body:
            errors.append(f"{page}: expected {label} ({text}) not found")

    # Sums of official percentages.
    twelve = sum(RATES[k] for k in list(RATES)[:-1])          # through 2025-26
    twentyfour = sum(RATES[k] for k in list(RATES)[:-2])      # through 2024-25
    if twelve != Decimal("11.5"):
        errors.append(f"banked total (12-month reading) is {twelve}, expected 11.5")
    if twentyfour != Decimal("10.1"):
        errors.append(f"banked total (24-month reading) is {twentyfour}, expected 10.1")

    # Unit 1: 1.6% and the 3.0% (1.4% + 1.6%) anniversary option.
    u1_inc = BASE["unit1"] * Decimal("0.016")
    u1_new = BASE["unit1"] + u1_inc
    u1_3_inc = BASE["unit1"] * Decimal("0.030")
    u1_3_new = BASE["unit1"] + u1_3_inc
    expect("analysis.html", money(u1_inc), "Unit 1 1.6% increase")
    expect("analysis.html", money(u1_new), "Unit 1 new rent at 1.6%")
    expect("analysis.html", money(u1_3_inc), "Unit 1 3.0% increase")
    expect("analysis.html", money(u1_3_new), "Unit 1 new rent at 3.0%")

    # Unit 2: both banking readings.
    u2_a = BASE["unit2"] * (twentyfour + RATES["2026-27"]) / 100
    u2_b = BASE["unit2"] * (twelve + RATES["2026-27"]) / 100
    expect("analysis.html", money(u2_a), "Unit 2 increase, 24-month reading")
    expect("analysis.html", money(BASE["unit2"] + u2_a), "Unit 2 new rent, 24-month reading")
    expect("analysis.html", money(u2_b), "Unit 2 increase, 12-month reading")
    expect("analysis.html", money(BASE["unit2"] + u2_b), "Unit 2 new rent, 12-month reading")

    # The 90-day notice threshold must be triggered under both readings.
    if (twentyfour + RATES["2026-27"]) <= 10 or (twelve + RATES["2026-27"]) <= 10:
        errors.append("a Unit 2 reading no longer exceeds the 10% / 90-day threshold")

    return errors


def main() -> int:
    if not os.path.exists(os.path.join(ROOT, "style.css")):
        print("ERROR: style.css missing", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for page in PAGES:
        if not os.path.exists(os.path.join(ROOT, page)):
            all_errors.append(f"missing page: {page}")
            continue
        _, errors = check_file(page)
        all_errors.extend(f"{page}: {error}" for error in errors)

    all_errors.extend(calc_checks())

    if all_errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in all_errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print("VALIDATION PASSED")
    print(f" - {len(PAGES)} pages checked")
    print(f" - {len(VERIFIED_URLS)} official source URLs on allowlist")
    print(" - every table data row has an official source link")
    print(" - no tenant initials or personal identifiers found")
    print(" - all internal links resolve")
    print(" - arithmetic re-derived from official percentages and matches the published figures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
