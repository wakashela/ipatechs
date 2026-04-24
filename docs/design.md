---
version: alpha
name: IPA Techs — Industrial Precision Dark
description: >
  Visual identity system for IPA Techs, East Africa's premier industrial spare
  parts and engineering solutions supplier. The system communicates mechanical
  authority, precision, and reliability through an Industrial Precision Dark
  aesthetic: near-black steel backgrounds, vivid industrial orange accents,
  bold condensed typography, and angular clip-path geometry instead of
  traditional rounded corners.

colors:
  primary: "#FF6600"
  primary-hover: "#FF8800"
  primary-muted: "#FF660015"
  surface: "#080808"
  surface-raised: "#101010"
  surface-card: "#181818"
  surface-elevated: "#222222"
  surface-steel: "#2A2A2A"
  on-surface: "#F0F0F0"
  on-surface-high: "#FFFFFF"
  on-surface-muted: "#888888"
  on-primary: "#000000"
  border: "#141414"
  border-subtle: "#1A1A1A"

typography:
  display:
    fontFamily: Bebas Neue
    fontSize: 7rem
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: 0.03em
  headline-xl:
    fontFamily: Bebas Neue
    fontSize: 4.5rem
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: Bebas Neue
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Barlow Condensed
    fontSize: 1.3rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Barlow Condensed
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.3em
  nav-link:
    fontFamily: Barlow Condensed
    fontSize: 0.85rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.15em
  body-md:
    fontFamily: Barlow
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.8
  body-sm:
    fontFamily: Barlow
    fontSize: 0.9rem
    fontWeight: 400
    lineHeight: 1.7
  body-xs:
    fontFamily: Barlow
    fontSize: 0.8rem
    fontWeight: 500
    lineHeight: 1.5
  stat-num:
    fontFamily: Bebas Neue
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1

rounded:
  none: 0px
  sm: 4px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  2xl: 128px
  gutter: 24px
  section-v: 128px
  container-max: 1280px
  container-px: 32px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    padding: 0.9rem 2rem
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    backgroundColor-overlay: "{colors.on-surface-high}"
    overlay-opacity: "0.15"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-surface-high}"
    borderColor: "{colors.border-subtle}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    padding: 0.9rem 2rem
  button-ghost-hover:
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "transparent"
    textColor: "{colors.on-surface-muted}"
    typography: "{typography.nav-link}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.border}"
  nav-link-hover:
    textColor: "{colors.on-surface-high}"
  nav-link-active-indicator:
    backgroundColor: "{colors.primary}"
    height: 2px
  service-card:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.on-surface}"
    padding: 2.5rem 2rem
    rounded: "{rounded.none}"
  service-card-hover:
    backgroundColor: "{colors.surface-raised}"
    borderColor: "{colors.primary}"
    border-position: bottom
    border-height: 2px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
  feature-icon:
    backgroundColor: "{colors.primary-muted}"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    size: 48px
  blog-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.none}"
  modal:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.on-surface}"
    borderColor: "{colors.border}"
  input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-surface}"
    borderColor: "{colors.border}"
    typography: "{typography.body-sm}"
    padding: 0.75rem 1rem
  input-focus:
    borderColor: "{colors.primary}"
  ticker-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  cta-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  section-label:
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
---

# IPA Techs Design System

## Overview

**Industrial Precision Dark** — the design language for IPA Techs merges the raw authority of heavy machinery with the visual discipline of precision engineering.

The aesthetic is intentionally severe: near-black backgrounds evoke steel floors and factory walls; a single, vivid industrial orange (`#FF6600`) acts as the sole accent, drawing the eye to every call to action and interactive element. There are no soft gradients, no playful pastels, no decorative flourishes. Every pixel earns its place.

The typographic system is built around two complementary families. **Bebas Neue** — a tall, bold, all-caps display face — carries all major headings and statistics, projecting the confidence of industrial signage. **Barlow Condensed** handles labels, navigation, and UI copy in all-caps with generous letter spacing, reinforcing the sense of precision. **Barlow** (regular weight) handles all body text, providing legibility contrast against the condensed display faces.

Angular **clip-path polygon cutoffs** replace traditional border-radius everywhere: cards, buttons, icons, badges, and image frames are chamfered at their corners — a custom `polygon(0 0, N% 0, 100% M%, 100% 100%, ...)` pattern that signals engineered precision and differentiates IPA Techs from generic web templates.

