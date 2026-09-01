"""Validation helpers for NeuroWhisper configuration."""

from typing import Any


REQUIRED_SECTIONS = (
    "classifier",
    "karaone",
    "sacred",
)


def validate_config(config: dict[str, Any]) -> None:
    """Validate the minimum structure required by NeuroWhisper."""
    if not isinstance(config, dict):
        raise TypeError("Configuration must be a dictionary.")

    missing = [section for section in REQUIRED_SECTIONS if section not in config]

    if missing:
        raise ValueError(
            "Missing required configuration sections: "
            + ", ".join(missing)
        )

    classifier = config["classifier"]
    karaone = config["karaone"]

    if not isinstance(classifier, dict):
        raise TypeError("'classifier' must be a mapping.")

    if not isinstance(karaone, dict):
        raise TypeError("'karaone' must be a mapping.")

    if "random_state" in classifier:
        if not isinstance(classifier["random_state"], int):
            raise TypeError("'classifier.random_state' must be an integer.")

    if "test_size" in classifier:
        test_size = classifier["test_size"]
        if not isinstance(test_size, (int, float)) or not 0 < test_size < 1:
            raise ValueError("'classifier.test_size' must be between 0 and 1.")
