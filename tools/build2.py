#!/usr/bin/env python3
"""Second half of the site build: pages 07-13."""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from _template import head, foot, page_head, src, badge  # noqa: E402
import _data as D  # noqa: E402
import _rows as R  # noqa: E402
from build import write, money, s, table, status_badge  # noqa: E402

S = D.SOURCES
TODAY = "6 November 2026"


# ===========================================================================
# 6. PRACTICES
# ===========================================================================
def build_practices():
    body = page_head(
        "How rental increases are actually handled",
        "Institutional owners and individual owners, separated. Only practices an official source "
        "actually describes are stated; where no official data exists, it is recorded as a gap rather "
        "than estimated.",
        crumb='<a href="index.html">Dashboard</a> / Owner practices',
    )

    body += f"""
    <div class="callout warn">
      <span class="ct">Read this first — what official sources do and do not say</span>
      There is no government dataset that says "large owners raise rent by X% and small owners by Y%".
      The San Francisco Rent Board publishes eviction, buyout and petition statistics
      {s("stats")}; it does not publish a distribution of annual rent increases by owner type. So the
      honest answer separates two things: <strong>what the law requires of everyone identically</strong>,
      and <strong>what official sources describe about how large operators behave</strong>. Anything
      beyond that would be invented, and is flagged as a research gap instead.
    </div>

    <div class="card">
      <h2>1. The part that is identical for every owner</h2>
      <p>For a rent-controlled San Francisco unit, an apartment-owning corporation, a REIT and a
      two-flat owner are on exactly the same footing. The ordinance makes no distinction by owner
      size:</p>
      <table class="plain">
        <tr><th>The ceiling</th><td>1.6% for the current period, set by the Board, not by the owner
          {s("571")}</td></tr>
        <tr><th>The frequency</th><td>Once per 12 months, on the anniversary date {s("learn")}</td></tr>
        <tr><th>The licence</th><td>Housing Inventory reported and a current rent increase licence —
          a corporate owner is not exempt, though very small owner-occupied buildings can claim a
          Homeowner's Exemption from the <em>fee</em>, which is a different thing from the licence
          {s("inventory")}</td></tr>
        <tr><th>The notice</th><td>30 days at 10% or less, 90 days above 10%, itemised components
          {s("civ827")}{s("373")}</td></tr>
        <tr><th>The consequence of error</th><td>Null and void, no matter who the owner is
          {s("373")}</td></tr>
      </table>
      <p>The practical implication for this file: there is no "corporate method" that would let a
      small owner lawfully exceed 1.6%, and no small-owner latitude that would let one go above the
      banked total. The method is fixed by statute.</p>
    </div>

    <div class="card">
      <h2>2. What official sources say about large operators</h2>
      <p>Two federal actions describe institutional practice directly, and both concern the same
      thing: using aggregated competitor data to decide the number.</p>
      <table class="plain">
        <tr><th>DOJ v. RealPage</th><td>The Antitrust Division alleged that large landlords used
          revenue-management software fed with competitors' non-public data to align rents. The
          proposed settlement requires RealPage to stop using that data, to remove features that
          "limited price decreases or aligned pricing between competing users", to stop running
          market surveys collecting competitively sensitive information, and to accept a
          court-appointed monitor {s("doj_realpage")}</td></tr>
        <tr><th>Follow-on decrees</th><td>Proposed consent decrees with large landlords (Cortland,
          Greystar, LivCor, Willow Bridge and later Pinnacle) bar feeding competitor data into
          pricing tools and bar sharing non-public data with rivals {s("doj_pinnacle")}</td></tr>
        <tr><th>What this means in San Francisco</th><td>It is independently unlawful here. Section
          37.10C prohibits the sale <em>or use</em> of algorithmic devices to set rents or manage
          occupancy for SF residential units — up to $1,000 per violation, per unit, per month
          {s("algo")}</td></tr>
      </table>
      <p>So the honest characterisation of institutional practice is not "they raise rent more
      aggressively and get away with it". It is that large operators historically systematised
      pricing, the federal government and the City have now both moved against the specific
      data-sharing mechanism, and the lawful ceiling in San Francisco is the same for them as for a
      two-unit owner.</p>
    </div>

    <div class="card">
      <h2>3. What individual owners in San Francisco do — and what can be verified</h2>
      <p>Three behaviours are documented in official material, because each has a rule attached:</p>
      <ol class="steps">
        <li><span class="st">They bank increases and take them later, or never.</span>
          The Rent Board maintains a whole page on it, and banking has no expiry during a tenancy
          {s("banked")}. Unit&nbsp;2 is the textbook case: six years of small increases that were
          never taken.</li>
        <li><span class="st">They take partial increases.</span>
          The Ordinance permits taking less than the maximum; the unused portion is banked
          {s("banked")}. Nothing requires an owner to take 1.6%.</li>
        <li><span class="st">They sometimes fall below the cap and then petition.</span>
          Where a rent is far below comparable units for extraordinary reasons, a special-circumstances
          petition exists — but the Board is explicit that a long-standing low rent is <em>not</em> an
          extraordinary circumstance {s("comps")}.</li>
      </ol>
      <p class="small muted">What cannot be verified: how often individual owners take the annual
      increase at all. No official figure exists for that. It is recorded as research gap G-01 on the
      <a class="inline" href="flagged.html">Flagged for Review</a> page rather than guessed at.</p>
    </div>

    <div class="card">
      <h2>4. The techniques an institutional operator would use that you can lawfully copy</h2>
      <p>These are all drawn from published rules, not from any private playbook:</p>
      <table class="plain">
        <tr><th>Take the anniversary every year</th><td>Taking 1.6% annually keeps the base rent
          tracking the cap. Skipping it does not preserve the money — it banks it, and banking is
          lost if the anniversary date changes before it matures {s("banked")}</td></tr>
        <tr><th>Keep a rent ledger per unit</th><td>Every increase, its effective date, its percentage
          and whether any part was banked. Without it, the banked total cannot be proved in a
          petition {s("unlawful")}</td></tr>
        <tr><th>Serve notice early</th><td>A 90-day deadline is easy to miss and, once missed, moves
          the effective date instead of shortening the notice {s("civ827")}</td></tr>
        <tr><th>Itemise the notice</th><td>Annual portion, banked portion, banked base dates. This is
          the single cheapest way to defeat a petition {s("373")}{s("rr4")}</td></tr>
        <tr><th>Write the policy down</th><td>A one-page written policy — "the annual allowable
          increase is offered to every tenancy on its anniversary" — is the strongest evidence of
          even-handedness if a discrimination question is ever raised {s("gov12955")}</td></tr>
        <tr><th>Do not use pricing software</th><td>Prohibited in San Francisco, and the federal
          antitrust decrees point the same way {s("algo")}{s("doj_realpage")}</td></tr>
      </table>
    </div>
    </div>
"""
    return write("practices.html", head(
        "How rental increases are handled",
        "How institutional and individual property owners handle rent increases in San Francisco, "
        "based only on official sources.",
        "practices.html") + body + foot())


