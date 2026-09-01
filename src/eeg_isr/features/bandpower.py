"""Frequency-domain EEG features."""

from collections.abc import Sequence

import numpy as np
from scipy.signal import welch

from eeg_isr.features.band_config import BandConfig


def bandpower(
    signal: Sequence[float],
    sampling_rate: float,
    band: BandConfig,
) -> float:
    """Calculate power contained in an EEG frequency band."""
    values = np.asarray(signal, dtype=float)

    if values.ndim != 1 or values.size < 2:
        raise ValueError(
            "Signal must be a one-dimensional sequence "
            "with at least two samples."
        )

    frequencies, power = welch(
        values,
        fs=sampling_rate,
        nperseg=min(256, values.size),
    )

    mask = (
        (frequencies >= band.low)
        & (frequencies < band.high)
    )

    if not np.any(mask):
        return 0.0

    return float(
        np.trapezoid(
            power[mask],
            frequencies[mask],
        )
    )
