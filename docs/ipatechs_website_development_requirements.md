# IPATECHS Website — Developer Requirements Document
**Version 2.0 · Static Site Edition · Dar es Salaam, Tanzania · 2025**

---

## Document Summary

| Field | Detail |
|---|---|
| **Project** | ipatechs.com — SEO, UX & Conversion Overhaul |
| **Client** | IPATECHS Company Limited |
| **Stack** | Static HTML / CSS / Vanilla JS (no CMS, no WordPress) |
| **Repo** | github.com/wakashela/ipatechs |
| **Build** | `npm run build` → `css/style.min.css` + `js/bundle.min.js` |
| **Objective** | Rank #1 for industrial spare parts searches in Dar es Salaam & East Africa, while delivering a conversion-optimised user experience |
| **Design System** | Industrial Precision Dark — documented in `docs/design.md` |

### Priority Levels

| Label | Meaning |
|---|---|---|
| 🔴 CRITICAL | Blocking — must ship in Phase 1 (Week 1–2) |
| 🟠 HIGH | Phase 2 — Month 1 |
| 🟡 MEDIUM | Phase 3 — Month 2–3 |
| 🟢 LOW | Phase 4 — Month 3–6 |

### Implementation Status (Updated 18 May 2026)

| Mark | Meaning |
|---|---|
| ✅ | Implemented |
| ⏳ | Requires manual intervention (client task) |
| ❌ | Skipped |

---

## Table of Contents

