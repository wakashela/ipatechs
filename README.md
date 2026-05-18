# IPATECHS Company Limited

**Industrial Spare Parts & Engineering Solutions — Dar es Salaam, Tanzania**

[ipatechs.com](https://www.ipatechs.com) · info@ipatechs.com · +255 750 304 097

---

## Overview

Static HTML/CSS/vanilla JS website for IPATECHS — East Africa's trusted supplier of industrial spare parts, bearings, motors, pumps, and engineering equipment. Optimised for SEO performance on Google Tanzania and designed for conversion through WhatsApp — the primary B2B communication channel in the region.

**Objective:** Rank #1 for industrial spare parts searches in Dar es Salaam and East Africa while delivering a conversion-optimised user experience.

## Tech Stack

| Layer | Technology |
|---|---|
| HTML | Semantic HTML5, no framework |
| CSS | Custom CSS with CSS variables (`css/style.css`) |
| JS | Vanilla JavaScript (ES5 compatible), no framework |
| Fonts | Google Fonts — Bebas Neue, Barlow Condensed, Barlow |
| Build | `clean-css` (minification), `uglify-js` (minification + mangling) |
| Dev Server | `live-server` (port 3000) |
| Hosting | Static files served via any web server or CDN |

## Project Structure

```
├── index.html                          # Homepage
├── css/
│   ├── style.css                       # Source stylesheet (2,900+ lines)
│   └── style.min.css                   # Minified build output
├── js/
│   ├── components.js                   # Shared nav, footer, modals for subpages
│   ├── industries.js                   # Industry data + modal handlers
│   ├── products.js                     # Product data + detail modal
│   ├── articles.js                     # Blog article data + modal (8 articles)
│   ├── search.js                       # Client-side product/industry/article search
│   ├── main.js                         # Nav, counters, reveal animations, forms, GTM events
│   └── bundle.min.js                   # Minified build output
├── assets/
│   ├── images/                         # Local images (24 Unsplash JPGs + logo)
│   └── brands/                         # Brand logo assets (placeholder)
├── blog/
│   ├── index.html                      # Blog listing page (8 articles)
│   └── [slug]/index.html              # 8 standalone article pages
├── [service-slug]/index.html           # 9 service pages
├── [location]/index.html               # 2 location landing pages
├── sitemap.xml                         # 21 URLs
├── robots.txt                          # Allow all, sitemap reference
├── 404.html                            # (to be created)
├── package.json                        # Build scripts + dependencies
└── docs/
    ├── design.md                       # Design system — Industrial Precision Dark
    └── ipatechs_website_development_requirements.md  # Full requirements + status
```

## Pages (21 total)

### Homepage
- `/` — Full landing page with hero, services, industries, products, partners, testimonials, blog, CTA

### Service Pages (9)
- `/industrial-spare-parts/` — Bearings, hydraulics, seals, power transmission
- `/mechanical-engineering/` — Motors, gearboxes, pumps, valves
- `/electrical-engineering/` — Switchgear, VFDs, ABB/Siemens products
- `/material-engineering/` — Alloys, corrosion-resistant materials, welding
- `/petroleum-gas-engineering/` — Pipeline parts, Rotork actuators, gas safety
- `/power-energy-solutions/` — Generators, transformers, solar equipment
- `/mining-equipment-east-africa/` — Crusher parts, conveyors, CAT/Komatsu
- `/automation-engineering/` — PLC, SCADA, Siemens/Rockwell automation
- `/construction-equipment/` — CAT, Terex, JCB parts and equipment

### Location Pages (2)
- `/tanzania/` — Nationwide coverage across all regions
- `/dar-es-salaam/` — Local delivery across all 5 DSM districts

### Blog (9)
- `/blog/` — Article listing
- `/blog/skf-bearings-tanzania/` — SKF bearings buyer's guide
- `/blog/spare-parts-dar-es-salaam/` — DSM supplier selection guide
- `/blog/cummins-engine-parts/` — Cummins parts for East Africa
- `/blog/abb-siemens-distributor/` — ABB/Siemens procurement guide
- `/blog/plc-scada-tanzania/` — PLC/SCADA automation trends
- `/blog/mechanical/` — Mechanical engineering products
- `/blog/electrical/` — Electrical engineering products
- `/blog/automation/` — Industrial automation overview

## Design System

**Industrial Precision Dark** — documented in `docs/design.md`.

- **Primary accent:** `#FF6600` (industrial orange — CTAs, accents, labels only)
- **Surface hierarchy:** `#080808` → `#101010` → `#181818` → `#222222`
- **Typography:** Bebas Neue (headings/stats), Barlow Condensed (nav/labels/buttons), Barlow (body)
- **Shape language:** Angular `clip-path` polygon chamfers replace `border-radius`
- **No new colors allowed** — power is in single-accent restraint

## Getting Started

### Prerequisites
- Node.js and npm

### Install
```bash
git clone https://github.com/wakashela/ipatechs.git
cd ipatechs
npm install
```

### Development
```bash
npm run dev
```
Starts `live-server` on port 3000 with hot reload and no auto-browser-open.

### Build
```bash
npm run build
```
Minifies CSS and JS:
- `css/style.css` → `css/style.min.css`
- `js/components.js` + `js/industries.js` + `js/products.js` + `js/articles.js` + `js/search.js` + `js/main.js` → `js/bundle.min.js`

For production, service pages and subpages reference:
```html
<link rel="stylesheet" href="/css/style.min.css" />
<script defer src="/js/bundle.min.js"></script>
```

## SEO Features

- **22 unique, keyword-optimised title/meta description pairs**
- **Canonical URLs** on every page
- **Open Graph + Twitter Card** meta tags for social sharing
- **JSON-LD** structured data: `LocalBusiness`, `Service`, `Article`, `Organization`, `WebSite`
- **sitemap.xml** (21 URLs) + **robots.txt**
- **Semantic HTML5** with proper heading hierarchy
- **Static HTML content** on all subpages (no JS-rendered content)
- **Lazy loading** on 79 below-fold images
- **Local image hosting** (no external CDN dependencies)
- **Breadcrumb navigation** on location and blog pages

## Conversion Features

- **WhatsApp float button** — fixed green pulse button on every page
- **Simplified enquiry form** — 3 fields (name, WhatsApp, message), submits via WhatsApp pre-fill
- **Delivery promise strip** — same-day quotes, 24-72hr delivery, East Africa coverage
- **Product search bar** — client-side search across products, industries, and articles
- **Google Tag Manager** integration with dataLayer events for conversions

## Manual Setup Required

See `docs/ipatechs_website_development_requirements.md` Section 8 for full details.

| Task | Priority |
|---|---|
| Create `assets/images/og-image.jpg` (1200×630px) | High |
| Set up Google Business Profile + Maps API key | High |
| Configure Cloudflare (free tier) | High |
| Replace `GTM-XXXXXXX` with real container ID | High |
| Provide 6 real client testimonials | Medium |
| Provide team member photos + names | Medium |
| Submit sitemap to Google Search Console | Medium |
| Run PageSpeed Insights (target: mobile ≥ 80) | Medium |
| WebP image conversion (`cwebp` needed) | Low |
| Swahili translations (professional translator) | Low |

## License

Proprietary — IPATECHS Company Limited. All rights reserved.
