"""Table row data. Each row is a dict; `src` must be a key in _data.SOURCES
(or None to render the row as unverified). Rendered by build.py."""

from _data import SOURCES

# ---------------------------------------------------------------------------
# UNIT FACTS (anonymised). Dates and amounts are preserved exactly as supplied.
# ---------------------------------------------------------------------------
UNIT_FACTS = [
    dict(
        field="Unit label", unit1="Unit 1", unit2="Unit 2",
        src=None, note="Owner's own labelling. Placeholder — no address published.",
        status="Anonymised",
    ),
    dict(
        field="Neighbourhood / ZIP", unit1="Outer Sunset, 94122", unit2="Outer Sunset, 94122",
        src=None, note="Supplied by owner. The Rent Ordinance applies citywide, so the ZIP does not "
                       "change the rent cap. No unit-level official record consulted.",
        status="Owner-supplied",
    ),
    dict(
        field="Year built", unit1="1940", unit2="1940",
        src="rentlaws",
        note="1940 is on or before June 13, 1979, so the unit is within the Rent Ordinance's "
             "rent-control cutoff if it is not otherwise exempt.",
        status="Coverage confirmed by date test",
    ),
    dict(
        field="Rent-control coverage", unit1="Covered (subject to confirmation it is not an exempt "
             "single-family home or condo)", unit2="Same",
        src="rentlaws",
        note="SF Rent Board: units built on or before 6/13/1979 generally have rent control, unless "
             "they fall in an exempt class (e.g. most single-family homes and condos where the tenancy "
             "began on or after 1 Jan 1996).",
        status="Verified rule / unit facts unconfirmed",
    ),
    dict(
        field="Last lease start", unit1="1 February 2025", unit2="1 June 2019",
        src=None, note="Owner-supplied. Drives the anniversary date.",
        status="Owner-supplied",
    ),
    dict(
        field="Base rent at that lease start", unit1="$3,995.00 / month", unit2="$3,150.00 / month",
        src=None, note="Owner-supplied.", status="Owner-supplied",
    ),
    dict(
        field="Initial lease tenants", unit1="L O, V N, JP", unit2="E R, I S",
        src=None, note="Placeholder initials only. Full identifiers withheld from this site.",
        status="Anonymised",
    ),
    dict(
        field="Current tenants", unit1="L O and M T", unit2="E R and I S",
        src=None, note="Owner-supplied. Placeholder initials only.", status="Anonymised",
    ),
    dict(
        field="Tenancy event", unit1="V N and JP no longer in occupancy; M T added; rent restated at "
             "$3,995.00 from 1 April 2026",
        unit2="No change in tenancy since 1 June 2019",
        src=None, note="Owner-supplied narrative.", status="Owner-supplied",
    ),
    dict(
        field="Original occupant still resident?", unit1="Yes — L O", unit2="Yes — E R and I S",
        src="614",
        note="Decisive. Section 6.14 / Costa-Hawkins unlimited increases only arise when the LAST "
             "original occupant no longer permanently resides in the unit. An original occupant "
             "remains in both units, so the annual cap continues to apply.",
        status="Verified rule applied",
    ),
    dict(
        field="Anniversary date", unit1="1 February (if the tenancy continued) — see flag", unit2="1 June",
        src="rr1",
        note="Rule 1.11(a): the anniversary date is the date the tenant's current rent became "
             "effective; the next increase may take effect no less than one year later.",
        status="Verified rule applied",
    ),
    dict(
        field="Rent increases taken since last lease start",
        unit1="None recorded between 1 Feb 2025 and 1 Apr 2026",
        unit2="None recorded between 1 June 2019 and today",
        src=None, note="Owner-supplied statement. Not independently verified against Rent Board "
                       "records — see Flagged for Review F-01.",
        status="Owner-supplied / unverified",
    ),
    dict(
        field="Rent increase licence on file (Housing Inventory)",
        unit1="Unverified", unit2="Unverified",
        src="inventory",
        note="A current rent increase licence must be on file on the effective date or the notice is "
             "not enforceable. Check the Rent Board Portal before serving any notice.",
        status="Unverified — action required",
    ),
]

