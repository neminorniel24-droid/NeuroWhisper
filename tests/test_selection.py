import numpy as np
import pytest

from eeg_isr.features.selection import KBestSelector


def test_kbest_reduces_features():
    rng = np.random.default_rng(42)

    X = rng.normal(size=(30, 10))
    y = np.array([0, 1] * 15)

    selector = KBestSelector(k=4)
    transformed = selector.fit_transform(X, y)

    assert transformed.shape == (30, 4)
    assert selector.get_support().sum() == 4


def test_transform_requires_fit():
    selector = KBestSelector(k=2)

    with pytest.raises(RuntimeError):
        selector.transform(np.ones((5, 4)))


def test_k_cannot_exceed_features():
    selector = KBestSelector(k=20)

    with pytest.raises(ValueError):
        selector.fit(
            np.ones((10, 5)),
            np.array([0, 1] * 5),
        )
