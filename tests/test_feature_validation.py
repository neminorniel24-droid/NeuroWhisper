import numpy as np
import pytest

from eeg_isr.features.validation import validate_feature_matrix


def test_validate_feature_matrix():
    x = validate_feature_matrix(np.ones((4, 6)), expected_samples=4)
    assert x.shape == (4, 6)


def test_reject_nan():
    with pytest.raises(ValueError):
        validate_feature_matrix(np.array([[1.0, np.nan]]))
