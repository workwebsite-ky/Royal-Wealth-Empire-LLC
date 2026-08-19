# -*- coding: utf-8 -*-
"""Shared chrome (head / header / footer) for every page of the site."""

SITE = "https://www.royalwealthempire.com"
EMAIL = "Theroyalwealthempire@gmail.com"
EMAIL2 = "info@royalwealthempire.com"
PHONE = "(331) 205-7720"
PHONE_TEL = "+13312057720"
PHONE2 = "(630) 996-1134"
PHONE2_TEL = "+16309961134"
PHONE3 = "(331) 290-5638"
PHONE3_TEL = "+13312905638"
FB = "https://www.facebook.com/pretty.bambii.5"
IG = "https://www.instagram.com/royalwealth.empire"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="Royal Wealth Empire LLC">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{site}/{slug}">

<!-- Open Graph / social -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Royal Wealth Empire LLC">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{slug}">
<meta property="og:image" content="{site}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/assets/img/og-image.jpg">
<meta name="theme-color" content="#072220">

<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">

<!-- Fonts: Playfair Display (crest serif) · Poppins (collateral sans) · Alex Brush (script accents) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<link rel="stylesheet" href="assets/css/style.css">
{schema}
</head>
<body>

<a class="skip-link" href="#main">Skip to main content</a>

<!-- ============================ PRELOADER ============================ -->
<div id="preloader" role="status" aria-label="Loading">
  <div class="pre-inner">
    <img class="pre-crown" src="assets/img/logo-mark.png" alt="" width="90" height="61">
    <div class="pre-name">Royal Wealth Empire</div>
    <div class="pre-bar"><span></span></div>
  </div>
</div>
"""

NAV_ITEMS = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("pricing.html", "Pricing"),
    ("about.html", "About"),
    ("partners.html", "Tax Partners"),
    ("contact.html", "Contact"),
]

HEADER = """
<!-- ============================= HEADER ============================== -->
<header class="site-header">
  <nav class="nav" aria-label="Primary">
    <a class="brand" href="index.html" aria-label="Royal Wealth Empire LLC — home">
      <img src="assets/img/logo-mark.png" alt="Royal Wealth Empire LLC crown and RWE monogram logo" width="68" height="46">
      <span class="brand-text">
        <span class="brand-name">Royal Wealth Empire</span>
        <span class="brand-sub">Where Wealth Becomes Legacy</span>
      </span>
    </a>

    <div class="nav-menu">
      {links}
    </div>

    <div class="nav-cta">
      <a class="btn btn-gold btn-sm" href="contact.html">
        Book Your Free Consult
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>

<!-- Mobile drawer -->
<div class="mobile-menu" id="mobileMenu">
  {mlinks}
  <a class="btn btn-gold" href="contact.html" style="border-bottom:0">Book Your Free Consult</a>
  <p class="mm-contact">__PHONE__ &nbsp;•&nbsp; __EMAIL__</p>
</div>

<main id="main">
""".replace("__PHONE__", PHONE).replace("__EMAIL__", EMAIL)

FOOTER = """
</main>