The brand voice is: **trusted**, **direct**, **technically authoritative**. IPA Techs does not need to shout; its restraint communicates confidence.

## Colors

The palette is a strict monochromatic dark foundation broken by one high-energy accent.

- **Primary (`#FF6600`):** Industrial Orange — the sole interactive driver. Used exclusively for CTAs, active states, hover indicators, section labels, icon tints, and the ticker/CTA bands. Directly references the safety orange of industrial environments and heavy equipment brands (Caterpillar, Terex).
- **Primary Hover (`#FF8800`):** A slightly warmer shift on hover, keeping the interaction feedback within the orange family.
- **Primary Muted (`#FF6600` at ~8% opacity):** Used for icon backgrounds and card highlights, providing tinted depth without competing with solid primary elements.
- **Surface (`#080808`):** Near-black — the page base. Not pure black; the slight warmth of `#080808` prevents harshness.
- **Surface Raised (`#101010`):** One step above surface, used for the nav (when scrolled), features strip, services section, and the enquiry modal.
- **Surface Card (`#181818`):** The resting background for product cards, blog cards, and form inputs — creates perceptible layering without dramatic contrast.
- **Surface Elevated (`#222222`):** The highest surface layer, reserved for steel borders, separators, and the hover state of the `surface-steel` strip.
- **On-Surface (`#F0F0F0`):** Primary text — warm off-white, slightly softer than pure white for extended reading comfort.
- **On-Surface High (`#FFFFFF`):** Pure white reserved for headings, active navigation items, and high-emphasis labels.
- **On-Surface Muted (`#888888`):** Secondary text — captions, metadata, body copy, and inactive nav links. Provides sufficient contrast against `#101010` for WCAG AA (5.27:1).
- **On-Primary (`#000000`):** Text placed on any orange background — black ensures maximum contrast (21:1 against `#FF6600`).
- **Border (`#141414`):** Near-invisible dividers used for nav border, card grid separators, and section lines.

A noise texture overlay at 35% opacity is applied globally as a CSS `body::before` pseudo-element using an inline SVG `feTurbulence` filter, adding subtle grain that references industrial steel surfaces.

## Typography

The typography system pairs display authority with data clarity.

- **Bebas Neue** (display & headline): Loaded from Google Fonts. A tall, condensed, all-caps grotesque with zero lowercase usage. Used for the hero title, all `section-title` headings, statistic counters, and the footer logo mark. Its narrow proportions allow massive font sizes without consuming horizontal real estate.
- **Barlow Condensed** (labels, nav, UI copy): All-caps with generous letter-spacing (0.15–0.3em). Used for nav links, section labels, button text, card titles, and any UI element that needs to read as "system text" rather than editorial copy.
- **Barlow** (body): The regular-weight variant for paragraphs, descriptions, and longer-form content. Light (300) to medium (500) weights only — never bold in body contexts.

**Scale:**
- `display` (Bebas Neue, fluid `3.5–7rem`): Hero heading only.
- `headline-xl` (Bebas Neue, `clamp(2.8rem, 5vw, 4.5rem)`): All section titles.
- `headline-lg` (Bebas Neue, `3rem`): Stat numbers, large subsection titles.
- `headline-md` (Barlow Condensed 700, `1.3rem`): Service card titles, product names.
- `label-caps` (Barlow Condensed 700, `0.75rem`, `0.3em`): Section eyebrows and category labels — always paired with a `2rem` orange leading rule (`::before` pseudo-element).
- `nav-link` (Barlow Condensed 600, `0.85rem`, `0.15em`): Navigation items and all button text.
- `body-md` (Barlow 400, `1rem`, `1.8`): Hero subtitle and about section prose.
- `body-sm` (Barlow 400, `0.9rem`, `1.7`): Service and blog card descriptions.
- `body-xs` (Barlow 500, `0.8rem`): Meta text, timestamps, footer copy.

Text selection uses `background: #FF6600; color: #000` to reinforce the brand accent even in reading interactions.

## Layout

The layout follows a **Fluid Fixed-Max Grid** model.

A single centered container with `max-width: 1280px` and `padding: 0 2rem` spans all sections. The grid structure adapts per section type:

