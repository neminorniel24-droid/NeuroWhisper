"""Configurable EEG frequency-band definitions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BandConfig:
    """Configuration for one EEG frequency band."""

    name: str
    low: float
    high: float

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Band name cannot be empty.")

        if self.low < 0:
            raise ValueError("Band lower frequency cannot be negative.")

        if self.high <= self.low:
            raise ValueError(
                "Band upper frequency must be greater than lower frequency."
            )


DEFAULT_BAND_CONFIGS = (
    BandConfig("delta", 1.0, 4.0),
    BandConfig("theta", 4.0, 8.0),
    BandConfig("alpha", 8.0, 13.0),
    BandConfig("beta", 13.0, 30.0),
    BandConfig("gamma", 30.0, 45.0),
)


def get_band(
    name: str,
    bands: tuple[BandConfig, ...] = DEFAULT_BAND_CONFIGS,
) -> BandConfig:
    """Return a band by name."""
    normalized = name.strip().lower()

    for band in bands:
        if band.name.lower() == normalized:
            return band

    raise KeyError(f"Unknown frequency band: {name}")