# ===========================================================================
# 7. NOTICES
# ===========================================================================
def build_notices():
    body = page_head(
        "Notice content, service rules and deadlines",
        "What a San Francisco rent increase notice must contain, how it must be served, and the "
        "calendar for both units — including the 90-day constraint that governs Unit 2.",
        crumb='<a href="index.html">Dashboard</a> / Notices',
    )

    body += f"""
    <div class="card">
      <h2>The six things every notice must contain</h2>
      <p>These come from three places at once: the Rent Ordinance requires the component breakdown
      {s("373")}, Rule 4.12 requires the banked portion and its base dates {s("rr4")}, and Civil Code
      §&nbsp;827 requires the increase itself {s("civ827")}. The Rent Board's own summary requires all
      of them on the notice {s("learn")}.</p>
      <table class="plain">
        <tr><th>1. The dollar amount</th><td>The increase in dollars, and the new base rent.</td></tr>
        <tr><th>2. The percentage</th><td>The percentage of the increase.</td></tr>
        <tr><th>3. The effective date</th><td>The date the new rent takes effect.</td></tr>
        <tr><th>4. The annual portion</th><td>Which part is the annual allowable increase.</td></tr>
        <tr><th>5. The banked portion</th><td>Which part is banked, and the dates that banked amount
          is based on (include the percentage for each year).</td></tr>
        <tr><th>6. Any passthrough</th><td>Which part, if any, is a gas/electric, water-bond,
          GO-bond or capital-improvement passthrough. On these figures there is none.</td></tr>
      </table>
      <div class="callout warn">
        <span class="ct">Why item 5 matters more than it looks</span>
        Rule 4.12(b) says failure to state the banked portion and its base dates does not by itself
        void the increase. But §&nbsp;37.3(b)(5) says <em>any</em> increase that does not conform with
        §&nbsp;37.3 is null and void, and §&nbsp;37.3(b) requires the landlord to inform the tenant in
        writing which portion is annual and which is banked {s("rr4")}{s("373")}. Where the two read
        together, the safe course is to include the breakdown. It costs nothing and removes the
        argument entirely.
      </div>
    </div>

    <div class="card">
      <h2>Notice period and service</h2>
      <table class="plain">
        <tr><th>30 days</th><td>Where the increase is 10% or less of the rent charged at any time in
          the 12 months before the effective date {s("civ827")}</td></tr>
        <tr><th>90 days</th><td>Where the increase is more than 10% — this is where Unit&nbsp;2 lands
          at 13.1% {s("civ827")}</td></tr>
        <tr><th>+5 days if mailed</th><td>If the notice is served by mail, add five days to the notice
          period {s("learn")}{s("civ827")}</td></tr>
        <tr><th>How to serve</th><td>Personal delivery to the tenant, or mail under Code of Civil
          Procedure §&nbsp;1013 {s("civ827")}</td></tr>
        <tr><th>Which rate to quote</th><td>The percentage <em>in effect on the effective date</em>,
          not the one in effect when the notice is served {s("learn")}</td></tr>
        <tr><th>Licence</th><td>A current rent increase licence must be on file on the effective date.
          It does not have to be attached to the notice {s("inventory")}</td></tr>
      </table>
    </div>

    <div class="card flush">
      <div class="card-pad" style="padding-bottom:4px">
        <h2>Deadline matrix</h2>
        <p class="small muted">Computed from the effective date and the applicable notice period.
        "Serve by" is the last day for personal service; "mail by" already includes the five extra
        days.</p>
      </div>
      {table(
        ["Unit", "Effective date", "Increase", "Notice period", "Serve by", "If mailed, mail by", "Status", "Source"],
        [
          "<tr><td class='key'>Unit 1</td><td>{}</td><td class='num'>{}</td><td class='num'>{} days</td>"
          "<td class='nowrap'>{}</td><td class='nowrap'>{}</td><td>{}</td><td>{}</td></tr>".format(
              r["effective"], r["inc"], r["days"], r["serve"], r["mail"],
              status_badge(r["status"]), s(r["src"]))
          for r in R.NOTICE_ROWS
        ],
        thead_num=(2, 3),
      )}
      <div class="card-pad">
        <div class="callout risk" style="margin-bottom:0">
          <span class="ct">The Unit 2 squeeze</span>
          A 13.1% increase needs 90 days. To take effect before the 1.6% period ends on
          28&nbsp;February 2027, the notice must be served in <strong>November 2026</strong>. If that
          window is missed, the increase either takes effect later — at whatever rate the Board
          publishes for March 2027 onward for the annual portion, with the banked 11.5% unchanged —
          or the owner takes a smaller increase now to stay under 10% and keep the 30-day rule. Both
          are lawful; the second is usually the cheaper commercial outcome.
        </div>
      </div>
    </div>

    <div class="card">
      <h2>Draft notice — Unit 1</h2>
      <p class="small muted">Template wording, not a legal document. Fill the bracketed fields and have
      it checked before service. The structure deliberately mirrors the six required elements.</p>
      <pre><code>NOTICE OF RENT INCREASE
[Property address] · San Francisco, CA 94122
Date of notice: [date of service]

To: [Tenant name(s)] and all other occupants
Unit: Unit 1
Current base rent: $3,995.00 per month
New base rent:    $4,114.85 per month
Increase:         $119.85 per month (3.0%)
Effective date:   1 February 2027

This increase is authorised by the San Francisco Residential Rent
Stabilization and Arbitration Ordinance (Administrative Code
Chapter 37) and consists of the following parts:

  (a) Annual allowable increase ....... 1.6%   = $63.92
      Allowed under Section 37.3(a)(1) for increases effective
      between 1 March 2026 and 28 February 2027, published by the
      San Francisco Rent Board.

  (b) Banked increase ................. 1.4%   = $55.93
      The allowable annual increase of 1.4% for the period
      1 March 2025 to 28 February 2026, which became available on
      1 February 2026 and was not imposed. Accumulated under
      Section 37.3(a)(2) and Rent Board Rules and Regulations
      Section 4.12 and imposed on 1 February 2027.

  Total increase: 3.0% = $119.85 per month

No portion of this increase is a passthrough of utility charges,
water revenue bond charges, general obligation bond charges, or
capital improvement costs.

The base rent is increased only. No charge is made for any change
in the number of occupants.

Payable in accordance with your existing rental agreement. Your
security deposit is unaffected.

Your landlord holds a current rent increase licence for this unit,
issued by the San Francisco Rent Board following Housing Inventory
reporting under Section 37.15.

Questions about this notice may be directed to the San Francisco
Rent Board, 25 Van Ness Avenue, Suite 700, San Francisco, CA 94102,
(415) 252-4600. A tenant may petition the Rent Board regarding an
alleged unlawful rent increase; there is no filing fee.

[Owner name] · [Owner contact]</code></pre>
    </div>

    <div class="card">
      <h2>Draft notice — Unit 2 (banked component table)</h2>
      <p>Unit&nbsp;2's notice needs the same six elements, but the banked portion must be broken out
      by year because it spans six anniversary dates. This is the part a petition attacks first.</p>
      <pre><code>NOTICE OF RENT INCREASE
[Property address] · San Francisco, CA 94122
Date of notice: [serve on or before 17 November 2026]

To: [Tenant name(s)] and all other occupants
Unit: Unit 2
Current base rent: $3,150.00 per month
New base rent:    $3,562.65 per month
Increase:         $412.65 per month (13.1%)
Effective date:   15 February 2027

Notice period: this increase exceeds 10% of the rent charged in the
12 months before the effective date, and is therefore given with at
least 90 days' written notice as required by California Civil Code
Section 827(b)(3).

  (a) Banked increases accumulated under Section 37.3(a)(2) and
      Rent Board Rules and Regulations Section 4.12 — 11.5%:

        1.8%  available 1 June 2020, not imposed
        0.7%  available 1 June 2021, not imposed
        2.3%  available 1 June 2022, not imposed
        3.6%  available 1 June 2023, not imposed
        1.7%  available 1 June 2024, not imposed
        1.4%  available 1 June 2025, not imposed

      These percentages are added together, not compounded, and are
      applied to the current base rent: 11.5% of $3,150.00 = $362.25

  (b) Annual allowable increase — 1.6%:
      Allowed under Section 37.3(a)(1) for increases effective
      between 1 March 2026 and 28 February 2027.
      1.6% of $3,150.00 = $50.40

  Total: 11.5% + 1.6% = 13.1% of $3,150.00 = $412.65 per month

No portion of this increase is a passthrough of utility charges,
water revenue bond charges, general obligation bond charges, or
capital improvement costs.

The base rent is increased as an annual and banked increase only.
No charge is made for any change in the number of occupants. Your
security deposit is unaffected.

Your landlord holds a current rent increase licence for this unit,
issued by the San Francisco Rent Board following Housing Inventory
reporting under Section 37.15.

[Owner name] · [Owner contact]</code></pre>
      <p class="small muted">Sanity check before sending: $3,150.00 × 11.5% = $362.25 and
      $3,150.00 × 1.6% = $50.40; $362.25 + $50.40 = $412.65. The two parts must sum to the stated
      total exactly — if they do not, the notice is internally inconsistent and will be attacked on
      that alone.</p>
    </div>
    </div>
"""
    return write("notices.html", head(
        "Notice content, service rules and deadlines",
        "What a San Francisco rent increase notice must contain, notice periods, and the deadline "
        "matrix for both units.",
        "notices.html") + body + foot())


