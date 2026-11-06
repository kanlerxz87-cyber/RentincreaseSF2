"""Canonical data for the Rental Increase SF site.

Every statutory/regulatory claim carries an official `src` URL taken from a
.government domain (sf.gov / sfrb.org / leginfo.legislature.ca.gov / law.cornell
for the U.S. Code / hud.gov / bls.gov / justice.gov). Rows that could not be
confirmed against an official source are marked src=None and rendered as
"unverified" everywhere. Nothing in this file is inferred.

Verification status codes
  VERIFIED   - value read directly off the official page/PDF linked in `src`
  PARTIAL    - official page exists but does not state the specific point;
               the point is a reasoned application of a verified rule
  UNVERIFIED - no official source found; value left blank
"""

# ----------------------------------------------------------------------------
# Source register
# ----------------------------------------------------------------------------
SOURCES = {
    "571":    "https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf",
    "learn":  "https://www.sf.gov/learn-about-rent-increases-san-francisco",
    "learn_old": "https://sf.gov/reports/march-2023/learn-about-rent-increases-san-francisco",
    "rates":  "https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit",
    "news26": "https://www.sf.gov/news--annual-rent-increase-3126-22827-announced",
    "373":    "https://www.sf.gov/information--sec-373-rent-limitations",
    "373b":   "https://www.sf.gov/information/sec-373-rent-limitations",
    "rentlaws": "https://www.sf.gov/learn-about-san-francisco-rental-laws",
    "banked": "https://www.sf.gov/information--banked-rent-increases",
    "multiyear": "https://www.sf.gov/information--annual-rent-increase-multiple-years",
    "rr4":    "https://www.sf.gov/reports/december-2022/rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring",
    "rr1":    "https://www.sf.gov/reports/december-2022/rent-board-rules-and-regulations-part-i-definitions",
    "rr_all": "https://www.sf.gov/documents/36249/625_RR_Complete_1-13-26.pdf",
    "rr225":  "https://www.sf.gov/documents/625/626_RR_Complete_2-25-25.pdf",
    "rramend": "https://media.api.sf.gov/documents/626A_Complete_List_of_Amendments_to_the_RRs_1-13-26.pdf",
    "rrindex": "https://www.sf.gov/reports--rent-board-rules-and-regulations",
    "inventory": "https://www.sf.gov/rent-board-housing-inventory",
    "petitions": "https://www.sf.gov/landlord-petitions-and-passthroughs",
    "unlawful": "https://www.sf.gov/report-unlawful-rent-increase-or-request-review-your-rent-history",
    "hardship": "https://www.sf.gov/tenant-financial-hardship-applications",
    "614":    "https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins",
    "614p":   "https://www.sf.gov/information--petition-determination-pursuant-section-614-andor-costa-hawkins",
    "121":    "https://www.sf.gov/information--tenant-occupancy-petitions",
    "occupants": "https://www.sf.gov/information--charging-additional-occupants-prohibited",
    "algo":   "https://www.sf.gov/information--algorithmic-devices-set-rent-are-prohibited-san-francisco",
    "comps":  "https://www.sf.gov/information--special-circumstances-petitions-based-rents-comparable-units",
    "om":     "https://www.sf.gov/information/topic-no-322-operating-and-maintenance-expense-petitions",
    "capital": "https://sf.gov/apply-raise-rents-capital-improvement-costs",
    "util":   "https://sf.gov/information/topic-no-325-utility-passthroughs",
    "referral": "https://www.sf.gov/reports--january-2025--rent-board-referral-listing",
    "stats":  "https://www.sf.gov/information--rent-board-statistics-and-reports",
    "index":  "https://www.sf.gov/information--index-landlord-and-tenant-information",
    "ab1482": "https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482",
    "ab1482bill": "https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201920200AB1482",
    "civ1947_12": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12",
    "civ827": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827",
    "civ1942_5": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5",
    "civ1946_2": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1946.2",
    "civ1954_53": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.53",
    "civ1954_50": "https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=5.&part=4.&chapter=2.7.&article=",
    "civ51":  "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=51",
    "civ51_text": "https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=1.&title=&part=2.&chapter=&article=",
    "gov12955": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955",
    "gov12955_7": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955.7",
    "fha3604": "https://www.law.cornell.edu/uscode/text/42/3604",
    "hud_fha": "https://www.hud.gov/helping-americans/fair-housing-act-overview",
    "hud_fmr": "https://www.huduser.gov/portal/datasets/fmr.html",
    "doj_realpage": "https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and",
    "doj_pinnacle": "https://www.justice.gov/opa/pr/justice-department-reaches-proposed-consent-decree-pinnacle-one-americas-largest-landlords",
    "bls_cpi": "https://www.bls.gov/regions/west/news-release/consumerpriceindex_sanfrancisco.htm",
    "edi":    "https://www.edi.courts.ca.gov/",
}

