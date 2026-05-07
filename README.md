# hugo-xpage

A black, white, and electric-yellow Hugo theme for personal sites and technical blogs.
Multilingual (en / 简体中文 / 繁體中文) lang-blocks switched client-side. Five image
shortcodes plus on-demand KaTeX, Mermaid, and Prism syntax highlighting that load only
when a page actually uses them. Square-design contract — no rounded chrome buttons,
custom crosshair cursor, click-to-lightbox on every image, Live Photo with hover-play.

> Live demo: [peritrix.com](https://peritrix.com).

---

## Demo

```bash
git clone https://github.com/Jensen-JZ/hugo-xpage.git
cd hugo-xpage/exampleSite
hugo server -D --bind 127.0.0.1 --port 1313 --disableFastRender
# → http://localhost:1313/
```

The exampleSite ships two posts:
- `hello-world.md` — minimal multilingual post template
- `feature-showcase.md` — exercises every block (Markdown, Prism, KaTeX, Mermaid, all 5 shortcodes)

---

## Install in your own site

The theme works the standard Hugo way: clone into `themes/` and reference it in your config.

```bash
# from the root of your Hugo site
mkdir -p themes
git submodule add https://github.com/Jensen-JZ/hugo-xpage.git themes/hugo-xpage
```

Then in your `hugo.toml`:

```toml
theme = "hugo-xpage"
```

That's it. Copy the contents of `exampleSite/data/`, `exampleSite/content/`, and the `[params]` block from `exampleSite/hugo.toml` into your own site as a starting point.

---

## What you get

| Feature | Status |
|---|---|
| Multilingual posts via `<div class="lang-block">` (en / zh / tw) | ✓ |
| Single-page portfolio layout (hero · about · what-do · journey · projects · writing · photography · contact) | ✓ |
| Long-form blog with multilingual lang-blocks | ✓ |
| Full SEO surface — OG, Twitter Card, canonical, sitemap, RSS, robots.txt | ✓ |
| Open Graph card (1200×630) | ✓ |
| 5 shortcodes — `image-size`, `image-grid`, `image-carousel`, `live-photo`, `mermaid` | ✓ |
| On-demand Prism.js syntax highlighting (only loads if the page has fenced code) | ✓ |
| On-demand KaTeX (only if `$$ … $$` or `\\(…\\)` exists on the page) | ✓ |
| On-demand Mermaid v10 (only if `<pre class="mermaid">` exists) | ✓ |
| Click-to-lightbox on every image | ✓ |
| Live Photo hover-to-play with LIVE badge | ✓ |
| Custom crosshair cursor + theme switcher + search modal + back-to-top | ✓ |
| Square-design contract — no `border-radius` outside chrome nav pills | ✓ |
| 404 page (branded) | ✓ |

A blank-content page with no math, no diagrams, no code stays at zero JS dependencies.

---

## Project layout

```
hugo-xpage/
├── archetypes/              # default.md
├── assets/                  # bundled JS/CSS (theme assets)
├── i18n/                    # Hugo i18n hook (real i18n lives in exampleSite/data/i18n.toml)
├── layouts/
│   ├── _default/
│   │   ├── single.html      # post template
│   │   └── list.html        # listing template
│   ├── index.html           # homepage (long single-page)
│   ├── 404.html
│   ├── partials/
│   │   ├── chrome/          # nav · rail · lightbox · search · seo · ...
│   │   ├── sections/        # homepage sections (hero/about/whatdo/...)
│   │   ├── post-styles/     # _article.css · _shortcodes.css (inlined)
│   │   └── post-scripts/    # _base.js · _shortcodes.js · _codeblock.js · _mermaid.js
│   └── shortcodes/
│       ├── image-size.html
│       ├── image-grid.html
│       ├── image-carousel.html
│       ├── live-photo.html
│       └── mermaid.html
├── static/
│   ├── assets/site-header.css   # 20 KB — single CSS source-of-truth
│   ├── assets/live/             # 6 demo Live Photo .mov + .jpg pairs
│   └── favicon.ico
├── theme.toml
├── LICENSE
└── exampleSite/
    ├── hugo.toml            # placeholder values — copy [params] into your own
    ├── content/posts/
    │   ├── hello-world.md
    │   └── feature-showcase.md
    ├── data/                # 8 toml files driving the homepage sections
    │   ├── about.toml
    │   ├── identity.toml
    │   ├── whatdo.toml
    │   ├── journey.toml
    │   ├── projects.toml
    │   ├── photography.toml
    │   ├── social.toml
    │   └── i18n.toml        # all UI strings in 3 languages
    └── static/assets/
        └── og-card.png      # demo OG card — replace with your own
```

---

## Authoring posts

The frontmatter convention is rigid because the listing/i18n machinery depends on it.
Use `exampleSite/content/posts/hello-world.md` as the canonical template.

```yaml
---
title: "Post Title"
slug: post-slug
date: '2026-01-01T00:00:00+00:00'
weight: 1
postId: post-slug
i18nKey: post.slug.title
categoryI18n: cat.notes      # cat.research / cat.tech / cat.travel / cat.lifestyle / cat.notes
dateDisplay: 2026·01·01
bylineDate: 2026 · 01 · 01
kickers:                     # eyebrow text per language
  en: NOTES · 2026
  zh: 笔记 · 2026
  tw: 筆記 · 2026
readTimes:
  en: 1 min read
  zh: 阅读约 1 分钟
  tw: 閱讀約 1 分鐘
heroCaption: F · 001 · KEY
titles:                      # per-language H1
  en: "..."
  zh: "..."
  tw: "..."
decks:                       # SEO description + listing deck
  en: "..."
  zh: "..."
  tw: "..."
prev: { href: /posts/X.html, title: "← Previous title" }
next: { href: /posts/Y.html, title: "Next title →" }
lastmod: '2026-01-01T00:00:00+00:00'
---
```

The body must be wrapped in three `<div class="lang-block" data-lang="en|zh|tw">`
containers, with `data-active="true"` on the default. The runtime in
`partials/post-scripts/_base.html` toggles visibility on language switch.

### Shortcodes

| Block               | Syntax                                                                                              |
|---------------------|------------------------------------------------------------------------------------------------------|
| Single image        | `{{</* image-size src="…" alt="…" caption="…" center="true" */>}}`                                    |
| Image grid          | `{{</* image-grid columns="2" gap="1rem" images="src1\|\|cap1, src2\|\|cap2" */>}}`                    |
| Image carousel      | `{{</* image-carousel width="90%" center="true" autoplay="false" caption="…" images="s1, s2, s3" */>}}` |
| Live Photo          | `{{</* live-photo src="img.png" video="vid.mov" width="60%" caption="…" center="true" */>}}`           |
| Mermaid diagram     | `{{</* mermaid caption="…" */>}}` … `{{</* /mermaid */>}}`                                            |
| Math (inline)       | `\\(\\nabla_\\theta \\mathcal{L}\\)`                                                                  |
| Math (display)      | `$$ … $$`                                                                                            |
| Code with highlight | Standard fenced ` ``` `lang `… ` ``` `                                                                |

### Drafts

Add `draft: true` to the frontmatter. Local preview with `hugo server -D`. Production build (`hugo --gc --minify`) skips drafts automatically.

---

## Configuration

Copy the `[params]` block from `exampleSite/hugo.toml` into your own site's `hugo.toml`:

```toml
[params]
  author          = 'Your Full Name'
  authorFamiliar  = 'You'
  handle          = '@yourhandle'
  email           = 'hello@example.com'
  domain          = 'example.com'
  homepageURL     = 'https://example.com'
  description     = 'A short description for SEO and social cards.'
  ogImage         = 'https://example.com/assets/og-card.png'
  twitterHandle   = '@yourhandle'
  # … plus hero / chrome / copy fields — see exampleSite/hugo.toml for the full set
```

All UI strings live in `data/i18n.toml` (one section per language). Replace the
copy in each `[en]` / `[zh]` / `[tw]` block to translate the entire site.

The 8 `data/*.toml` files drive the homepage sections — about rows, identity
fields, what-I-do columns, journey timeline, projects, photography frames,
contact links. Edit them to match your own content.

---

## Design contracts (gotchas worth knowing)

The theme has a few opinionated behaviors that are easy to break if you don't
know they exist:

- **`<mark>` padding is 0.** The yellow swipe must hug the glyph; any padding obscures the previous character.
- **No `cursor: pointer`.** Custom crosshair for chrome, `cursor: zoom-in` for images, native pointer only inside the lightbox.
- **No `border-radius: 999px`** outside chrome nav pills. All buttons are square.
- **CJK-safe heading anchors.** The slugifier in `_base.html` keeps non-ASCII characters and dedupes IDs.
- **Goldmark eats `\(`.** When writing inline math, escape with double backslash `\\(...\\)`. Single `\(...\)` would render as literal `(...)`.
- **Mermaid + multi-language collision.** Three identical diagrams in three `lang-block` clones cause v10 to fail on duplicate node IDs. The loader renders only the active `lang-block` and re-renders on language switch — this is already handled.
- **Prism `language-X` regex collision.** The autoloader's class regex matches both `language-X` and `lang-X`, so `<div class="lang-block">` would trigger a 404 for a phantom `prism-block.min.js`. Suppressed by `Prism.manual = true` and explicit `Prism.highlightElement` calls — already handled.

---

## External CDN dependencies (loaded on demand)

The theme is HTML-first. JavaScript only loads when the page actually needs it:

- `prismjs@1.29.0` — `prism-core` + autoloader + `prism-tomorrow.css`
- `katex@0.16.11` — `katex.min.js` + `auto-render.min.js` + `katex.min.css`
- `mermaid@10.9.1` — `mermaid.esm.min.mjs`

All three are loaded from jsdelivr. No bundler. No npm install.

---

## Deployment

The exampleSite produces a 5–6 MB `public/` of plain static files. Deploy anywhere:

```bash
hugo --gc --minify
# rsync, Cloudflare Pages, Vercel, GitHub Pages, Netlify — pick any
rsync -avz public/ user@host:/var/www/site/
```

---

## License & credits

MIT — see [LICENSE](LICENSE).

Runtime libraries (loaded from jsdelivr):

- [Hugo](https://gohugo.io) (BSD-3) — static site generator
- [Prism.js](https://prismjs.com) (MIT) — syntax highlighting
- [KaTeX](https://katex.org) (MIT) — math typesetting
- [Mermaid](https://mermaid.js.org) (MIT) — diagrams
- Inter / Newsreader / JetBrains Mono — typefaces (Google Fonts + system stack)

The theme code is © 2026 Jensen-JZ. Demo Live Photo clips bundled with the
theme are CC0 / generated. The example post copy is placeholder text and free
to delete.

If you build something with this, I'd love to see it — file an issue or PR
to add it to a "made with hugo-xpage" list.
