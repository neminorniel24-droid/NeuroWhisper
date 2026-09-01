import numpy as np
import pytest

from eeg_isr.features.scaling import FeatureScaler


def test_scaler_normalizes_training_features():
    X = np.array([
        [1.0, 10.0],
        [2.0, 20.0],
        [3.0, 30.0],
    ])

    scaler = FeatureScaler()
    transformed = scaler.fit_transform(X)

    assert transformed.shape == X.shape
    assert np.allclose(
        transformed.mean(axis=0),
        0.0,
        atol=1e-10,
    )


def test_transform_requires_fit():
    scaler = FeatureScaler()

    with pytest.raises(RuntimeError):
        scaler.transform([[1.0, 2.0]])


def test_scaler_rejects_nan():
    scaler = FeatureScaler()

    with pytest.raises(ValueError):
        scaler.fit([[1.0, float("nan")]])