# ---------------------------------------------------------------------------
# THE THREE LEGAL LAYERS
# ---------------------------------------------------------------------------
LAW_ROWS = [
    # --- LOCAL ---
    dict(level="Local", topic="Annual cap (AGA)",
         rule="The Board publishes the CPI increase each 1 March; a licensed landlord may raise base "
              "rent by no more than 60% of that CPI change, capped at 7%.",
         value="1.6% for increases effective 1 Mar 2026 – 28 Feb 2027",
         src="373", status="Verified"),
    dict(level="Local", topic="AGA — current published rate",
         rule="The Rent Board's current published allowable annual increase.",
         value="1.6% (3/1/2026 – 2/28/2027)", src="rates", status="Verified"),
    dict(level="Local", topic="AGA — methodology",
         rule="Rule 1.12: 60% of the 12-month CPI change to 31 October; rounded to one decimal; max "
              "7%. Because the Oct-2025 CPI was never published, October 2025 is approximated as the "
              "geometric mean of the Aug-2025 and Dec-2025 CPI values.",
         value="Rule amended 13 Jan 2026", src="rr1", status="Verified"),
    dict(level="Local", topic="AGA — historical table",
         rule="Continuous published table of allowable annual increases, 4/1/1982 to date.",
         value="46 periods; see AGA history page", src="571", status="Verified"),
    dict(level="Local", topic="Frequency",
         rule="One increase per 12 months; the first may be imposed 12 months after the lease began. "
              "An increase imposed later than the anniversary becomes the new anniversary date.",
         value="Max 1 increase / 12 months", src="learn", status="Verified"),
    dict(level="Local", topic="Banking",
         rule="Rule 4.12: an unused increase (or unused portion) may be accumulated and imposed on a "
              "later anniversary date, once every 12 months; a full 12 months must have elapsed from "
              "the date it could have been imposed. Banked amounts are added, never compounded, never "
              "rounded up.",
         value="No cap on banked total", src="rr4", status="Verified"),
    dict(level="Local", topic="Banking — plain-language statement of the 12-month test",
         rule="SF.gov: a skipped increase is banked only if at least 24 full months pass without any "
              "rent increase; otherwise it is lost. This is the same test as Rule 4.12 expressed from "
              "the prior anniversary date (12 months of waiting + 12 months to accrue).",
         value="Reconciled — see Verification log V-03", src="banked", status="Verified"),
    dict(level="Local", topic="Base rent only",
         rule="The percentage is applied to base rent only (including parking/storage). Temporary "
              "passthroughs and fluctuating charges are excluded. Increases may not be rounded up.",
         value="No rounding up", src="learn", status="Verified"),
    dict(level="Local", topic="Rounding tolerance",
         rule="Rule 4.10(b): a good-faith increase that does not exceed the limits by more than 0.5% "
              "of the prior base rent may be readjusted by an ALJ rather than voided.",
         value="0.5% of prior base rent tolerance", src="rr4", status="Verified"),
    dict(level="Local", topic="Licence precondition",
         rule="A landlord must hold a current rent increase licence (Housing Inventory reported) "
              "before imposing an annual or banked increase. Notice is unenforceable without it.",
         value="Required on the effective date", src="inventory", status="Verified"),
    dict(level="Local", topic="Notice content",
         rule="§ 37.3(b): before or on the date of legal notice the landlord must state in writing "
              "which portion is the annual increase, which is banked, and which is any passthrough.",
         value="Itemised breakdown required", src="373", status="Verified"),
    dict(level="Local", topic="Non-conforming increase",
         rule="§ 37.3(b)(5): any rent increase that does not conform with § 37.3 is null and void.",
         value="Null and void", src="373", status="Verified"),
    dict(level="Local", topic="Above-cap increases",
         rule="§ 37.3(a)(8): a landlord seeking more than the permitted amounts must petition for a "
              "rental arbitration hearing. Petitions cost nothing to file.",
         value="6 petition types", src="petitions", status="Verified"),
    dict(level="Local", topic="Comparable-rent petition",
         rule="Topic 323: a rent above the cap may be justified if rent is far below comparable units "
              "due to extraordinary circumstances. 'The mere fact that a long-standing tenant is "
              "paying significantly less than market rent is not considered an extraordinary "
              "circumstance.'",
         value="Likely closed on these facts", src="comps", status="Verified"),
    dict(level="Local", topic="Operating & maintenance petition",
         rule="A landlord may petition for an increase based on documented increases in operating and "
              "maintenance expenses (capped at 7%).",
         value="Requires petition + proof", src="om", status="Verified"),
    dict(level="Local", topic="Capital improvement passthrough",
         rule="Certified capital improvements may be passed through, subject to amortisation and a "
              "10% / 12-month ceiling for seismic work.",
         value="Requires certification", src="capital", status="Verified"),
    dict(level="Local", topic="Additional occupants",
         rule="§ 37.3(a)(11): a landlord may not raise rent solely because a tenant added an "
              "occupant, even if the lease says otherwise. Such an increase is unlawful.",
         value="Prohibited", src="occupants", status="Verified"),
    dict(level="Local", topic="Section 6.14 / Costa-Hawkins",
         rule="An unlimited increase on remaining occupants is available only when the LAST original "
              "occupant has vacated, and only if a written 6.14 notice was served on each subsequent "
              "occupant within a reasonable time (generally 60 days).",
         value="Inapplicable here — an original occupant remains in both units", src="614",
         status="Verified / inapplicable"),
    dict(level="Local", topic="Algorithmic rent-setting",
         rule="§ 37.10C (effective 14 Oct 2024) prohibits selling or using algorithmic devices / "
              "revenue-management software to set rents or occupancy for SF residential units. "
              "Penalties up to $1,000 per violation per unit per month, plus attorneys' fees.",
         value="Prohibited", src="algo", status="Verified"),
    dict(level="Local", topic="Tenant petition to challenge",
         rule="A tenant may file a petition alleging an unlawful rent increase and/or for a "
              "determination of lawful rent. No filing fee, no time limit.",
         value="No fee, no deadline", src="unlawful", status="Verified"),
    dict(level="Local", topic="Hardship deferral",
         rule="Financial-hardship relief is NOT available for annual or banked increases or for "
              "Costa-Hawkins increases — only for passthrough-type increases.",
         value="Not available for AGA increases", src="hardship", status="Verified"),
    dict(level="Local", topic="Retaliation (local overlay)",
         rule="Chapter 49A requires a landlord to confer in good faith with a certified Tenant "
              "Association on rent increases; breach can support a decrease-in-housing-services "
              "petition.",
         value="Only if a Tenant Association is certified (5+ units)", src="referral",
         status="Verified via Ch. 49A text"),
    # --- STATE ---
    dict(level="State", topic="AB 1482 rent cap",
         rule="Civ. Code § 1947.12: 5% + regional CPI, max 10% per 12 months, measured against the "
              "lowest rent charged in the prior 12 months.",
         value="8.8% for SF, 1 Aug 2026 – 31 Jul 2027", src="ab1482", status="Verified"),
    dict(level="State", topic="AB 1482 does NOT apply here",
         rule="§ 1947.12(d)(3) exempts housing subject to a local ordinance that restricts annual "
              "increases to less than the state cap. The SF cap (1.6%) is lower, so SF governs and "
              "AB 1482's 8.8% is unavailable.",
         value="Local cap controls", src="civ1947_12", status="Verified"),
    dict(level="State", topic="Notice period",
         rule="Civ. Code § 827(b): 30 days' written notice if the increase is 10% or less of the "
              "lowest rent charged in the prior 12 months; 90 days if more than 10%. Add 5 days if "
              "served by mail.",
         value="30 / 90 days", src="civ827", status="Verified"),
    dict(level="State", topic="Service of notice",
         rule="§ 827(b)(1): personal delivery, or mail under Code Civ. Proc. § 1013.",
         value="Personal or mail", src="civ827", status="Verified"),
    dict(level="State", topic="Just cause",
         rule="Civ. Code § 1946.2 and Rent Ordinance § 37.9: a tenancy may not be terminated without "
              "just cause. Expiration of a lease is not just cause.",
         value="Just cause required", src="civ1946_2", status="Verified"),
    dict(level="State", topic="Retaliation",
         rule="Civ. Code § 1942.5(a): after a tenant's good-faith habitability complaint or agency "
              "complaint, the landlord may not increase rent within 180 days. § 1942.5(d): rent may "
              "not be increased at all to retaliate for tenant organising.",
         value="180-day bar after a complaint", src="civ1942_5", status="Verified"),
    dict(level="State", topic="Costa-Hawkins",
         rule="Civ. Code § 1954.53(a) lets an owner set initial and subsequent rates on vacancy; "
              "§ 1954.53(d)(3) expressly does not apply to a partial change in occupancy where an "
              "original occupant remains in lawful possession.",
         value="Does not unlock a market-rate reset here", src="civ1954_53", status="Verified"),
    dict(level="State", topic="Unruh Civil Rights Act",
         rule="Civ. Code § 51(b): all persons are entitled to full and equal accommodations in all "
              "business establishments regardless of sex, race, colour, religion, ancestry, national "
              "origin, disability, medical condition, genetic information, marital status, sexual "
              "orientation, citizenship, primary language or immigration status.",
         value="Applies to housing", src="civ51", status="Verified"),
    dict(level="State", topic="FEHA housing discrimination",
         rule="Gov. Code § 12955(a): an owner may not discriminate against or harass a person because "
              "of race, colour, religion, sex, gender, gender identity, gender expression, sexual "
              "orientation, marital status, national origin, ancestry, familial status, source of "
              "income, disability, veteran or military status, or genetic information.",
         value="Protected classes enumerated", src="gov12955", status="Verified"),
    dict(level="State", topic="FEHA — coercion / interference",
         rule="Gov. Code § 12955.7: it is unlawful to coerce, intimidate, threaten or interfere with "
              "a person's exercise of rights under § 12955.",
         value="Separate violation", src="gov12955_7", status="Verified"),
    # --- FEDERAL ---
    dict(level="Federal", topic="No federal rent cap",
         rule="Neither the Fair Housing Act nor any other federal statute cited by HUD sets a ceiling "
              "on residential rent. Federal law regulates discrimination, not price.",
         value="No federal rent control", src="hud_fha", status="Verified (absence of provision)"),
    dict(level="Federal", topic="Fair Housing Act — terms and conditions",
         rule="42 U.S.C. § 3604(b): it is unlawful to discriminate in the terms, conditions or "
              "privileges of the rental of a dwelling because of race, colour, religion, sex, "
              "familial status or national origin.",
         value="Applies to rent-setting", src="fha3604", status="Verified"),
    dict(level="Federal", topic="FHA protected classes",
         rule="Race, colour, national origin, religion, sex, familial status, disability.",
         value="7 federal classes", src="hud_fha", status="Verified"),
    dict(level="Federal", topic="Algorithmic pricing antitrust",
         rule="DOJ Antitrust Division: proposed settlement requiring RealPage to stop using "
              "competitors' non-public data and to remove features that aligned pricing. Follow-on "
              "decrees with large landlords.",
         value="Institutional practice under enforcement", src="doj_realpage", status="Verified"),
    dict(level="Federal", topic="CPI source for the SF cap",
         rule="BLS publishes the SF-Oakland-Hayward CPI-U that feeds the AGA. The October 2025 "
              "release does not exist because of the 2025 lapse in appropriations.",
         value="Oct 2025 CPI not published", src="bls_cpi", status="Verified"),
]

