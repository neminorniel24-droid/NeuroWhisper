import json

from eeg_isr.data.manifest import DatasetManifest, DatasetRecord


def test_manifest_subject_count(tmp_path):
    manifest = DatasetManifest(
        dataset_name="KaraOne",
        records=[
            DatasetRecord("S01", "a.fif", True),
            DatasetRecord("S01", "b.fif", True),
            DatasetRecord("S02", "c.fif", True),
        ],
    )

    assert manifest.subject_count == 2

    output = tmp_path / "manifest.json"
    manifest.to_json(output)

    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["dataset_name"] == "KaraOne"
    assert len(data["records"]) == 3
