"""Sanity check standard EEG frequency band naming conventions."""

EXPECTED_BANDS = {"delta", "theta", "alpha", "beta", "gamma"}

def test_expected_band_names():
    # Documents the conventional EEG band names used in this project
    assert "alpha" in EXPECTED_BANDS
    assert "gamma" in EXPECTED_BANDS