# ---------------------------------------------------------------------------
# CALCULATIONS
# ---------------------------------------------------------------------------
UNIT1_CALC = [
    dict(scenario="A — Annual increase only, new anniversary date",
         basis="1.6% (rate in effect 3/1/26–2/28/27)",
         pct="1.6%", amount=63.92, new_rent=4058.92,
         notice="30 days", src="571",
         comment="The 1.4% that could have been taken on 1 Feb 2026 is lost, because fewer than 12 "
                 "months elapse before this effective date."),
    dict(scenario="B — Banked 1.4% + annual 1.6%, on the 1 February anniversary",
         basis="1.4% (2025-26) banked + 1.6% (2026-27) annual",
         pct="3.0%", amount=119.85, new_rent=4114.85,
         notice="30 days", src="rr4",
         comment="Preserves the 1 February anniversary. The 1.4% is banked on 1 Feb 2027 — exactly 24 "
                 "months after the 1 Feb 2025 lease start and 12 months after it first became "
                 "available. This is the maximum lawful amount."),
]
UNIT1_TOTAL = dict(base=3995.00, pct="3.0%", amount=119.85, new_rent=4114.85)

UNIT2_CALC = [
    dict(scenario="A — Full banked history + current annual",
         pct="13.1%", banked="11.5%", current="1.6%", amount=412.65, new_rent=3562.65,
         src="rr4",
         comment="1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = 11.5% banked (each is more than 24 months old "
                 "by today), plus the 1.6% annual in effect on any effective date up to 28 Feb 2027. "
                 "Requires 90-day notice."),
    dict(scenario="B — Banked history, but annual skipped",
         pct="11.5%", banked="11.5%", current="0%", amount=362.25, new_rent=3512.25,
         src="rr4",
         comment="Still more than 10%, so still 90-day notice. No advantage over A unless the owner "
                 "wants to reserve the current year."),
    dict(scenario="C — Current annual only, no banking",
         pct="1.6%", banked="0%", current="1.6%", amount=50.40, new_rent=3200.40,
         src="571",
         comment="Lawful but permanently forfeits 11.5% of banked entitlement. Banking has no expiry "
                 "during a tenancy, so there is no requirement to take it — but also no way to "
                 "recover it later at a higher base."),
]
UNIT2_TOTAL = dict(base=3150.00, pct="13.1%", amount=412.65, new_rent=3562.65)

