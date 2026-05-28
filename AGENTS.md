# IPATECHS Project - Agent Instructions

## Image Generation

When product images, hero banners, warehouse scenes, or commercial photography are needed for any page, use the **product-image-generation** skill.

This skill:
- Accepts structured prompts with filename, aspect ratio, and size
- Generates via HuggingFace (FLUX.1, SDXL) or Together AI (FLUX.1-schnell-Free)
- Embedds brand visual traits (SKF, FAG, Timken, Donaldson, Parker, Gates, etc.) in prompts
- Outputs images to specified directories

**Output directory for all generated images:** `assets/images/nano-banana/`

## Project Structure

- `index.html` — Main landing page
- `css/style.css` — Global stylesheet
- `js/` — JavaScript modules (main.js, search.js, products.js, industries.js, components.js, articles.js)
- `*service-pages/` — Individual service subpages (e.g., `industrial-spare-parts/`, `mechanical-engineering/`)
- `image-preview/` — Image preview/gallery page
- `blog/` — Blog pages
- `assets/images/` — Static images
- `assets/images/nano-banana/` — AI-generated product images

## Coding Conventions

- Font: Barlow + Barlow Condensed + Bebas Neue
- CSS variables: `--orange`, `--dark2`, `--dark4`, `--border`, `--muted`, `--white`, `--light`
- Max-width for content: 800px on subpages
- No comments unless requested
- Use existing patterns from other service pages for consistency