# Short, human labels for the source register table
SOURCE_LABELS = {
    "571": ("SF Rent Board Form 571 — Allowable Annual Rent Increases 1982–present", "City & County of San Francisco", "Primary"),
    "learn": ("Learn about rent increases in San Francisco", "SF Rent Board", "Primary"),
    "rates": ("Current Rates — rent increase, relocation, security deposit", "SF Rent Board", "Primary"),
    "news26": ("Annual Rent Increase for 3/1/26 – 2/28/27 Announced (14 Jan 2026)", "SF Rent Board", "Primary"),
    "373": ("Sec. 37.3 — Rent Limitations (Rent Ordinance text)", "SF Rent Board", "Primary"),
    "rentlaws": ("Learn about San Francisco rental laws (coverage / 6-13-1979 cutoff)", "SF Rent Board", "Primary"),
    "banked": ("Banked rent increases", "SF Rent Board", "Primary"),
    "multiyear": ("Annual rent increase for multiple years", "SF Rent Board", "Primary"),
    "rr4": ("Rent Board Rules Part IV — §§ 4.10, 4.11, 4.12 Banking", "SF Rent Board", "Primary"),
    "rr1": ("Rent Board Rules Part I — § 1.11 Anniversary date, § 1.12 Annual rent increase", "SF Rent Board", "Primary"),
    "rr_all": ("Complete Rent Board Rules and Regulations (amended 1/13/26)", "SF Rent Board", "Primary"),
    "rrindex": ("The Rent Board Rules and Regulations (index)", "SF Rent Board", "Primary"),
    "rramend": ("Complete list of amendments to the Rules (through 1/13/26)", "SF Rent Board", "Primary"),
    "inventory": ("The Rent Board Housing Inventory / rent increase license", "SF Rent Board", "Primary"),
    "petitions": ("Landlord Petitions and Passthroughs", "SF Rent Board", "Primary"),
    "unlawful": ("Report an unlawful rent increase / request review of rent history", "SF Rent Board", "Primary"),
    "hardship": ("Tenant Financial Hardship Applications", "SF Rent Board", "Primary"),
    "614": ("Rent increases under Section 6.14 and Costa-Hawkins", "SF Rent Board", "Primary"),
    "614p": ("Petition for determination under § 6.14 and/or Costa-Hawkins", "SF Rent Board", "Primary"),
    "121": ("Tenant in Occupancy Petitions (§ 1.21)", "SF Rent Board", "Primary"),
    "occupants": ("Charging for additional occupants prohibited", "SF Rent Board", "Primary"),
    "algo": ("Algorithmic devices that set rent are prohibited in SF", "SF Rent Board", "Primary"),
    "comps": ("Special circumstances petitions based on rents for comparable units", "SF Rent Board", "Primary"),
    "om": ("Operating and maintenance expense petitions (§ 6.10 / Topic 322)", "SF Rent Board", "Primary"),
    "capital": ("Capital improvement passthroughs", "SF Rent Board", "Primary"),
    "util": ("Utility passthroughs", "SF Rent Board", "Primary"),
    "referral": ("Rent Board Referral Listing (tenant & landlord resources)", "SF Rent Board", "Primary"),
    "stats": ("Rent Board Statistics and Reports", "SF Rent Board", "Primary"),
    "index": ("Index of Landlord and Tenant Information", "SF Rent Board", "Primary"),
    "ab1482": ("The California Tenant Protection Act of 2019 (AB 1482)", "SF Rent Board", "Primary"),
    "ab1482bill": ("AB 1482 — chaptered bill text", "California Legislature", "Primary"),
    "civ1947_12": ("Civil Code § 1947.12 — 5% + CPI rent cap", "California Legislature", "Primary"),
    "civ827": ("Civil Code § 827 — notice of rent increase / 30 vs 90 days", "California Legislature", "Primary"),
    "civ1942_5": ("Civil Code § 1942.5 — retaliation", "California Legislature", "Primary"),
    "civ1946_2": ("Civil Code § 1946.2 — just cause", "California Legislature", "Primary"),
    "civ1954_53": ("Civil Code § 1954.53 — Costa-Hawkins, initial and subsequent rates", "California Legislature", "Primary"),
    "civ1954_50": ("Civil Code § 1954.50 et seq. — Costa-Hawkins Rental Housing Act", "California Legislature", "Primary"),
    "civ51": ("Civil Code § 51 — Unruh Civil Rights Act", "California Legislature", "Primary"),
    "gov12955": ("Gov. Code § 12955 — FEHA housing discrimination", "California Legislature", "Primary"),
    "gov12955_7": ("Gov. Code § 12955.7 — unlawful practice / coercion, interference", "California Legislature", "Primary"),
    "fha3604": ("42 U.S.C. § 3604 — Fair Housing Act, prohibited practices", "U.S. Code (Cornell LII)", "Primary"),
    "hud_fha": ("Housing discrimination under the Fair Housing Act (protected classes)", "U.S. Dept. of Housing & Urban Development", "Primary"),
    "hud_fmr": ("HUD Fair Market Rents (40th percentile gross rents)", "U.S. Dept. of Housing & Urban Development", "Primary"),
    "doj_realpage": ("Justice Department Requires RealPage to End Sharing of Competitively Sensitive Information", "U.S. Dept. of Justice, Antitrust Division", "Primary"),
    "doj_pinnacle": ("Justice Department Reaches Proposed Consent Decree with Pinnacle", "U.S. Dept. of Justice, Antitrust Division", "Primary"),
    "bls_cpi": ("Consumer Price Index, San Francisco Area — August 2026", "U.S. Bureau of Labor Statistics", "Primary"),
}