# Notice-deadline matrix (computed, not hand-typed)
NOTICE_ROWS = [
    dict(effective="1 Dec 2026", inc="3.0%", days=30, serve="1 Nov 2026", mail="27 Oct 2026",
         status="deadline passed", src="civ827"),
    dict(effective="15 Dec 2026", inc="3.0%", days=30, serve="15 Nov 2026", mail="10 Nov 2026",
         status="open", src="civ827"),
    dict(effective="1 Jan 2027", inc="3.0%", days=30, serve="2 Dec 2026", mail="27 Nov 2026",
         status="open", src="civ827"),
    dict(effective="1 Feb 2027", inc="3.0%", banked=True, days=30, serve="2 Jan 2027",
         mail="28 Dec 2026", status="open — recommended for Unit 1", src="rr4"),
    dict(effective="1 Dec 2026", inc="13.1%", days=90, serve="2 Sep 2026", mail="28 Aug 2026",
         status="deadline passed", src="civ827"),
    dict(effective="1 Jan 2027", inc="13.1%", days=90, serve="3 Oct 2026", mail="28 Sep 2026",
         status="deadline passed", src="civ827"),
    dict(effective="4 Feb 2027", inc="13.1%", days=90, serve="6 Nov 2026", mail="1 Nov 2026",
         status="open until today only", src="civ827"),
    dict(effective="15 Feb 2027", inc="13.1%", days=90, serve="17 Nov 2026", mail="12 Nov 2026",
         status="open — recommended for Unit 2", src="civ827"),
]

