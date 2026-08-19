# Royal Wealth Empire LLC — Website

A premium, fully responsive, 6-page static website for **Royal Wealth Empire LLC**
(Brittany "Bamz" Hill, Founder & CEO).

Pure **HTML + CSS + vanilla JavaScript**. No build step, no frameworks, no dependencies.
Double-click `index.html` and it runs.

---

## 1. What's in the box

```
royal-wealth-empire/
├── index.html          Home
├── services.html       Services
├── pricing.html        Packages & pricing
├── about.html          Brittany's story / mission
├── partners.html       Tax Partner recruitment + application form
├── contact.html        Contact form, details, Google Map
├── robots.txt          SEO
├── sitemap.xml         SEO
├── assets/
│   ├── css/style.css   All styling (one commented file)
│   ├── js/main.js      All interactivity (one commented file)
│   └── img/            Your logo, photos, flyers, banner + backgrounds
└── build/              Source templates + generators (NOT needed to run the site)
```

`build/` is optional. If you edit the HTML directly you can delete that folder —
the six `.html` files in the root are complete, standalone pages.

---

## 2. Brand colours

Sampled directly from your logo, banner and flyers. The whole palette lives at the
top of `assets/css/style.css` under `:root` — change one value there and it updates
across all six pages.

| Token | Hex | Where it came from |
|---|---|---|
| `--green-900` / `--ink-900` | `#04100F` | Deepest emerald — page background |
| `--green-800` | `#072220` | The flyer background green |
| `--green-500` | `#17413E` | Mid emerald for washes |
| `--teal-600`  | `#095458` | The banner's teal panel |
| `--teal-400`  | `#17828B` | Bright teal headline accent ("OPPORTUNITIES") |
| `--gold-500`  | `#D0A660` | **Primary gold** — the RWE crest gold |
| `--gold-600`  | `#B9904F` | Deep gold for gradients |
| `--gold-300`  | `#E4D0A9` | Gold highlight |
| `--cream`     | `#F7F2EA` | The ivory panels on your flyers |

Fonts: **Playfair Display** (headings, matches the crest serif), **Poppins** (body,
matches your flyer sans) and **Alex Brush** (the script accents — "Hi, I'm",
"My Promise To You", "Together, We Are Royal"). All three load from Google Fonts.

---

## 3. Your images

Everything in `assets/img/` is built from the files you supplied. To replace any of
them, **overwrite the file keeping the same filename** — no code changes needed.

| Filename | What it is | Where it appears |
|---|---|---|
| `logo-mark.png` | Gold RWE crest, background removed | Header, footer, preloader |
| `logo-full.jpg` | Full marble crest with wordmark | Reserved for print / light backgrounds |
| `favicon.png` | Crest on the emerald brand tile | Browser tab |
| `brittany-portrait.jpg` | Teal-blazer headshot | Home hero, Tax Partners |
| `brittany-office.jpg` | White-suit office photo | Home intro, About story, Partners |
| `flyer-about.jpg` | "Hi, I'm Brittany" flyer | Home gallery, About |
| `flyer-launch.jpg` | Launch announcement flyer | Home |
| `flyer-team.jpg` | Tax Advisor & Associates welcome | Home gallery, About |
| `flyer-enrollment.jpg` | Back-2-School enrolment flyer | **Not currently used** — see note below |
| `banner-wide.jpg` | Wide "Accuracy Opens Opportunities" banner | Home, Services |
| `og-image.jpg` | Link preview card | Social sharing |
| `hero-*.jpg`, `texture-deco.jpg` | Emerald/gold gradient backdrops | Page headers |

> **Note on the enrolment flyer:** it shows a limited-time back-to-school price
> ($29 / $89) that has passed. Displaying it live would advertise pricing you may no
> longer honour, so it's bundled in the folder but not shown on any page. Send a
> current version and it drops straight into the Tax Partners page.

---

## 4. Editing text