<!-- ============================= FOOTER ============================== -->
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">

      <div class="footer-brand">
        <a class="brand" href="index.html">
          <img src="assets/img/logo-mark.png" alt="Royal Wealth Empire LLC logo" width="76" height="52">
          <span class="brand-text">
            <span class="brand-name">Royal Wealth Empire</span>
            <span class="brand-sub">Where Wealth Becomes Legacy</span>
          </span>
        </a>
        <p style="font-size:.92rem;max-width:38ch">
          Professional, accurate and reliable tax preparation for individuals and small
          businesses — led by Brittany &ldquo;Bamz&rdquo; Hill from Chicago, Illinois and
          filed virtually in all 50 states.
        </p>
        <p class="script" style="font-size:1.6rem;margin-top:14px">Together, We Are Royal.</p>
        <div class="socials">
          <a href="__FB__" target="_blank" rel="noopener" aria-label="Royal Wealth Empire on Facebook">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
          </a>
          <a href="__IG__" target="_blank" rel="noopener" aria-label="Royal Wealth Empire on Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>
          </a>
          <a href="mailto:__EMAIL__" aria-label="Email Royal Wealth Empire">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="15" rx="3"/><path d="m3 7 9 6 9-6"/></svg>
          </a>
          <a href="tel:__TEL__" aria-label="Call Royal Wealth Empire">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>
          </a>
        </div>
      </div>

      <div>
        <h4>Explore</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="about.html">About Brittany</a></li>
          <li><a href="partners.html">Become a Tax Partner</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>

      <div>
        <h4>Services</h4>
        <ul class="footer-links">
          <li><a href="services.html#individual">Individual Tax Returns</a></li>
          <li><a href="services.html#business">Business Tax Returns</a></li>
          <li><a href="services.html#bookkeeping">Bookkeeping &amp; Payroll</a></li>
          <li><a href="services.html#planning">Tax Planning &amp; Consulting</a></li>
          <li><a href="services.html#audit">Audit Support</a></li>
          <li><a href="services.html#literacy">Financial Literacy</a></li>
          <li><a href="services.html#mentorship">Mentorship</a></li>
        </ul>
      </div>

      <div>
        <h4>Connect With Me</h4>
        <ul class="footer-links">
          <li><a href="tel:__TEL__">__PHONE__ &nbsp;(office)</a></li>
          <li><a href="tel:__TEL2__">__PHONE2__</a></li>
          <li><a href="tel:__TEL3__">__PHONE3__ &nbsp;(personal)</a></li>
          <li><a href="mailto:__EMAIL__">__EMAIL__</a></li>
          <li><a href="mailto:__EMAIL2__">__EMAIL2__</a></li>
          <li>Chicago, Illinois &nbsp;•&nbsp; All 50 states</li>
          <li style="color:var(--gold-400);font-weight:600">Mon–Sat &nbsp;9:00am – 7:00pm CT</li>
        </ul>
      </div>

    </div>

    <p class="disclaimer">
      <strong>Disclaimer:</strong> Royal Wealth Empire LLC provides tax preparation, tax planning
      and financial literacy education. Information on this website is for general educational
      purposes and is not legal, investment or individualised tax advice. Fees vary based on the
      complexity of your return, the forms required and the schedules filed. Refund amounts and
      IRS processing times are determined solely by the Internal Revenue Service and applicable
      state agencies, and are never guaranteed by Royal Wealth Empire LLC.
    </p>

    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> Royal Wealth Empire LLC. All rights reserved.</p>
      <nav aria-label="Legal">
        <a href="contact.html">Privacy</a>
        <a href="contact.html">Terms</a>
        <a href="partners.html">Careers</a>
      </nav>
    </div>
  </div>
</footer>

<!-- ========================== FLOATING UI ============================ -->
<a class="quick-call" href="tel:__TEL__" aria-label="Call Royal Wealth Empire now">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>
  <span>__PHONE__</span>
</a>

<button id="toTop" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

for _a, _b in [("__FB__", FB), ("__IG__", IG),
               ("__EMAIL2__", EMAIL2), ("__EMAIL__", EMAIL),
               ("__TEL2__", PHONE2_TEL), ("__TEL3__", PHONE3_TEL), ("__TEL__", PHONE_TEL),
               ("__PHONE2__", PHONE2), ("__PHONE3__", PHONE3), ("__PHONE__", PHONE)]:
    FOOTER = FOOTER.replace(_a, _b)


def header_for(slug):
    links = "\n      ".join(
        '<a href="{0}"{1}>{2}</a>'.format(
            href, ' class="active"' if href == slug else "", label)
        for href, label in NAV_ITEMS
    )
    mlinks = "\n  ".join(
        '<a href="{0}">{1}</a>'.format(href, label) for href, label in NAV_ITEMS
    )
    return HEADER.format(links=links, mlinks=mlinks)
