from eeg_isr.features.metadata import feature_families, feature_names


def test_feature_metadata_registry():
    names = feature_names()
    families = feature_families()

    assert names
    assert len(names) == len(set(names))
    assert len(names) == len(families)
