# Engineers Fortune Cookie 🥠

A static site that shows a random fortune on every page load. Great for internal team dashboards, office screens, or a moment of reflection between deploys.

Live on GitHub Pages. The browser picks the fortune, so there is no server.

---

## Project Structure

```
docs/                          # The GitHub Pages site
├── index.html
├── .nojekyll
└── fortunes/
    ├── engineering.txt        # Engineering fortunes (one per line)
    ├── general.txt            # General fortunes (optional "N→" prefix is stripped)
    └── lawyer.txt             # Lawyer fortunes
```

---

## Adding or Editing Fortunes

Edit the file for the mode you want in `docs/fortunes/`. One fortune per line. Then commit and push.

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
