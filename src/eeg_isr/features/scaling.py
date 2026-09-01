"""Feature scaling utilities for EEG machine learning."""

from typing import Any

import numpy as np
from sklearn.preprocessing import StandardScaler


class FeatureScaler:
    """Leakage-safe standardization of feature matrices."""

    def __init__(self) -> None:
        self._scaler = StandardScaler()
        self._fitted = False

    def fit(self, X: Any) -> "FeatureScaler":
        """Fit scaling parameters using training data only."""
        values = np.asarray(X, dtype=float)

        if values.ndim != 2:
            raise ValueError(
                "Feature matrix must be two-dimensional."
            )

        if not np.isfinite(values).all():
            raise ValueError(
                "Feature matrix contains NaN or infinite values."
            )

        self._scaler.fit(values)
        self._fitted = True

        return self

    def transform(self, X: Any) -> np.ndarray:
        """Transform features using fitted training statistics."""
        if not self._fitted:
            raise RuntimeError(
                "FeatureScaler must be fitted before transform."
            )

        values = np.asarray(X, dtype=float)

        if values.ndim != 2:
            raise ValueError(
                "Feature matrix must be two-dimensional."
            )

        return self._scaler.transform(values)

    def fit_transform(self, X: Any) -> np.ndarray:
        """Fit on training data and transform it."""
        return self.fit(X).transform(X)
