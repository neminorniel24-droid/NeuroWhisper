"""Utilities for reproducible experiments."""

import os
import random

import numpy as np


def set_seed(seed: int) -> None:
    """Set common random seeds used by NeuroWhisper."""
    if not isinstance(seed, int):
        raise TypeError("seed must be an integer.")

    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    try:
        import tensorflow as tf

        tf.random.set_seed(seed)
    except ImportError:
        pass
