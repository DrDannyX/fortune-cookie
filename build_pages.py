"""Copy the fortune files into docs/fortunes/ for GitHub Pages.

Run after editing any *-fortunes.txt file:

    python build_pages.py

GitHub Pages serves the docs/ folder as a static site (Settings -> Pages ->
Source: "Deploy from a branch", folder: /docs).
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "docs" / "fortunes"

FILES = {
    "engineering-fortunes.txt": "engineering.txt",
    "general-fortunes.txt": "general.txt",
    "lawyer-fortunes.txt": "lawyer.txt",
}


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for src_name, dest_name in FILES.items():
        shutil.copyfile(ROOT / src_name, DEST / dest_name)
        print(f"copied {src_name} -> docs/fortunes/{dest_name}")


if __name__ == "__main__":
    main()