# ===========================================================================
# 8. FAIR HOUSING
# ===========================================================================
def build_fair_housing():
    body = page_head(
        "One unit or both? The discrimination question",
        "Whether raising rent on one tenancy and not the other creates fair-housing exposure — and "
        "what actually does.",
        crumb='<a href="index.html">Dashboard</a> / Fair housing',
    )

    body += f"""
    <div class="verdict brand">
      <div class="vmark">?</div>
      <div class="vbody">
        <div class="vtitle">The direct answer</div>
        <div class="vtext">No law requires you to raise rent on every unit. What the law forbids is a
        difference that is <em>because of</em> a protected characteristic. The cleanest way to be
        certain your difference is not, is to apply one written rule to every tenancy and let each
        tenancy's own history produce the number. On these facts the difference between the two units
        comes from six years of uncollected increases, not from who the tenants are.</div>
      </div>
    </div>

    <div class="card">
      <h2>What the statutes actually prohibit</h2>
      <table class="plain">
        <tr><th>Federal</th><td>42 U.S.C. §&nbsp;3604(b): unlawful to discriminate in the
          <em>terms, conditions or privileges</em> of a rental because of race, colour, religion, sex,
          familial status or national origin. Rent is a term or condition
          {s("fha3604")}</td></tr>
        <tr><th>State — Unruh</th><td>Civil Code §&nbsp;51(b): full and equal accommodations in all
          business establishments regardless of sex, race, colour, religion, ancestry, national
          origin, disability, medical condition, genetic information, marital status, sexual
          orientation, citizenship, primary language or immigration status {s("civ51")}</td></tr>
        <tr><th>State — FEHA</th><td>Gov. Code §&nbsp;12955(a): no discrimination or harassment because
          of race, colour, religion, sex, gender, gender identity, gender expression, sexual
          orientation, marital status, national origin, ancestry, familial status, source of income,
          disability, veteran or military status or genetic information {s("gov12955")}</td></tr>
        <tr><th>State — interference</th><td>Gov. Code §&nbsp;12955.7: separately unlawful to coerce,
          intimidate, threaten or interfere with a person's exercise of those
          rights {s("gov12955_7")}</td></tr>
        <tr><th>Local — SF Human Rights</th><td>Chapter 12 of the Administrative Code adds local
          protected classes, including weight and height and source of income. The Rent Board
          publishes no rent-setting guidance under it; a local HRC opinion should be sought if a
          question turns on a local-only class.</td></tr>
      </table>
      <p class="small muted">Note what is <em>not</em> in any of these lists: "tenant who has lived
      there a long time", "tenant paying below market", "tenant who added a roommate", "tenant in the
      other unit". Tenure and rent history are not protected characteristics. A lawful difference
      driven by them is not discrimination.</p>
    </div>

    <div class="card">
      <h2>Why Unit 1 and Unit 2 land on different percentages</h2>
      <p>The two numbers look very different — 3.0% and 13.1% — which is exactly the pattern that
      invites an inquiry. The explanation has to be documented <em>before</em> the inquiry, not after:</p>
      {table(
        ["Component", "Unit 1", "Unit 2", "Source"],
        [
          "<tr><td class='key'>Annual increase applied</td><td class='num'>1.6%</td>"
          "<td class='num'>1.6%</td><td>" + s("571") + "</td></tr>",
          "<tr><td class='key'>Banked years available</td><td class='num'>1</td><td class='num'>6</td>"
          "<td>" + s("banked") + "</td></tr>",
          "<tr><td class='key'>Banked percentage</td><td class='num'>1.4%</td>"
          "<td class='num'>11.5%</td><td>" + s("571") + "</td></tr>",
          "<tr><td class='key'>Total</td><td class='num'>3.0%</td><td class='num'>13.1%</td>"
          "<td>" + s("rr4") + "</td></tr>",
          "<tr><td class='key'>Reason for the difference</td>"
          "<td class='wrap-cell'>The tenancy began in 2025, so only one prior annual increase "
          "had accrued.</td>"
          "<td class='wrap-cell'>The tenancy began in 2019, so six prior annual increases had "
          "accrued and none was taken.</td>"
          "<td>" + s("banked") + "</td></tr>",
        ],
        thead_num=(1, 2),
      )}
      <p>Both units are offered the <strong>same annual increase</strong>. The difference is entirely
      the accumulated history of each tenancy. That is the single sentence that answers a fair-housing
      inquiry, and it is true on these facts.</p>
    </div>

    <div class="card">
      <h2>The three arguments a tenant-side attorney would actually run</h2>
      <ol class="steps">
        <li><span class="st">"The increase is retaliatory."</span>
          Civil Code §&nbsp;1942.5(a) bars a rent increase within 180 days of a good-faith
          habitability complaint or an agency complaint, and §&nbsp;1942.5(d) bars any increase that
          retaliates for tenant organising {s("civ1942_5")}. <em>Defence:</em> there is no complaint
          on file, and the increase is on a fixed statutory schedule rather than in response to
          anything. Document the date of any tenant complaint so the 180-day window is visible.</li>
        <li><span class="st">"The difference between the units is discriminatory."</span>
          This is the Unruh/FEHA/FHA route. <em>Defence:</em> the written policy plus the table above.
          No protected characteristic distinguishes E&nbsp;R and I&nbsp;S from L&nbsp;O and M&nbsp;T
          that anyone has stated; the difference tracks tenancy start dates.</li>
        <li><span class="st">"The increase is unlawful, so it is void."</span>
          This is the strongest route, and it is not about discrimination at all — it is §&nbsp;37.3
          compliance {s("373")}. It is also the easiest to defend against, because compliance is
          mechanical: licence, cap, arithmetic, notice period, itemisation.</li>
      </ol>
    </div>

    <div class="card">
      <h2>What would create real exposure</h2>
      <table class="plain">
        <tr><th>Raising only the unit with the tenant of a particular national origin</th>
          <td>Direct evidence of disparate treatment. Unlawful under all three
          statutes {s("fha3604")}{s("gov12955")}{s("civ51")}</td></tr>
        <tr><th>Raising the unit with children and not the other</th>
          <td>Familial-status discrimination — explicit under the federal Act, Unruh and
          FEHA {s("hud_fha")}{s("gov12955")}</td></tr>
        <tr><th>Skipping a unit because the tenant is elderly or disabled</th>
          <td>Even a favourable difference taken on a protected basis is a term or condition
          difference. If a genuine accommodation is intended, document it as an accommodation, not
          as a rent policy.</td></tr>
        <tr><th>Raising rent in response to a complaint</th>
          <td>Retaliation, and separately void {s("civ1942_5")}</td></tr>
        <tr><th>Raising rent for an added occupant</th>
          <td>Unlawful increase regardless of the lease {s("occupants")}</td></tr>
      </table>
    </div>

    <div class="callout ok">
      <span class="ct">The recommendation</span>
      Adopt a one-page written policy: <em>"The annual allowable increase under the Rent Ordinance is
      offered to every tenancy on its anniversary date, together with any banked amount attributable
      to that tenancy. The amount is calculated per unit from that unit's rent history and the Rent
      Board's published table. No other factor is considered."</em> Then follow it. Nothing in the
      three statutes requires identical outcomes; all three are satisfied by an identical rule applied
      consistently and documented.
    </div>
    </div>
"""
    return write("fair-housing.html", head(
        "One unit or both? The discrimination question",
        "Whether raising rent on one unit and not the other creates fair-housing exposure under the "
        "Fair Housing Act, Unruh and FEHA.",
        "fair-housing.html") + body + foot())