- **Hero:** `grid-template-columns: 1fr 1fr` — editorial split between text content and image.
- **Services:** `grid-template-columns: repeat(3, 1fr)` — equal-width cards separated by `1.5px` border-colored gaps.
- **Products:** `grid-template-columns: repeat(4, 1fr)` — dense catalogue grid.
- **Industries:** `grid-template-columns: repeat(4, 1fr)` — portrait image cards.
- **Portfolio:** `grid-template-columns: repeat(12, 1fr)` — asymmetric masonry pattern (6+6, then 4+4+4) to break the regular grid rhythm.
- **Blog:** `grid-template-columns: repeat(3, 1fr)`.
- **Footer:** `grid-template-columns: 2fr 1fr 1fr 1fr`.

**Spacing scale** follows an 8px base system with `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`, `2xl: 128px`. All section vertical padding is `8rem` (128px) top and bottom.

**Navigation** is `position: fixed` with `z-index: 1000`, transitioning from fully transparent to a `backdrop-filter: blur(20px)` frosted glass panel on scroll (triggered at `scrollY > 60px`).

A full-width **ticker band** (Industrial Orange background, scrolling marquee of service categories) sits between the Hero and the Features Strip, serving as a visual separator and brand energy booster.

The **back-to-top button** is `position: fixed; bottom: 2rem; right: 2rem`, appearing only after `scrollY > 400px`.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** — no box shadows are used for cards or containers. Instead, distinct surface levels (`#080808` → `#101010` → `#181818` → `#222222`) create implicit Z-stacking.

The exceptions are **interactive hover states** on product cards and blog cards, which lift via `transform: translateY(-6px)` combined with `box-shadow: 0 20px 60px rgba(0,0,0,0.4)`. This elevation communicates interactivity without introducing decorative shadow in the resting state.

Button hover states for `button-primary` use `box-shadow: 0 12px 40px rgba(255,102,0,0.35)` — an orange glow that reinforces the brand color while suggesting clickability.

The hero section uses radial gradient atmospheric glows (`rgba(255,102,0,0.08)` and `rgba(255,102,0,0.05)`) positioned at specific coordinates to create subtle depth without physical shadow.

A global noise texture pseudo-element (`body::before`, `opacity: 0.35`) adds micro-texture that reads as depth under close inspection.

## Shapes

**Angular Chamfer** is the defining shape language of IPA Techs.

All cards, buttons, icons, badges, and image frames use `clip-path: polygon(...)` cutoffs at one or more corners — never `border-radius`. The chamfer depth varies by component size:

- **Buttons:** `clip-path: polygon(0 0, 95% 0, 100% 20%, 100% 100%, 5% 100%, 0 80%)` (bottom-left and top-right cuts).
- **Hero image / About image:** `clip-path: polygon(0 0, 88% 0, 100% 12%, 100% 100%, 12% 100%, 0 88%)` — larger chamfer for visual drama.
- **Feature icons / Service icons:** `clip-path: polygon(0 0, 80% 0, 100% 20%, 100% 100%, 20% 100%, 0 80%)` — small square icon with proportional chamfer.
- **Portfolio / Industry cards:** `clip-path: polygon(0 0, 97% 0, 100% 3%, 100% 100%, 3% 100%, 0 97%)` — subtle chamfer on full-bleed imagery.
- **Product cards:** `clip-path: polygon(0 0, 95% 0, 100% 5%, 100% 100%, 5% 100%, 0 95%)`.
- **CTA / Year badges:** Single-corner chamfer on the bottom-left or matching corner.

The `rounded` token scale provides `none: 0px` (primary value), `sm: 4px` (reserved only for scroll bar thumb and minor browser-native elements), and `full: 9999px` (reserved for the pulsing status dot in the hero float tag).

No element uses mixed corner treatments (some rounded, some sharp) within the same component.

## Components

### Buttons

Two button variants exist. Both use `font-family: Barlow Condensed; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase`.

**Primary button** (`button-primary`): Solid `#FF6600` fill, `#000` text, clip-path chamfer, internal `::after` white overlay (`opacity: 0 → 0.15`) on hover. On hover: `translateY(-2px)` + orange glow shadow. Icon arrows shift `translateX(4px)` on hover.

**Ghost button** (`button-ghost`): Transparent background, white `border: 1px solid rgba(255,255,255,0.2)`, transitions to `border-color: #FF6600; color: #FF6600` on hover. No transform on ghost hover.

### Navigation

The nav logo combines a clip-path chamfered orange icon mark with Bebas Neue wordmark (`IPA` white + `TECHS` orange). Nav links use `Barlow Condensed 600`, muted grey resting color, with a `scaleX(0 → 1)` orange underline on hover (`transform-origin: left`).

