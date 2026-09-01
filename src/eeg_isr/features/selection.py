"""Feature-selection utilities for EEG classification."""

from typing import Any

import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif


class KBestSelector:
    """Leakage-safe K-best feature selector."""

    def __init__(self, k: int = 50) -> None:
        if k < 1:
            raise ValueError("k must be at least 1.")

        self.k = k
        self._selector = SelectKBest(
            score_func=f_classif,
            k=k,
        )
        self._fitted = False

    def fit(self, X: Any, y: Any) -> "KBestSelector":
        """Fit feature selection using training data only."""
        features = np.asarray(X, dtype=float)
        labels = np.asarray(y)

        if features.ndim != 2:
            raise ValueError(
                "Feature matrix must be two-dimensional."
            )

        if features.shape[0] != labels.shape[0]:
            raise ValueError(
                "Number of samples and labels must match."
            )

        if not np.isfinite(features).all():
            raise ValueError(
                "Feature matrix contains NaN or infinite values."
            )

        if self.k > features.shape[1]:
            raise ValueError(
                f"k={self.k} exceeds the number of "
                f"features={features.shape[1]}."
            )

        self._selector.fit(features, labels)
        self._fitted = True

        return self

    def transform(self, X: Any) -> np.ndarray:
        """Transform features using the fitted selector."""
        if not self._fitted:
            raise RuntimeError(
                "KBestSelector must be fitted before transform."
            )

        features = np.asarray(X, dtype=float)

        return self._selector.transform(features)

    def fit_transform(
        self,
        X: Any,
        y: Any,
    ) -> np.ndarray:
        """Fit selector on training data and transform it."""
        return self.fit(X, y).transform(X)

    def get_support(self) -> np.ndarray:
        """Return a boolean mask of selected features."""
        if not self._fitted:
            raise RuntimeError(
                "KBestSelector must be fitted before get_support."
            )

        return self._selector.get_support()