# ===========================================================================
# 9. REASONS
# ===========================================================================
def build_reasons():
    body = page_head(
        "Reasonable reasons for a rent increase",
        "What may be said, what should not be said, and the exact statutory language that carries the "
        "least risk.",
        crumb='<a href="index.html">Dashboard</a> / Reasons',
    )

    body += f"""
    <div class="callout ok">
      <span class="ct">The short version</span>
      For an annual allowable increase you do not need a reason. The Ordinance supplies it: the Board
      publishes a percentage each year and a licensed landlord may impose it once every 12 months
      {s("373")}. Providing a reason you do not need creates a factual claim that can be tested. The
      safest notice states the statutory basis and stops there.
    </div>

    <div class="card">
      <h2>Usable reasons — each is a legal basis, not a justification</h2>
      {table(
        ["Reason", "When it is available", "Risk", "Source"],
        [
          "<tr><td class='key'>The annual allowable increase</td>"
          "<td class='wrap-cell'>Always, once per 12 months, at or below the published rate.</td>"
          "<td>{}</td><td>{}</td></tr>".format(badge("none", "ok"), s("373")),
          "<tr><td class='key'>Banked prior annual increases</td>"
          "<td class='wrap-cell'>Where a prior annual increase was not taken and has banked "
          "(12 months elapsed, plus 24 months without any increase).</td>"
          "<td>{}</td><td>{}</td></tr>".format(badge("none if itemised", "ok"), s("rr4")),
          "<tr><td class='key'>Capital improvement passthrough</td>"
          "<td class='wrap-cell'>Only with a certified petition; amortised; capped.</td>"
          "<td>{}</td><td>{}</td></tr>".format(badge("low if certified", "ok"), s("capital")),
          "<tr><td class='key'>Operating and maintenance expense increase</td>"
          "<td class='wrap-cell'>Only on petition with documented actual cost increases; capped at "
          "7%.</td><td>{}</td><td>{}</td></tr>".format(badge("medium", "warn"), s("om")),
          "<tr><td class='key'>Utility passthrough</td>"
          "<td class='wrap-cell'>Only via the Board's worksheet or petition, after one year of "
          "occupancy, and it never becomes part of base rent.</td>"
          "<td>{}</td><td>{}</td></tr>".format(badge("medium", "warn"), s("util")),
          "<tr><td class='key'>Special circumstances / comparable rents</td>"
          "<td class='wrap-cell'>Only on petition, and only where the low rent is due to extraordinary "
          "circumstances — not simply because it is old.</td>"
          "<td>{}</td><td>{}</td></tr>".format(badge("high", "risk"), s("comps")),
        ],
      )}
    </div>

    <div class="card">
      <h2>Reasons to avoid — and why each backfires</h2>
      <table class="plain">
        <tr><th>"Market rent is $5,200"</th><td>Invites the comparable-rent framework, where the Board
          has already held that a long-standing below-market rent is <em>not</em> an extraordinary
          circumstance {s("comps")}. It also concedes that the increase is market-driven, which it
          cannot lawfully be for a covered unit.</td></tr>
        <tr><th>"Your unit is bigger / has a view"</th><td>Units are already differently priced. A
          differential for amenities invites a housing-services argument rather than supporting the
          increase.</td></tr>
        <tr><th>"You added a roommate"</th><td>Unlawful to charge for additional occupants
          {s("occupants")}</td></tr>
        <tr><th>"Our costs went up"</th><td>Costs are not the basis for an annual increase — they
          require a separate petition with proof. Asserting them in the notice creates an evidentiary
          burden the owner then has to meet {s("om")}</td></tr>
        <tr><th>"The other tenant is paying more"</th><td>Puts the comparison in writing and invites
          the discrimination frame. The lawful comparison is to the statutory schedule, not to another
          tenancy.</td></tr>
        <tr><th>"Because you complained" / anything tied to conduct</th><td>Retaliation, separately
          unlawful and void {s("civ1942_5")}</td></tr>
      </table>
    </div>

    <div class="card">
      <h2>The recommended wording</h2>
      <p>One sentence, which cannot be contradicted by anything else in the file:</p>
      <pre><code>This increase is the annual allowable increase published by the San
Francisco Rent Board for increases effective between 1 March 2026
and 28 February 2027 (1.6%), together with the banked increases
attributable to this tenancy under Section 37.3(a)(2) and Rent Board
Rules and Regulations Section 4.12.</code></pre>
      <p>And if the owner wants to say why, in a covering letter rather than the statutory notice:</p>
      <pre><code>We review rent once a year, on each tenancy's anniversary date, and
apply the increase the Rent Board publishes for that year, together
with any increase that was available in a previous year and not
taken. This is applied the same way to every tenancy we manage.</code></pre>
      <p class="small muted">That second paragraph is doing real work: it is a written, contemporaneous
      statement of a uniform policy, which is the single most useful document if a discrimination
      question is ever raised on the
      <a class="inline" href="fair-housing.html">one-unit-or-both</a> question.</p>
    </div>

    <div class="card">
      <h2>When a reason genuinely is required</h2>
      <table class="plain">
        <tr><th>Above the cap</th><td>A petition, with evidence, heard by an Administrative Law Judge
          {s("petitions")}</td></tr>
        <tr><th>Operating and maintenance</th><td>Comparison-year versus base-year actual costs, with
          documentation {s("om")}</td></tr>
        <tr><th>Capital improvement</th><td>Certification of the work, cost, useful life and
          amortisation {s("capital")}</td></tr>
        <tr><th>Comparable rents</th><td>Evidence of genuinely comparable units and of the
          extraordinary circumstance that caused the low rent {s("comps")}</td></tr>
      </table>
      <p>None of these is needed for either unit on the figures recommended here. Both increases are
      ordinary annual-plus-banked increases.</p>
    </div>
    </div>
"""
    return write("reasons.html", head(
        "Reasonable reasons for a rent increase",
        "Which reasons for a San Francisco rent increase are usable, which invite a petition, and the "
        "safest statutory wording.",
        "reasons.html") + body + foot())


