#!/usr/bin/env python3
"""Re-derive every published dollar amount and notice deadline from official inputs.

Nothing on the site is typed by hand that could be computed instead. This script
recomputes the figures from the Rent Board's published percentages and the
statutory notice periods, then asserts that each computed string actually appears
in the published HTML. It fails loudly if the site and the arithmetic drift apart.

Official inputs:
  * Allowable annual percentages - SF Rent Board Info Sheet 571 (26-27)
    https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf
  * Banking mechanics - https://www.sf.gov/information--banked-rent-increases
    and Rules 4.12 (12 full months from when the increase could have been imposed)
  * Notice periods - Civil Code 827(b)(2) and (b)(3)(A); +5 days if mailed per
    https://www.sf.gov/learn-about-rent-increases-san-francisco

Run:  python3 scripts/verify_calculations.py
"""

from __future__ import annotations

import os
import re
import sys
from datetime import date, timedelta
from decimal import Decimal, ROUND_DOWN

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REVIEW_DATE = date(2026, 11, 10)

# SF Rent Board Info Sheet 571: percentage in effect on each 1 June / 1 February.
RATE_571 = {
    "2019-03-01": Decimal("2.6"),
    "2020-03-01": Decimal("1.8"),
    "2021-03-01": Decimal("0.7"),
    "2022-03-01": Decimal("2.3"),
    "2023-03-01": Decimal("3.6"),
    "2024-03-01": Decimal("1.7"),
    "2025-03-01": Decimal("1.4"),
    "2026-03-01": Decimal("1.6"),
}

UNIT1_BASE = Decimal("3995.00")
UNIT2_BASE = Decimal("3150.00")

errors: list[str] = []
checks = 0


