import numpy as np
import pytest

from eeg_isr.models.classical import SVMClassifier


def test_svm_classifier():
    rng = np.random.default_rng(42)

    X = rng.normal(size=(30, 5))
    y = np.array([0, 1] * 15)

    model = SVMClassifier()
    model.fit(X, y)

    predictions = model.predict(X)

    assert predictions.shape == y.shape
    assert set(predictions).issubset({0, 1})


def test_prediction_requires_training():
    model = SVMClassifier()

    with pytest.raises(RuntimeError):
        model.predict(np.ones((5, 2)))


def test_mismatched_labels():
    model = SVMClassifier()

    with pytest.raises(ValueError):
        model.fit(
            np.ones((10, 2)),
            np.ones(5),
        )
