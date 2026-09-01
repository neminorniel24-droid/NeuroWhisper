"""Typed configuration models for EEG-ISR."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ClassifierConfig:
    """Classifier configuration."""

    random_state: int = 42
    test_size: float = 0.2
    n_splits: int = 5

    def __post_init__(self) -> None:
        if not 0 < self.test_size < 1:
            raise ValueError("test_size must be between 0 and 1.")

        if self.n_splits < 2:
            raise ValueError("n_splits must be at least 2.")


@dataclass(frozen=True)
class KaraOneConfig:
    """Kara One dataset configuration."""

    raw_data_dir: str
    filtered_data_dir: str
    features_dir: str
    subjects: Any = "all"
    tasks: list[int] = field(default_factory=list)


@dataclass(frozen=True)
class ProjectConfig:
    """Top-level NeuroWhisper configuration."""

    classifier: ClassifierConfig
    karaone: KaraOneConfig


def build_project_config(config: dict[str, Any]) -> ProjectConfig:
    """Build typed configuration from a YAML dictionary."""
    classifier_data = config.get("classifier", {})
    karaone_data = config.get("karaone", {})

    classifier = ClassifierConfig(
        random_state=classifier_data.get("random_state", 42),
        test_size=classifier_data.get("test_size", 0.2),
        n_splits=classifier_data.get("n_splits", 5),
    )

    karaone = KaraOneConfig(
        raw_data_dir=karaone_data.get(
            "raw_data_dir",
            "files/Data/KaraOne/EEG_raw/",
        ),
        filtered_data_dir=karaone_data.get(
            "filtered_data_dir",
            "files/Data/KaraOne/EEG_data-1/",
        ),
        features_dir=karaone_data.get(
            "features_dir",
            "files/Features/KaraOne/features-1/",
        ),
        subjects=karaone_data.get("subjects", "all"),
        tasks=karaone_data.get("tasks", []),
    )

    return ProjectConfig(
        classifier=classifier,
        karaone=karaone,
    )
