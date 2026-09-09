"""Configuration for EEG preprocessing."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PreprocessingConfig:
    low_frequency: float = 0.5
    high_frequency: float = 50.0
    notch_frequency: float | None = None
    resample_frequency: float | None = None

    def __post_init__(self) -> None:
        if self.low_frequency <= 0:
            raise ValueError("low_frequency must be positive.")
        if self.high_frequency <= self.low_frequency:
            raise ValueError("high_frequency must exceed low_frequency.")
        if self.notch_frequency is not None and self.notch_frequency <= 0:
            raise ValueError("notch_frequency must be positive.")
        if self.resample_frequency is not None and self.resample_frequency <= 0:
            raise ValueError("resample_frequency must be positive.")
