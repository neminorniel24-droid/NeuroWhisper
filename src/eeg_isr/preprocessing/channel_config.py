"""Configuration for EEG channel-selection experiments."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ChannelConfig:
    """Defines the EEG channels used by an experiment."""

    name: str
    channels: tuple[str, ...]

    @property
    def count(self) -> int:
        """Return the number of selected channels."""
        return len(self.channels)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Channel configuration needs a name.")

        if not self.channels:
            raise ValueError(
                "At least one EEG channel must be selected."
            )

        if len(set(self.channels)) != len(self.channels):
            raise ValueError(
                "Channel configuration contains duplicates."
            )


def make_channel_config(
    name: str,
    channels: list[str] | tuple[str, ...],
) -> ChannelConfig:
    """Create a normalized channel configuration."""
    normalized = tuple(
        channel.strip()
        for channel in channels
        if channel.strip()
    )

    return ChannelConfig(
        name=name,
        channels=normalized,
    )
