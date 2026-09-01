from pathlib import Path

import pytest

from eeg_isr.utils.config_loader import load_yaml_config


def test_load_yaml_config(tmp_path: Path):
    config = tmp_path / "config.yaml"
    config.write_text("model:\n  name: svm\n", encoding="utf-8")

    result = load_yaml_config(config)

    assert result["model"]["name"] == "svm"


def test_missing_config_raises():
    with pytest.raises(FileNotFoundError):
        load_yaml_config("/does/not/exist/config.yaml")