Every page is plain, commented HTML. Search for the sentence you want to change
and type over it. Common edits:

- **Phone / email** — three numbers are listed site-wide: `(331) 205-7720` (office),
  `(630) 996-1134` (alternate, from your flyer) and `(331) 290-5638` (personal), plus
  both `Theroyalwealthempire@gmail.com` and `info@royalwealthempire.com`. If you want
  fewer, edit `build/template.py` and re-run the build, or find-and-replace in the six
  HTML files.
- **Prices** — `pricing.html`, look for `<span class="amt">Custom</span>` and put your
  number in (e.g. `<span class="amt">$150</span>`). There's a comment marking each one.
- **Stats counters** — search `data-count=` and change the number; the counter
  animation adapts automatically.
- **Testimonials** — `index.html` has a ready-made testimonial section sitting inside an
  HTML comment near the bottom. It's commented out deliberately: the site should only
  publish reviews real clients actually wrote. When you have them (with permission),
  uncomment the block and paste them in.
- **FAQ** — add or remove `.faq-item` blocks; the accordion is automatic.

---

## 5. How the contact forms work

Both forms (Contact page + Tax Partner application) use a **mailto fallback**: on
submit they open the visitor's email app with every field pre-filled and addressed
to `Theroyalwealthempire@gmail.com`. This works with zero backend and zero cost.

**To get submissions delivered straight to your inbox instead**, sign up for a free
form service (Formspree, Web3Forms, Netlify Forms) and change the form tag:

```html
<!-- from -->
<form class="form-card" data-mailto-form="Theroyalwealthempire@gmail.com" ...>

<!-- to -->
<form class="form-card" action="https://formspree.io/f/YOUR_ID" method="POST">
```

Removing the `data-mailto-form` attribute is what switches the behaviour off.

---

## 6. Going live

The site is 100% static, so it can be hosted free on almost anything:

1. **Netlify / Vercel** — drag the whole folder onto the dashboard. Live in seconds.
2. **GitHub Pages** — push the folder to a repo, enable Pages on the main branch.
3. **Any cPanel host / Hostinger / GoDaddy** — upload the folder contents into
   `public_html` via FTP.

**After it's live:** open `sitemap.xml`, `robots.txt` and the `<link rel="canonical">`
line at the top of each HTML file, and replace
`https://www.royalwealthempire.com` with your real domain. Then submit the sitemap
in Google Search Console.

---

## 7. Features included

- Sticky glass navigation with animated underlines + full-screen mobile drawer
- Gold crest preloader
- Hero with parallax background and animated headline reveal
- Scroll-reveal animations on every section (IntersectionObserver)
- Animated statistic counters
- Cursor-follow spotlight glow on cards
- Infinite marquee trust strip
- Accordion FAQs on four pages
- Two working forms with validation + mailto delivery
- Google Maps embed (Chicago, IL)
- Floating click-to-call button + back-to-top button
- Full SEO: unique meta titles/descriptions, Open Graph + Twitter cards,
  JSON-LD `AccountingService` schema, semantic headings, image alt text,
  canonical URLs, sitemap and robots.txt
- Accessibility: skip link, ARIA labels, keyboard-operable menu and accordions,
  visible focus rings, `prefers-reduced-motion` support

---

## 8. Regenerating the artwork (optional)

`build/prep_assets.sh` turns your original logo/photos/flyers into the web-ready files
in `assets/img/`, `build/gen_images.py` generates the emerald-and-gold gradient
backgrounds with Pillow, and `build/build.py` reassembles the six pages from
`build/src/` plus the shared header/footer in `build/template.py`.

```bash
pip install pillow
bash build/prep_assets.sh /path/to/your/originals   # re-cut photos & logo
python build/gen_images.py                          # rebuild backgrounds
python build/build.py                               # rebuild the six HTML pages
```

You do **not** need to run these unless you want to change the shared nav or footer
in one place instead of six.

---

© Royal Wealth Empire LLC. Where wealth becomes legacy.