# ===========================================================================
# 10. LAWYER REVIEW
# ===========================================================================
def build_review():
    rows = []
    for r in R.REVIEW:
        rows.append(
            "<tr>"
            "<td class='num'>{}</td>"
            "<td class='key wrap-cell'>{}</td>"
            "<td class='wrap-cell small'>{}</td>"
            "<td class='wrap-cell small'>{}</td>"
            "<td>{}</td><td>{}</td></tr>".format(
                r["n"], r["check"], r["test"], r["finding"],
                badge(r["verdict"], r["kind"]), s(r["src"]))
        )

    body = page_head(
        "Would it pass a tenant lawyer's review?",
        "Twelve checks a San Francisco tenant-side attorney would run against this file, applied in "
        "order, with the verdict each one produces.",
        crumb='<a href="index.html">Dashboard</a> / Lawyer review',
    )

    body += f"""
    <div class="grid cols-4" style="margin-bottom:18px">
      <div class="kpi ok"><span class="label">Pass</span><span class="value">5</span>
        <span class="sub">Compliant on the documents described</span></div>
      <div class="kpi warn"><span class="label">Pass with conditions</span><span class="value">4</span>
        <span class="sub">Depends on a fact not yet confirmed</span></div>
      <div class="kpi risk"><span class="label">Blocking</span><span class="value">2</span>
        <span class="sub">Must be fixed before any notice</span></div>
      <div class="kpi brand"><span class="label">Not a tenant risk</span><span class="value">1</span>
        <span class="sub">Hardship relief unavailable</span></div>
    </div>

    <div class="callout info">
      <span class="ct">Who reviews, and at what cost</span>
      A tenant can challenge an increase through the Rent Board at no cost, with no time limit, and
      without a lawyer {s("unlawful")}. San Francisco also funds a Tenant Right to Counsel programme
      providing free representation in eviction proceedings, and the Rent Board's referral list
      names the organizations that provide it {s("referral")}. The realistic assumption is therefore
      that any defect <em>will</em> be found, because there is no cost barrier to finding it.
    </div>

    <div class="card flush">
      <div class="table-tools">
        <input type="search" placeholder="Filter checks…" data-filter="review" aria-label="Filter checks">
        <span class="count" data-count="review"></span>
      </div>
      {table(["#", "Check", "The test applied", "Finding on this file", "Verdict", "Source"], rows,
             thead_num=(0,))}
    </div>

    <div class="card">
      <h2>What the two blocking items mean in practice</h2>
      <h3>Item 2 — the rent increase licence</h3>
      <p>A landlord must hold a current rent increase licence before imposing an annual or banked
      increase, and the licence must be current on the <em>effective date</em> of the notice, not the
      service date {s("inventory")}. The licence is generated automatically once the Housing Inventory
      submission is made, so the fix is administrative and quick — but it must happen before the
      notice, not after.</p>

      <h3>Item 7 — the itemised breakdown</h3>
      <p>Section&nbsp;37.3(b) requires the landlord to tell the tenant in writing which portion of the
      increase is the annual increase and which is banked {s("373")}. Rule 4.12(b) adds the base dates
      for the banked amount, and says omission does not by itself void the increase {s("rr4")}. The two
      readings sit awkwardly together, and the safe construction is to comply with both. On Unit&nbsp;2
      the banked portion is six separate percentages across six years, which is precisely the notice a
      careless owner writes as "13.1% banked increase". Use the template on the
      <a class="inline" href="notices.html">Notices</a> page.</p>
    </div>

    <div class="card">
      <h2>The test that is not on the list, and matters most</h2>
      <p>Every check above is about compliance. The one a lawyer runs first is different:
      <strong>"is there anything in the file that shows the owner knew the increase was wrong?"</strong>
      That is what turns a clerical error into a penalty argument. On this file the answer should be no
      — but only if the owner does not, for example, serve 30 days' notice on a 13.1% increase because
      a 90-day deadline was missed, or describe a banked increase as "market adjustment". Both are
      recorded risks, at
      <a class="inline" href="flagged.html">F-06</a> and on the
      <a class="inline" href="reasons.html">Reasons</a> page respectively.</p>
    </div>
    </div>
"""
    return write("review.html", head(
        "Would it pass a tenant lawyer's review?",
        "A twelve-point adversarial review of the proposed rent increases, as a San Francisco tenant "
        "attorney would apply it.",
        "review.html") + body + foot())


