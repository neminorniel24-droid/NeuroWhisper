"""Sanity check the set of valid KaraOne epoch types used in this project."""

VALID_EPOCH_TYPES = {"clearing", "thinking", "stimuli", "speaking"}

def test_thinking_is_valid_epoch_type():
    assert "thinking" in VALID_EPOCH_TYPES

def test_epoch_type_count():
    assert len(VALID_EPOCH_TYPES) == 4
