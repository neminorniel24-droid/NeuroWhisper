"""Statistical EEG features."""

from collections.abc import Sequence

import numpy as np


def statistical_features(
    signal: Sequence[float],
) -> dict[str, float]:
    """Calculate basic statistical features."""
    values = np.asarray(signal, dtype=float)

    if values.ndim != 1 or values.size == 0:
        raise ValueError(
            "Signal must be a non-empty 1D sequence."
        )

    return {
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "variance": float(np.var(values)),
        "rms": float(np.sqrt(np.mean(values**2))),
        "absolute_mean": float(np.mean(np.abs(values))),
    }
