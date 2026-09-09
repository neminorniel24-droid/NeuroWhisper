"""Reusable EEG preprocessing operations."""

import mne

from eeg_isr.preprocessing.config import PreprocessingConfig


def preprocess_raw(
    raw: mne.io.BaseRaw,
    config: PreprocessingConfig | None = None,
) -> mne.io.BaseRaw:
    """Apply configured filtering to an MNE Raw object."""
    config = config or PreprocessingConfig()

    processed = raw.copy()

    processed.filter(
        l_freq=config.low_frequency,
        h_freq=config.high_frequency,
        verbose="ERROR",
    )

    if config.notch_frequency is not None:
        processed.notch_filter(
            freqs=config.notch_frequency,
            verbose="ERROR",
        )

    if config.resample_frequency is not None:
        processed.resample(
            config.resample_frequency,
            verbose="ERROR",
        )

    return processed
