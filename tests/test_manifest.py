import json
from pathlib import Path

from eeg_isr.data.manifest import (
    build_manifest,
    infer_subject,
    save_manifest,
)


def test_infer_subject():
    assert infer_subject("subject01.fif") == "S01"
    assert infer_subject("sub_02.edf") == "S02"
    assert infer_subject("random.fif") is None


def test_build_manifest(tmp_path: Path):
    first = tmp_path / "subject01.fif"
    second = tmp_path / "subject02.fif"

    first.write_bytes(b"1234")
    second.write_bytes(b"123456")

    records = build_manifest(tmp_path)

    assert len(records) == 2
    assert records[0].subject == "S01"
    assert records[0].size_bytes == 4


def test_save_manifest(tmp_path: Path):
    first = tmp_path / "subject01.fif"
    first.write_bytes(b"test")

    records = build_manifest(tmp_path)
    output = save_manifest(records, tmp_path / "manifest.json")

    data = json.loads(output.read_text(encoding="utf-8"))

    assert len(data) == 1
    assert data[0]["subject"] == "S01"
