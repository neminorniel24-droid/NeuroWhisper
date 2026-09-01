import pytest

from eeg_isr.preprocessing.channel_config import (
    ChannelConfig,
    make_channel_config,
)


def test_channel_count():
    config = ChannelConfig(
        name="reduced-4",
        channels=("C3", "C4", "Cz", "Fz"),
    )

    assert config.count == 4


def test_factory_removes_empty_values():
    config = make_channel_config(
        "test",
        ["C3", "", " C4 "],
    )

    assert config.channels == ("C3", "C4")


def test_empty_channels_rejected():
    with pytest.raises(ValueError):
        ChannelConfig(
            name="empty",
            channels=(),
        )


def test_duplicate_channels_rejected():
    with pytest.raises(ValueError):
        ChannelConfig(
            name="duplicate",
            channels=("C3", "C3"),
        )
