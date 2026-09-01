from pathlib import Path

import pytest

from eeg_isr.data.validation import (
    assert_files_exist,
    validate_files,
)


def test_validate_files(tmp_path: Path):
    existing = tmp_path / "existing.dat"
    existing.write_text("test", encoding="utf-8")

    missing = tmp_path / "missing.dat"

    result = validate_files([existing, missing])

    assert result == [missing]


def test_assert_files_exist(tmp_path: Path):
    missing = tmp_path / "missing.dat"

    with pytest.raises(FileNotFoundError):
        assert_files_exist([missing])