On mobile (`< 768px`), the nav links hide; a hamburger (three 26×2px white bars) triggers a full-screen overlay menu with Bebas Neue links at `3rem`.

### Cards

**Service Card:** `background: #101010`, bottom border indicator scales in on hover (`scaleX(0 → 1)`), large ghost number in top-right corner that tints orange on hover. No box-shadow at rest.

**Product Card:** `background: #181818`, chamfered clip-path, white product image area (`background: #fff`, `padding: 1.5rem`), `translateY(-6px)` + shadow lift on hover. Enquiry button at card base.

**Blog Card:** `background: #181818`, image thumbnail desaturated (`filter: saturate(0.6)`), saturates to `0.8` + `scale(1.05)` on hover. Card lifts `translateY(-4px)`.

**Industry Card:** Full-bleed portrait image, `filter: brightness(0.4) saturate(0.5)` at rest, dims further on hover with the overlay shifting toward orange (`rgba(255,102,0,0.25)`). Category number ghost-overlaid in top-left.

### Section Label

Every section eyebrow uses a `div.label` pattern: `Barlow Condensed 700`, `0.75rem`, `0.3em` letter-spacing, `#FF6600`, with a `2rem × 2px` orange bar prepended via `::before`. This is the only use of the primary color for text (never used for body copy).

### Modals & Forms

The enquiry modal uses `backdrop-filter: blur(8px)` on a `rgba(0,0,0,0.85)` overlay. The modal panel itself is `#101010` with chamfer clip-path. Inputs are `#181818` with `border: 1px solid #141414`, transitioning to `border-color: #FF6600` on focus. Submit button uses full-width `button-primary`.

### Ticker / Marquee

Two infinite-scroll ticker bands are used: a primary orange band at the top (service categories, black text) and a grey partner brand scroller in the Partners section. Both animate via `translateX` keyframes; the primary band also doubles as a visual section separator.

### Scroll Reveal

All major content blocks use a shared `.reveal` pattern: `opacity: 0; transform: translateY(40px)` at rest, transitioning to `opacity: 1; transform: none` when entering the viewport via `IntersectionObserver`. Directional variants `.reveal-left` and `.reveal-right` use horizontal translations. Staggered `transition-delay` values (in `0.1s` increments) create cascade effects across grid children.

## Do's and Don'ts

**Do:**
- Use `#FF6600` only for interactive affordances, section labels, icon tints, and the ticker/CTA bands. It must never appear as decorative color or for large background areas (except the ticker and CTA band, where it is the full point).
- Apply clip-path chamfers consistently across all card and button shapes. Never mix chamfered and rounded corners within the same section or component group.
- Use Bebas Neue exclusively for headings, statistics, and the logo wordmark — not for body copy, labels, or buttons.
- Keep surface layering sequential: `#080808` (page) → `#101010` (raised) → `#181818` (card) → `#222222` (elevated). Never jump more than one level without a section context shift.
- Maintain the `label-caps` pattern (eyebrow + leading orange rule) for all section introductions.
- Use `color: transparent; -webkit-text-stroke: 2px #ffffff` for the "outline" title word in the hero. This contrast technique should remain unique to the hero and not be replicated elsewhere.
- Preserve the noise texture overlay (`body::before`) — it is essential to the industrial surface feel.

**Don't:**
- Don't use `border-radius` on any card, button, image, or interactive element. All softening is handled by clip-path chamfers.
- Don't add new colors to the palette. The power of the system depends on the single-accent restraint. If a new informational color is needed (e.g., error states), derive it from the orange family.
- Don't use Bebas Neue below `1.5rem` — at small sizes it loses legibility and degrades to illegible squinting.
- Don't use box shadows at resting state on cards or containers. Shadows appear only on hover and on button interactions.
- Don't use purple, blue, or "tech" gradients (purple-to-blue is explicitly excluded from this brand). The system is warm (orange on near-black), not cool.
- Don't place white or light text directly on `#FF6600` backgrounds without verifying contrast — only `#000000` (21:1) passes WCAG AAA on the primary orange.
- Don't animate more than one scroll-reveal per visible viewport area simultaneously. Stagger delays must not exceed `0.8s` total across a group.
- Don't use Inter, Roboto, or system-ui fonts anywhere in the design — they are explicitly incompatible with the brand's industrial character.
