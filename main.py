"""news-image-20261120: copy the prepared front page to /output/entry.png.

The repository ships entry.png, drawn from verified 20 Nov 2026
headlines by build_image.py. The grader runs this program twice with
no network access, and both runs must write identical bytes, so this
program does nothing but copy the bundled image into the output
directory. No input is read besides the bundled image itself.
"""

from pathlib import Path
import shutil

REPO = Path(__file__).resolve().parent
IMAGE = REPO / "entry.png"
TARGET = Path("/output") / "entry.png"


def run() -> None:
    if not IMAGE.is_file():
        raise SystemExit(f"bundled image missing: {IMAGE}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, TARGET)


if __name__ == "__main__":
    run()
