import numpy as np
import mne

from eeg_isr.preprocessing.pipeline import preprocess_raw


def test_preprocess_raw():
    info = mne.create_info(["Cz"], sfreq=100, ch_types=["eeg"])
    raw = mne.io.RawArray(np.random.default_rng(0).normal(size=(1, 1000)), info)

    processed = preprocess_raw(raw)

    assert processed.info["sfreq"] == 100
    assert processed.get_data().shape == raw.get_data().shape
