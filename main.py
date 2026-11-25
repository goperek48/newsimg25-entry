"""news-image-20261125 entry (Python 3.13, standard library only).

The entry image is the file entry.png beside this program: a newspaper
front page summing up Wednesday 25 November 2026, composed from three
generated news photographs (a burning Russian warship in Benghazi harbour,
the PIF Tower in Riyadh after a Houthi drone strike, and the White House
Medal of Freedom ceremony) with a masthead, headlines and captions drawn
in crisp type.

The program copies that image to /output/entry.png and then verifies the
copy: same bytes as the source, a whole PNG, at most 1 MiB and at most
1024 by 1024 pixels, so both grader runs must produce identical valid
output. It is fully deterministic: every run writes the exact same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def png_dimensions(data: bytes) -> tuple:
    """Return (width, height) from a PNG's IHDR chunk; raise on bad input."""
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)

    with open(dest, "rb") as handle:
        data = handle.read()
    width, height = png_dimensions(data)
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"entry.png is {width}x{height}, over the 1024x1024 limit")
    if sha256(dest) != sha256(SOURCE):
        raise SystemExit("copied entry.png differs from the source image")

    print(f"wrote {dest} ({len(data)} bytes, {width}x{height}, "
          f"sha256 {sha256(dest)[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
