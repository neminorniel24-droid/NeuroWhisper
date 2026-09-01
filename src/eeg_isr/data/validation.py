"""Dataset integrity validation."""

from pathlib import Path


def validate_files(paths: list[str | Path]) -> list[Path]:
    """Return missing dataset files.

    No dataset files are modified.
    """
    return [
        Path(path)
        for path in paths
        if not Path(path).is_file()
    ]


def assert_files_exist(paths: list[str | Path]) -> None:
    """Raise an error if any expected dataset files are missing."""
    missing = validate_files(paths)

    if missing:
        formatted = "\n".join(str(path) for path in missing)
        raise FileNotFoundError(
            f"Missing dataset files:\n{formatted}"
        )
