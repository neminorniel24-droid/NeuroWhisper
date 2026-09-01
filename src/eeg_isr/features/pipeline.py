"""Reusable EEG feature extraction pipeline."""

from collections.abc import Sequence

from eeg_isr.features.band_config import (
    DEFAULT_BAND_CONFIGS,
    BandConfig,
)
from eeg_isr.features.bandpower import bandpower
from eeg_isr.features.statistical import statistical_features


def extract_band_features(
    signal: Sequence[float],
    sampling_rate: float,
    bands: tuple[BandConfig, ...] = DEFAULT_BAND_CONFIGS,
) -> dict[str, float]:
    """Extract band-power features from one EEG signal."""
    return {
        f"{band.name}_power": bandpower(
            signal,
            sampling_rate,
            band,
        )
        for band in bands
    }


def extract_features(
    signal: Sequence[float],
    sampling_rate: float,
    bands: tuple[BandConfig, ...] = DEFAULT_BAND_CONFIGS,
) -> dict[str, float]:
    """Extract a combined set of EEG features."""
    features = {}

    features.update(
        statistical_features(signal)
    )

    features.update(
        extract_band_features(
            signal,
            sampling_rate,
            bands,
        )
    )

    return features
