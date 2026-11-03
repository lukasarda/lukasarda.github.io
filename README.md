# lukasarda.github.io

Source of the personal website of Lukas Arda, published at <https://lukasarda.github.io>.
Built with [Quarto](https://quarto.org) and deployed by GitHub Actions on every push to `master`.

The site code is adapted from [aliperego.github.io](https://github.com/aliperego/aliperego.github.io)
by Alice Perego (MIT License); the design is [Stellar](https://html5up.net/stellar) by HTML5 UP (CC BY 3.0).

## Where things are

| Path                 | Content                                                                 |
| -------------------- | ----------------------------------------------------------------------- |
| `_metadata.yml`      | Name, role, affiliation, email, profile links, CV PDF, navigation menu  |
| `index.qmd`          | Home page: intro, Get in touch, Codes, Teaching, Talks, Outreach, Personal |
| `publications.qmd`   | Publications page, from `publications.bib`                              |
| `cv.qmd`             | CV page                                                                 |
| `data/`              | Entries of the home-page sections (`tools.yml` is the Codes section)    |
| `custom.scss`        | Colours, fonts, header picture                                          |
| `assets/`            | Favicon, header picture, fonts; put the CV PDF and photos here          |
| `scripts/hero-pattern.py` | Generates `assets/hero-pattern.svg` (zoom-whirl geodesic)          |
| `_engine/`           | Layout filter, shortcodes, styles; no editing needed                    |

Each section of a page is a `## Heading`; the navigation links to a home-page section with
`index.qmd#heading-in-lowercase`. HTML comments `<!-- ... -->` never reach the published pages.

## Local preview

```bash
conda activate website      # environment with Quarto
quarto preview
```

The preview reloads on save. Nothing is public until you push to `master`.
