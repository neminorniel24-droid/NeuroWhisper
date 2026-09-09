"""Sanity check documented EEG channel group names."""

CHANNEL_GROUPS = {"frontal", "central", "temporal", "parietal", "occipital"}

def test_temporal_in_groups():
    assert "temporal" in CHANNEL_GROUPS

def test_five_groups_documented():
    assert len(CHANNEL_GROUPS) == 5