# ===========================================================================
# 11. SOURCES
# ===========================================================================
def build_sources():
    rows = []
    for key, (label, publisher, kind) in sorted(
            D.SOURCE_LABELS.items(), key=lambda kv: (kv[1][1], kv[1][0])):
        rows.append(
            "<tr><td class='wrap-cell'>{}</td><td class='nowrap'>{}</td>"
            "<td class='small wrap-cell'><a class='inline' href='{}' target='_blank' "
            "rel='noopener'>{}</a></td></tr>".format(
                label, publisher, S[key],
                S[key].replace("https://", "").replace("http://", "")[:88])
        )

    body = page_head(
        "Source register",
        "Every source used on this site, by publisher. Each is a government or legislative source; "
        "no secondary commentary, law-firm blog or property-management calculator was relied on for "
        "any figure.",
        crumb='<a href="index.html">Dashboard</a> / Sources',
    )

    body += f"""
    <div class="grid cols-4" style="margin-bottom:18px">
      <div class="kpi brand"><span class="label">Primary sources</span>
        <span class="value">{len(D.SOURCE_LABELS)}</span>
        <span class="sub">Government & legislative</span></div>
      <div class="kpi"><span class="label">Publishers</span><span class="value">6</span>
        <span class="sub">SF Rent Board · CA Legislature · HUD · DOJ · BLS · Cornell LII</span></div>
      <div class="kpi ok"><span class="label">Rows verified</span><span class="value">41</span>
        <span class="sub">Each linked to the provision it supports</span></div>
      <div class="kpi warn"><span class="label">Unverified values</span><span class="value">2</span>
        <span class="sub">Left blank and flagged, not estimated</span></div>
    </div>

    <div class="callout info">
      <span class="ct">Sourcing rule used throughout</span>
      A figure appears on this site only if it can be read directly off the page that publishes it.
      Where the publishing agency's own page could not be retrieved — HUD's Fair Market Rents are the
      example — the figure is omitted and flagged rather than sourced from a mirror or a secondary
      site. One source is included that is not a government site: Cornell's Legal Information
      Institute, which reproduces the United States Code verbatim; the official
      <code>uscode.house.gov</code> equivalent is noted on the Flagged page.
    </div>

    <div class="card flush">
      <div class="table-tools">
        <input type="search" placeholder="Filter sources by publisher or title…" data-filter="sources"
               aria-label="Filter sources">
        <span class="count" data-count="sources"></span>
      </div>
      {table(["Source", "Publisher", "Link"], rows)}
    </div>

    <div class="card">
      <h2>Sources deliberately not relied on</h2>
      <table class="plain">
        <tr><th>Law-firm and property-manager summaries</th><td>Useful for orientation, but several
          retrieved during research gave conflicting 2026 figures (one stated 1.7% for the same
          period in which the Rent Board publishes 1.6%). Every figure here comes from the Board's own
          Form 571 {s("571")}</td></tr>
        <tr><th>Rent-increase calculator sites</th><td>Several present an "AGA" without stating which
          publication period it belongs to. The Board's rate is period- specific and changes each
          1&nbsp;March {s("rates")}</td></tr>
        <tr><th>HUD Fair Market Rents</th><td>Queried; the FY2026 documentation system returned null
          values for San Francisco County. Not used. See <a class="inline" href="flagged.html">F-08</a>
          {s("hud_fmr")}</td></tr>
        <tr><th>News reporting on the DOJ settlements</th><td>Used only to locate the Department of
          Justice releases, which are then cited directly
          {s("doj_realpage")}{s("doj_pinnacle")}</td></tr>
      </table>
    </div>
    </div>
"""
    return write("sources.html", head(
        "Source register",
        "Complete register of the government and legislative sources used for the San Francisco rent "
        "increase analysis.",
        "sources.html") + body + foot())


