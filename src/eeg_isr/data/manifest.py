"""Dataset manifest generation utilities."""

from dataclasses import asdict, dataclass
from pathlib import Path
import json
import re


@dataclass(frozen=True)
class DatasetFile:
    """Metadata for one dataset file."""

    path: str
    filename: str
    size_bytes: int
    subject: str | None


def infer_subject(filename: str) -> str | None:
    """Infer a subject identifier from a filename."""
    patterns = (
        r"(?:subject|sub|participant)[_-]?(\d+)",
        r"\bS(\d+)\b",
    )

    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)

        if match:
            return f"S{int(match.group(1)):02d}"

    return None


def build_manifest(
    root: str | Path,
    patterns: tuple[str, ...] = ("*.fif", "*.edf", "*.set"),
) -> list[DatasetFile]:
    """Build metadata for EEG files below a directory."""
    root_path = Path(root).expanduser().resolve()

    if not root_path.exists():
        return []

    files: set[Path] = set()

    for pattern in patterns:
        files.update(root_path.rglob(pattern))

    return [
        DatasetFile(
            path=str(path),
            filename=path.name,
            size_bytes=path.stat().st_size,
            subject=infer_subject(path.name),
        )
        for path in sorted(files)
        if path.is_file()
    ]


def save_manifest(
    records: list[DatasetFile],
    output: str | Path,
) -> Path:
    """Save manifest metadata as JSON."""
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = [asdict(record) for record in records]

    output_path.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )

    return output_path
