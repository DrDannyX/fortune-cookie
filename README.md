# Engineers Fortune Cookie 🥠

A static site that shows a random fortune on every page load. Great for internal team dashboards, office screens, or a moment of reflection between deploys.

Live on GitHub Pages. The browser picks the fortune, so there is no server.

---

## Project Structure

```
├── engineering-fortunes.txt   # Source: engineering fortunes (one per line)
├── general-fortunes.txt       # Source: general fortunes (optional "N→" prefix is stripped)
├── lawyer-fortunes.txt        # Source: lawyer fortunes
├── build_pages.py             # Copies the source files into docs/fortunes/
└── docs/                      # The GitHub Pages site
    ├── index.html
    ├── .nojekyll
    └── fortunes/              # Generated copies, do not edit by hand
```

---

## Adding or Editing Fortunes

1. Edit the top-level `*-fortunes.txt` file for the mode you want. One fortune per line.
2. Sync them into the Pages folder:
   ```bash
   python3 build_pages.py
   ```
3. Commit and push.

---

## Deploying to GitHub Pages

One-time setup: **Settings → Pages → Build and deployment → Deploy from a branch**, branch `main`, folder `/docs`.

After that, every push to `main` updates the site.

## Preview Locally

```bash
python3 -m http.server 8000 --directory docs
# open http://localhost:8000
```

## Modes

| URL | Fortunes |
| --- | --- |
| `/` | Engineers (default) |
| `/?mode=general` | General |
| `/?mode=lawyer` | Lawyers |

---

## Requirements

- Python 3 (only for `build_pages.py`, standard library only)
