import pytest

from eeg_isr.utils.config_loader import load_yaml_config
from eeg_isr.utils.config_validation import validate_config


def test_project_config_is_valid():
    config = load_yaml_config("config.yaml")
    validate_config(config)


def test_missing_section_is_rejected():
    config = {
        "classifier": {},
        "karaone": {},
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_invalid_test_size_is_rejected():
    config = {
        "classifier": {"test_size": 2},
        "karaone": {},
        "sacred": {},
    }

    with pytest.raises(ValueError):
        validate_config(config)