# ---------------------------------------------------------------------------
# LAWYER-REVIEW CHECKLIST
# ---------------------------------------------------------------------------
REVIEW = [
    dict(n=1, check="Is the unit covered by the Rent Ordinance?",
         test="Built on or before 13 June 1979; not a separately-alienable single-family home or "
              "condo with a tenancy that began on or after 1 Jan 1996.",
         finding="Probably covered — built 1940. Must confirm the unit is not an exempt "
                 "single-family home or condo, and check the Property Information Map.",
         verdict="PASS subject to confirmation", kind="warn", src="rentlaws"),
    dict(n=2, check="Does the owner hold a current rent increase licence?",
         test="Housing Inventory reported; licence current on the effective date of the notice.",
         finding="Unverified. This is the single most common defect that voids an otherwise valid "
                 "increase. Check the Rent Board Portal before serving.",
         verdict="UNVERIFIED — blocking", kind="risk", src="inventory"),
    dict(n=3, check="Is the increase at or below the allowable annual amount?",
         test="Increase ≤ the published AGA for the period in which it takes effect, plus properly "
              "banked amounts; applied to base rent only; not rounded up.",
         finding="Unit 1: 3.0% is within 1.4% banked + 1.6% annual. Unit 2: 13.1% is within 11.5% "
                 "banked + 1.6% annual. Both arithmetically within the cap.",
         verdict="PASS", kind="ok", src="571"),
    dict(n=4, check="Is the arithmetic exact?",
         test="Apply the percentages to base rent; do not compound banked amounts; do not round up.",
         finding="$3,995.00 × 3.0% = $119.85 → $4,114.85. $3,150.00 × 13.1% = $412.65 → $3,562.65. "
                 "Both exact to the cent, no rounding up, banked percentages added not compounded.",
         verdict="PASS", kind="ok", src="rr4"),
    dict(n=5, check="Is the timing lawful — one increase per 12 months?",
         test="No increase in the 12 months before the effective date; first increase at least 12 "
              "months after the lease began.",
         finding="Unit 1: last rent effective 1 Feb 2025 (or 1 Apr 2026 — see F-02). Unit 2: last "
                 "rent effective 1 Jun 2019. No increase within 12 months in either.",
         verdict="PASS subject to F-02", kind="warn", src="learn"),
    dict(n=6, check="Has adequate written notice been given?",
         test="30 days if the increase is 10% or less; 90 days if more than 10%; +5 days if mailed; "
              "the notice must state dollar amount, percentage and effective date.",
         finding="Unit 1 (3.0%) needs 30 days. Unit 2 (13.1%) needs 90 days, which means serving by "
                 "mid-November 2026 for a February 2027 effective date.",
         verdict="PASS if deadlines on the Notices page are met", kind="warn", src="civ827"),
    dict(n=7, check="Does the notice itemise the components?",
         test="§ 37.3(b) and Rule 4.12(b): the notice must state which portion is the annual "
              "increase and which is banked, and the dates the banked amount is based on.",
         finding="Failure to itemise the banked portion and its base dates does not by itself void "
                 "the increase under Rule 4.12(b), but it is the first thing a tenant petition "
                 "attacks, and § 37.3(b)(5) voids a non-conforming increase.",
         verdict="MUST FIX — use the template on the Notices page", kind="risk", src="373"),
    dict(n=8, check="Is any part of the increase prohibited?",
         test="No charge for additional occupants; no algorithmic pricing; no increase within 180 "
              "days of a habitability complaint; no retaliatory increase.",
         finding="Unit 1 gained a tenant (M T). Charging more because of that occupant would be "
                 "unlawful. The increase must rest on the anniversary, not on occupancy.",
         verdict="PASS if correctly framed", kind="warn", src="occupants"),
    dict(n=9, check="Is the differential between the two units explainable without protected traits?",
         test="Unruh / FEHA / FHA: no differential treatment on the basis of a protected "
              "characteristic. A differential explained by documented tenancy facts is lawful.",
         finding="Unit 1 gets 3.0% and Unit 2 gets 13.1%, but both take the same 1.6% annual plus "
                 "their own banked history. The difference is tenancy length, not tenant identity.",
         verdict="PASS — but write the policy down", kind="ok", src="gov12955"),
    dict(n=10, check="Is the reason for the increase stated or stateable?",
         test="For an AGA increase no justification is required; the statute supplies the reason. "
              "Any reason given must not be a proxy for a protected characteristic.",
         finding="Use the statutory basis. Do not cite market rent, comparable units or tenant "
                 "conduct — each invites a comparable-rent or retaliation argument.",
         verdict="PASS if statutory wording is used", kind="ok", src="learn"),
    dict(n=11, check="Would the increase survive a tenant petition?",
         test="Rent Board petition alleging unlawful increase; ALJ reviews licence, notice, "
              "arithmetic and component disclosure. Non-conforming = null and void.",
         finding="On the documents described, yes — provided the licence exists and the notice is "
                 "itemised. Those are the two points where this file is currently exposed.",
         verdict="PASS subject to items 2 and 7", kind="warn", src="unlawful"),
    dict(n=12, check="Is the tenant's hardship position addressed?",
         test="Hardship relief does not apply to annual or banked increases.",
         finding="A tenant cannot defer an AGA increase on hardship grounds. Expect this to be "
                 "raised anyway; the correct answer is the Rent Board's own page.",
         verdict="NO DEFENCE AVAILABLE TO TENANT", kind="info", src="hardship"),
]