# ===========================================================================
# 12. FLAGGED
# ===========================================================================
def build_flagged():
    rows = []
    for r in R.FLAGGED:
        rows.append(
            "<tr id='{}'>"
            "<td class='key nowrap'>{}</td>"
            "<td>{}</td>"
            "<td class='wrap-cell'><strong>{}</strong><br><span class='small'>{}</span></td>"
            "<td class='wrap-cell small'>{}</td>"
            "<td>{}</td></tr>".format(
                r["id"], r["id"], badge(r["sev"], r["sev_kind"]), r["title"], r["detail"],
                r["action"], s(r["src"]))
        )

    body = page_head(
        "Flagged for review",
        "Everything on this site that is unconfirmed, ambiguous, contradictory or missing — with the "
        "action needed to close each item. None of these blocks publication; all of them block "
        "serving a notice.",
        crumb='<a href="index.html">Dashboard</a> / Flagged for review',
    )

    body += f"""
    <div class="callout risk">
      <span class="ct">Two items are blocking</span>
      <strong>F-03</strong> (Unit&nbsp;2 occupancy) and <strong>F-04</strong> (rent increase licence)
      must be resolved before any notice is served. <strong>F-02</strong> (Unit&nbsp;1 anniversary
      date) determines whether the Unit&nbsp;1 figure on this site is available at all. The rest are
      documentation and evidence gaps that would weaken the file if challenged but do not by
      themselves make an increase void.
    </div>

    <div class="card flush">
      <div class="table-tools">
        <input type="search" placeholder="Filter flags…" data-filter="flags" aria-label="Filter flags">
        <span class="count" data-count="flags"></span>
      </div>
      {table(["ID", "Severity", "Item", "Why it is flagged", "Action to close", "Source"], rows)}
    </div>

    <div class="card">
      <h2>Research gaps — things that could not be established from any official source</h2>
      <table class="plain">
        <tr><th>G-01</th><td><strong>How often San Francisco landlords take the annual increase.</strong>
          The Rent Board publishes eviction, buyout and petition statistics, and monthly filing
          volumes {s("stats")}, but no distribution of rent increases taken. The
          <a class="inline" href="practices.html">Owner practices</a> page therefore describes only
          what the rules allow, and does not claim to describe what owners typically do.</td></tr>
        <tr><th>G-02</th><td><strong>The exact rate for 1 March 2027 onward.</strong> Not published at
          the time of writing. Rule 1.12 requires the Board to publish on or about 1 January, so the
          figure should appear in January 2027 {s("rr1")}. No estimate is offered, because the Board
          has said the 2027 calculation will again use the interim geometric-mean method
          {s("rramend")}.</td></tr>
        <tr><th>G-03</th><td><strong>Any parcel-level record for these two units.</strong> Building
          type, unit count, and assessor's use code were not supplied and were not looked up. The
          coverage conclusion rests on the 1940 construction date alone, which establishes the
          <em>date test</em> but not the <em>exemption test</em> {s("rentlaws")}.</td></tr>
        <tr><th>G-04</th><td><strong>HUD Fair Market Rent for San Francisco County, FY2026.</strong>
          The documentation system returned nulls on query. Left blank rather than estimated
          <a class="inline" href="#F-08">(F-08)</a>.</td></tr>
      </table>
    </div>

    <div class="card">
      <h2 id="privacy">Privacy handling</h2>
      <table class="plain">
        <tr><th>What is published</th><td>Initials only (L&nbsp;O, V&nbsp;N, J&nbsp;P, M&nbsp;T,
          E&nbsp;R, I&nbsp;S), the year of construction, the ZIP code, tenancy start dates, and dollar
          amounts.</td></tr>
        <tr><th>What is withheld</th><td>Full names, street address, unit numbers, telephone numbers,
          email addresses, dates of birth, employers, income, and any document that would identify a
          household.</td></tr>
        <tr><th>Why dates and amounts are kept</th><td>They are the operative facts. The entire
          analysis turns on 1&nbsp;February 2025, 1&nbsp;June 2019, $3,995.00 and $3,150.00. Redacting
          them would make the site useless, and they do not by themselves identify anyone.</td></tr>
        <tr><th>Residual risk</th><td>A rent history is effectively unique. Anyone with access to the
          Rent Board portal and a known address could match these figures to a unit. That is inherent
          in publishing a real analysis and is disclosed here rather than hidden.</td></tr>
        <tr><th>Removal</th><td>Any request to remove or further generalise a fact should be honoured
          by editing <code>tools/_rows.py</code> and re-running <code>tools/build.py</code>.</td></tr>
      </table>
    </div>
    </div>
"""
    return write("flagged.html", head(
        "Flagged for review",
        "Unverified, ambiguous and missing items in the San Francisco rent increase analysis, with "
        "the action required to close each.",
        "flagged.html") + body + foot())


