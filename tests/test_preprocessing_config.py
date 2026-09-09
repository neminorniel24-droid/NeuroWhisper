import pytest

from eeg_isr.preprocessing.config import PreprocessingConfig


def test_default_preprocessing_config():
    config = PreprocessingConfig()

    assert config.low_frequency == 0.5
    assert config.high_frequency == 50.0


def test_invalid_frequency_range():
    with pytest.raises(ValueError):
        PreprocessingConfig(low_frequency=50, high_frequency=10)