# ---------------------------------------------------------------------------
# FLAGGED ITEMS
# ---------------------------------------------------------------------------
FLAGGED = [
    dict(id="F-01", sev="Medium", sev_kind="warn",
         title="Rent histories are owner-supplied and not independently verified",
         detail="The site states that no increases were taken on either unit. That is taken from the "
                "prompt, not from a Rent Board record. If any increase was in fact taken, every "
                "figure on the Calculations page changes.",
         action="Pull the rent history for each unit from the Rent Board portal, or buy a Rent "
                "History report, before serving any notice.",
         src="inventory"),
    dict(id="F-02", sev="High", sev_kind="risk",
         title="Unit 1 — is this a continuing tenancy or a new tenancy as of 1 April 2026?",
         detail="The prompt calls 1 April 2026 a 'continuing tenancy' at the same $3,995.00. But the "
                "occupants changed (V N and JP left, M T joined) and a new term apparently began. If "
                "a NEW tenancy was created on 1 April 2026, the anniversary date is 1 April 2026 and "
                "no annual increase may take effect before 1 April 2027 — which would make scenario "
                "B unavailable. If the tenancy continued with L O in place, the anniversary is "
                "1 February and scenario B is available. Costa-Hawkins § 1954.53(d)(3) does not "
                "itself reset the rate while an original occupant remains, but the parties' own "
                "agreement can create a new term.",
         action="Ask the Rent Board counselor to fix the anniversary date. Do not serve a notice on "
                "Unit 1 until it is fixed.",
         src="civ1954_53"),
    dict(id="F-03", sev="High", sev_kind="risk",
         title="Unit 2 — confirm both original tenants are still in occupancy",
         detail="The analysis assumes E R and I S are both still resident and are the original "
                "tenants from 1 June 2019. If both original occupants had left and a 6.14 notice was "
                "duly served, an unlimited increase would be available instead; if a 6.14 notice was "
                "never served, the annual cap continues to apply.",
         action="Confirm occupancy. Check whether any written 6.14 notice was ever served. A 6.14 "
                "notice cannot be served retroactively.",
         src="614"),
    dict(id="F-04", sev="High", sev_kind="risk",
         title="Rent increase licence status unknown for both units",
         detail="Neither unit has a confirmed current rent increase licence. A notice served without "
                "one is unenforceable on its effective date, even if every other element is perfect.",
         action="Log into the Rent Board Portal, confirm the Housing Inventory filing is current for "
                "both units, and download or record the licence.",
         src="inventory"),
    dict(id="F-05", sev="Medium", sev_kind="warn",
         title="Coverage not confirmed at parcel level",
         detail="Built 1940 passes the date test, but a pre-1979 building can still contain units "
                "that are exempt (for example a separately-alienable single-family home or condo "
                "where the tenancy began on or after 1 January 1996). The building type has not been "
                "supplied.",
         action="Look the property up on the SF Property Information Map and confirm the number of "
                "units and the assessor's use code.",
         src="rentlaws"),
    dict(id="F-06", sev="Low", sev_kind="info",
         title="Unit 2's increase crosses the 10% threshold",
         detail="13.1% is more than 10% of the lowest rent charged in the prior 12 months, so it "
                "requires 90 days' written notice rather than 30. A 90-day deadline is easy to miss "
                "and, once missed, pushes the effective date out by months.",
         action="Serve by 17 November 2026 for a 15 February 2027 effective date, or re-plan the "
                "effective date.",
         src="civ827"),
    dict(id="F-07", sev="Low", sev_kind="info",
         title="Unit 1 may have already forfeited the 1.4% increase",
         detail="The 1.4% increase became available on 1 February 2026. Under Rule 4.12 it is only "
                "banked once 12 months have elapsed from that date, and under the Rent Board's "
                "plain-language statement once 24 months have passed without any increase. Both "
                "tests mature on 1 February 2027. Any effective date before then loses the 1.4% "
                "permanently.",
         action="If the 1.4% matters, set the Unit 1 effective date at 1 February 2027 — not "
                "earlier.",
         src="banked"),
    dict(id="F-08", sev="Low", sev_kind="info",
         title="HUD Fair Market Rent figures could not be retrieved",
         detail="HUD's FY2026 Fair Market Rent documentation system returned null values for San "
                "Francisco County when queried. No FMR figure is published on this site rather than "
                "risk an unverified number. FMR is in any event a federal subsidy benchmark, not a "
                "rent-control ceiling, so it does not affect either unit's lawful rent.",
         action="If the figure is needed, read it directly from the HUD FMR dataset file linked in "
                "the source register.",
         src="hud_fmr", unverified=True),
    dict(id="F-09", sev="Low", sev_kind="info",
         title="No official source quantifies how many SF owners take the annual increase",
         detail="The question 'how do individual owners handle increases' has no official statistic "
                "behind it. The Rent Board publishes eviction, buyout and petition statistics, but "
                "not a rate of annual-increase take-up. Rather than estimate, this site reports only "
                "what the Rent Board publishes and marks the rest as a research gap.",
         action="None — recorded as a known gap in the evidence base.",
         src="stats", unverified=True),
]
