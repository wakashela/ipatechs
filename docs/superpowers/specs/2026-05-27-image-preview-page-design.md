# Image Preview Page — Design Spec

## Purpose

A local development helper page for previewing nano-banana generated images. Used to evaluate AI-generated images before integrating them into the ipatechs website. Accessible via `npm run dev` (live-server, port 3000).

## Architecture

### Technology
- Single static HTML file: `image-preview/index.html`
- No new JS or CSS files — all logic is inline in the page
- Reuses `css/style.css` for base styles (CSS variables, typography, dark theme)
- Nav and footer injected by existing `js/components.js` (standard subpage pattern)

### Image Discovery
- Page reads the live-server directory listing (live-server serves HTML directory indexes on subdirectories)
- Fetches the directory index page via `fetch()`, parses `<a>` tags to find image files (`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.avif`)
- No hardcoded image list, no extra scripts

### Default Directory
- `assets/images/nano-banana/` — dedicated subdirectory for nano-banana outputs (keeps generated images separate from existing site images)
- Overridable via URL query param: `?dir=assets/images/` or `?dir=assets/images/some-other-folder/`

### Routing
- Vercel rewrite: `/image-preview` → `/image-preview/index.html`
- No entry in sitemap.xml (dev-only tool, not for users)

## Page Structure

### Hero (compact, matching subpage pattern)
- `min-height: 40vh`, `display: block`, centered content `max-width: 800px`
- Title: "Image Preview"
- Subtitle: "Preview and compare nano-banana generated images"
- Shows current directory path in muted text

### Toolbar
- Sticky bar below hero (or fixed at top after scroll)
- Left: directory breadcrumb (editable text input to switch directories)
- Center: image count ("24 images")
- Right: "Compare Mode" toggle button (orange when active)
- When compare mode is active, gallery shows selection checkboxes/borders

### Gallery Grid
- **3-column masonry layout** (varying heights, natural feel for mixed aspect ratios)
- Uses CSS columns or a simple grid with row-span adjustments based on natural aspect ratio
- On desktop: 3 columns
- On tablet (max-width: 768px): 2 columns
- On mobile (max-width: 600px): 1 column
- Images use `object-fit: cover` with a subtle dark overlay (matches site style: `filter: brightness(0.5) saturate(0.4)`)
- On hover: overlay lifts, image brightens to full color, caption slides up from bottom
- Caption shows filename (Barlow Condensed, 0.75rem, muted)
- Images use `loading="lazy"`
- Container has `clip-path: polygon()` chamfered corners (matching site convention)

### Compare Mode (gallery state)
- Toggle via toolbar button
- Active state indicated by orange border on toolbar button
- Clicking an image selects it (orange chamfered border, 3px)
- Clicking same image deselects it
- When exactly 2 images selected, the comparison view opens automatically

## Lightbox

- Opens when clicking a gallery image (non-compare mode)
- Dark backdrop overlay (`rgba(0,0,0,0.9)` with noise texture)
- Image container: `max-width: 90vw`, `max-height: 80vh`, centered, chamfered edges
- Top bar: filename (left, Bebas Neue, orange), dimensions + file size (right, muted)
- Bottom bar: image counter ("3 of 24", left), "Add to Compare" button (right, orange outline)
- Prev/Next: on-screen arrow buttons (orange on hover) + keyboard arrow keys
- Close: X button top-right + Escape key + click backdrop
- Image auto-scales to fit viewport, maintains aspect ratio
- CSS transitions for open/close (matching existing modal patterns)

## Comparison View

- Opens when 2 images are selected via compare mode or "Add to Compare" buttons
- Replaces gallery grid (same page, different view state)
- Top bar: "image-a.png vs image-b.png" labels (left name in white, right name in orange)
- Controls: Reset, Swap, Back to Gallery buttons
- Main area: two images side by side, separated by a draggable vertical orange bar
- **Slider behavior:** clip the left image to the slider position; left image is positioned at 50% width, right image fills remaining space. Dragging the handle adjusts the clip of the left image
- Orange divider line (2px) + chamfered handle (clip-path: polygon, 24x24px, orange)
- Handle draggable via mouse/touch, nudged via keyboard arrow keys
- Swap button flips which image is left vs right
- Reset centers the slider at 50%
- Exit returns to gallery grid (clears selection)

## Data Flow

```
URL query param (?dir=...) 
  → fetch directory listing 
  → parse image URLs 
  → render gallery grid 
  → user interaction (click, compare, lightbox) 
  → update view state
```

## State Management
- Simple JavaScript object in page scope:
  - `currentDir`: string, the directory being previewed
  - `images`: array of `{url, name, ext}` 
  - `imagesLoaded`: array of promises for `{width, height, fileSize}` per image
  - `selectedForCompare`: array (max 2 indices)
  - `viewMode`: 'gallery' | 'lightbox' | 'comparison'
  - `lightboxIndex`: current image index in lightbox
  - `comparisonSlider`: 0-1 position of the slider handle

## Error Handling
- If directory fetch fails: show error message "Cannot read directory. Check the path."
- If directory has no images: show empty state "No images found in this directory"
- If image fails to load: show broken-image placeholder (muted, with icon)
- If comparison has only 1 image in directory: comparison mode shows warning

## CSS
- ~60-80 lines of inline styles in a `<style>` block in `<head>`
- Uses CSS variables from style.css for all colors
- No border-radius (chamfers only)
- Transitions use `var(--transition)` cubic-bezier
- Responsive breakpoints: 768px, 600px (matching existing site)

## JS
- ~150-200 lines of inline JS in a `<script>` block before `</body>`
- No dependencies, no frameworks, no modules
- Self-executing IIFE to avoid global namespace pollution
- Functions for: fetchDirectory, renderGallery, openLightbox, closeLightbox, navigateLightbox, toggleCompareMode, selectForCompare, openComparison, closeComparison
- Debounced resize handler for masonry recalculation
- Passive touchevent listeners for slider dragging