def money(value: Decimal) -> Decimal:
    """Rent Board rule: increases are not rounded up."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_DOWN)


def usd(value: Decimal) -> str:
    return f"${value:,.2f}"


def rate_on(day: date) -> Decimal:
    """The percentage in effect on a given date, per the 571 table."""
    applicable = [d for d in RATE_571 if date.fromisoformat(d) <= day]
    if not applicable:
        raise ValueError(f"no published rate for {day}")
    return RATE_571[max(applicable)]


def banks_on(available: date) -> date:
    """Rules 4.12: a full 12 months must elapse from when it could be imposed."""
    return date(available.year + 1, available.month, available.day)


def expect_in_pages(label: str, needle: str, pages: list[str]) -> None:
    global checks
    checks += 1
    for page in pages:
        with open(os.path.join(ROOT, page), "r", encoding="utf-8") as handle:
            body = handle.read()
        if needle not in body:
            errors.append(f"{label}: computed value {needle!r} not found in {page}")


def expect(label: str, actual, expected) -> None:
    global checks
    checks += 1
    if actual != expected:
        errors.append(f"{label}: computed {actual!r}, site declares {expected!r}")


def main() -> int:
    global checks

    # ------------- Base-date consistency -------------
    # Every page is stamped "Last verified: <LAST_VERIFIED>" by sync_nav.py. If that
    # stamp and REVIEW_DATE disagree, the published day counts are wrong by the
    # difference. The two are asserted against each other on every run.
    with open(os.path.join(ROOT, "scripts", "sync_nav.py"), encoding="utf-8") as handle:
        stamp = re.search(r'LAST_VERIFIED\s*=\s*"(\d{4}-\d{2}-\d{2})"', handle.read())
    if not stamp:
        errors.append("base date: could not read LAST_VERIFIED from scripts/sync_nav.py")
    else:
        expect("nav stamp equals the calculation base date",
               date.fromisoformat(stamp.group(1)), REVIEW_DATE)

    # ---------------- Unit 1 ----------------
    # Tenancy 2025-02-01, never increased. First allowance available 2026-02-01.
    u1_available = date(2026, 2, 1)
    u1_skipped = rate_on(u1_available)                       # 1.4%
    expect("Unit 1 skipped allowance", u1_skipped, Decimal("1.4"))
    expect("Unit 1 banks on", banks_on(u1_available), date(2027, 2, 1))

    u1_anniversary = date(2027, 2, 1)
    u1_current = rate_on(u1_anniversary)                     # 1.6%
    u1_total = u1_skipped + u1_current                       # 3.0%
    expect("Unit 1 total percent", u1_total, Decimal("3.0"))

    u1_inc = money(UNIT1_BASE * u1_total / 100)
    u1_new = UNIT1_BASE + u1_inc
    expect("Unit 1 increase", u1_inc, Decimal("119.85"))
    expect("Unit 1 new rent", u1_new, Decimal("4114.85"))

    # Early scenario: only the current allowance, the skipped 1.4% is lost.
    u1_early_inc = money(UNIT1_BASE * u1_current / 100)
    expect("Unit 1 early increase", u1_early_inc, Decimal("63.92"))
    expect("Unit 1 early new rent", UNIT1_BASE + u1_early_inc, Decimal("4058.92"))

    # 3.0% <= 10% -> 30 days, +5 if mailed.
    u1_serve = u1_anniversary - timedelta(days=30)
    u1_serve_mail = u1_anniversary - timedelta(days=35)
    expect("Unit 1 serve by", u1_serve, date(2027, 1, 2))
    expect("Unit 1 serve by mail", u1_serve_mail, date(2026, 12, 28))

    # ---------------- Unit 2 ----------------
    # Tenancy 2019-06-01, assumed never increased. Anniversary 1 June.
    banked_components = []
    for year in range(2020, 2027):
        available = date(year, 6, 1)
        pct = rate_on(available)
        if banks_on(available) <= REVIEW_DATE:
            banked_components.append((available, pct))
    u2_banked = sum((p for _, p in banked_components), Decimal("0"))
    expect("Unit 2 banked components", len(banked_components), 6)
    expect("Unit 2 banked percent", u2_banked, Decimal("11.5"))
    expect("Unit 2 2026 allowance not yet banked", banks_on(date(2026, 6, 1)) > REVIEW_DATE, True)

    u2_effective = date(2027, 2, 15)
    u2_current = rate_on(u2_effective)                       # 1.6%, expires 2027-02-28
    u2_total = u2_banked + u2_current                        # 13.1%
    expect("Unit 2 total percent", u2_total, Decimal("13.1"))

    u2_inc = money(UNIT2_BASE * u2_total / 100)
    expect("Unit 2 increase", u2_inc, Decimal("412.65"))
    expect("Unit 2 new rent", UNIT2_BASE + u2_inc, Decimal("3562.65"))

    # 13.1% > 10% -> 90 days, +5 if mailed.
    u2_serve = u2_effective - timedelta(days=90)
    u2_serve_mail = u2_effective - timedelta(days=95)
    expect("Unit 2 serve by", u2_serve, date(2026, 11, 17))
    expect("Unit 2 serve by mail", u2_serve_mail, date(2026, 11, 12))
    expect("Unit 2 earliest effective if served today", REVIEW_DATE + timedelta(days=90), date(2027, 2, 8))
    expect("Unit 2 earliest effective if mailed today", REVIEW_DATE + timedelta(days=95), date(2027, 2, 13))
    # The closing window: the last date ANY effective date inside the published-rate
    # window (which ends 2027-02-28) can still be served for.
    expect("Unit 2 last day to serve for 2027-02-28", date(2027, 2, 28) - timedelta(days=90), date(2026, 11, 30))
    expect("Unit 2 last day to serve for 2027-02-28 (mailed)", date(2027, 2, 28) - timedelta(days=95), date(2026, 11, 25))

    # Phased alternative: 10.0% now, remainder stays banked, 30-day notice.
    u2_phase_pct = Decimal("10.0")
    u2_phase_inc = money(UNIT2_BASE * u2_phase_pct / 100)
    expect("Unit 2 phased increase", u2_phase_inc, Decimal("315.00"))
    expect("Unit 2 phased new rent", UNIT2_BASE + u2_phase_inc, Decimal("3465.00"))
    expect("Unit 2 remainder banked", u2_total - u2_phase_pct, Decimal("3.1"))
    expect("Unit 2 phased serve by", u2_effective - timedelta(days=30), date(2027, 1, 16))
    expect("Unit 2 phased serve by mail", u2_effective - timedelta(days=35), date(2027, 1, 11))

    # Anniversary alternative.
    u2_anniversary = date(2027, 6, 1)
    expect("Unit 2 anniversary serve by", u2_anniversary - timedelta(days=90), date(2027, 3, 3))
    expect("Unit 2 anniversary serve by mail", u2_anniversary - timedelta(days=95), date(2027, 2, 26))

    # Proposed ordinance File No. 261020 (flag F-27). NOT law. If enacted as proposed it would
    # cap the banked + capital-improvement components at 10%/year; the annual allowance is not
    # in that list, so the ceiling would be 10% + 1.6% = 11.6%. Published only as a labelled
    # conditional on flagged.html.
    u2_proposed_pct = Decimal("10.0") + u2_current
    expect("Proposed-cap conditional percent", u2_proposed_pct, Decimal("11.6"))
    u2_proposed_inc = money(UNIT2_BASE * u2_proposed_pct / 100)
    expect("Proposed-cap conditional increase", u2_proposed_inc, Decimal("365.40"))
    expect("Proposed-cap conditional new rent", UNIT2_BASE + u2_proposed_inc, Decimal("3515.40"))
    expect_in_pages("Proposed-cap conditional increase", usd(u2_proposed_inc), ["flagged.html"])
    expect_in_pages("Proposed-cap conditional new rent", usd(UNIT2_BASE + u2_proposed_inc), ["flagged.html"])

    # Occupancy window.
    expect("Days since added occupancy", (REVIEW_DATE - date(2026, 4, 1)).days, 223)

    # Earliest effective date reachable from today (Unit 1's 30-day notice).
    expect("Unit 1 earliest reachable effective date", REVIEW_DATE + timedelta(days=30), date(2026, 12, 10))
    expect("Unit 1 earliest reachable effective date (mailed)", REVIEW_DATE + timedelta(days=35), date(2026, 12, 15))

    # ---------------- Published-value sweep ----------------
    analysis = ["analysis.html"]
    expect_in_pages("Unit 1 increase", usd(u1_inc), analysis + ["executive-summary.html", "checklist.html", "units.html"])
    expect_in_pages("Unit 1 new rent", usd(u1_new), analysis + ["executive-summary.html", "checklist.html", "units.html"])
    expect_in_pages("Unit 1 early increase", usd(u1_early_inc), analysis + ["units.html"])
    expect_in_pages("Unit 1 early new rent", usd(UNIT1_BASE + u1_early_inc), analysis + ["units.html"])
    expect_in_pages("Unit 2 increase", usd(u2_inc), analysis + ["checklist.html", "units.html"])
    expect_in_pages("Unit 2 new rent", usd(UNIT2_BASE + u2_inc), analysis + ["checklist.html", "units.html"])
    expect_in_pages("Unit 2 phased increase", usd(u2_phase_inc), ["checklist.html", "units.html"])
    expect_in_pages("Unit 2 phased new rent", usd(UNIT2_BASE + u2_phase_inc), ["checklist.html", "units.html"])
    expect_in_pages("Unit 1 serve-by date", u1_serve.isoformat(), ["checklist.html"])
    expect_in_pages("Unit 1 mailed serve-by date", u1_serve_mail.isoformat(), ["checklist.html"])
    expect_in_pages("Unit 2 serve-by date", u2_serve.isoformat(), ["checklist.html"])
    expect_in_pages("Unit 2 mailed serve-by date", u2_serve_mail.isoformat(), ["checklist.html"])
    closing = (date(2027, 2, 28) - timedelta(days=90)).isoformat()
    closing_mail = (date(2027, 2, 28) - timedelta(days=95)).isoformat()
    published_closing = ["checklist.html", "index.html", "executive-summary.html", "analysis.html", "flagged.html"]
    expect_in_pages("Unit 2 closing service date", closing, published_closing)
    expect_in_pages("Unit 2 closing service date (mailed)", closing_mail, published_closing)
    expect_in_pages("Unit 2 earliest effective if served today",
                    (REVIEW_DATE + timedelta(days=90)).isoformat(), ["banking-rule.html", "index.html", "executive-summary.html"])
    expect_in_pages("Days since added occupancy", "223 days", ["flagged.html", "occupancy.html"])

    # ---------------- Closing service window (AUDIT.md A-02) ----------------
    u2_window_close = date(2027, 2, 28)
    u2_close_personal = u2_window_close - timedelta(days=90)      # 2026-11-30
    u2_close_mail = u2_window_close - timedelta(days=95)          # 2026-11-25
    expect("Unit 2 closing service date, personal", u2_close_personal, date(2026, 11, 30))
    expect("Unit 2 closing service date, mailed", u2_close_mail, date(2026, 11, 25))
    expect("Unit 2 days left to serve, personal", (u2_close_personal - REVIEW_DATE).days, 20)
    expect("Unit 2 days left to serve, mailed", (u2_close_mail - REVIEW_DATE).days, 15)

    deadline_pages = ["index.html", "executive-summary.html", "checklist.html",
                      "flagged.html", "banking-rule.html"]
    expect_in_pages("Unit 2 closing service date, personal",
                    u2_close_personal.isoformat(), deadline_pages)
    expect_in_pages("Unit 2 closing service date, mailed",
                    u2_close_mail.isoformat(), deadline_pages)
    expect_in_pages("Unit 2 closing effective date",
                    u2_window_close.isoformat(), deadline_pages)
    expect_in_pages("Unit 2 days left to serve, personal",
                    str((u2_close_personal - REVIEW_DATE).days) + " / "
                    + str((u2_close_mail - REVIEW_DATE).days), ["banking-rule.html"])

    # ------------- Printed day-count strings in the service-window table -------------
    # banking-rule.html prints "days until the last day to serve" for each scenario as
    # "<personal> / <mailed>", counted from REVIEW_DATE. The arithmetic above is asserted
    # on its own; these assertions tie it to the strings a reader actually sees, so a
    # stale base date or a mis-copied cell fails here.
    banking = ["banking-rule.html"]

    def daypair(effective: date, notice_days: int) -> str:
        personal = effective - timedelta(days=notice_days)
        mailed = effective - timedelta(days=notice_days + 5)
        return f"{(personal - REVIEW_DATE).days} / {(mailed - REVIEW_DATE).days}"

    for label, effective, notice_days in [
        ("suggested 2027-02-15", u2_effective, 90),
        ("closing 2027-02-28", date(2027, 2, 28), 90),
        ("phased 10.0%", u2_effective, 30),
        ("Unit 1 anniversary 2027-02-01", u1_anniversary, 30),
        ("Unit 2 true anniversary 2027-06-01", date(2027, 6, 1), 90),
    ]:
        expect_in_pages(f"days left — {label}", daypair(effective, notice_days), banking)

    # ---------------- Residual source audit (F-29/F-30, 2026-11-10) ----------------
    proposal_pages = ["index.html", "checklist.html", "laws.html", "process.html", "practices.html",
                      "banking-rule.html", "analysis.html", "executive-summary.html", "flagged.html"]
    expect_in_pages("File 261020 pending status", "Pending Committee Action", proposal_pages)
    expect_in_pages("File 261020 proposed applicability", "2026-09-15", proposal_pages)
    expect_in_pages("Unit 2 annual allowance is not separately banked",
                    "not separately banked", ["banking-rule.html", "flagged.html"])
    expect_in_pages("corrected tenant-resource description",
                    "small claims court papers for rental debt", ["tenant-protections.html", "flagged.html"])

    # ---------------- Scope is conditional on unverified intake (F-31, 2026-11-10) ----------------
    # § 37.15(a) reaches units "subject to this Chapter 37" and § 37.15(c) splits the phase-in by
    # building size. The published site must not assert that this particular building is in scope
    # as a fact: the unit count and the build year are owner-supplied.
    expect_in_pages("scope condition published as F-31", "F-31",
                    ["executive-summary.html", "index.html", "flagged.html"])
    expect_in_pages("u15(c) under-ten phase-in date stated", "2023-03-01",
                    ["flagged.html", "index.html"])
    expect_in_pages("u15(c) under-ten phase-in date stated (prose)", "March 1, 2023",
                    ["executive-summary.html"])
    # ---------------- answers.html (task 47, 2026-11-10) ----------------
    # The Q&A page restates answers already published elsewhere. These assertions tie it to the
    # same official percentages and dates, so a figure cannot be typed into it by hand and drift.
    answers = ["answers.html"]
    expect_in_pages("Q&A: current annual percentage", "1.6%", answers)
    expect_in_pages("Q&A: Unit 1 total percentage", "3.0%", answers)
    expect_in_pages("Q&A: Unit 1 increase", usd(u1_inc), answers)
    expect_in_pages("Q&A: Unit 1 new rent", usd(u1_new), answers)
    expect_in_pages("Q&A: Unit 1 early increase", usd(u1_early_inc), answers)
    expect_in_pages("Q&A: Unit 2 total percentage", "13.1%", answers)
    expect_in_pages("Q&A: Unit 2 increase", usd(u2_inc), answers)
    expect_in_pages("Q&A: Unit 2 new rent", usd(UNIT2_BASE + u2_inc), answers)
    expect_in_pages("Q&A: Unit 2 phased new rent", usd(UNIT2_BASE + u2_phase_inc), answers)
    expect_in_pages("Q&A: license phase-in start date", "March 1, 2023", answers)
    expect_in_pages("Q&A: coverage date", "June 14, 1979", answers)
    expect_in_pages("Q&A: Rent Board Fee amount", "$59.00", answers)
    expect_in_pages("Q&A: exemption deadline", "December 14, 2026", answers)
    expect_in_pages("Q&A: File 261020 status", "Pending Committee Action", answers)
    expect_in_pages("Q&A: 2027-28 rate left blank", "2027-02-28", answers)

    # ---------------- Coverage condition (F-33) and federal label (F-34) ----------------
    # The Rent Board's coverage test has two limbs. The site must state both, and must not present
    # the federal "no ceiling" point as a verified rule.
    coverage_pages = ["laws.html", "answers.html"]
    expect_in_pages("coverage: pre-1979-06-14 limb", "June 14, 1979", coverage_pages)
    expect_in_pages("coverage: not-a-single-family-dwelling limb", "not used as a single family dwelling", coverage_pages)
    expect_in_pages("coverage: two-unit building not exempt", "two-unit building", coverage_pages)
    expect_in_pages("federal rule labelled as no-source-located", "no federal", ["laws.html"])

    # ---------------- Forbidden regressions (C-01, 2026-11-10) ----------------
    # The site must never again assert that banked amounts can only be given at the time of an
    # annual increase, or that a banked balance cannot be imposed later. sf.gov states that a
    # properly banked increase "does not expire" and may be imposed on a future anniversary date
    # or at another time when a rent increase is allowed.
    forbidden = [
        "may only be given at the time of an annual increase",
        "cannot be imposed on its own later",
        "cannot be imposed on its own on a date",
        "2024-10/538%202024-25",
        # Unconditional scope assertion withdrawn under F-31 (2026-11-10): the unit count and
        # build year are owner-supplied, so the site states the rule, not the conclusion of fact.
        "Your building is in scope",
        "A two-unit building falls in that second group",
    ]
    for page in sorted(f for f in os.listdir(ROOT) if f.endswith(".html")):
        with open(os.path.join(ROOT, page), encoding="utf-8") as handle:
            body = handle.read()
        for phrase in forbidden:
            checks += 1
            if phrase in body:
                errors.append(f"forbidden regression: {phrase!r} found in {page}")

    if errors:
        print("CALCULATION VERIFICATION FAILED", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1

    print("CALCULATION VERIFICATION PASSED")
    print(f" - {checks} assertions from official percentages and statutory notice periods")
    print(f" - Unit 1: {u1_total}% -> {usd(u1_inc)} -> {usd(u1_new)} effective {u1_anniversary}")
    print(f" - Unit 2: {u2_banked}% banked + {u2_current}% current = {u2_total}% -> {usd(u2_inc)} -> {usd(UNIT2_BASE + u2_inc)}")
    print(" - every computed value found in the published HTML")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
