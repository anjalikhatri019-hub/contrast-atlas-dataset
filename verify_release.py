"""Verify the participant-safe CONTRAST ATLAS release against public hashes."""
import hashlib
import json
import sys
import zipfile
from pathlib import Path


def digest(stream):
    result = hashlib.sha256()
    for block in iter(lambda: stream.read(1 << 20), b""):
        result.update(block)
    return result.hexdigest()


def main(path):
    manifest = json.loads(Path(__file__).with_name("public_release_manifest.json").read_text(encoding="utf-8"))
    archive = Path(path)
    if archive.stat().st_size != manifest["archive"]["bytes"]:
        raise ValueError("archive size mismatch")
    with archive.open("rb") as handle:
        if digest(handle) != manifest["archive"]["sha256"]:
            raise ValueError("archive SHA-256 mismatch")
    with zipfile.ZipFile(archive) as zipped:
        entries = {entry.filename: entry for entry in zipped.infolist() if not entry.is_dir()}
        expected = {row["path"]: row for row in manifest["members"]}
        if len(entries) != manifest["member_count"] or set(entries) != set(expected):
            raise ValueError("archive member inventory mismatch")
        for name, row in expected.items():
            if entries[name].file_size != row["bytes"]:
                raise ValueError(f"member size mismatch: {name}")
            with zipped.open(name) as handle:
                if digest(handle) != row["sha256"]:
                    raise ValueError(f"member SHA-256 mismatch: {name}")
    print(f"Verified {archive.name}: {len(expected)} members")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python verify_release.py participant_dataset.zip")
    main(sys.argv[1])
