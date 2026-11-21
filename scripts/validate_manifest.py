#!/usr/bin/env python3
"""Validate a public-format data manifest without opening images or labels."""

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

REQUIRED = {"image_id", "specimen_id", "weld_id", "split", "annotation_status"}
ALLOWED_SPLITS = {"train", "val", "test", "external_test"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED - fields
        if missing:
            return [f"Missing required columns: {', '.join(sorted(missing))}"]

        rows = list(reader)

    seen_images: set[str] = set()
    groups: dict[str, set[str]] = defaultdict(set)
    for line, row in enumerate(rows, start=2):
        image_id = row["image_id"].strip()
        specimen_id = row["specimen_id"].strip()
        weld_id = row["weld_id"].strip()
        split = row["split"].strip()

        if not image_id or not specimen_id or not weld_id:
            errors.append(f"Line {line}: image_id, specimen_id and weld_id must be non-empty.")
            continue
        if image_id in seen_images:
            errors.append(f"Line {line}: duplicate image_id {image_id!r}.")
        seen_images.add(image_id)

        if split not in ALLOWED_SPLITS:
            errors.append(f"Line {line}: unsupported split {split!r}.")
        groups[f"specimen:{specimen_id}"].add(split)
        groups[f"weld:{weld_id}"].add(split)

    for group, splits in sorted(groups.items()):
        if len(splits) > 1:
            errors.append(f"Group leakage: {group} occurs in {', '.join(sorted(splits))}.")

    if not rows:
        errors.append("Manifest has no data rows.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if not args.manifest.is_file():
        parser.error(f"Manifest not found: {args.manifest}")

    errors = validate(args.manifest)
    if errors:
        print("\n".join(f"ERROR: {message}" for message in errors), file=sys.stderr)
        return 1

    print("Manifest structure and group split checks passed.")
    print("This does not verify image contents, annotation completeness or physical normality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
