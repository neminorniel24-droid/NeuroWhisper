"""Classical machine-learning models for EEG classification."""

from typing import Any

import numpy as np
from sklearn.svm import SVC


class SVMClassifier:
    """SVM classifier with a small, reusable project interface."""

    def __init__(
        self,
        kernel: str = "rbf",
        random_state: int = 42,
    ) -> None:
        self.kernel = kernel
        self.random_state = random_state

        self._model = SVC(
            kernel=kernel,
            random_state=random_state,
        )

        self._fitted = False

    def fit(
        self,
        X: Any,
        y: Any,
    ) -> "SVMClassifier":
        """Fit the SVM classifier."""
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

        self._model.fit(features, labels)
        self._fitted = True

        return self

    def predict(self, X: Any) -> np.ndarray:
        """Predict labels."""
        if not self._fitted:
            raise RuntimeError(
                "SVMClassifier must be fitted before prediction."
            )

        return self._model.predict(
            np.asarray(X, dtype=float)
        )
