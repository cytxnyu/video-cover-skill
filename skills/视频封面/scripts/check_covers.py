#!/usr/bin/env python3
"""Read-only dimensions and decode validation for the two final covers."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def inspect(path: Path, ratio: list[int]) -> dict:
    from PIL import Image

    path = path.expanduser().resolve()
    if not path.is_file():
        return {"path": str(path), "ok": False, "error": "Image file does not exist"}
    try:
        with Image.open(path) as image:
            file_format = image.format
            image.verify()
        with Image.open(path) as image:
            image.load()
            orientation = image.getexif().get(274, 1)
            width, height = image.size
            if orientation in (5, 6, 7, 8):
                width, height = height, width
        ratio_ok = width * ratio[1] == height * ratio[0]
        format_ok = file_format in ("PNG", "JPEG")
        extension_ok = path.suffix.lower() in ({".png"} if file_format == "PNG" else {".jpg", ".jpeg"})
        return {
            "path": str(path), "width": width, "height": height,
            "ratio": f"{ratio[0]}:{ratio[1]}", "ratio_ok": ratio_ok,
            "format": file_format, "format_ok": format_ok, "extension_ok": extension_ok,
            "ok": ratio_ok and format_ok and extension_ok,
        }
    except (OSError, ValueError, SyntaxError) as error:
        return {"path": str(path), "ok": False, "error": f"Image decode failed: {error}"}


def validate(portrait: Path, landscape: Path) -> dict:
    spec_path = Path(__file__).resolve().parents[1] / "references" / "delivery-spec.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    images = {
        "portrait": inspect(portrait, spec["variants"]["portrait"]["ratio"]),
        "landscape": inspect(landscape, spec["variants"]["landscape"]["ratio"]),
    }
    distinct = portrait.resolve() != landscape.resolve()
    if portrait.exists() and landscape.exists():
        distinct = distinct and not portrait.samefile(landscape)
    return {
        "ok": distinct and all(item["ok"] for item in images.values()),
        "distinct_files": distinct, "images": images,
        "visual_review": "REQUIRED: identity, wording, content, style and independent layout need visual inspection.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--portrait", type=Path, required=True)
    parser.add_argument("--landscape", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = validate(args.portrait, args.landscape)
    except (ImportError, OSError, ValueError, KeyError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