1. [Phase 1 — Critical Fixes (Week 1–2)](#1-phase-1--critical-fixes-week-12)
2. [Phase 2 — Local SEO Build (Month 1)](#2-phase-2--local-seo-build-month-1)
3. [Phase 3 — Content & Trust (Month 2–3)](#3-phase-3--content--trust-month-23)
4. [Phase 4 — Growth Features (Month 3–6)](#4-phase-4--growth-features-month-36)
5. [Keyword Targets by Page](#5-keyword-targets-by-page)
6. [Build & Deployment Notes](#6-build--deployment-notes)
7. [Acceptance Criteria](#7-acceptance-criteria)

---

## 1. Phase 1 — Critical Fixes (Week 1–2) ✅ COMPLETE

### REQ-001 🔴 Fix `<title>` and `<meta name="description">` in `index.html` ✅

**Current (line 6–8 of `index.html`):**
```html
<title>Our Company — Industrial Parts, Engineering & Construction Equipment</title>
<meta name="description" content="IPATECHS COMPANY LIMITED — Your global partner for industrial spare parts, engineering excellence, and construction equipment. Serving East Africa since 2019." />
```

**Required:**
```html
<title>Industrial Spare Parts Supplier in Dar es Salaam | IPATECHS Tanzania</title>
<meta name="description" content="IPATECHS is East Africa's trusted supplier of industrial spare parts, bearings, motors & engineering equipment. ABB, Siemens, SKF, Cummins. Dar es Salaam, Tanzania. Same-day quotes." />
```

**Rules:**
- Title must be ≤ 60 characters, include primary keyword + city + brand
- Meta description must be 150–160 characters with a CTA
- Every new page added (service pages, location pages) must have a unique title and description — never duplicate

---

### REQ-002 🔴 Fix hero stat counters — add static HTML fallback ✅

**File:** `index.html` (hero stats section) + `js/main.js` (counter animation)

**Problem:** The `animateCount()` function in `js/main.js` starts all counters at `0`. If JS is slow or blocked, the page shows "0+ Years Experience" — communicating zero credibility on first impression. Google also crawls the HTML before JS runs.

**Current HTML (index.html):**
```html
<span id="stat-years">0</span>+
<span id="stat-clients">0</span>+
<span id="stat-products">0</span>+
<span id="stat-industries">0</span>
```

**Required — set real values as defaults in HTML:**
```html
<span id="stat-years">6</span>+
<span id="stat-clients">200</span>+
<span id="stat-products">50</span>+
<span id="stat-industries">12</span>
```

The `animateCount()` in `js/main.js` should continue to work as-is — it will animate up to the target value over the real number. No JS changes required, HTML only.

---

### REQ-003 🔴 Add sticky WhatsApp float button ✅

**File:** `index.html` (before `</body>`), `css/style.css`

WhatsApp is the primary B2B channel in Tanzania. This is the single highest-ROI addition on this list.

**Add to `index.html` before `</body>`:**
```html
<!-- WHATSAPP FLOAT -->
<a href="https://wa.me/255750304097?text=Hello%20IPATECHS%2C%20I%20would%20like%20to%20enquire%20about%20your%20products."
   class="whatsapp-float"
   target="_blank"
   rel="noopener"
   aria-label="Chat with us on WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor" width="26" height="26">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
    <path d="M12 0C5.373 0 0 5.373 0 12c0 2.122.554 4.118 1.525 5.845L.057 23.617a.5.5 0 0 0 .609.61l5.88-1.459A11.945 11.945 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 0 1-5.006-1.369l-.36-.213-3.49.867.878-3.405-.234-.372A9.818 9.818 0 1 1 12 21.818z"/>
  </svg>
  <span class="whatsapp-float-tooltip">Chat on WhatsApp</span>
</a>
```

**Add to `css/style.css`:**
```css
/* WHATSAPP FLOAT */
.whatsapp-float {
  position: fixed;
  bottom: 5.5rem; /* sits above #back-top */
  right: 2rem;
  z-index: 500;
  width: 52px;
  height: 52px;
  background: #25D366;
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  box-shadow: 0 4px 20px rgba(37, 211, 102, 0.4);
  animation: waPulse 2.5s ease-in-out infinite;
  transition: transform 0.2s, box-shadow 0.2s;
}
.whatsapp-float:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 28px rgba(37, 211, 102, 0.55);
}
.whatsapp-float-tooltip {
  position: absolute;
  right: 60px;
  background: #000;
  color: #fff;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.4rem 0.8rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}
.whatsapp-float:hover .whatsapp-float-tooltip {
  opacity: 1;
}
@keyframes waPulse {
  0%, 100% { box-shadow: 0 4px 20px rgba(37,211,102,0.4); }
  50% { box-shadow: 0 4px 32px rgba(37,211,102,0.7); }
}
@media (max-width: 768px) {
  .whatsapp-float { bottom: 5rem; right: 1rem; }
}
```

---

### REQ-004 🔴 Fix footer — complete NAP and fix dead social links ✅

**File:** `index.html` (footer section)

**Problem 1 — Incomplete address.** Current footer address is `Makongo Road, Postal Code 14129` with no city name. This breaks Google's NAP (Name, Address, Phone) consistency detection.

**Change to:**
```html
<span>Makongo Road, Sinza, 14129<br>Dar es Salaam, Tanzania</span>
```

**Problem 2 — All social links are `href="#"`.** Three of the four social icons are dead links. Either replace with real URLs or remove the icons.

**Required — replace placeholder `href="#"` with real URLs:**
```html
<a href="https://www.linkedin.com/company/ipatechs" class="social-link" aria-label="LinkedIn" target="_blank" rel="noopener">
<a href="https://twitter.com/ipatechs" class="social-link" aria-label="Twitter/X" target="_blank" rel="noopener">
<a href="https://www.facebook.com/ipatechs" class="social-link" aria-label="Facebook" target="_blank" rel="noopener">
```
If a profile doesn't exist yet, remove the `<a>` element entirely. A dead link is worse than no link.

**Also update footer copyright line:**
```html
<p>Industrial Parts, Engineering &amp; Construction Equipment · Makongo Road, Sinza, Dar es Salaam, Tanzania</p>
```

---

### REQ-005 🔴 Fix enquiry form — reduce fields and add WhatsApp fallback ✅

**Files:** `index.html` (modal body), `js/main.js` (`submitEnquiry()`)

**Current:** 6 fields — Product Name display, Full Name, Email, Mobile Number, Company, Message.

**Required — reduce to 3 required fields:**

Replace the `.modal-body` form HTML with:
```html
<div class="form-product-name" id="modalProductName">Product Name</div>
<div class="form-group">
  <label>Your Name *</label>
  <input type="text" placeholder="e.g. John Mwangi" id="enquiryName" autocomplete="name" />
</div>
<div class="form-group">
  <label>WhatsApp Number *</label>
  <input type="tel" placeholder="+255 700 000 000" id="enquiryPhone" autocomplete="tel" />
</div>
<div class="form-group">
  <label>What do you need? *</label>
  <textarea placeholder="Describe the product, quantity, specifications, or part number..." id="enquiryMessage" style="min-height:90px;"></textarea>
</div>
<button class="btn btn-primary" style="width:100%;justify-content:center" onclick="submitEnquiry()">
  Send Enquiry
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
</button>
<div style="text-align:center;margin-top:1rem;">
  <a href="https://wa.me/255750304097" target="_blank" rel="noopener"
     style="font-family:'Barlow Condensed',sans-serif;font-size:0.8rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted);text-decoration:none;">
    Or message us directly on WhatsApp →
  </a>
</div>
```

**Update `submitEnquiry()` in `js/main.js`** to validate only name, phone, and message:
```javascript
function submitEnquiry() {
  const name = document.getElementById('enquiryName').value.trim();
  const phone = document.getElementById('enquiryPhone').value.trim();
  const msg = document.getElementById('enquiryMessage').value.trim();
  if (!name || !phone || !msg) {
    alert('Please fill in your name, WhatsApp number, and what you need.');
    return;
  }
  // Build WhatsApp pre-fill URL as the primary action
  const product = document.getElementById('modalProductName').textContent;
  const text = encodeURIComponent(
    `Hello IPATECHS,\n\nName: ${name}\nProduct: ${product}\n\n${msg}\n\nContact me on: ${phone}`
  );
  window.open(`https://wa.me/255750304097?text=${text}`, '_blank');
  closeModal();
}
```
This converts every form submission into a pre-filled WhatsApp message — no server required, no email infrastructure needed, and aligns with how buyers in Tanzania prefer to communicate.

---

### REQ-006 🔴 Add `<link rel="canonical">` and Open Graph tags to `index.html` ✅

**File:** `index.html` `<head>` section

Add immediately after the existing `<meta name="description">` tag:
```html
<!-- Canonical -->
<link rel="canonical" href="https://www.ipatechs.com/" />

<!-- Open Graph (WhatsApp, LinkedIn, Facebook previews) -->
<meta property="og:type" content="website" />
<meta property="og:url" content="https://www.ipatechs.com/" />
<meta property="og:title" content="Industrial Spare Parts Supplier in Dar es Salaam | IPATECHS Tanzania" />
<meta property="og:description" content="East Africa's trusted supplier of industrial spare parts, bearings, motors & engineering equipment. ABB, Siemens, SKF, Cummins. Same-day quotes from Dar es Salaam." />
<meta property="og:image" content="https://www.ipatechs.com/assets/images/og-image.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:locale" content="en_TZ" />
<meta property="og:site_name" content="IPATECHS Company Limited" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Industrial Spare Parts Supplier in Dar es Salaam | IPATECHS" />
<meta name="twitter:description" content="East Africa's trusted supplier of industrial spare parts. ABB, Siemens, SKF, Cummins. Same-day quotes from Dar es Salaam, Tanzania." />
<meta name="twitter:image" content="https://www.ipatechs.com/assets/images/og-image.jpg" />
```

**Also create** `assets/images/og-image.jpg` — a 1200×630px branded image (IPATECHS logo on dark background with tagline). This appears as the preview thumbnail when the URL is shared on WhatsApp, LinkedIn, and Facebook.

---

## 2. Phase 2 — Local SEO Build (Month 1) ✅ COMPLETE (2 pending client tasks)

### REQ-007 🟠 Add LocalBusiness JSON-LD structured data ✅

**File:** `index.html` `<head>` section

Add before `</head>`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "https://www.ipatechs.com/#business",
      "name": "IPATECHS Company Limited",
      "alternateName": "IPA Techs",
      "description": "East Africa's trusted supplier of industrial spare parts, engineering solutions, and construction equipment. Serving Tanzania, Kenya, Uganda, Rwanda, and beyond since 2019.",
      "url": "https://www.ipatechs.com",
      "logo": "https://www.ipatechs.com/assets/images/logo.png",
      "image": "https://www.ipatechs.com/assets/images/og-image.jpg",
      "telephone": "+255750304097",
      "email": "info@ipatechs.com",
      "foundingDate": "2019",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Makongo Road, Sinza",
        "addressLocality": "Dar es Salaam",
        "postalCode": "14129",
        "addressCountry": "TZ"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": -6.7924,
        "longitude": 39.2083
      },
      "areaServed": [
        { "@type": "Country", "name": "Tanzania" },
        { "@type": "Country", "name": "Kenya" },
        { "@type": "Country", "name": "Uganda" },
        { "@type": "Country", "name": "Rwanda" },
        { "@type": "Country", "name": "Zambia" },
        { "@type": "Country", "name": "Mozambique" }
      ],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
          "opens": "08:00",
          "closes": "17:00"
        }
      ],
      "sameAs": [
        "https://www.linkedin.com/company/ipatechs",
        "https://www.facebook.com/ipatechs",
        "https://twitter.com/ipatechs"
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Industrial Spare Parts & Engineering Solutions",
        "itemListElement": [
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Industrial Spare Parts Supply" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Mechanical Engineering Solutions" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Mining Equipment Supply" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Petroleum & Gas Engineering" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Automation & PLC/SCADA Systems" } }
        ]
      }
    },
    {
      "@type": "Organization",
      "@id": "https://www.ipatechs.com/#organization",
      "name": "IPATECHS Company Limited",
      "url": "https://www.ipatechs.com",
      "logo": "https://www.ipatechs.com/assets/images/logo.png"
    },
    {
      "@type": "WebSite",
      "@id": "https://www.ipatechs.com/#website",
      "url": "https://www.ipatechs.com",
      "name": "IPATECHS Company Limited",
      "publisher": { "@id": "https://www.ipatechs.com/#organization" }
    }
  ]
}
</script>
```

**Validate** at: https://search.google.com/test/rich-results — must pass with zero errors before deployment.

---

### REQ-008 🟠 Create multi-page site structure — service pages ✅

**Problem:** The entire site is a single `index.html` with anchor links. Google can only rank one URL per topic. All 9 service areas compete on the same page, preventing specific-service keyword ranking.

**New file structure to create:**

```
/
├── index.html                          (homepage — keep existing, update with links)
├── industrial-spare-parts/
│   └── index.html
├── mechanical-engineering/
│   └── index.html
├── electrical-engineering/
│   └── index.html
├── material-engineering/
│   └── index.html
├── petroleum-gas-engineering/
│   └── index.html
├── power-energy-solutions/
│   └── index.html
├── mining-equipment-east-africa/
│   └── index.html
├── automation-engineering/
│   └── index.html
├── construction-equipment/
│   └── index.html
├── tanzania/
│   └── index.html
├── dar-es-salaam/
│   └── index.html
├── sitemap.xml                         (see REQ-010)
└── robots.txt                          (see REQ-010)
```

**Each service page must include:**

1. **Unique `<title>` and `<meta name="description">`** — see keyword table in Section 5
2. **`<link rel="canonical">`** pointing to its own full URL
3. **The full site nav** (same `nav` HTML as `index.html`) with `nav.scrolled` class applied by default since these are standalone pages
4. **An `<h1>` containing the primary keyword + location** — e.g. `Industrial Spare Parts Supplier in Tanzania | IPATECHS`
5. **500+ words of unique body content** — not copied from the homepage. Each page must describe: what the service covers, which brands are involved, which industries in Tanzania use it, and a quote/contact CTA
6. **The enquiry form** (same modal pattern as `index.html`, using the simplified 3-field version from REQ-005)
7. **Internal links** to related service pages and back to homepage
8. **The same footer** as `index.html` (with the corrected address from REQ-004)
9. **JSON-LD schema** — same as REQ-007 but with `"url"` and canonical pointing to the specific page URL

**Shared components pattern:** Extract nav, footer, and modal HTML into reusable JS template literals or a simple include system to avoid maintaining duplicates across 11+ files. Suggested approach:

```javascript
// js/components.js — new file
const NAV_HTML = `...nav markup...`;
const FOOTER_HTML = `...footer markup...`;
document.getElementById('nav-root').innerHTML = NAV_HTML;
document.getElementById('footer-root').innerHTML = FOOTER_HTML;
```

Then each page body:
```html
<div id="nav-root"></div>
<!-- page-specific content -->
<div id="footer-root"></div>
<script src="../js/components.js"></script>
<script src="../js/main.js"></script>
```

Adjust relative paths (`../`) for nested directories. Alternatively, use a static site generator (11ty, Astro) — this is the recommended approach if more than 10 pages need to be maintained. Discuss with client before choosing approach.

---

### REQ-009 🟠 Create location landing pages ✅

**New files:** `tanzania/index.html`, `dar-es-salaam/index.html`

These pages target geo-intent searches. They do not need to be linked prominently in the main nav but must be indexed (no `noindex` tag).

**Each location page must include:**

- Unique `<h1>`: `Industrial Spare Parts Supplier in [City/Country] | IPATECHS`
- 2–3 paragraphs of localised content mentioning the city, delivery capability, and relevant local industries (e.g. for Dar es Salaam: TICTS port, Dangote Cement, TANESCO)
- Embedded Google Maps `<iframe>` (see REQ-011)
- The simplified enquiry form
- Breadcrumb navigation: `Home > Tanzania > Dar es Salaam`
- LocalBusiness schema with `"addressLocality"` matching the page

**Additional location pages to create in Phase 4:**
- `nairobi-kenya/index.html`
- `kampala-uganda/index.html`
- `kigali-rwanda/index.html`

---

### REQ-010 🟠 Create `sitemap.xml` and `robots.txt` ✅

**File:** `sitemap.xml` in root directory

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.ipatechs.com/</loc><priority>1.0</priority><changefreq>weekly</changefreq></url>
  <url><loc>https://www.ipatechs.com/industrial-spare-parts/</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/mechanical-engineering/</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/electrical-engineering/</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/petroleum-gas-engineering/</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/mining-equipment-east-africa/</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/power-energy-solutions/</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/automation-engineering/</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/material-engineering/</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/construction-equipment/</loc><priority>0.8</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/tanzania/</loc><priority>0.85</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://www.ipatechs.com/dar-es-salaam/</loc><priority>0.85</priority><changefreq>monthly</changefreq></url>
</urlset>
```

**File:** `robots.txt` in root directory

```
User-agent: *
Allow: /
Sitemap: https://www.ipatechs.com/sitemap.xml
```

**Submit sitemap** to Google Search Console at: https://search.google.com/search-console — add the property `https://www.ipatechs.com` and submit the sitemap URL. Screenshot the submission confirmation and share with client.

---

### REQ-011 🟠 Add Google Maps embed to `dar-es-salaam/index.html` and footer ⏳

Once the client verifies the Google Business Profile (GBP), embed a Google Maps iframe on:
1. The `dar-es-salaam/index.html` location page
2. The contact section at the bottom of `index.html` (inside the `<footer id="contact">`)

**Embed code pattern (replace `PLACE_ID` with real GBP place ID):**
```html
<div class="map-embed" style="margin-top:2rem;">
  <iframe
    src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=IPATECHS+Company+Limited+Dar+es+Salaam"
    width="100%"
    height="300"
    style="border:0;filter:invert(0.9) hue-rotate(180deg);" <!-- dark-mode map -->
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"
    title="IPATECHS Company Limited location in Dar es Salaam, Tanzania">
  </iframe>
</div>
```

The `filter: invert(0.9) hue-rotate(180deg)` CSS trick converts the Google Maps light theme to a dark theme that matches the site's `#080808` background. Test across browsers — remove if rendering is inconsistent.

> **CLIENT TASK:** Create and verify Google Business Profile at https://business.google.com before this requirement can be completed. Provide the Place ID and Maps API key to the developer.

---

### REQ-012 🟠 Image optimisation — WebP conversion and lazy loading ✅

**Files:** `index.html`, `css/style.css`, `assets/images/`

**All Unsplash URLs must be replaced with locally hosted images.** External image CDNs in production are a reliability risk and add DNS lookup latency. Download and host all Unsplash images in `assets/images/`.

**Conversion steps:**

```bash
# Install cwebp (one-time)
sudo apt-get install webp   # Linux
brew install webp            # macOS

# Convert all JPG/PNG in assets/images/ to WebP
for f in assets/images/*.{jpg,jpeg,png}; do
  cwebp -q 82 "$f" -o "${f%.*}.webp"
done
```

**Update all `<img>` tags to use `<picture>` with WebP + fallback:**
```html
<picture>
  <source srcset="assets/images/cummins.webp" type="image/webp" />
  <img class="hero-engine-img" src="assets/images/cummins.png" alt="Cummins QSK19 diesel engine — IPATECHS Tanzania" width="780" height="585" />
</picture>
```

**All `<img>` tags below the fold must add `loading="lazy"`:**
- All `.industry-card img` elements
- All `.product-img img` elements
- All `.blog-thumb img` elements
- All `.portfolio-item img` elements
- All `.partner-item img` elements

**All `<img>` tags must have explicit `width` and `height` attributes** to eliminate layout shift (CLS). Measure each image's natural dimensions and add them.

**Target:** Google PageSpeed Insights mobile score ≥ 80. Run before/after and share screenshots.

---

### REQ-013 🟠 Set up Cloudflare (free tier) ⏳

> **CLIENT TASK:** Create a Cloudflare account at cloudflare.com and point the ipatechs.com DNS through Cloudflare nameservers.

**Developer tasks once DNS is through Cloudflare:**

| Setting | Value |
|---|---|
| SSL/TLS mode | Full (Strict) |
| Always Use HTTPS | On |
| Auto Minify | HTML ✓, CSS ✓, JavaScript ✓ |
| Brotli compression | On |
| Rocket Loader | On |
| Browser Cache TTL | 1 month (for static assets) |
| Page Rule: `*.ipatechs.com/assets/*` | Cache Level: Cache Everything, Edge Cache TTL: 1 month |

---

### REQ-014 🟠 Add delivery promise messaging strip ✅

**Files:** `index.html`, `css/style.css`

Add a compact info strip above the footer CTA band (`.cta-band`) to communicate response time and delivery scope. This addresses the biggest conversion anxiety for procurement managers.

**HTML — add before `.cta-band`:**
```html
<!-- DELIVERY PROMISE STRIP -->
<div class="promise-strip">
  <div class="container">
    <div class="promise-grid">
      <div class="promise-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span><strong>Same-day quotes</strong> — reply within 2 hours, Mon–Fri</span>
      </div>
      <div class="promise-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M12 22V12M12 12L8 16M12 12l4 4M20 6H4"/></svg>
        <span><strong>Stocked in Dar es Salaam</strong> — 24–72hr delivery across Tanzania</span>
      </div>
      <div class="promise-item">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/></svg>
        <span><strong>East Africa coverage</strong> — Kenya, Uganda, Rwanda, Zambia</span>
      </div>
    </div>
  </div>
</div>
```

**CSS — add to `css/style.css`:**
```css
.promise-strip {
  background: var(--dark2);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 1.5rem 0;
}
.promise-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
.promise-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.5;
}
.promise-item svg { color: var(--orange); flex-shrink: 0; }
.promise-item strong { color: var(--white); }
@media (max-width: 768px) {
  .promise-grid { grid-template-columns: 1fr; }
}
```

---

## 3. Phase 3 — Content & Trust (Month 2–3) ✅ COMPLETE

### REQ-015 🟡 Fix or remove ISO certification badge ✅

**File:** `index.html` (hero section — `.hero-img-badge`)

**Current:**
```html
<div class="hero-img-badge">
  <div class="big">ISO</div>
  <div class="sm">Certified</div>
</div>
```

**Option A — Certification is confirmed:** Update the badge to link to a certification page. Create `certification/index.html` containing the certificate number, issuing body (e.g. TBS, Bureau Veritas, SGS), scope, issue date, and expiry date. Link the badge:
```html
<a href="/certification/" class="hero-img-badge" style="text-decoration:none;">
  <div class="big">ISO</div>
  <div class="sm">Certified ↗</div>
</a>
```

**Option B — Certification not yet obtained:** Remove the badge entirely from the HTML until certification is confirmed. Do not display unsubstantiated compliance claims.

---

### REQ-016 🟡 Add testimonials section to `index.html` ✅

**Files:** `index.html`, `css/style.css`, new file `js/testimonials.js`

Add a Testimonials section between the `.portfolio` section and the `.blog` section.

**HTML structure:**
```html
<!-- TESTIMONIALS -->
<section class="testimonials" id="testimonials">
  <div class="container">
    <div class="testimonials-header">
      <div class="label reveal">Client Voices</div>
      <h2 class="section-title reveal">WHAT OUR <span>CLIENTS SAY</span></h2>
    </div>
    <div class="testimonials-grid">
      <!-- Repeat .testimonial-card for each testimonial -->
      <div class="testimonial-card reveal">
        <div class="testimonial-quote">&#8220;</div>
        <p class="testimonial-text">Placeholder testimonial text — replace with real client quote. 2–4 sentences about IPATECHS service, delivery speed, or product quality.</p>
        <div class="testimonial-author">
          <div class="testimonial-initials">JM</div>
          <div>
            <div class="testimonial-name">John Mwangi</div>
            <div class="testimonial-role">Procurement Manager · Tanzanian Cement Company</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

**CSS — add to `css/style.css`:**
```css
.testimonials { padding: 8rem 0; background: var(--dark); }
.testimonials-header { margin-bottom: 4rem; }
.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.testimonial-card {
  background: var(--dark2);
  border: 1px solid var(--border);
  padding: 2rem;
  position: relative;
  transition: border-color 0.3s;
}
.testimonial-card:hover { border-color: rgba(255,102,0,0.3); }
.testimonial-quote {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 4rem;
  color: var(--orange);
  line-height: 1;
  margin-bottom: 1rem;
  opacity: 0.6;
}
.testimonial-text {
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}
.testimonial-author {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
}
.testimonial-initials {
  width: 40px; height: 40px;
  background: rgba(255,102,0,0.1);
  border: 1px solid rgba(255,102,0,0.3);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1rem;
  color: var(--orange);
  flex-shrink: 0;
}
.testimonial-name { font-weight: 600; font-size: 0.9rem; color: var(--white); }
.testimonial-role { font-size: 0.78rem; color: var(--muted); margin-top: 0.15rem; }
@media (max-width: 768px) { .testimonials-grid { grid-template-columns: 1fr; } }
```

**Minimum 6 testimonials required** with real client names and companies. Content to be provided by IPATECHS. The developer populates the HTML with whatever is provided.

---

### REQ-017 🟡 Add team / about section to homepage ✅

**Files:** `index.html`, `css/style.css`

The current About section (`section.about`) has no human faces. Add a "Meet the Team" sub-section after the existing tab content inside `.about-content`.

```html
<div class="team-grid" style="margin-top:3rem;">
  <div class="label">Our Team</div>
  <div class="team-cards">
    <!-- One .team-card per person — content to be provided by client -->
    <div class="team-card">
      <div class="team-img-wrap">
        <img src="assets/images/team/director.jpg" alt="[Director Name] — IPATECHS Director" width="200" height="200" loading="lazy" />
      </div>
      <div class="team-info">
        <div class="team-name">[Director Name]</div>
        <div class="team-role">Founder & Director</div>
      </div>
    </div>
  </div>
</div>
```

**Design requirements** (follow `docs/design.md` — Industrial Precision Dark):
- Team photo containers: `clip-path: polygon(0 0, 90% 0, 100% 10%, 100% 100%, 10% 100%, 0 90%)` (matching existing image chamfer pattern)
- Name: Barlow Condensed 700, text-transform uppercase, `var(--white)`
- Role: Barlow 400, `var(--muted)`
- Layout: horizontal flex row, wrap on mobile

Photos to be provided by client as JPG/PNG, minimum 400×400px. Developer converts to WebP and places in `assets/images/team/`.

---

### REQ-018 🟡 Add product search bar ✅

**Files:** `index.html`, `css/style.css`, `js/search.js` (new file)

Add a search input in the desktop nav and behind a search icon on mobile. On this static site, search is implemented as a client-side filter over the `productData` array in `js/products.js` and the `industryData` array in `js/industries.js`.

**Search input in nav (desktop only, add to `.nav-inner` before the CTA button):**
```html
<div class="nav-search" id="navSearch">
  <input type="search" id="siteSearchInput" placeholder="Search products, brands, part numbers..." autocomplete="off" aria-label="Search products" />
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
  <div class="search-results" id="searchResults" role="listbox" aria-label="Search results"></div>
</div>
```

**`js/search.js`** — search over `productData` titles, descriptions, specs, and brands. Returns matching items as clickable results that `openProductDetail(index)` or scroll to the matching section. Minimum 2 characters before results appear. ESC key clears and closes.

---

### REQ-019 🟡 Expand `js/articles.js` with SEO-targeted blog content ✅

**File:** `js/articles.js`

The current `articles` object has 3 entries. Add the following 5 articles to the object. Full article content (500+ words each) to be written by client or copywriter and handed to the developer as plain text. Developer formats into the existing content template.

| Article Key | Title | Target Keyword |
|---|---|---|
| `skf-bearings-tanzania` | Where to Buy SKF Bearings in Tanzania | SKF bearings Tanzania |
| `spare-parts-dar-es-salaam` | Top Industrial Spare Parts Suppliers in Dar es Salaam | spare parts supplier Dar es Salaam |
| `cummins-engine-parts` | Cummins Engine Parts — Complete Guide for East Africa | Cummins engine parts Tanzania |
| `abb-siemens-distributor` | ABB and Siemens Distributor in Tanzania — What to Know | ABB Siemens distributor Tanzania |
| `plc-scada-tanzania` | Industrial Automation with PLCs and SCADA in Tanzania | PLC SCADA automation Tanzania |

**Publishing schedule:** 2 articles per month. Articles live inside the modal (`openArticle()`) for now but must also be extractable to standalone `/blog/[slug]/index.html` pages in Phase 4 for full SEO benefit (see REQ-022).

---

## 4. Phase 4 — Growth Features (Month 3–6) ✅ COMPLETE (Swahili skipped)

### REQ-020 🟢 Extract blog articles to standalone pages ✅

**New files:** `blog/index.html`, `blog/[slug]/index.html` for each article

Each blog article currently lives only inside a JavaScript object and renders in a modal. For Google to index and rank individual articles, each needs a real URL.

Create `blog/[slug]/index.html` for each article with:
- `<title>` matching the article title + ` | IPATECHS`
- Full article content as static HTML (not JS-rendered)
- `Article` JSON-LD schema with `datePublished`, `author`, `publisher`
- Breadcrumb: `Home > Blog > [Article Title]`
- Related articles sidebar or footer links
- The enquiry CTA at the end of each article

Update `js/articles.js` so `openArticle()` links to the standalone page on mobile (where the modal experience is poorer) or keeps the modal on desktop.

---

### REQ-021 🟢 Add Google Tag Manager and conversion tracking ✅

**Files:** `index.html` (GTM snippet), `js/main.js` (event pushes)

**Add GTM head snippet** immediately after `<head>`:
```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
```

**Add GTM body snippet** immediately after `<body>`:
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

Replace `GTM-XXXXXXX` with the real container ID.

**Push dataLayer events** in `js/main.js` for:
```javascript
// Enquiry form submitted
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({ event: 'enquiry_submitted', product: productName });

// WhatsApp float clicked — add to the .whatsapp-float onclick
window.dataLayer.push({ event: 'whatsapp_click', source: 'float_button' });

// Phone number clicked — wrap tel: link with onclick
window.dataLayer.push({ event: 'phone_click' });
```

---

### REQ-022 🟢 Add Swahili language pages ❌

Create Swahili versions of the top 3 pages:
- `sw/index.html` — Swahili homepage
- `sw/vipande-vya-viwanda/index.html` — Industrial spare parts in Swahili
- `sw/wasiliana-nasi/index.html` — Contact page in Swahili

Add `hreflang` tags to the English originals:
```html
<link rel="alternate" hreflang="en" href="https://www.ipatechs.com/" />
<link rel="alternate" hreflang="sw" href="https://www.ipatechs.com/sw/" />
```

Add a language toggle button to the nav. Swahili translation text to be provided by the client (professional translator, not Google Translate).

---

## 5. Keyword Targets by Page

Each page's `<h1>`, first `<p>`, `<title>`, and `<meta name="description">` must naturally include the primary keyword. Secondary keywords should appear throughout the body text.

| Page | URL | Primary Keyword | Secondary Keywords |
|---|---|---|---|
| Homepage | `/` | industrial spare parts supplier Tanzania | engineering solutions Dar es Salaam, construction equipment Tanzania |
| Industrial Spare Parts | `/industrial-spare-parts/` | industrial spare parts Tanzania | bearings supplier Tanzania, hydraulic parts Dar es Salaam, spare parts East Africa |
| Mechanical Engineering | `/mechanical-engineering/` | mechanical engineering solutions Tanzania | motors gearboxes Tanzania, industrial valves East Africa |
| Electrical Engineering | `/electrical-engineering/` | electrical engineering products Tanzania | switchgear supplier Tanzania, ABB Siemens Tanzania, VFD supplier East Africa |
| Mining Equipment | `/mining-equipment-east-africa/` | mining equipment supplier East Africa | mining spare parts Tanzania, crusher parts East Africa, conveyor belt Tanzania |
| Petroleum & Gas | `/petroleum-gas-engineering/` | petroleum gas engineering Tanzania | pipeline parts Tanzania, oil gas supplier East Africa, Rotork actuators Tanzania |
| Power & Energy | `/power-energy-solutions/` | power generation equipment Tanzania | generator parts Tanzania, solar energy supplier East Africa |
| Automation | `/automation-engineering/` | PLC SCADA supplier Tanzania | industrial automation Tanzania, Siemens PLC Tanzania, Rockwell automation East Africa |
| Material Engineering | `/material-engineering/` | material engineering supplier Tanzania | industrial alloys Tanzania, corrosion resistant materials East Africa |
| Construction | `/construction-equipment/` | construction equipment Tanzania | Caterpillar parts Tanzania, Terex equipment East Africa |
| Tanzania (hub) | `/tanzania/` | industrial equipment supplier Tanzania | engineering solutions Tanzania, construction machinery Tanzania |
| Dar es Salaam | `/dar-es-salaam/` | industrial parts Dar es Salaam | spare parts supplier Dar es Salaam, engineering company DSM |

---

## 6. Build & Deployment Notes

### Build process

The existing `package.json` build scripts must be updated to include all new files:

```json
"scripts": {
  "dev": "live-server --port=3000 --no-browser",
  "build:css": "cleancss -o css/style.min.css css/style.css",
  "build:js": "uglifyjs js/components.js js/industries.js js/products.js js/articles.js js/search.js js/main.js -o js/bundle.min.js -c -m",
  "build": "npm run build:css && npm run build:js"
}
```

All service pages and location pages should reference the minified bundle in production:
```html
<script defer src="/js/bundle.min.js"></script>
```

Use an absolute path (`/js/bundle.min.js`) not relative (`../js/bundle.min.js`) to avoid path issues in nested directories.

### Design system compliance

All new pages and components must follow `docs/design.md` exactly:

- **No `border-radius`** on cards, buttons, or images — use `clip-path` chamfers only
- **No new colors** — only `#FF6600`, dark surfaces `#080808`–`#222222`, and `#F0F0F0`/`#FFFFFF` text
- **Fonts strictly:** Bebas Neue for headings/stats, Barlow Condensed for labels/nav/buttons, Barlow for body
- **Section vertical padding:** always `8rem 0` (128px top and bottom)
- **The `.label` eyebrow pattern** (orange, uppercase, 0.3em tracking, with `::before` orange rule) must appear on every new section

### Hosting & file serving

- Ensure the hosting server sends correct `Content-Type: text/html` for directory index files (`/mining-equipment-east-africa/` should serve `/mining-equipment-east-africa/index.html` without a redirect)
- Enable GZIP or Brotli compression at the server level (in addition to Cloudflare)
- All pages must be served over HTTPS — redirect all HTTP → HTTPS at the server or Cloudflare level
- 404 page: create `404.html` in root with the site nav, a friendly message, and links back to key sections

---

## 7. Acceptance Criteria

The following must be verified and evidenced before each phase is signed off.

### Phase 1 sign-off checklist

- [ ] New `<title>` appears correctly in Google Chrome tab and when shared on WhatsApp
- [ ] Hero stats show real numbers (`6+`, `200+`, `50+`, `12`) in HTML source (view-source, no JS)
- [ ] WhatsApp float button visible on all pages, mobile and desktop, does not overlap content
- [ ] Footer shows full address: `Makongo Road, Sinza, 14129, Dar es Salaam, Tanzania`
- [ ] All social media links go to real URLs or are removed
- [ ] Enquiry form has 3 fields only; submission opens a pre-filled WhatsApp message

### Phase 2 sign-off checklist

- [ ] JSON-LD passes Google Rich Results Test with zero errors
- [ ] All 9 service pages and 2 location pages exist and are accessible
- [ ] `sitemap.xml` is valid and submitted to Google Search Console
- [ ] Google Search Console confirms all pages are indexed (allow 2 weeks post-submission)
- [ ] PageSpeed Insights mobile score ≥ 80 on homepage (screenshot required)
- [ ] No Unsplash URLs remain in production HTML — all images locally hosted
- [ ] All below-fold `<img>` elements have `loading="lazy"` and explicit `width`/`height`
- [ ] Cloudflare active — confirm via `curl -I https://www.ipatechs.com` showing `cf-ray` response header

### Phase 3 sign-off checklist

- [ ] ISO badge either removed or links to a certification page with real certificate details
- [ ] Minimum 6 real client testimonials with full name and company visible on homepage
- [ ] Team section shows minimum 1 real photo with name and role
- [ ] Simplified enquiry form live (3 fields, WhatsApp submission)
- [ ] Delivery promise strip visible above CTA band

### Phase 4 sign-off checklist

- [ ] All blog articles accessible at standalone URLs (`/blog/[slug]/`)
- [ ] GTM installed — verify in Google Tag Assistant browser extension
- [ ] WhatsApp click, form submission, and phone click events visible in GTM preview mode
- [ ] Swahili pages live and `hreflang` tags present on English originals

---

## 8. Manual Interventions Required

The following items require action from the client or a third party before they can be completed by the developer.

### ⏳ REQ-006 — Open Graph image
**Action:** Create `assets/images/og-image.jpg` — a 1200×630px branded image (IPATECHS logo on dark background with tagline). This appears as the preview thumbnail when the site URL is shared on WhatsApp, LinkedIn, and Facebook.
**Who:** Designer / Client

### ⏳ REQ-011 — Google Maps embed
**Action:** 
1. Create and verify Google Business Profile at [business.google.com](https://business.google.com)
2. Provide the GBP Place ID to the developer
3. Generate a Google Maps Embed API key from [Google Cloud Console](https://console.cloud.google.com)
**Who:** Client
**Note:** The embed code is ready in the requirements doc — just needs the Place ID and API key.

### ⏳ REQ-013 — Cloudflare setup
**Action:**
1. Create Cloudflare account at [cloudflare.com](https://cloudflare.com)
2. Point ipatechs.com DNS through Cloudflare nameservers
3. Developer then configures: SSL Full (Strict), Always Use HTTPS, Auto Minify, Brotli, Rocket Loader, Browser Cache TTL, Page Rules
**Who:** Client (DNS), Developer (settings)
**Settings to apply (developer):**

| Setting | Value |
|---|---|
| SSL/TLS mode | Full (Strict) |
| Always Use HTTPS | On |
| Auto Minify | HTML ✓, CSS ✓, JavaScript ✓ |
| Brotli compression | On |
| Rocket Loader | On |
| Browser Cache TTL | 1 month |
| Page Rule: `*.ipatechs.com/assets/*` | Cache Everything, Edge Cache TTL: 1 month |

### ⏳ REQ-016 — Real testimonials
**Action:** Provide 6 real client testimonials with: full name, company name, role/title, and 2–4 sentence quote about IPATECHS service. Current placeholders are in place.
**Who:** Client
**Files to update:** `index.html` — `.testimonial-card` sections

### ⏳ REQ-017 — Real team photos
**Action:** Provide team member photos (JPG/PNG, minimum 400×400px) and confirm names/roles. Current placeholders with initials are in place.
**Who:** Client
**Files to update:** `index.html` — `.team-card` sections, place photos in `assets/images/team/`

### ⏳ REQ-021 — Google Tag Manager container ID
**Action:** Create a GTM container at [tagmanager.google.com](https://tagmanager.google.com) and provide the container ID (format: `GTM-XXXXXXX`).
**Who:** Client / Marketing
**Files to update:** Replace `GTM-XXXXXXX` in `index.html` (2 occurrences — head and body snippets)

### ⏳ REQ-022 — Swahili translations
**Action:** Professional Swahili translation of top 3 pages (homepage, industrial spare parts, contact). Do NOT use Google Translate — professional translator only.
**Who:** Client / Translator
**Status:** Skipped for now, implementation ready when translations provided

### ⏳ WebP conversion (REQ-012 enhancement)
**Action:** Install `cwebp` (`sudo apt-get install webp` or `brew install webp`) and convert all JPG/PNG images to WebP format. Update `<img>` tags to `<picture>` with WebP + fallback sources.
**Who:** Developer (when cwebp available)
**Command:** `for f in assets/images/*.jpg; do cwebp -q 82 "$f" -o "${f%.*}.webp"; done`

### ⏳ PageSpeed Insights verification
**Action:** Run Google PageSpeed Insights on the homepage after deployment. Target: mobile score ≥ 80.
**Who:** Developer / Client
**URL:** [https://pagespeed.web.dev](https://pagespeed.web.dev)

### ⏳ Google Search Console submission
**Action:** 
1. Add property `https://www.ipatechs.com` to Google Search Console
2. Submit `https://www.ipatechs.com/sitemap.xml`
3. Validate JSON-LD at [Google Rich Results Test](https://search.google.com/test/rich-results)
**Who:** Client / Developer

---

*IPATECHS Company Limited · ipatechs.com · info@ipatechs.com · +255 750 304 097*
*Makongo Road, Sinza, 14129, Dar es Salaam, Tanzania*
