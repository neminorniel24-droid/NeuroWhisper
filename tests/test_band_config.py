import pytest

from eeg_isr.features.band_config import (
    DEFAULT_BAND_CONFIGS,
    BandConfig,
    get_band,
)


def test_default_bands():
    assert len(DEFAULT_BAND_CONFIGS) == 5


def test_get_alpha_band():
    band = get_band("alpha")

    assert isinstance(band, BandConfig)
    assert band.low == 8.0
    assert band.high == 13.0


def test_band_names_are_case_insensitive():
    assert get_band("BETA").name == "beta"


def test_invalid_band():
    with pytest.raises(KeyError):
        get_band("unknown")


def test_invalid_range():
    with pytest.raises(ValueError):
        BandConfig("invalid", 20, 10)
