from pathlib import Path

from eeg_isr.data.integrity import (
    check_file,
    invalid_files,
    validate_dataset_files,
)


def test_existing_file(tmp_path: Path):
    path = tmp_path / "sample.fif"
    path.write_bytes(b"test")

    result = check_file(path)

    assert result.exists
    assert result.size_bytes == 4
    assert not result.is_empty


def test_empty_file(tmp_path: Path):
    path = tmp_path / "empty.fif"
    path.touch()

    result = check_file(path)

    assert result.exists
    assert result.is_empty


def test_missing_file(tmp_path: Path):
    result = check_file(tmp_path / "missing.fif")

    assert not result.exists
    assert result.is_empty


def test_dataset_validation(tmp_path: Path):
    good = tmp_path / "good.fif"
    bad = tmp_path / "bad.fif"

    good.write_bytes(b"EEG")
    bad.touch()

    records = validate_dataset_files([good, bad])
    invalid = invalid_files(records)

    assert len(records) == 2
    assert len(invalid) == 1
    assert invalid[0].path == str(bad)
