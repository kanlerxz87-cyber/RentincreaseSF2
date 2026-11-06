"""Shared HTML chrome for the Rental Increase SF static site.

No external dependencies. Output is plain static HTML served from the repo root
by GitHub Pages (branch `main`, path `/`, legacy build type).
"""

SITE = "Rental Increase SF"

# Ordered navigation. (href, label, short-label)
NAV = [
    ("index.html",         "Dashboard"),
    ("summary.html",       "Summary"),
    ("units.html",         "Units"),
    ("calculations.html",  "Calculations"),
    ("laws.html",          "Laws"),
    ("aga-history.html",   "AGA history"),
    ("practices.html",     "Owner practices"),
    ("notices.html",       "Notices"),
    ("fair-housing.html",  "Fair housing"),
    ("reasons.html",       "Reasons"),
    ("review.html",        "Lawyer review"),
    ("sources.html",       "Sources"),
    ("flagged.html",       "Flagged"),
    ("verification.html",  "Verification"),
]


def head(title, desc, active, extra_head=""):
    nav = "\n".join(
        '        <a href="{h}"{a}>{l}</a>'.format(
            h=h, l=l, a=' aria-current="page"' if h == active else ""
        )
        for h, l in NAV
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {SITE}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<meta property="og:title" content="{title} — {SITE}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%231d4ed8'/%3E%3Ctext x='16' y='22' font-family='system-ui,sans-serif' font-size='16' font-weight='700' fill='%23fff' text-anchor='middle'%3E%24%3C/text%3E%3C/svg%3E">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="mark" aria-hidden="true">$</span>
      <span>Rental Increase SF
        <small>Outer Sunset · ZIP 94122 · Rent Ordinance analysis</small>
      </span>
    </a>
    <nav class="nav" aria-label="Primary">
{nav}
    </nav>
  </div>
</header>
<main id="main">
"""


def foot(active=""):
    return f"""</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="disclaim">
      <strong>Not legal advice.</strong> This site organises publicly available
      official sources so a property owner can check their own numbers. It is a
      research aid, not a legal opinion. Rent Ordinance questions should be put
      to a San Francisco Rent Board counselor (415-252-4600) and, for a
      tenancy-specific opinion, to a licensed attorney. Every figure is linked
      to the agency that publishes it; anything that could not be confirmed is
      listed on the <a href="flagged.html">Flagged for Review</a> page rather
      than guessed.
    </div>
    <div>
      <a href="sources.html">Source register</a> ·
      <a href="flagged.html">Flagged for review</a> ·
      <a href="verification.html">Verification log</a> ·
      <a href="https://github.com/kanlerxz87-cyber/RentincreaseSF2">Repository</a>
    </div>
  </div>
</footer>
<script src="assets/app.js" defer></script>
</body>
</html>
"""


def page_head(h1, lede, crumb=None):
    c = ""
    if crumb:
        c = f'      <p class="crumb">{crumb}</p>\n'
    return f"""  <div class="wrap">
{c}    <div class="page-head">
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
    </div>
"""


def src(url, label=None):
    """Inline source link."""
    import re

    text = label or re.sub(r"^https?://(www\.)?", "", url).split("?")[0]
    if len(text) > 46:
        text = text[:44] + "…"
    return f'<span class="srclink">[<a href="{url}" target="_blank" rel="noopener">{text}</a>]</span>'


def badge(text, kind="muted"):
    return f'<span class="badge {kind}">{text}</span>'
