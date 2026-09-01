import numpy as np

from eeg_isr.features.pipeline import (
    extract_band_features,
    extract_features,
)


def test_extract_band_features():
    sampling_rate = 128
    time = np.arange(1280) / sampling_rate
    signal = np.sin(2 * np.pi * 10 * time)

    features = extract_band_features(
        signal,
        sampling_rate,
    )

    assert "delta_power" in features
    assert "theta_power" in features
    assert "alpha_power" in features
    assert "beta_power" in features
    assert "gamma_power" in features


def test_extract_features_combines_feature_types():
    sampling_rate = 128
    time = np.arange(1280) / sampling_rate
    signal = np.sin(2 * np.pi * 10 * time)

    features = extract_features(
        signal,
        sampling_rate,
    )

    assert "mean" in features
    assert "std" in features
    assert "alpha_power" in features
    assert len(features) == 10
