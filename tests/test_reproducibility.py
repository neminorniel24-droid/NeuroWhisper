import numpy as np

from eeg_isr.utils.reproducibility import set_seed


def test_numpy_reproducibility():
    set_seed(42)
    first = np.random.random(5)

    set_seed(42)
    second = np.random.random(5)

    assert np.array_equal(first, second)
