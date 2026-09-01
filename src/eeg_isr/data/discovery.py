"""Utilities for discovering dataset files."""

from pathlib import Path


def discover_files(
    root: str | Path,
    patterns: tuple[str, ...] = ("*.fif", "*.edf", "*.set"),
) -> list[Path]:
    """Recursively discover EEG files below a directory."""
    root_path = Path(root).expanduser()

    if not root_path.exists():
        return []

    files: set[Path] = set()

    for pattern in patterns:
        files.update(root_path.rglob(pattern))

    return sorted(path.resolve() for path in files if path.is_file())