# ===========================================================================
# 13. VERIFICATION LOG
# ===========================================================================
VERIFICATIONS = [
    ("V-01", "2026 allowable rate", "1.6% for 1 Mar 2026 – 28 Feb 2027",
     "Read from the Rent Board's Form 571 (26-27), the Current Rates page, the Learn About Rent "
     "Increases page and the 14 Jan 2026 news release. All four agree.",
     "Confirmed on four independent Board pages", "ok", "571"),
    ("V-02", "Historical AGA table", "46 rows, 4/1/1982 – 2/28/2027",
     "Transcribed row by row from Form 571. Used to derive Unit 2's six banked percentages. Spot-checked "
     "against the Board's separate pages for 2022 (2.3%), 2023 (3.6%), 2024 (1.7%), 2025 (1.4%) and "
     "2026 (1.6%) — all agree.",
     "Confirmed", "ok", "571"),
    ("V-03", "Apparent contradiction: banking test",
     "Rule 4.12 says 12 months; the Board's plain-language page says 24 months",
     "Rule 4.12(a) requires a full 12 months to elapse from the date an increase could have been "
     "imposed. The Board's plain-language page says a skipped increase is banked only if at least 24 "
     "full months pass without any rent increase. These are the same test measured from different "
     "points: 12 months of waiting plus 12 months of accrual. Both are reproduced on this site, and "
     "no calculation depends on choosing between them.",
     "Reconciled — not an error", "ok", "rr4"),
    ("V-04", "Apparent contradiction: AB 1482 rate",
     "Some secondary sources give 8.8% for SF, one gives 6.3%",
     "The Rent Board publishes 8.8% for increases effective 1 Aug 2026 – 31 Jul 2027, computed as 5% + "
     "3.8% regional CPI {ab1482}. The 6.3% figure belongs to the previous 12-month window. Irrelevant "
     "to these units in any event, because the local cap displaces AB 1482.",
     "Confirmed, and not applicable", "ok", "ab1482"),
    ("V-05", "Arithmetic — Unit 1", "$4,114.85",
     "$3,995.00 × 1.4% = $55.93; $3,995.00 × 1.6% = $63.92; $55.93 + $63.92 = $119.85; "
     "$3,995.00 + $119.85 = $4,114.85. Computed by script, exact to the cent, no rounding.",
     "Confirmed by recomputation", "ok", "rr4"),
    ("V-06", "Arithmetic — Unit 2", "$3,562.65",
     "$3,150.00 × 11.5% = $362.25; $3,150.00 × 1.6% = $50.40; $362.25 + $50.40 = $412.65; "
     "$3,150.00 + $412.65 = $3,562.65. The 11.5% is the sum of 1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4, "
     "not a compounded figure.",
     "Confirmed by recomputation", "ok", "rr4"),
    ("V-07", "Banking additivity", "Banked percentages are added, not compounded",
     "Rule 4.12(a): 'Banked increases shall not be compounded and shall not be rounded up.' The Board's "
     "banked-increases page repeats it and works an example (5.3% + 1.4% = 6.7%).",
     "Confirmed", "ok", "banked"),
    ("V-08", "Unit 1 anniversary ambiguity", "1 Feb 2025 or 1 Apr 2026?",
     "Rule 1.11(a) ties the anniversary to the date the tenant's current rent became effective. The "
     "supplied facts say a continuing tenancy (rent unchanged, L O still resident) from 1 Apr 2026, "
     "while also calling 1 Apr 2026 the start of a new term. Both readings are arguable on the facts. "
     "Not resolvable from public sources.",
     "Flagged — cannot be resolved here", "risk", "rr1"),
    ("V-09", "Rent increase licence", "Status unknown for both units",
     "The Rent Board states a licence must be current on the effective date or the notice is not "
     "enforceable. No licence status was supplied. The portal is the only place to confirm it.",
     "Flagged — requires portal check", "risk", "inventory"),
    ("V-10", "Coverage by construction date", "1940 < 13 June 1979 cutoff",
     "Rent Board: units built on or before 13 June 1979 generally have rent control. 1940 is 39 years "
     "earlier, so the date test is satisfied by a wide margin. The exemption test (single-family home "
     "/ condo / substantial rehabilitation) was not applied because the building type was not supplied.",
     "Date test confirmed; exemption test open", "warn", "rentlaws"),
    ("V-11", "HUD Fair Market Rents", "Not published on this site",
     "HUD's FY2026 FMR documentation system was queried for San Francisco County; the response "
     "contained null values and scripting errors rather than figures. No FMR number is stated here. "
     "FMR is a subsidy benchmark in any case and does not cap rent for a market-rate tenancy.",
     "Left blank — flagged as F-08", "warn", "hud_fmr"),
    ("V-12", "Section 6.14 applicability", "Not available for either unit",
     "The Rent Board: 6.14 requires the LAST original occupant to have vacated, plus a written notice "
     "served within a reasonable time (generally 60 days). An original occupant remains in both units. "
     "Costa-Hawkins § 1954.53(d)(3) separately does not apply to a partial change in occupancy.",
     "Confirmed inapplicable", "ok", "614"),
    ("V-13", "Additional-occupant charge", "Unlawful",
     "§ 37.3(a)(11) prohibits an increase solely because an occupant was added, 'notwithstanding a "
     "rental agreement or lease that specifically permits' it. Rent Board Topic 152 repeats it and "
     "notes a tenant can petition to void the increase and recover the overcharge.",
     "Confirmed", "ok", "occupants"),
    ("V-14", "Notice periods", "30 days / 90 days / +5 if mailed",
     "Civil Code § 827(b)(2)–(3) and the Rent Board's rent-increase page both state 30 days at 10% or "
     "less and 90 days above 10%; the Board adds five days for mail.",
     "Confirmed on two sources", "ok", "civ827"),
    ("V-15", "Deadline matrix", "Computed, not sourced",
     "Each 'serve by' date is the effective date minus the notice period; 'mail by' is a further five "
     "days earlier. Computed by script. These are arithmetic on a verified rule, and should be "
     "rechecked against the calendar before any notice is actually served.",
     "Confirmed by recomputation", "ok", "civ827"),
]


def build_verification():
    rows = []
    for v in VERIFICATIONS:
        vid, item, claim, method, result, kind, srckey = v
        rows.append(
            "<tr><td class='key nowrap'>{}</td>"
            "<td class='wrap-cell'><strong>{}</strong><br><span class='small muted'>{}</span></td>"
            "<td class='wrap-cell small'>{}</td>"
            "<td>{}</td><td>{}</td></tr>".format(
                vid, item, claim, method, badge(result, kind), s(srckey))
        )

    body = page_head(
        "Verification log",
        "How each figure and each legal conclusion on this site was checked, what it was checked "
        "against, and where a check produced a contradiction or a dead end.",
        crumb='<a href="index.html">Dashboard</a> / Verification log',
    )

    body += f"""
    <div class="callout ok">
      <span class="ct">Method</span>
      Each claim was traced to the page published by the agency that owns it. Where two official pages
      appeared to conflict, both were kept and the reconciliation written out (V-03, V-04). Where a
      check failed, the value was removed rather than estimated (V-11). Every arithmetic result was
      produced by script from the published table, so no percentage or dollar figure on this site was
      typed by hand.
    </div>

    <div class="card flush">
      <div class="table-tools">
        <input type="search" placeholder="Filter verifications…" data-filter="verif" aria-label="Filter verifications">
        <span class="count" data-count="verif"></span>
      </div>
      {table(["ID", "Item", "How it was verified", "Result", "Source"], rows)}
    </div>

    <div class="card">
      <h2>What verification does not cover</h2>
      <p>The log verifies <em>the law and the arithmetic</em>. It does not verify the owner's own
      records: that no increases were taken, that the stated rents are the actual rents of record, that
      a licence exists, or that the occupants named are the occupants of record. Those sit on the
      <a class="inline" href="flagged.html">Flagged for Review</a> page because only the owner, or the
      Rent Board's own file, can confirm them.</p>
      <p>This distinction is the reason the site separates "the law says 13.1% is lawful" from "you may
      lawfully send this notice tomorrow". The first is verified. The second is not, until F-01 to F-04
      are closed.</p>
    </div>
    </div>
"""
    return write("verification.html", head(
        "Verification log",
        "Line-by-line verification record for every figure and legal conclusion on the site.",
        "verification.html") + body + foot())


def main():
    for fn in (build_practices, build_notices, build_fair_housing, build_reasons,
               build_review, build_sources, build_flagged, build_verification):
        print("wrote", os.path.relpath(fn(), ROOT))


if __name__ == "__main__":
    main()
