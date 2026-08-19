# -*- coding: utf-8 -*-
"""Assembles the static site: src/<page>.html body + shared head/header/footer."""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from template import HEAD, FOOTER, header_for, SITE, EMAIL, PHONE, PHONE_TEL, FB, IG

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "build", "src")

ORG_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": ["AccountingService", "ProfessionalService"],
    "name": "Royal Wealth Empire LLC",
    "alternateName": "Royal Wealth Empire",
    "description": ("Virtual tax preparation, tax planning and business filing services for "
                    "individuals and small businesses in all 50 states, led by Founder & CEO "
                    "Brittany “Bamz” Hill."),
    "url": SITE,
    "logo": SITE + "/assets/img/logo-full.jpg",
    "image": SITE + "/assets/img/og-image.jpg",
    "email": EMAIL,
    "telephone": PHONE,
    "priceRange": "$$",
    "founder": {"@type": "Person", "name": "Brittany Hill", "jobTitle": "Founder & CEO"},
    "address": {"@type": "PostalAddress", "addressLocality": "Chicago",
                "addressRegion": "IL", "addressCountry": "US"},
    "areaServed": {"@type": "Country", "name": "United States"},
    "slogan": "Where Wealth Becomes Legacy",
    "serviceType": ["Individual Tax Returns", "Business Tax Returns",
                    "Bookkeeping & Payroll", "Tax Planning & Consulting", "Audit Support",
                    "Amended Returns", "1099-K & 1095-A Assistance", "Financial Literacy",
                    "Mentorship & Coaching"],
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "09:00", "closes": "19:00"}],
    "sameAs": [FB, IG]
}, indent=2)

PAGES = {
    "index.html": dict(
        title="Royal Wealth Empire LLC | Virtual Tax Preparation in All 50 States",
        desc=("Royal Wealth Empire LLC offers premium virtual tax preparation, tax planning and "
              "business filing in all 50 states. Founded by Brittany “Bamz” Hill in "
              "Chicago, Illinois. Now accepting clients — book your free consultation today."),
        keywords=("virtual tax preparer, tax preparation all 50 states, online tax preparer, "
                  "Chicago Illinois tax service, Royal Wealth Empire, Brittany Hill tax advisor, "
                  "self employed tax preparation, small business tax filing"),
    ),
    "services.html": dict(
        title="Tax Services | Individual, Business & Self-Employed | Royal Wealth Empire LLC",
        desc=("Individual and business tax returns, bookkeeping and payroll, tax planning and "
              "consulting, audit support, financial literacy and mentorship — prepared "
              "virtually for clients in all 50 states."),
        keywords=("individual tax return preparation, small business tax services, 1099 tax "
                  "preparation, self employed tax filing, LLC formation service, amended tax "
                  "return, IRS notice help, virtual tax preparer"),
    ),
    "pricing.html": dict(
        title="Tax Preparation Pricing & Packages | Royal Wealth Empire LLC",
        desc=("Transparent, flat-fee tax preparation packages for individuals, self-employed "
              "filers and business owners. Every quote is confirmed in writing before we begin."),
        keywords=("tax preparation pricing, tax preparer fees, flat fee tax preparation, "
                  "small business tax packages, self employed tax preparation cost"),
    ),
    "about.html": dict(
        title="About Brittany “Bamz” Hill | Founder & CEO | Royal Wealth Empire LLC",
        desc=("Meet Brittany “Bamz” Hill, Founder & CEO of Royal Wealth Empire LLC. "
              "From paycheck to paycheck to building leaders — the story behind a tax firm "
              "built on education, opportunity and financial empowerment."),
        keywords=("Brittany Hill tax preparer, Royal Wealth Empire founder, black woman owned tax "
                  "firm, Chicago Illinois tax professional, women owned tax business"),
    ),
    "partners.html": dict(
        title="Become a Tax Partner | Start Your Own Tax Business | Royal Wealth Empire LLC",
        desc=("Now hiring Tax Partners nationwide. Get training, software, PTIN guidance, mentorship "
              "and a proven system to launch your own tax business with Royal Wealth Empire LLC."),
        keywords=("become a tax preparer, start your own tax business, tax partner opportunity, "
                  "tax preparer training, work from home tax jobs, tax office partnership"),
    ),
    "contact.html": dict(
        title="Contact Royal Wealth Empire LLC | Book a Free Tax Consultation",
        desc=("Call (331) 205-7720 or email Theroyalwealthempire@gmail.com to book your free virtual "
              "tax consultation. Based in Chicago, Illinois — serving all 50 states."),
        keywords=("contact tax preparer, book tax consultation, virtual tax appointment, "
                  "Chicago Illinois tax office, free tax consultation"),
    ),
}


def build():
    out = []
    for slug, meta in PAGES.items():
        body_path = os.path.join(SRC, slug)
        with open(body_path, encoding="utf-8") as f:
            body = f.read()

        extra = ""
        if slug == "index.html":
            extra = '\n<script type="application/ld+json">\n%s\n</script>' % ORG_SCHEMA

        html = (
            HEAD.format(title=meta["title"], desc=meta["desc"], keywords=meta["keywords"],
                        site=SITE, slug=("" if slug == "index.html" else slug), schema=extra)
            + header_for(slug)
            + body
            + FOOTER
        )
        dest = os.path.join(ROOT, slug)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(html)
        out.append((slug, len(html)))
    for slug, n in out:
        print("%-16s %6.1f KB" % (slug, n / 1024))


if __name__ == "__main__":
    build()
