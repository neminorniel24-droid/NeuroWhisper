"""Validation helpers for extracted EEG features."""

import numpy as np


def validate_feature_matrix(
    features: np.ndarray,
    expected_samples: int | None = None,
) -> np.ndarray:
    """Validate and return a 2-D finite feature matrix."""
    array = np.asarray(features, dtype=float)

    if array.ndim != 2:
        raise ValueError("Feature matrix must be 2-dimensional.")

    if array.shape[0] == 0 or array.shape[1] == 0:
        raise ValueError("Feature matrix must not be empty.")

    if expected_samples is not None and array.shape[0] != expected_samples:
        raise ValueError("Unexpected number of feature samples.")

    if not np.isfinite(array).all():
        raise ValueError("Feature matrix contains non-finite values.")

    return array
