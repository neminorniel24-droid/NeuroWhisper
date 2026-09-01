"""Dataset inventory utilities."""

from collections import Counter
from pathlib import Path

from eeg_isr.data.discovery import discover_files


def build_inventory(root: str | Path) -> dict[str, object]:
    """Build a lightweight inventory without reading EEG contents."""
    files = discover_files(root)

    suffixes = Counter(
        path.suffix.lower()
        for path in files
    )

    return {
        "root": str(Path(root).expanduser().resolve()),
        "file_count": len(files),
        "extensions": dict(sorted(suffixes.items())),
        "files": [str(path) for path in files],
    }
