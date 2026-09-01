"""Lightweight integrity checks for EEG dataset files."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FileIntegrity:
    """Integrity information for one file."""

    path: str
    exists: bool
    size_bytes: int
    is_empty: bool


def check_file(path: str | Path) -> FileIntegrity:
    """Check whether a dataset file exists and is non-empty."""
    file_path = Path(path).expanduser()

    if not file_path.exists():
        return FileIntegrity(
            path=str(file_path),
            exists=False,
            size_bytes=0,
            is_empty=True,
        )

    if not file_path.is_file():
        return FileIntegrity(
            path=str(file_path),
            exists=False,
            size_bytes=0,
            is_empty=True,
        )

    size = file_path.stat().st_size

    return FileIntegrity(
        path=str(file_path),
        exists=True,
        size_bytes=size,
        is_empty=size == 0,
    )


def validate_dataset_files(
    paths: list[str | Path],
) -> list[FileIntegrity]:
    """Return integrity information for all supplied files."""
    return [check_file(path) for path in paths]


def invalid_files(
    records: list[FileIntegrity],
) -> list[FileIntegrity]:
    """Return missing or empty files."""
    return [
        record
        for record in records
        if not record.exists or record.is_empty
    ]
