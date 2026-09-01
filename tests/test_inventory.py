from pathlib import Path

from eeg_isr.data.inventory import build_inventory


def test_build_inventory(tmp_path: Path):
    (tmp_path / "a.fif").write_text("test", encoding="utf-8")
    (tmp_path / "b.fif").write_text("test", encoding="utf-8")
    (tmp_path / "c.edf").write_text("test", encoding="utf-8")

    inventory = build_inventory(tmp_path)

    assert inventory["file_count"] == 3
    assert inventory["extensions"][".fif"] == 2
    assert inventory["extensions"][".edf"] == 1
