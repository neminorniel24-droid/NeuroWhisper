from pathlib import Path

from eeg_isr.data.discovery import discover_files


def test_discover_files(tmp_path: Path):
    eeg_dir = tmp_path / "eeg"
    eeg_dir.mkdir()

    first = eeg_dir / "subject01.fif"
    second = eeg_dir / "subject02.edf"
    ignored = eeg_dir / "notes.txt"

    first.write_text("test", encoding="utf-8")
    second.write_text("test", encoding="utf-8")
    ignored.write_text("test", encoding="utf-8")

    result = discover_files(eeg_dir)

    assert first.resolve() in result
    assert second.resolve() in result
    assert ignored.resolve() not in result


def test_missing_directory_returns_empty(tmp_path: Path):
    result = discover_files(tmp_path / "missing")
    assert result == []
